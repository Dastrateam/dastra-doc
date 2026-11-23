"""Builds a GitBook-like preview of a documentation pull request.

Usage:
    python -I build_preview.py <pull request number> <output folder> [--repo <dastra-doc clone>]
    python -I build_preview.py --worktree <worktree folder> <output folder>

The second form previews the working files of a worktree against origin/main, committed or not, before any
pull request exists.

The clone is found in this order: --repo, the DASTRA_DOC_REPO environment variable, the repository holding
this script, the current directory.

Writes in the output folder:
    index.html   the viewer (assets/viewer.html of this skill)
    data.json    the pages of the pull request, before and after, with their images and link titles
    img/         the images those pages show, taken from the pull request head

A page is included when the pull request changes it, or when it shows an image the pull request changes.
Needs `gh` (authenticated) and `git`. It fetches, but never checks out, pushes or changes a branch, an index
or a working file. With --worktree it stores one unreferenced snapshot commit of the working files.
"""

import hashlib
import io
import json
import os
import posixpath
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = "Dastrateam/dastra-doc"
LANGS = ("fr", "en", "de", "nl")
SKILL = Path(__file__).resolve().parent.parent
ROOT = None
MAX_PAGES = 120
MAX_IMAGES = 240
MAX_IMAGE_WIDTH = 1600
IMAGE_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")


def run(args, check=True, binary=False):
    out = subprocess.run(args, cwd=ROOT, capture_output=True)
    if check and out.returncode != 0:
        sys.exit(f"{' '.join(args[:4])} failed: {out.stderr.decode('utf-8', 'replace').strip()[:300]}")
    if out.returncode != 0:
        return None
    return out.stdout if binary else out.stdout.decode("utf-8", "replace")


def find_repo(explicit):
    """Top folder of the first candidate that is a clone of the documentation repository."""
    for candidate in (explicit, os.environ.get("DASTRA_DOC_REPO"), str(SKILL), os.getcwd()):
        if not candidate or not Path(candidate).is_dir():
            continue
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=candidate, capture_output=True, text=True)
        if top.returncode != 0:
            continue
        url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=top.stdout.strip(), capture_output=True, text=True)
        if REPO.split("/")[1] in url.stdout:
            return Path(top.stdout.strip())
    sys.exit("No clone of dastra-doc found: pass --repo <path> or set DASTRA_DOC_REPO.")


def snapshot(worktree):
    """(commit, branch) of the working files of a worktree, made through a temporary index."""
    env = dict(os.environ, GIT_INDEX_FILE=os.path.join(tempfile.mkdtemp(), "index"))

    def git(*args):
        out = subprocess.run(["git", *args], cwd=worktree, capture_output=True, text=True, env=env)
        if out.returncode != 0:
            sys.exit(f"git {args[0]} failed in {worktree}: {out.stderr.strip()[:300]}")
        return out.stdout.strip()

    git("read-tree", "HEAD")
    git("add", "-A")
    commit = git("commit-tree", git("write-tree"), "-p", "HEAD", "-m", "doc-preview snapshot")
    return commit, git("rev-parse", "--abbrev-ref", "HEAD")


def show(rev, path):
    """Text of a file at a revision, or None."""
    return run(["git", "show", f"{rev}:{path}"], check=False)


def split_front_matter(text):
    """(description, body) of a page."""
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    lines = text[3:end].strip("\n").split("\n")
    description = ""
    for i, raw in enumerate(lines):
        match = re.match(r"description:\s*(.*)$", raw)
        if not match:
            continue
        value = match.group(1).strip()
        if value[:1] in (">", "|"):
            block = []
            for nxt in lines[i + 1:]:
                if nxt.strip() and not nxt.startswith((" ", "\t")):
                    break
                block.append(nxt.strip())
            value = " ".join(part for part in block if part)
        elif len(value) > 1 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        description = value
    return description, text[end + 4:].lstrip("\n")


def title_of(body):
    match = re.search(r"^# +(.+)$", body or "", re.M)
    return match.group(1).strip() if match else ""


