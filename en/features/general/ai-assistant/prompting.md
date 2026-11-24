---
description: >-
  Phrase your requests to Dastra AI so the answers are complete and sourced: five habits, tested example requests, how to check an answer and how to turn a request you repeat into a skill.
---

# Write effective requests

Dastra AI answers from your workspace, so the answer is only as precise as the request. Name the records you mean, say what you want back and, in Edit mode, ask it to look before it acts. This page gives five habits, example requests and the way to check an answer.

The examples were tested in a demo workspace, the one of a fictitious retailer, Brightmoor Retail Group. Replace its record names with yours.

## Five principles

### Name the scope with the app's words

When a request names a group of records that Dastra does not know as such, the assistant has to guess which ones you mean. List the records, or use the words of the app: processing activity, data subject request, organizational unit.

| Instead of | Write |
| --- | --- |
| `Compare the retention periods of our marketing processing activities and flag the ones that look inconsistent. Answer as a table.` The assistant chose three activities and left out others of the same kind. | `Compare the retention periods of these processing activities: Newsletter and promotional emails, Newsletter campaigns, Targeted advertising and retargeting, Personalised product recommendations and Brightmoor Rewards loyalty programme. Show each activity's retention rule and period in a table and flag any that look inconsistent.` Five rows, each with its retention rule and a flag. |
| `Add the tag "Reviewed 2026" to the processing activities of Brightmoor UK Ltd.` The assistant read "entity" as the name of a record and offered an unrelated activity. | `Add the tag "Reviewed 2026" to the processing activities of the Legal & Compliance department of Brightmoor Retail Group.` Edit mode. The assistant found the organizational unit, saw that the tag did not exist and stopped at an authorization card to create it. |

### Ask for the evidence, not just the verdict

A yes or no question is answered from a flag in the register. Ask for the data behind it, then for the flag.

| Instead of | Write |
| --- | --- |
| `Which processing activities process health or other sensitive data and have no DPIA?` Two right activities, but only from the sensitive-data flag, and no health data identified. | `List all processing activities with their data categories and whether a DPIA is recorded. Then flag those that process special-category data, such as health data, and have no DPIA. Answer as a table.` Every activity in a table, the same two flagged, and the reason: a linked dataset contains sick leave certificates. |

### Give context with `@` or by opening the record

On a record, the assistant starts from what the record holds: its counters, its linked measures and vendors. Two ways to give it that context:

* Open the record and press **Ctrl+J** (**Cmd+J** on Mac). The record is attached above the message box. The panel reopens the previous conversation: click **New conversation** first.
* Type `@` and a few letters of the record name, then pick the row. The mention becomes a chip in your message. The menu lists records and documents, sometimes with close names: pick the row of the right type.

The [Analyze examples](#example-requests-by-goal) below use both.

### Ask for the format, then iterate in the same conversation

Say how you want the answer: a table, the columns, the order, a number of lines. Then refine in the same conversation. A follow-up reuses the previous list instead of searching again, so the new answer stays consistent with it.

1. `List the data subject requests that are not closed, with their type, requester and due date, oldest first.`
2. `Now group them by request type and count them.`

### Find, then act

In Edit mode, a request that creates something from a general description gives a general result. Ask the assistant to list what is missing first, then to act on that list.

| Instead of | Write |
| --- | --- |
| `Create an action plan with three tasks to complete the processing activity "Supplier and contract management".` The tasks were generic supplier-management tasks and missed the gaps of the record. | `First list what is missing in the processing activity "Supplier and contract management". Then create an action plan with one task for each of the three most important gaps.` Edit mode. Three High tasks that match the gaps: retention periods, personal data inventory and purposes, recipients and transfers. |

Every change of Edit mode stops at an **Authorization required** card: see [Read the authorization card](#read-the-authorization-card).

## Example requests by goal

Each request below was tested as written. The mode is the one it was tested in. The requests of the principles above are examples too: the retention comparison and the sensitive data question for analyzing and finding, the tag and the action plan for changing records.

| Goal | Write | Mode |
| --- | --- | --- |
| Find | `List the data subject requests that are not closed, with their type, requester and due date, oldest first.` | **Ask** |
| Analyze a record | `Summarize this processing activity in five lines, then list what is missing to complete it.` From the panel opened on the processing activity "Supplier and contract management". | **Ask** |
| Analyze a record | `@Online order management Which security measures would you expect for this processing that are not linked yet?` The mention is a chip. | **Ask** |
| Iterate | `Keep only the ones created this year.` In the conversation of the list above. | **Ask** |
| Iterate | `Now group them by request type and count them.` In the same conversation. | **Ask** |
| Draft | `Draft a reply to request 2BEX36WB, in English, formal tone, confirming we received it and that we will answer within one month.` Nothing is sent or saved: copy the draft with **Copy**. | **Ask** |
| Build an artifact | `Draw a diagram of the data flows of the Online order management processing activity.` The answer links to an [artifact](artifacts.md). | **Ask** |
| Run a skill | `/dpo_opinion`, then in the same conversation: `This message is the referral, made today by Emma Walsh, DPO. Question: can this processing activity stay published while its retention rule and personal data fields are missing?` On the processing activity "Supplier and contract management". | **Ask** |

## Check and steer the answer

### Read the steps and the sources

Under an answer, a line such as **3 tool(s) used** tells you what the assistant did. Click **Show tools** to see the steps, for example Browsing records or Reading a record. If the steps do not match what you meant, rephrase the scope.

Records are named in the answer, not linked: in a table, the rows are plain text. Search the name in the register to open the record.

The assistant also says what it could not establish. In the tests, it noted that a measure "not linked" does not prove that it is "not implemented", that due dates are in UTC, and that the routes of a diagram beyond the recorded purposes are indicative. Read these sentences: they tell you what to check.

{% hint style="info" %}
An answer is a proposal to check, not a conclusion. See [AI as a starting point, not a final answer](README.md#ai-as-a-starting-point-not-a-final-answer).
{% endhint %}

### Read the authorization card

In **Edit** mode, the assistant shows an **Authorization required** card before each change. It names the tool, for example **Creating a tag** or **Creating an action plan**. Click **Show arguments** to see exactly what it is about to send: the records, the labels, the tasks.

**Decline** changes nothing. The assistant confirms it ("no tasks were created") and offers to revise. If you send another message while a card is waiting, the card no longer applies. The choices of the card are described in [Ask and Edit modes](README.md#ask-and-edit-modes).

### Rate the answer

Click **Good response** or **Bad response** under an answer. A **Bad response** opens a window where you can say what was wrong. Dastra stores the rating and the comment with the message.

## Good to know

* Check the mode before you send. The mode is **Edit** by default for users who can edit. Switch to **Ask** for a question that must not change anything.
* Start a new conversation for a new topic. The panel reopens the previous conversation: click **New conversation** at the top of the panel. A follow-up works on the previous answer, a new topic does not need it.
* Check the row you pick in the `@` menu. It mixes records and documents, and a document can have a name close to a record's.
* A skill needs its inputs in the message. `/dpo_opinion` alone only asks for the referral: who made it, when, and the question.

## Turn a request you repeat into a skill

If you retype the same request often, save it as a skill and recall it with `/`. A skill keeps your wording, and your team can share it. See [Skills](agents/skills.md).
