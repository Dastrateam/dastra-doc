---
name: doc-preview
description: >-
  Renders a documentation pull request of dastra-doc the way GitBook shows it: each changed page with its
  images, cards, columns, tabs and hints, the changed blocks marked, before and after, two languages side by
  side. Use when asked to see, preview, read or review what a doc PR looks like ("aperçu de la PR",
  "visualiser la PR 117", "à quoi ressemble cette PR", "/doc-preview 117").
---

# Doc PR preview

GitBook has no preview before a merge, and a GitHub diff shows Markdown on one side and images on the other.
This skill builds a page that renders the pull request as a reader will see it, and publishes it as a private
claude.ai artifact named **Doc PR <number>**.

Read only on GitHub and on the repository: the script fetches, but never checks out, commits, pushes, comments
or approves.

## Arguments

The pull request number (`117` or `#117`). It can be open, merged or closed. With no number, list the open
pull requests (`gh pr list --repo Dastrateam/dastra-doc`) and ask which one.

## Step 1: build

```bash
python -I <repository root>/.claude/skills/doc-preview/scripts/build_preview.py <number> <scratchpad>/doc-preview/<number>
```

It writes `index.html` (the viewer of `assets/viewer.html`), `data.json` and an `img/` folder, and prints the
number of pages and images and the size. Run from a copy of this skill outside the repository, it needs the
clone: add `--repo <path of a dastra-doc clone>` or set `DASTRA_DOC_REPO`. It needs `gh` signed in with read access. If it stops on an error,
report it and stop.

Pass the scratchpad folder by its **full long path** (`C:\Users\<name>\AppData\…`), never its short form
(`C:\Users\NAME~1\…`): the Artifact tool refuses to publish files given through a short path.

## Step 2: publish

Publish `index.html` with the Artifact tool, with `root` set to the output folder and `files` listing
`data.json` and every file of `img/` (paths relative to the folder). On a first publish pass `icon: "book"` and
a one-sentence `description` naming the pull request.

- Same pull request again in this conversation (new commits): build again in the same folder and publish the
  same `index.html`: the link stays the same.
- Same pull request from another conversation: list the artifacts (`action: "list"`), take the one titled
  **Doc PR <number>** and pass its `url`, so the people who have the link keep it. Remove the images that are no
  longer used by passing `null` for them in `files`.

The artifact is private. To let a reviewer open it, the owner shares it from the page's Share menu; say so when
handing over the link.

## Step 3: report

Give the link and, in a few lines, what the pull request contains: pages by status and language, the pages
included only because one of their images changed, and anything the script left out. Do not judge the content:
this skill shows it. For a review of the text, use `/doc-review`.

## What the preview shows

- **Pages**: every page of `fr/`, `en/`, `de/` and `nl/` that the pull request adds, changes, renames or
  deletes, plus the pages that show an image it changes (status `images`). `SUMMARY.md` changes are shown as a
  diff, since the summary sets the order and the URL of the pages.
- **Après / Avant**: the page at the head of the pull request, or as it was at the point the branch left
  `main`. In **Après**, a green margin marks the blocks added or changed, and a red line that opens holds the
  blocks removed or replaced. A block is a paragraph, a list, a table or a whole GitBook block: one changed word
  marks its whole block.
- **Comparer avec**: the same page in another language of the pull request, side by side, to check that the
  structures match.
- **Images**: taken from the pull request, at the `width` the page sets. An image the pull request adds or
  changes is outlined. A path that resolves to no file shows "Image introuvable".
- **Links**: a link to a page of the pull request opens it in the preview; any other page opens on GitHub at
  the head commit.

## Limits

- The rendering follows GitBook's blocks (hints, tabs, columns, steppers, cards, content references, expandable
  blocks, figures), not its exact fonts, spacing or navigation. A layout doubt on a new kind of block is still
  checked on the published page after the merge.
- Images wider than 1,600 px are scaled down. At most 240 images and 120 pages are included; the script says
  what it left out.
- The viewer loads two libraries from cdnjs (marked, DOMPurify): the page content is sanitized before it is
  shown.