def targets(body, pattern):
    return [m for m in re.findall(pattern, body or "")]


def resolve(page, target):
    """Repository path of a relative link or image target of a page, or None."""
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target or re.match(r"[a-z]+:|/|\{", target, re.I):
        return None
    path = posixpath.normpath(posixpath.join(posixpath.dirname(page), target.replace("\\ ", " ").replace("%20", " ")))
    return None if path.startswith("..") else path


def image_targets(body):
    found = targets(body, r"<img\b[^>]*\bsrc=\"([^\"]+)\"") + targets(body, r"!\[[^\]]*\]\(<([^>]+)>\)")
    return found + targets(body, r"!\[[^\]]*\]\(([^)<\s]+)")


def link_targets(body):
    found = targets(body, r"\]\(<?([^)>\s]+\.md)(?:#[^)>\s]*)?>?\)") + targets(body, r"\burl=\"([^\"#]+\.md)")
    return found + targets(body, r"\bhref=\"([^\"#]+\.md)")


def export_image(data, out):
    """Writes an image, scaled down when it is wider than the preview shows it."""
    if out.suffix.lower() in (".png", ".jpg", ".jpeg"):
        try:
            from PIL import Image
            image = Image.open(io.BytesIO(data))
            if image.width > MAX_IMAGE_WIDTH:
                image = image.resize((MAX_IMAGE_WIDTH, round(image.height * MAX_IMAGE_WIDTH / image.width)))
                image.save(out, optimize=True)
                return
        except Exception:
            pass
    out.write_bytes(data)


