---
name: doc-review
description: Review Dastra documentation pages (GitBook, fr/en/de/nl) against the house style and vocabulary. Checks a warm but serious tone with no AI-writing or sales markers, no emojis, no em dashes, the form of address of each language (vous, you, Sie, u), Dastra's privacy, product and technical glossary, UI labels that match the app word for word, and parity with the French source page. Reports findings per page with proposed rewrites, and applies them with --fix. Use for "relis cette page", "relecture de la doc", "vérifie le style de cette PR doc", "/doc-review en/features/ropa", "/doc-review --fix", or before opening or merging a dastra-doc pull request.
---

# Documentation review

Review pages of this repository against three references, then report or fix:

- [`references/style.md`](references/style.md): voice, writing markers to remove, typography, page structure,
  safe editing of GitBook files.
- [`references/languages.md`](references/languages.md): source and parity rules, UI labels, and the rules of
  each language.
- [`references/glossary.md`](references/glossary.md): the term to use for each privacy, product and technical
  concept in the four languages, and the variants to replace.

Read the three files before reviewing. They are the rules; this file is the procedure.

## Arguments

- Paths of pages or folders (`en/features/ropa`, `fr/getting-started/quickstart.md`). Without a path, the
  scope is the pages changed on the current branch against `origin/main`, committed or not.
- `--fix`: apply the corrections after the report. Without it, the review only reports.

## Step 1: scope

Run the script (it finds the repository root through git, so it works from any directory; page paths are
relative to the repository root):

```bash
python -I <repository root>/.claude/skills/doc-review/scripts/lint_doc.py <paths>
```

It prints the pages in scope and the mechanical findings, grouped by page, each with its line or line range,
severity (`error`, `warning`, `hint`, `info`) and rule. Besides style and vocabulary, it catches broken relative
links and images, empty `alt` texts, translated front matter keys, question headings, skipped heading levels and
menu paths written with `→`. If it says "No documentation page to check", ask which pages to review.

The UI label check needs the Dastra application repository. The script looks for `--app <path>`, then the
`DASTRA_REPO` environment variable, then a `Dastra` folder next to this repository or one level above. When it
prints "UI labels not checked", pass `--app`.

Above 15 pages, review folder by folder and report as you go; for a whole language space, ask before starting.

## Step 2: read each page

Read every page in scope in full. The script finds patterns; the reading pass judges the text. For each page:

1. **Tone.** Does it read like a knowledgeable colleague: direct, warm, serious? Mark the sentences that sell,
   pad, announce instead of saying, or sound machine-written (the patterns of `style.md` a regex cannot see:
   three adjectives in a row, "not only… but", a colon reveal, an empty intro or conclusion, bold everywhere).
2. **Terms in context.** The script flags forbidden variants; check also that the right term is used for the
   right role (controller and processor are not interchangeable, an entity is not any organizational unit).
3. **Script findings.** Confirm or dismiss each one. A `term` finding inside a UI label is not an error: the
   label wins (glossary rule 1). A `heading-case` finding on a product name is not an error.
4. **UI labels.** The script checks the bold and quoted text of lines that contain an action verb (click,
   select, tick…) or a menu path; read the other labels yourself (a list of actions, a field described in a
   table). Search the app strings of the page language: `<lang>.json`, and `*.<lang>.resx` for French, German
   and Dutch or the `.resx` files without a culture suffix for English:

   ```bash
   git -C <Dastra repo> grep -n -i -F "<label>" -- "Dastra.WebApp/src/assets/lang/modules/*/fr.json" "*.fr.resx"
   ```

   - The key tells you which screen a string belongs to. A string found under an unrelated key, or under two
     keys with different values for the same field, proves nothing: mark it "to verify on screen".
   - If the app has a close but different wording, propose the exact app wording. If nothing matches, write
     "to verify in the app". Never invent a label and never translate one yourself.
   - When the label is on screen but contradicts the glossary, or reads wrong (a calque, a mistranslation),
     keep it in the page and list it in the "app side" part of the report.
   - Labels of third-party screens (Entra ID, Google Tag Manager, Jira, ChatGPT…) are not in the app: dismiss
     them. Bold used for emphasis rather than for a label falls under the tone check.
5. **Parity** (`en/`, `de/`, `nl/` pages). Open the French page at the same path for every translated page,
   whether or not the script reports a parity gap: it only compares counts of headings, steps, bullets,
   figures, hints and embeds. Say what is missing or extra (a section, a step, an item of a list, a video). When
   the French page is the one behind or has its own defects, say so under "Page française source": it is fixed
   in a French change, not in the translation. Do not translate missing content during a review unless asked.
6. **Facts.** Do not rewrite a claim about product behavior, a limit, a price or a legal obligation. If one
   looks wrong or outdated, you may read the app code to make the question precise, but report it as a
   question: the user decides.

## Step 3: report

Write the report in French, page by page: French pages first (they are the source), then English, German and
Dutch. Within a page, corrections before rewrites. Identical findings on consecutive lines take one row with
a line range (68-77).

```markdown
### en/features/ropa/README.md

**À corriger**
| Ligne | Règle | Texte actuel | Proposition |
| --- | --- | --- | --- |
| 12 | emoji | ## ⚙️ Settings | ## Settings |

**À reformuler** (ton, marqueurs)
| Ligne | Texte actuel | Proposition | Pourquoi |

**Libellés à vérifier dans l'app**
- L34 « Generate assessment » : introuvable dans en.json, à vérifier à l'écran.

**Parité avec la page française**
- Il manque la section « Fusionner des traitements » (fr L40 à 58).

**Page française source**
- fr L53 « La bonne nouvelle… ! » : ton commercial, à corriger côté français.
```

Then, once for the whole review:

- **Côté app**: labels that look wrong in the app (calques, inconsistencies), to fix through Localazy, not in
  the documentation.
- **Questions**: facts to check before changing them.
- A one-line count: pages reviewed, corrections, rewrites, labels to verify, questions.

Leave out the sections that are empty. Do not list dismissed script findings.

## Step 4: fix (only with `--fix`, or when the user asks after the report)

1. Apply the corrections and rewrites of the report, nothing else. Rewrite the sentence, not the paragraph,
   unless the paragraph is filler to delete.
2. Follow "Editing GitBook files safely" in `style.md`: GitBook syntax intact, no renamed file or path, an
   anchor added before changing a `SUMMARY.md` group heading that has none, page titles still matching their
   `SUMMARY.md` entries.
3. Leave "to verify" labels, parity gaps and questions untouched: they are listed for the user. Repair a broken
   link only when the right target is certain (the same page at its current path); otherwise list it.
4. Run the script again on the same paths: no `error` may remain on the pages you changed, except those you
   explain (a label quoted from the app).
5. Show `git diff --stat` and the main changes. Do not commit and do not push: hand over a commit message in
   English, imperative mood, and wait for the user's go.

## Guardrails

- Never change meaning, facts, numbers or legal statements to improve style.
- Never invent a UI label, a feature or a setting; the app is the source of truth.
- One language per change, except for a correction that applies to the same page in every language (an emoji
  in the four `SUMMARY.md` files, a wrong label everywhere): then say so in the report.
- The glossary is maintained by the documentation team: propose a new row or variant at the end of the report
  instead of editing `glossary.md` during a review.
