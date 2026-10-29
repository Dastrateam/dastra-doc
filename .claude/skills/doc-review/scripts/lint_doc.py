"""Mechanical style checks for the Dastra documentation (fr/en/de/nl GitBook spaces).

Usage:
    python -I lint_doc.py [paths...] [--changed] [--app PATH] [--json]

With no path, checks the pages changed on the current branch against origin/main, committed or not.
A path can be a page or a folder, relative to the repository root. The glossary variants come from
references/glossary.md; UI labels are checked against the Dastra app translations when the app
repository is found (--app, DASTRA_REPO, or a sibling folder named Dastra).
Exit code 1 when at least one error is found.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

LANGS = ("fr", "en", "de", "nl")
SKILL_DIR = Path(__file__).resolve().parent.parent

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U0001F1E6-\U0001F1FF\u2600-\u27BF\u2B00-\u2BFF\u2300-\u23FF\uFE0F\u200D]"
)

ADDRESS = {
    "fr": (re.compile(r"(?<![\w-])(tu|toi|tes)(?![\w-])|\w-tu\b", re.I), "vous / votre"),
    "de": (re.compile(r"(?<![\w-])([Dd]u|dich|dir|[Dd]ein(e|en|em|er|es)?)(?![\w-])"), "Sie / Ihr"),
    "nl": (re.compile(r"(?<![\w-])(je|jij|jou|jouw|jezelf)(?![\w-])", re.I), "u / uw"),
}

# Strong markers: rewrite. Weak markers: rewrite only when a direct verb reads better.
MARKERS = {
    "fr": [
        r"bonne nouvelle", r"chez dastra,? nous", r"dans cet article", r"nous allons voir", r"en résumé",
        r"en conclusion", r"n.hésitez pas", r"il est important de noter", r"non seulement",
        r"que vous soyez", r"facilement", r"simplement", r"il suffit de", r"en quelques clics",
        r"en toute simplicité", r"puissant\w*", r"incontournable\w*", r"si tu veux", r"bien sûr",
        r"\(\d+ ?min\)", r"tirer parti", r"booste\w*", r"cliquez ici",
    ],
    "en": [
        r"the good news", r"at dastra,? we", r"in this article", r"we will see", r"in summary", r"in conclusion",
        r"feel free to", r"don.t hesitate", r"(it is|it.s) (worth noting|important to note)", r"keep in mind that",
        r"not only\b", r"whether you.re", r"\beasily\b", r"\bsimply\b", r"\bjust (click|select|choose)",
        r"in a few clicks", r"seamless(ly)?", r"\brobust\b", r"\bpowerful\b", r"\bcomprehensive\b", r"leverag\w+",
        r"empower\w*", r"streamlin\w+", r"\bdelve\b", r"dive into", r"effortless(ly)?",
        r"cutting-edge", r"if you want, i can", r"i hope this helps", r"\bcertainly\b",
        r"\(\d+ ?min\)", r"as smoothly and quickly", r"click here",
    ],
    "de": [
        r"die gute nachricht", r"in diesem artikel", r"zusammenfassend", r"zögern sie nicht",
        r"beachten sie,? dass", r"bitte beachten sie", r"nicht nur\b", r"ganz einfach", r"mit wenigen klicks",
        r"nahtlos\w*", r"leistungsstark\w*", r"mühelos\w*", r"\(\d+ ?min\)", r"hier klicken",
    ],
    "nl": [
        r"het goede nieuws", r"in dit artikel", r"samenvattend", r"aarzel niet", r"niet alleen\b",
        r"met een paar klikken", r"naadloos", r"krachtig\w*", r"moeiteloos", r"simpelweg", r"\bgewoon\b",
        r"\beenvoudig\b", r"houd er rekening mee", r"\(\d+ ?min\)", r"klik hier",
    ],
}
WEAK = {
    "fr": [r"permet(tent)? de", r"afin de", r"notez que"],
    "en": [r"(allows|enables) you to", r"in order to"],
    "de": [r"ermöglicht es ihnen", r"\beinfach\b"],
    "nl": [r"stelt u in staat"],
}

# Lines that name a UI element: the bold or quoted text they contain is checked against the app strings.
ACTION = {
    "fr": r"\b(cliquez|sélectionnez|choisissez|cochez|activez|allez dans|rendez-vous dans|ouvrez l.onglet)\b",
    "en": r"\b(click|select|choose|tick|check the|turn on|go to|open the \w+ tab)\b",
    "de": r"\b(klicken|wählen|aktivieren sie|kreuzen|gehen sie zu|öffnen sie die registerkarte)\b",
    "nl": r"\b(klik|selecteer|kies|vink|activeer|ga naar|open het tabblad)\b",
}
MENU_PATH = re.compile(r"\*\*\s*(?:>|→)\s*\*\*|\*\*[^*]+\s(?:>|→)\s[^*]+\*\*")

FAQ = re.compile(r"faq|questions fréquentes|häufig gestellte|veelgestelde", re.I)
FRONT_MATTER_KEYS = {"description", "icon", "cover", "coverY", "coverHeight", "layout", "hidden", "noIndex",
                     "metaLinks", "if"}

FRENCH_WORDS = {"les", "des", "une", "est", "vous", "votre", "avec", "dans", "pour", "sur", "cette", "sont",
                "être", "été", "aux", "qui", "que", "pas", "nous", "ces", "leur"}

PROPER = {"dastra", "google", "microsoft", "teams", "jira", "servicenow", "sap", "leanix", "onedrive",
          "sharepoint", "zapier", "tag", "manager", "consent", "mode", "trust", "center", "azure", "entra",
          "okta", "splunk", "dynatrace", "article", "cnil", "gdpr", "ai", "act", "excel", "word", "power", "bi",
          "slack", "hubspot", "salesforce", "filerskeepers", "tomorro", "dilitrust", "bleu", "outlook", "gmail",
          "chrome", "api", "sso", "scim", "iso", "edpb", "cepd", "tcf", "iab", "gpc", "v2", "rest", "json", "csv",
          "pdf", "markdown", "html", "privacy", "by", "design", "cookie", "office", "identity", "ad", "github"}
SMALL = {"a", "an", "the", "of", "and", "or", "to", "in", "on", "for", "with", "by", "from", "at", "vs",
         "de", "des", "du", "la", "le", "les", "et", "à", "au", "aux", "en", "d", "l", "un", "une", "par",
         "van", "het", "een", "voor", "met", "op", "te"}


def git(args, cwd):
    out = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    return out.stdout if out.returncode == 0 else ""


def repo_root():
    top = git(["rev-parse", "--show-toplevel"], SKILL_DIR).strip()
    return Path(top) if top else SKILL_DIR.parent.parent.parent


def load_glossary():
    """Return {lang: [(variant regex, preferred term, concept)]} from references/glossary.md."""
    rules = defaultdict(list)
    columns = None
    for line in (SKILL_DIR / "references" / "glossary.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            columns = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if columns is None:
            columns = [c.lower() for c in cells]
            continue
        if set(cells[0]) <= set("-: "):
            continue
        concept = cells[0]
        for lang in LANGS:
            if lang not in columns or "≠" not in cells[columns.index(lang)]:
                continue
            preferred, variants = cells[columns.index(lang)].split("≠", 1)
            for variant in (v.strip() for v in variants.split(",")):
                if not variant:
                    continue
                body = re.escape(variant).replace(r"\ ", r"\s+")
                flags = 0 if any(c.isupper() for c in variant) else re.I
                pattern = re.compile(rf"(?<![\w-]){body}(?:s|es|en|e|n)?(?![\w-])", flags)
                rules[lang].append((pattern, preferred.strip() or "see the glossary", concept))
    return rules


def find_app(explicit, root):
    candidates = [explicit, os.environ.get("DASTRA_REPO"), root.parent / "Dastra", root.parent.parent / "Dastra"]
    for c in candidates:
        if c and (Path(c) / "Dastra.WebApp" / "src" / "assets" / "lang" / "modules").is_dir():
            return Path(c)
    return None


def normalize_label(s):
    s = s.replace("’", "'").replace("\u00A0", " ").replace("\u202F", " ")
    s = re.sub(r"\s+", " ", s).strip().strip(":\"«»„“”").strip()
    s = re.sub(r"(\.\.\.|…)$", "", s).strip()
    return s.lower()


def load_labels(app):
    """Return {lang: set of normalized UI strings} from the app translations and backend resx files."""
    labels = defaultdict(set)

    def walk(node, lang):
        if isinstance(node, dict):
            for v in node.values():
                walk(v, lang)
        elif isinstance(node, str) and len(node) <= 120:
            labels[lang].add(normalize_label(node))

    modules = app / "Dastra.WebApp" / "src" / "assets" / "lang" / "modules"
    for module in modules.iterdir():
        for lang in LANGS:
            f = module / f"{lang}.json"
            if f.is_file():
                walk(json.loads(f.read_text(encoding="utf-8")), lang)
    for rel in git(["ls-files", "*.resx"], app).splitlines():
        m = re.search(r"\.(fr|de|nl)\.resx$", rel)
        lang = m.group(1) if m else ("en" if re.search(r"/[^./]+\.resx$", "/" + rel) else None)
        if not lang:
            continue
        try:
            for value in ET.parse(app / rel).getroot().iter("value"):
                if value.text and len(value.text) <= 120:
                    labels[lang].add(normalize_label(value.text))
        except ET.ParseError:
            continue
    return labels


def changed_pages(root):
    names = set(git(["diff", "--name-only", "--diff-filter=AMR", "origin/main...HEAD"], root).splitlines())
    names |= set(git(["diff", "--name-only", "--diff-filter=AMR", "HEAD"], root).splitlines())
    names |= set(git(["ls-files", "--others", "--exclude-standard"], root).splitlines())
    return sorted(n for n in names if re.match(r"(fr|en|de|nl)/.+\.md$", n))


def expand(paths, root):
    pages = []
    for p in paths:
        full = (root / p).resolve()
        if full.is_dir():
            pages += sorted(str(f.relative_to(root)).replace("\\", "/") for f in full.rglob("*.md")
                            if ".gitbook" not in f.parts)
        elif full.is_file():
            pages.append(str(full.relative_to(root)).replace("\\", "/"))
        else:
            print(f"Not found: {p}", file=sys.stderr)
    return pages


def prose(line):
    """Strip what is not prose: code, links targets, URLs, HTML tags, GitBook tags, escapes."""
    line = re.sub(r"`[^`]*`", " ", line)
    line = re.sub(r"\{%.*?%\}", " ", line)
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", line)
    line = re.sub(r"\]\([^)]*\)", "]", line)
    line = re.sub(r"<[^>]+>", " ", line)
    line = re.sub(r"https?://\S+|[\w.+-]+@[\w-]+\.[\w.]+|\b[\w-]+\.(eu|com|io|md|png|json)\b", " ", line)
    return line.replace("&#x20;", " ").replace("&nbsp;", " ")


def heading_case_issue(text, lang):
    letters = [c for c in text if c.isalpha()]
    if len(letters) > 4 and all(c.isupper() for c in letters):
        return "all-caps heading"
    if lang == "de":
        return None
    words = re.findall(r"[^\W\d_][\w'’-]*", text)[1:]
    words = [w for w in words if w.lower() not in SMALL and not w.isupper() and w.lower() not in PROPER]
    if len(words) >= 2 and all(w[0].isupper() for w in words):
        return "Title Case heading"
    return None


def structure(text):
    return Counter(
        headings=len(re.findall(r"^#{2,3} ", text, re.M)),
        steps=len(re.findall(r"^\s*\d+\. ", text, re.M)),
        bullets=len(re.findall(r"^\s*[*-] ", text, re.M)),
        figures=len(re.findall(r"<figure|!\[", text)),
        hints=len(re.findall(r"\{% hint", text)),
        embeds=len(re.findall(r"\{% embed", text)),
    )


def broken_links(raw, page_dir):
    """Relative link, image and content-ref targets of a line that do not exist on disk."""
    targets = re.findall(r"\]\(<([^>]+)>\)", raw) + re.findall(r"\]\(([^)<\s]+)", raw)
    targets += re.findall(r"(?:src|href|url)=\"([^\"]+)\"", raw)
    broken = []
    for target in targets:
        if re.match(r"[a-z]+:|#|/|\{", target, re.I):
            continue
        path = re.sub(r"\\(.)", r"\1", unquote(target.split("#", 1)[0].split("?", 1)[0]))
        if not path:
            continue
        full = (page_dir / path).resolve()
        if not (full.exists() or full.with_suffix(".md").exists() or (full / "README.md").exists()):
            broken.append(target)
    return broken


def check_page(rel, root, glossary, labels):
    lang = rel.split("/", 1)[0]
    text = (root / rel).read_text(encoding="utf-8")
    findings = []

    def add(line_no, severity, rule, message, excerpt):
        findings.append({"file": rel, "line": line_no, "severity": severity, "rule": rule,
                         "message": message, "excerpt": excerpt.strip()[:160]})

    lines = text.splitlines()
    front_matter_end = 0
    if lines and lines[0].strip() == "---":
        front_matter_end = next((i for i, l in enumerate(lines[1:], 2) if l.strip() == "---"), 0)
        for no, raw in enumerate(lines[1:front_matter_end - 1], 2):
            key = re.match(r"([^\s:#][^:]*):", raw)
            if key and key.group(1) not in FRONT_MATTER_KEYS:
                add(no, "error", "front-matter", f"\"{key.group(1)}\" is not a GitBook key: keys stay in English (description:)", raw)

    page_dir = (root / rel).parent
    in_code = False
    in_faq = bool(FAQ.search(rel))
    heading_level = 1
    for no, raw in enumerate(lines, 1):
        if raw.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or no <= front_matter_end and not raw.startswith("description:"):
            continue
        line = prose(raw)

        for target in broken_links(raw, page_dir):
            add(no, "error", "link", f"\"{target}\" does not exist", raw)
        if re.search(r"<img\b[^>]*\balt=\"\s*\"", raw):
            add(no, "warning", "alt", "describe what the figure shows in alt", raw)
        if MENU_PATH.search(line) and "→" in line:
            add(no, "warning", "menu-path", "separate the steps of a menu path with >, not →", raw)

        for m in EMOJI.finditer(raw if raw.startswith("#") else line):
            if m.group() in "\uFE0F\u200D":
                continue
            msg = "remove the emoji"
            if rel.endswith("SUMMARY.md") and raw.startswith("## ") and "<a " not in raw:
                msg += "; this group has no anchor: add <a href=\"#slug\" id=\"slug\"></a> with its current slug first"
            add(no, "error", "emoji", msg, raw)
            break
        if "—" in line:
            add(no, "error", "em-dash", "replace the em dash with a comma, a colon, parentheses or two sentences", raw)
        if " – " in line:
            add(no, "error", "en-dash", "spaced en dash used as a dash: rewrite as for an em dash", raw)
        if re.search(r"[^\s!]\s?!(?=\s|$|\*)", line):
            add(no, "warning", "exclamation", "remove the exclamation mark", raw)
        if re.search(r"\w(\.\.\.|…)(\s|$)", line) and "**" not in line:
            add(no, "warning", "ellipsis", "finish the list or write etc.", raw)

        if lang in ADDRESS:
            pattern, expected = ADDRESS[lang]
            m = pattern.search(line)
            if m:
                add(no, "error", "address", f"\"{m.group().strip()}\": address the reader with {expected}", raw)

        for pattern, preferred, concept in glossary.get(lang, []):
            m = pattern.search(line)
            if m:
                add(no, "warning", "term", f"\"{m.group()}\" ({concept}): use \"{preferred}\" unless it is a UI label", raw)

        for p in MARKERS.get(lang, []):
            m = re.search(p, line, re.I)
            if m:
                add(no, "warning", "marker", f"\"{m.group()}\": writing marker, rewrite (see style.md)", raw)
        for p in WEAK.get(lang, []):
            m = re.search(p, line, re.I)
            if m:
                add(no, "hint", "weak-marker", f"\"{m.group()}\": a direct verb may read better", raw)

        h = re.match(r"(#{1,6}) (.+)", raw)
        if h and not rel.endswith("SUMMARY.md"):
            title = re.sub(r"<[^>]+>", "", h.group(2)).strip()
            issue = heading_case_issue(EMOJI.sub("", title), lang)
            if issue:
                add(no, "warning", "heading-case", f"{issue}: use sentence case", raw)
            level = len(h.group(1))
            if level > heading_level + 1:
                add(no, "warning", "heading-level", f"heading level {level} under level {heading_level}: go down one level at a time", raw)
            heading_level = level
            in_faq = in_faq or bool(FAQ.search(title))
            if title.endswith("?") and not in_faq:
                add(no, "warning", "question-heading", "question as a heading outside a FAQ: state the topic", raw)

        if lang != "fr":
            words = set(re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", line.lower())) & FRENCH_WORDS
            if lang == "de":
                words.discard("des")
            if len(words) >= 4:
                add(no, "warning", "language", "looks like French left in a translated page", raw)

        quoted_label = False
        if labels is not None and (re.search(ACTION[lang], line, re.I) or MENU_PATH.search(line)):
            for m in re.finditer(r"\*\*([^*]{1,80})\*\*", line):
                if m.group(1).rstrip().endswith(":") or line[m.end():].lstrip().startswith(":"):
                    continue  # bold lead-in of a list item, not a label
                for label in re.split(r"\s+(?:>|→)\s+", m.group(1)):
                    key = normalize_label(label)
                    if key and len(key.split()) <= 6 and not key.isdigit() and key not in labels[lang]:
                        add(no, "info", "ui-label", f"\"{label.strip()}\" not found in the app's {lang} strings: verify it", raw)
            for quoted in re.findall(r"[\"«„“]\s?([^\"»“”]{2,60}?)\s?[\"»“”]", line):
                if quoted[0].isupper() and normalize_label(quoted) in labels[lang]:
                    quoted_label = True
                    add(no, "warning", "ui-label-format", f"\"{quoted.strip()}\" is a UI label: write it in bold, not in quotes", raw)
        if lang == "fr" and not quoted_label and re.search(r"[“”]|(?<![\w=])\"[^\"\s][^\"]*\"", line):
            add(no, "warning", "quotes", "French quotes « » for quoted words, bold for UI labels", raw)

    if lang != "fr" and not rel.endswith("SUMMARY.md"):
        source = root / ("fr" + rel[len(lang):])
        if not source.is_file():
            add(1, "info", "parity", "no French page at the same path", "")
        else:
            mine, theirs = structure(text), structure(source.read_text(encoding="utf-8"))
            gaps = [f"{k} {mine[k]} vs {theirs[k]} in French" for k in sorted(theirs | mine) if mine[k] != theirs[k]]
            if gaps:
                add(1, "info", "parity", "structure differs from the French page: " + ", ".join(gaps), "")
    return merge_runs(findings)


def merge_runs(findings):
    """Report the same finding on consecutive lines (a table column, a list) once, as a line range."""
    merged = []
    for f in sorted(findings, key=lambda f: f["line"]):
        prev = next((m for m in reversed(merged) if m["rule"] == f["rule"] and m["message"] == f["message"]), None)
        if prev and f["line"] == prev["end"] + 1:
            prev["end"] = f["line"]
        else:
            merged.append({**f, "end": f["line"]})
    return merged


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--changed", action="store_true", help="pages changed against origin/main (default)")
    parser.add_argument("--app", help="path to the Dastra application repository")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = repo_root()
    pages = expand(args.paths, root) if args.paths else changed_pages(root)
    pages = [p for p in pages if p.split("/", 1)[0] in LANGS]
    if not pages:
        print("No documentation page to check.")
        return 0

    app = find_app(args.app, root)
    labels = load_labels(app) if app else None
    glossary = load_glossary()
    findings = [f for p in pages for f in check_page(p, root, glossary, labels)]

    if args.json:
        print(json.dumps({"pages": pages, "app": str(app) if app else None, "findings": findings},
                         ensure_ascii=False, indent=1))
    else:
        totals = Counter(f["severity"] for f in findings)
        print(f"{len(pages)} page(s), {totals['error']} error(s), {totals['warning']} warning(s), "
              f"{totals['hint']} hint(s), {totals['info']} info")
        if not app:
            print("UI labels not checked: Dastra app repository not found (use --app or DASTRA_REPO).")
        by_file = defaultdict(list)
        for f in findings:
            by_file[f["file"]].append(f)
        for page in pages:
            if not by_file[page]:
                continue
            print(f"\n## {page}")
            for f in by_file[page]:
                lines = f"L{f['line']}" + (f"-{f['end']}" if f["end"] != f["line"] else "")
                excerpt = f"  | {f['excerpt']}" if f["excerpt"] else ""
                print(f"- {lines} {f['severity']} {f['rule']}: {f['message']}{excerpt}")
    return 1 if any(f["severity"] == "error" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