def main():
    global ROOT
    args = sys.argv[1:]

    def option(name):
        if name not in args:
            return None
        at = args.index(name)
        value = args[at + 1] if at + 1 < len(args) else None
        del args[at:at + 2]
        return value

    explicit, worktree = option("--repo"), option("--worktree")
    if worktree:
        if len(args) != 1:
            sys.exit(__doc__)
        ROOT = find_repo(worktree)
        out = Path(args[0]).resolve()
        head, branch = snapshot(worktree)
        run(["git", "fetch", "-q", "origin", "main"])
        pr = {"number": 0, "title": f"Working copy of {branch}", "url": "", "author": {"login": "not committed"},
              "headRefName": branch, "state": "LOCAL", "isDraft": False}
        base_ref = "origin/main"
    else:
        if len(args) != 2 or not args[0].lstrip("#").isdigit():
            sys.exit(__doc__)
        ROOT = find_repo(explicit)
        number = args[0].lstrip("#")
        out = Path(args[1]).resolve()
        pr = json.loads(run(["gh", "pr", "view", number, "--repo", REPO, "--json",
                             "number,title,url,author,headRefName,headRefOid,state,mergeCommit,isDraft"]))
        run(["git", "fetch", "-q", "origin", "main"])
        run(["git", "fetch", "-q", "origin", f"pull/{number}/head"])
        head = pr["headRefOid"]
        base_ref = f"{pr['mergeCommit']['oid']}^1" if pr["state"] == "MERGED" and pr.get("mergeCommit") else "origin/main"
    (out / "img").mkdir(parents=True, exist_ok=True)
    base = run(["git", "merge-base", base_ref, head]).strip()

    changes = {}
    for line in run(["git", "diff", "--name-status", "-M", base, head]).splitlines():
        parts = line.split("\t")
        if parts[0].startswith("R"):
            changes[parts[2]] = ("renamed", parts[1])
        else:
            changes[parts[1]] = ({"A": "added", "D": "deleted"}.get(parts[0], "modified"), parts[1])

    def is_page(path):
        return path.endswith(".md") and path.split("/")[0] in LANGS

    pages = []
    for path, (status, old) in sorted(changes.items()):
        if not is_page(path):
            continue
        if path.endswith("/SUMMARY.md"):
            diff = run(["git", "diff", "-U2", base, head, "--", path])
            lines = [l for l in diff.splitlines() if not l.startswith(("diff ", "index ", "--- ", "+++ "))]
            pages.append({"lang": path.split("/")[0], "path": path, "status": "summary", "title": "SUMMARY.md",
                          "diff": "\n".join(lines)})
            continue
        after = None if status == "deleted" else show(head, path)
        before = None if status == "added" else show(base, old)
        after_desc, after_body = split_front_matter(after) if after is not None else ("", None)
        before_desc, before_body = split_front_matter(before) if before is not None else ("", None)
        pages.append({"lang": path.split("/")[0], "path": path, "status": status,
                      "title": title_of(after_body) or title_of(before_body) or path,
                      "description": after_desc, "descriptionBefore": before_desc,
                      "after": after_body, "before": before_body})

    # Pages the pull request does not change, but whose images it changes.
    shown = {p["path"] for p in pages}
    changed_images = [p for p in changes if p.lower().endswith(IMAGE_EXT) and changes[p][0] != "deleted"]
    for image in changed_images:
        lang = image.split("/")[0]
        if lang not in LANGS:
            continue
        hits = run(["git", "grep", "-l", "-F", posixpath.basename(image), head, "--", f"{lang}/"], check=False) or ""
        for hit in hits.splitlines():
            path = hit.split(":", 1)[1]
            if path in shown or not is_page(path) or path.endswith("/SUMMARY.md") or len(pages) >= MAX_PAGES:
                continue
            desc, body = split_front_matter(show(head, path))
            if not any(resolve(path, t) == image for t in image_targets(body)):
                continue
            shown.add(path)
            pages.append({"lang": lang, "path": path, "status": "images", "title": title_of(body) or path,
                          "description": desc, "descriptionBefore": desc, "after": body, "before": body})

    images, titles, skipped = {}, {}, 0
    for page in pages:
        for body, rev in ((page.get("after"), head), (page.get("before"), base)):
            for target in image_targets(body):
                path = resolve(page["path"], target)
                if not path or path in images or not path.lower().endswith(IMAGE_EXT):
                    continue
                data = run(["git", "cat-file", "blob", f"{rev}:{path}"], check=False, binary=True)
                if data is None:
                    continue
                if len(images) >= MAX_IMAGES or len(data) > 14_000_000:
                    skipped += 1
                    continue
                name = hashlib.sha1(path.encode("utf-8")).hexdigest()[:12] + posixpath.splitext(path)[1].lower()
                export_image(data, out / "img" / name)
                images[path] = {"file": f"img/{name}", "changed": path in changes}
            if rev != head:
                continue
            for target in link_targets(body):
                path = resolve(page["path"], target)
                if path and path not in titles:
                    text = show(head, path)
                    titles[path] = title_of(split_front_matter(text)[1]) if text else ""

    data = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo": REPO,
        "pr": {"number": pr["number"], "title": pr["title"], "url": pr["url"], "author": pr["author"]["login"],
               "branch": pr["headRefName"], "state": pr["state"].lower(), "draft": pr["isDraft"]},
        "head": head, "base": base, "linkRef": "main" if worktree else head, "pages": pages, "images": images, "titles": titles,
    }
    (out / "data.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8", newline="\n")
    title = f"Doc PR {pr['number']}" if pr["number"] else f"Doc draft {pr['headRefName'].split('/')[-1]}"
    viewer = (SKILL / "assets" / "viewer.html").read_text(encoding="utf-8")
    (out / "index.html").write_text(viewer.replace("__TITLE__", title), encoding="utf-8", newline="\n")

    size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file())
    by_status = {}
    for page in pages:
        by_status[page["status"]] = by_status.get(page["status"], 0) + 1
    print(f"{title} ({pr['state'].lower()}): {len(pages)} pages "
          f"({', '.join(f'{n} {s}' for s, n in sorted(by_status.items()))}), {len(images)} images, "
          f"{size / 1_000_000:.1f} MB in {out}")
    if skipped:
        print(f"{skipped} images left out (limit of {MAX_IMAGES} images, or a file over 14 MB)")


if __name__ == "__main__":
    main()
