# Languages

The documentation exists in four GitBook spaces: `fr/`, `en/`, `de/`, `nl/`. Every page has **the same path in
the four languages** (English slugs, lowercase, hyphens), so `fr/features/ropa/merge.md` and
`nl/features/ropa/merge.md` are the same page.

## Source and parity

- **French is the source.** A change to the product is written in `fr/` first, then in `en/`, then `de/` and
  `nl/` are translated from English.
- **A translation says the same thing as its source**: same sections, same steps in the same order, same
  hints, same figures (with screenshots taken in the page language). Wording adapts to the language; facts,
  numbers, limits and legal statements do not.
- **Each page is entirely in its language.** No French sentence left in an English page, no English heading in
  a German page. Exceptions: product and third-party names, code, API fields, and UI labels of a screen that
  the app does not translate.
- When a translation lags behind its source, report the gap; do not translate a whole page during a review
  unless asked.

## UI labels

- A label is quoted **exactly as the app shows it in the page language**, in bold. Check it in
  `Dastra.WebApp/src/assets/lang/modules/*/<lang>.json` of the Dastra repository (English pages use `en.json`,
  not `en-GB.json`), then in the backend `.resx` files when the screen text comes from the API.
- A label that cannot be found is reported as "to verify in the app". Never invent one, never translate one
  yourself.
- Data shown in a screenshot or an example (a record name, a status typed by a customer) is not a label.

## French (`fr/`)

- **Vouvoiement**, always: « vous », « votre ». Never « tu ».
- Sentence case for headings, and no capital on module names in running text: « le registre des traitements »,
  « dans l'espace de travail ».
- Accented capitals: « État », « Équipe », « À partir de ».
- French quotation marks « … » with non-breaking spaces for quoted words (UI labels are in bold, not quoted).
  A space (non-breaking when possible) before `:`, `;`, `?` and `!`.
- Numbers: « 1 000 », « 3,5 % ». Dates: « 28 octobre 2026 ».
- Upload is « importer », download is « télécharger ». Avoid anglicisms when French has the word
  (« paramétrer », not « setter » ; « tableau de bord », not « dashboard »), except in the glossary's
  technical terms (webhook, API, SSO).

## English (`en/`)

- **US English**, as in the app: organization, customize, catalog, behavior, analyze, license.
- "You", imperative for instructions. Contractions are fine in moderation (don't, can't); they keep the tone
  human.
- Sentence case for headings ("Merge processing activities", not "Merge Processing Activities").
- Watch for French calques: subcontractor (processor), actor (stakeholder), concerned person (data subject),
  processings (processing activities), control authority (supervisory authority), eventually (when it means
  "possibly"), actually (when it means "currently"), "in the case where" (if), "realize a DPIA" (carry out).

## German (`de/`)

- **Sie**, always: « Sie », « Ihr ». Never « du ».
- Nouns are capitalized, otherwise sentence case in headings.
- German quotation marks „…“ for quoted words (UI labels in bold).
- Hyphenate compounds with an English or abbreviated part: API-Schlüssel, Cookie-Banner, KI-System, E-Mail.
- Prefer the German term when the app has one; keep English only where the app does.

## Dutch (`nl/`)

- **u / uw**, always, with the matching verb forms (« u kunt », « u hebt »). Never « je », « jij », « jouw ».
  When a sentence mixes the two, rewrite the whole sentence.
- Sentence case for headings.
- Compounds written as one word or with a hyphen, never as separate words: cookiebanner, AI-systeem, API-sleutel.
- Prefer the Dutch term when the app has one.
