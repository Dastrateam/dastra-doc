# Style

The documentation is read by DPOs, lawyers and compliance teams, most of them non-technical, often while they
are in the middle of a task in Dastra. They want to know what to do, where to click and why it matters for
compliance. The voice is that of a knowledgeable colleague: **human and warm, but serious**.

## Voice

- **Talk to the reader.** Use the form of address of the page language (see `languages.md`) and give
  instructions in the imperative: "Click **Add**", not "The user clicks Add" or "You will need to click Add".
- **Be direct.** Say what the feature does and what the reader does with it. Active voice, present tense.
- **Explain why when it helps the reader decide.** One sentence linking a step to the obligation it serves
  (Article 30, a retention rule, a supervisory authority's expectation) is welcome. A paragraph of general GDPR
  context in the middle of a procedure is not: link to the "useful reminders" page instead.
- **Be precise about the law.** Use the terms of the glossary, and never soften or overstate an obligation:
  "required by Article 30" and "recommended by the CNIL" are different claims.
- **Warm means plain and helpful**: a concrete example from the reader's work, a tip that saves a step, a
  reassuring sentence before an irreversible action. It does not mean exclamation marks, jokes, familiarity or
  enthusiasm.
- **Short sentences, one idea per paragraph.** Aim for sentences under 25 words and paragraphs of 1 to 4
  sentences. Split a sentence that chains three clauses.
- **No sales tone.** The documentation describes the product; it does not sell it. No superlatives, no
  promises about time saved, no "we believe".

## Writing markers to remove

Text that reads as machine-written or as marketing loses the reader's trust. `scripts/lint_doc.py` flags the
phrases it can match; the reading pass catches the patterns a regex cannot.

| Marker | Examples to rewrite | What to write instead |
| --- | --- | --- |
| Hype adjectives and verbs | seamless, robust, powerful, comprehensive, leverage, empower, streamline, unlock; puissant, incontournable, optimal ; nahtlos, leistungsstark ; naadloos, krachtig | The concrete fact: what it does, for whom. |
| Easiness claims | easily, simply, just click, in a few clicks; facilement, simplement, il suffit de, en quelques clics ; ganz einfach, mit wenigen Klicks ; eenvoudig (as an adverb), gewoon, simpelweg | Drop the adverb and give the step. If it is easy, the reader will see. |
| Sales openers | The good news is, At Dastra we believe, as smoothly as possible; Bonne nouvelle, Chez Dastra, nous pensons | State the fact. |
| Empty intros and outros | In this article we will see, In summary, In conclusion, Feel free to; Dans cet article, nous allons voir ; En résumé ; N'hésitez pas à | Start with the first useful sentence. End when the procedure ends. Replace "feel free to contact us" by the actual channel when it matters. |
| Signposting | It is worth noting, It is important to note, Keep in mind that; Il est important de noter, Notez que ; Bitte beachten Sie ; Houd er rekening mee dat | Say the thing. Use a `warning` hint if it is truly important. |
| Vague link text | click here, see this page; cliquez ici ; hier klicken ; klik hier | Name the destination: "see [Share the record](share.md)". |
| Rhetorical cadence | not only X but also Y; whether you are X or Y; three adjectives in a row; a colon that announces a reveal ("The result: …"); questions as headings when the page is not a FAQ | One plain statement. |
| Conversational leftovers | "If you want, I can…", "Certainly", "I hope this helps"; « Si tu veux, je peux… », « Bien sûr ! » | Delete. These are leftovers from an AI tool and must never be published. |
| Fake precision | "(1 min)" timings on steps, "in just 3 steps" | Delete. |
| Bold for emphasis | **whole sentences** or several **key ideas** per paragraph | Bold is for UI labels. At most one term in bold where it is defined. |
| Bold lead-in lists | "**Simplicity:** …", "**Flexibility:** …" on every bullet | A plain list, or short paragraphs with real headings. |

Weak signals, to rewrite only when a direct verb reads better: "allows you to", "enables you to", "in order to";
« permet de », « afin de » ; "ermöglicht es Ihnen", "einfach" ; "stelt u in staat om".

## Typography

- **No emojis**, anywhere: page titles, headings, body, tables, hints, captions, and the group headings of
  `SUMMARY.md`.
- **No em dash (—)**, and no spaced en dash ( – ) used as a dash. Use a comma, a colon, parentheses or two
  sentences. An en dash in a range (1–3) is fine.
- **No exclamation marks.**
- **No ellipsis to trail off** ("how easily you can reach the people…"). Finish the list or write "etc.".
- **Headings in sentence case**: capital on the first word and on proper nouns only (plus German nouns). No
  all-caps headings, no numbered H1, no trailing punctuation.
- **UI labels in bold**, exactly as on screen: "Click **Create data processing**". Not in quotes, not in
  italics. Menu paths with `>`: **Settings** > **Integrations**.
- **Code, endpoints, field names and values in backticks**: `POST /v1/datasubjectrequests`, `client_id`.

## Page structure

- One `#` title per page, identical to the label in `SUMMARY.md`.
- Front matter keys stay in English whatever the page language (`description:`, never `beschrijving:`): GitBook
  ignores any other key. The value of `description` is written in the page language.
- The first paragraph says what the page covers and who it is for, in one or two sentences. No "Introduction"
  or "Overview" heading when the introduction is one paragraph.
- Headings go down one level at a time (`##` under `#`, `###` under `##`) and state the topic, not a question,
  except in a FAQ.
- Procedures are numbered lists, one action per step, the expected result after the step when it is not obvious.
- Use `{% hint %}` sparingly: `info` for a useful precision, `warning` before something that could go wrong,
  `danger` before an irreversible action, `success` almost never. Two hints per page is already a lot.
- Every figure has an `alt` text describing what it shows and, when it adds something, a short caption. The
  screenshot shows the app in the page language.
- Links to other pages use relative paths to the `.md` file, and the target must exist. Link text says where it
  goes ("see [Merge processing activities](merge.md)"), never "click here". A link to dastra.eu points to the
  page language (`/fr/`, `/en/`, `/de/`; Dutch pages use `/en/`).

## Editing GitBook files safely

- Keep GitBook syntax intact: `{% hint %}`, `{% tabs %}`, `{% content-ref %}`, `{% embed %}`, `<figure>`, `<a id>`
  anchors, front matter. `&#x20;` escapes are export artifacts: leave them.
- Never rename a file or change a path: paths are the published URLs.
- In `SUMMARY.md`, the published URL of a group is the `id` of its `<a>` anchor, or the slugified title when it
  has none. Before changing a group heading that has no anchor (removing an emoji, fixing its case), add
  `<a href="#slug" id="slug"></a>` with the slug currently published, so the URLs of its pages do not move.
  Page entries in `SUMMARY.md` must keep matching the `#` title of their page.
