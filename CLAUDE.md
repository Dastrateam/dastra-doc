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
- Content organized by theme: `features/`, `api-references/`, `security/`, getting-started (`commencer/` or `getting-started/`), etc.

Note that many file and folder names remain in French even inside `en/`, `de/`, `nl/` (e.g. `en/features/generalites/`, `commencer/`), because slugs were kept when content was translated. **Never rename existing files or folders to "fix" this** — paths are the published URLs and renaming breaks links and anchors. Match the existing slug across languages when adding a translated page.

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

## Dastra source code (../../Dastra)

The full Dastra application source lives at `c:\_git\Dastra` (a sibling of this repo's parent: `../../Dastra` from this folder). Use it as the source of truth when documenting features — to verify actual behavior, UI labels, option names, API endpoints, and permissions instead of guessing:

- It is a .NET / C# backend + Vue 3 frontend monorepo (`Dastra.API`, `Dastra.WebApp`, `Dastra.Compliance.*`, `Dastra.AI.*`, etc.).
- It has its own `CLAUDE.md` and detailed instructions under `.github/instructions/` — read those before navigating it.
- Typical use from here: grep the frontend for a UI label to find the component, or the API projects for endpoint routes, then document what the code actually does.
