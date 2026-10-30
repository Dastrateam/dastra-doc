---
description: Learn what data retention periods are.
---

# Data retention period

## Definition

**Retention periods** are one of the fundamental principles of personal data protection. They derive from the principle of **storage limitation** (Article 5.1.e GDPR) and contribute to the **right to erasure**.

Key articles:

* **Article 5 GDPR** (storage limitation);
* **Article 30** (documentation in the record);
* **Articles 13 and 14** (information to data subjects).

Concretely, for each processing activity you must determine:

* a **fixed period** (or a set of periods per phase),
* and/or an **objective criterion** for calculating it (e.g. "+3 years after the last active contact").

***

## The data lifecycle

Retention is organised in **successive phases**. This lifecycle determines your retention rules.

| Phase                        | Purpose                    | Access                    | Example duration                     |
| ---------------------------- | -------------------------- | ------------------------- | ------------------------------------ |
| **Active use**               | Operational use            | Broad (business team)     | Duration of contract + execution     |
| **Intermediate archiving**   | Proof / defense of a right | Restricted (need-to-know) | Legal limitation period (e.g. 5 yrs) |
| **Final archiving** (public) | Historical interest        | Very restricted           | Transfer / selection by archives     |
| **Anonymization**            | Statistics / research      | Non-identifying data      | Unlimited if truly irreversible      |
| **Deletion**                 | End of lifecycle           | Not applicable            | At the end of the phases             |

{% hint style="info" %}
Your national data protection authority's guidance on retention periods typically covers: record keeping, reference documents, archiving/disposal procedures, instructions to processors, etc.
{% endhint %}

***

## How to determine them (methodology)

1. **Clarify the purpose** → What are you actually doing with the data? What is it used for?
2. **Map the phases** → Active use → intermediate archiving → anonymization/deletion
3. **Identify the legal bases and references** → Sector-specific laws and regulations, DPA guidance, internal reference frameworks
4. **Set a clear rule** → "**X years after \[event]**, then **archive Y years**, then **delete**" → or "**as long as…**, then **Z years after / \[criterion]**"
5. **Organise implementation** → **Automatic** or **managed** purge, logging, proof of execution
6. **Inform and document** → Privacy notice (Art. 13–14), record (Art. 30), internal policy

{% hint style="info" %}
If there is **no clear reference**, choose a period **proportionate to the purpose** and document the reasoning (accountability).
{% endhint %}

***

## Example rules (to be adapted)

| Context         | Data                            | Synthetic rule                                                       |
| --------------- | ------------------------------- | -------------------------------------------------------------------- |
| B2B prospects   | Identity, contact, opt-in trace | **3 years** after last active contact, then **deletion**             |
| HR, candidates | CVs, cover letters, interviews  | **2 years** after last contact with the candidate, unless objection  |
| Customers       | Contract, invoicing             | Contract + **5 years** (proof), then **archiving/deletion**          |
| CCTV            | Images                          | **30 days max**, except incident (evidentiary procedure)             |
| Cookies         | Identifiers, preferences        | Duration consistent with the consent banner and **proof of consent** |

> These values vary according to applicable texts, your sector and your risks: **document your choices**.

***

## People to involve

* **Business owner of the processing**: operational needs, triggering events
* **DPO / Legal**: compliance, applicable texts, balance of rights/freedoms
* **CISO / IT**: purge, anonymization, access restriction, logs
* **Processors**: compliant execution of **written instructions**

***

## Controlling implementation (audits)

* Periodically verify: relevance of periods, purge execution, archiving access, anonymization
* Log operations: disposal records, purge reports, logs
* Review upon any **change of purpose, legal basis or provider**

***

## Implementation in Dastra

### 1) In the **record**

* Enter a **readable rule** per dataset: "_3 years after last active contact (prospect), then deletion_"
* Add the **triggering criterion** (e.g. "date of last CRM activity", "contract end date")
* Link **references** (legal text, internal framework)

### 2) **Automate/manage** the purge

* Schedule **tasks** (reviews, purges, proof extractions)
* Use **workflow rules** and **regular reviews** for deadlines

### 3) **Proof**

* Store disposal records, purge reports, scripts and execution tickets in the **Documentation** section of the processing activity

***

## Intermediate archiving & security

* Restrict access (RBAC, compartmentalization)
* Log consultations
* Logical separation (archive vault/zone)
* Encrypt where relevant
* Plan **reversibility** with processors

***

## Anonymization vs pseudonymization

* **Anonymization**: irreversible → **outside GDPR scope** if truly non-re-identifiable
* **Pseudonymisation**: reversible with key → **still personal data** → Document the method, test **re-identifiability**, account for **auxiliary data**.

***

## AI & retention periods

For **AI systems**, define separate retention periods for:

* **Training** (datasets, versions),
* **Validation / testing**,
* **Inference logs** (traceability, transparency),
* **Evaluation sets** (bias, robustness).

Link these periods to your **AI systems register** to ensure GDPR / AI Act consistency.

***

## Useful references

* Retention guidance published by your national supervisory authority (for example, the CNIL guide on retention periods in France)
* Sector-specific laws and regulations that set minimum or maximum retention periods
* Codes of conduct and standards for your sector
* Collective agreements

***

{% hint style="success" %}
**Good practice:** Write _actionable_ rules ("X years after \[event], then purge or anonymization"), test them on a limited scope, then roll out broadly. Dastra helps you **document**, **schedule** and **prove** execution.
{% endhint %}

***

## For more information

{% content-ref url="../../features/ropa/activity/datasets.md" %}
[Datasets and retention](../../features/ropa/activity/datasets.md)
{% endcontent-ref %}

{% content-ref url="../../features/tasks/README.md" %}
[Planning](../../features/tasks/README.md)
{% endcontent-ref %}
