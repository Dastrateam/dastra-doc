---
description: >-
  Understand the questionnaire validation process in Dastra: reviewer
  approvals, final validation, revision requests and cancellation.
---

# Validate a questionnaire

Validation is the review stage that follows the finalisation of a questionnaire by its respondents. It lets the designated reviewers check every answer, request corrections where needed, then approve and publish the questionnaire.

## Response lifecycle

1. **Waiting for respondents / Started** — respondents fill in the form.
2. **Pending validation** — as soon as all **required** respondents have clicked **Finalize**, the response moves to this state and the reviewers are notified.
3. **Validated** — after all required reviewers have approved and the final validation has been performed.

From the "Pending validation" state there are three possible outcomes: **validate**, **request revisions** (send it back to the respondents) or **cancel** the questionnaire.

{% hint style="info" %}
If none of the buttons are available, check that the response really is in "Pending validation". All validation actions are blocked in any other status.
{% endhint %}

## Who validates?

Reviewers are defined when the questionnaire is scheduled (see [Schedule a questionnaire](scheduling-an-audit-or-a-pia.md)), in the **Owners** section:

* **Required reviewers** — all of them must approve the questionnaire before it can be validated. At least one required reviewer is mandatory.
* **Optional reviewers** — turn on "Add optional reviewers" to involve reviewers whose approval is tracked but **not blocking**.

Only these users can approve, validate, request revisions or cancel the response.

{% hint style="success" %}
You can disable this stage entirely when scheduling the questionnaire, with the "No validation step" option. The response is then published directly as soon as the respondents finalise it.
{% endhint %}

## The review screen

From the response, click **"Review and validate the questionnaire"**. The review screen mirrors the structure of the questionnaire: section navigation on the left, questions and answers in the centre, validation actions on the right.

### Qualifying each answer

Each question can be given an evaluation state:

* **No state** — the question has not been qualified (default, non-blocking)
* **Validated** — the answer is accepted
* **Needs revision** — the answer must be completed or corrected
* **Rejected** — the answer is refused

A selector at the top of each section applies the same state to all displayed questions at once.

For each question you can also:

* **Add an annotation** — an internal discussion with respondents and other reviewers
* **Add a task** — feeds straight into the action plan
* **Complete the justification** of the answer and **attach a file**
* **Qualify a risk** when the question is linked to one

{% hint style="warning" %}
If at least one question is marked "Needs revision" or "Rejected", approval and validation are blocked: use **"Request revisions"** to send the questionnaire back to the respondents.
{% endhint %}

## Approve the questionnaire

Each reviewer gives their approval individually, using the **"Approve questionnaire"** button:

* You can write **review comments**: they are kept and **included in the report export**.
* An **email notification** is sent to the reviewers who have not approved yet.

The **"Required approvals (n/total)"** panel summarises the state of each reviewer (approved, with the date, or "Pending approval"), plus a separate "Optional approvals" block where relevant. Each reviewer's review comments can be consulted there.

Two additional actions:

* **Revoke my approval** — withdraws your approval as long as the questionnaire has not been validated.
* If you are the **last required reviewer** to approve, Dastra immediately offers to move on to validation and publication.

## Validate and publish

The **"Validate questionnaire"** button only becomes active once **all required reviewers have approved** and no question is flagged for correction. The validation window shows:

* the number of validated questions out of the total;
* the state of the approvals;
* for a **PIA / DPIA**, the option to **apply the assessment date to the linked processing activity**;
* the option to send a **notification** to the stakeholders.

The response then moves to the **"Validated"** status with its publication date, and you are redirected to its report. You can then [export the report](export-questionnaire-report.md), generate an action plan or merge the answers into the linked object (see [Monitor questionnaires](monitor-questionnaires.md)).

## Request revisions

The **"Request revisions"** action sends the questionnaire back to the respondents:

* the response returns to "In progress" and a **new deadline** is computed from the template's delay (30 days by default);
* **every approval already given is reset**;
* a **correction round** is recorded in the response history;
* a notification is sent to each respondent, together with your review message — which you can write freely or pre-fill from an email template.

When the respondents finalise again, the validation cycle starts over.

## Cancel the questionnaire

The **"Cancel questionnaire"** action ends the cycle without publication. An optional comment lets you explain the reason; it is kept in the history and visible to the respondents. Approvals are reset and the response takes the **"Cancelled"** status: it can no longer be edited and is not compiled into the results.

## Tracking questionnaires awaiting validation

Questionnaires waiting for your approval are grouped under "Questionnaire pending validation" in your questionnaires, and flagged with the "Pending validation" badge in the lists and in the reporting views.
