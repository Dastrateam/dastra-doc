---
description: >-
  Understand the questionnaire validation process in Dastra: approver
  approvals, final validation, revision requests and cancellation.
---

# Validate a questionnaire

Validation is the review stage that follows the finalization of a questionnaire by its respondents. It lets the designated approvers check every answer, request corrections where needed, then approve and publish the questionnaire.

## Response lifecycle

1. **Waiting for respondents / Started**: respondents fill in the form.
2. **Pending validation**: as soon as all **required** respondents have clicked **Finalize**, the response moves to this state and the approvers are notified.
3. **Validated**: after all required approvers have approved and the final validation has been performed.

From the "Pending validation" state there are three possible outcomes: **validate**, **request revisions** (send it back to the respondents) or **cancel** the questionnaire.

{% hint style="info" %}
If none of the buttons are available, check that the response really is in "Pending validation". All validation actions are blocked in any other status.
{% endhint %}

## Who validates?

Reviewers are defined when the questionnaire is scheduled (see [Schedule a questionnaire](schedule.md)), in the **Approvers** section:

* **Required approvers**: all of them must approve the questionnaire before it can be validated. At least one required approver is mandatory.
* **Optional approvers**: turn on **Add optional approvers** to involve approvers whose approval is tracked but **not blocking**.

<figure><img src="../../.gitbook/assets/questionnaires-validate-1.png" alt="Approvers section of the scheduling form with the required and optional approvers"><figcaption><p>The Approvers section of the scheduling form</p></figcaption></figure>

The approvers proposed by default are set in the template's configuration, with the **Default questionnaire approvers** field (see [Create a questionnaire template](templates/README.md)). Only the approvers of the response can approve, validate, request revisions or cancel it.

{% hint style="success" %}
You can disable this stage entirely when scheduling the questionnaire, with the **Disable review step** option. The response is then published directly as soon as the respondents finalize it.
{% endhint %}

## The review screen

From the response, click **Review and validate the questionnaire**. The review screen mirrors the structure of the questionnaire: section navigation on the left, questions and answers in the center, validation actions on the right.

### Qualifying each answer

Each question can be given an evaluation state:

* **No state**: the question has not been qualified (default, non-blocking)
* **Validated**: the answer is accepted
* **Needs revision**: the answer must be completed or corrected
* **Rejected**: the answer is refused

A selector at the top of each section applies the same state to all displayed questions at once.

For each question you can also:

* **Add an annotation**: an internal discussion with respondents and other approvers
* **Add a task**: feeds straight into the action plan
* **Complete the justification** of the answer and **attach a file**
* **Qualify a risk** when the question is linked to one

{% hint style="warning" %}
If at least one question is marked "Needs revision" or "Rejected", approval and validation are blocked: use **"Request revisions"** to send the questionnaire back to the respondents.
{% endhint %}

## Approve the questionnaire

Each approver gives their approval individually, using the **"Approve questionnaire"** button:

* You can write **review comments**: they are kept and **included in the report export**.
* An **email notification** is sent to the approvers who have not approved yet.

The **"Required approvals (n/total)"** panel summarizes the state of each approver (approved, with the date, or "Pending approval"), plus a separate "Optional approvals" block where relevant. Each approver's review comments can be consulted there.

Two additional actions:

* **Revoke my approval**: withdraws your approval as long as the questionnaire has not been validated.
* If you are the **last required approver** to approve, Dastra immediately offers to move on to validation and publication.

## Validate and publish

The **"Validate questionnaire"** button only becomes active once **all required approvers have approved** and no question is flagged for correction. The validation window shows:

* the number of validated questions out of the total;
* the state of the approvals;
* for a **PIA / DPIA** linked to a processing activity, the message "The date of the last DPIA of the linked data processing record will be updated.": the processing activity's **Last DPIA Date** is updated automatically upon validation;
* the option to send a **notification** to the stakeholders.

The response then moves to the **"Validated"** status with its publication date, and you are redirected to its report. You can then [export the report](export.md), generate an action plan or merge the answers into the linked object (see [Monitor questionnaires](monitor.md)).

Upon validation, each respondent, internal or external, receives a notification email stating the questionnaire, the workspace and the validation date, with a link to their end screen. On that screen, the **Export to PDF** action lets them download their questions and answers, without a Dastra account. The export is only available once the questionnaire is validated, and each respondent can only export the questionnaire they answered. To validate without notifying, untick the notification option in the validation window.

## Request revisions

The **"Request revisions"** action sends the questionnaire back to the respondents:

* the response returns to "In progress" and a **new deadline** is computed from the template's delay (30 days by default);
* **every approval already given is reset**;
* a **correction round** is recorded in the response history;
* a notification is sent to each respondent, together with your review message, which you can write freely or pre-fill from an email template.

When the respondents finalize again, the validation cycle starts over.

## Cancel the questionnaire

The **"Cancel questionnaire"** action ends the cycle without publication. An optional comment lets you explain the reason; it is kept in the history and visible to the respondents. Approvals are reset and the response takes the **"Cancelled"** status: it can no longer be edited and is not compiled into the results.

## Tracking questionnaires awaiting validation

To find the questionnaires waiting for your approval, open **My responses** and filter on the **Pending validation** status. The same badge flags these responses in the lists and in the reporting views.
