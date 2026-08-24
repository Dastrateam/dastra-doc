# Dastra Documentation

This repository contains the source files for the [Dastra](https://doc.dastra.eu) product documentation, published via GitBook.

Dastra is a data governance and compliance platform helping DPO, legal, technical, and business teams manage their GDPR and AI Act obligations.

## Languages

The documentation is available in four languages, each in its own folder:

| Folder       | Language |
| ------------ | -------- |
| [`fr/`](fr/) | French   |
| [`en/`](en/) | English  |
| [`de/`](de/) | German   |
| [`nl/`](nl/) | Dutch    |

Each language folder contains a `SUMMARY.md` that defines the table of contents, and a `README.md` that serves as the landing page.

## Contributing

To contribute, edit the Markdown files in the relevant language folder and open a pull request against the `main` branch. The documentation is automatically published to GitBook on merge.

- Keep changes in scope: one language per PR unless the change is structural.
- Images and assets go in the `.gitbook/assets/` subfolder of the relevant language.
- Follow the existing file naming conventions (lowercase, hyphens, no accents in file names).
