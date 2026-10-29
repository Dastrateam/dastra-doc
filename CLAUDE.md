# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Source files for the [Dastra](https://doc.dastra.eu) product documentation, published via **GitBook**. Dastra is a data governance / GDPR & AI Act compliance platform. This is a pure Markdown content repo: there is no build, lint, or test step. Merging to `main` publishes automatically to GitBook (Git Sync). The sync is bidirectional — commits like "GitBook: Export content from English" were pushed by the GitBook web editor, so always pull before working.

## Repository structure

Four language folders, each one being an independent GitBook space:

| Folder | Language |
| ------ | -------- |
| `fr/`  | French — the primary/source language, usually written first |
| `en/`  | English |
| `de/`  | German |
| `nl/`  | Dutch |

Each language folder contains:

- `SUMMARY.md` — the table of contents. **A page not listed in `SUMMARY.md` does not appear in the published docs.** Section headers (`## ⚙️ Features`) become nav groups; nesting via indented list items.
- `README.md` — the landing page of the space (and each subfolder's `README.md` is that section's landing page).
- `.gitbook/assets/` — all images for that language. Reference them with relative paths (`../.gitbook/assets/foo.png`).
- Content organized by theme, with the same folders in every language: `gdpr/`, `getting-started/`, `features/`, `api/`, `security/`, `other/`, `partners/` (plus `frameworks/` in English and German).

## Paths and URLs

Every page has **one English path, identical in the four languages** (`fr/features/ropa/merge.md`, `en/features/ropa/merge.md`, …). The old French-slug URLs keep working through the `redirects:` of each language's `.gitbook.yaml`.

- A new page gets its English path from the start, the same in every language: short English folder names (`features/ropa`, `features/requests`), page names of one to three words, lowercase, hyphens, ASCII.
- The published URL of a page is the slug of its `##` group in `SUMMARY.md` (the `id` of the group's `<a>` anchor, or the slugified title) followed by the page path inside that group. Each group anchor matches its folder (`<a href="#features" id="features"></a>`); never change a group heading without keeping its anchor.
- Paths are published URLs: do not rename or move a page as part of a content change. A rename is a decision of its own, done in every language at once, with a redirect from the old URL in each `.gitbook.yaml` (key = old URL path without `.md`, value = new file path), after searching the Dastra app for links to the old path.
- Never rename `features/integrations/*`: the connectors of the app link to these paths.
- Changing a heading changes its anchor: update the links that point to it.

## Editing conventions

- File names: lowercase, hyphens, no accents.
- Pages start with optional YAML frontmatter (`description:` is used for SEO/preview), then a single `#` title that must match the label used in `SUMMARY.md`.
- GitBook-flavored Markdown is used throughout — preserve it:
  - `{% hint style="info" %}...{% endhint %}` (also `warning`, `danger`, `success`)
  - `{% tabs %}` / `{% tab title="..." %}`, `{% embed url="..." %}`, `{% content-ref url="..." %}`
  - `<figure><img src="..." alt=""><figcaption>...</figcaption></figure>` for images
  - `&#x20;` trailing-space escapes are artifacts of GitBook export — harmless, don't strip them in bulk.
- Adding a page = create the `.md` file **and** add its entry to that language's `SUMMARY.md`. When a change applies to the product (not language-specific wording), mirror it across all four languages — `fr/` first, then translate.
- PRs target `main`. Keep one language per PR unless the change is structural.
- Style, languages and vocabulary (tone, no emojis, form of address, glossary, UI labels) are defined in the `doc-review` skill (`.claude/skills/doc-review/`): follow its references when writing, and run `/doc-review` on the changed pages before opening a PR.

## Dastra source code (../../Dastra)

The full Dastra application source lives at `c:\_git\Dastra` (a sibling of this repo's parent: `../../Dastra` from this folder). Use it as the source of truth when documenting features — to verify actual behavior, UI labels, option names, API endpoints, and permissions instead of guessing:

- It is a .NET / C# backend + Vue 3 frontend monorepo (`Dastra.API`, `Dastra.WebApp`, `Dastra.Compliance.*`, `Dastra.AI.*`, etc.).
- It has its own `CLAUDE.md` and detailed instructions under `.github/instructions/` — read those before navigating it.
- Typical use from here: grep the frontend for a UI label to find the component, or the API projects for endpoint routes, then document what the code actually does.
