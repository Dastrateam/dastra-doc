---
description: Learn what data retention periods are.
---

# Data retention period

### 📖 Definition

**Retention periods** are one of the fundamental principles of personal data protection. They derive from the principle of **storage limitation** (Article 5.1.e GDPR) and contribute to the **right to erasure**.

> 🔗 Key articles: – **Art. 5 GDPR** (storage limitation) – **Art. 30 GDPR** (documentation in the record) – **Art. 13–14 GDPR** (information to data subjects)

Concretely, for each processing activity you must determine:

* a **fixed period** (or a set of periods per phase),
* and/or an **objective criterion** for calculating it (e.g. "+3 years after the last active contact").

***

### 🔄 The data lifecycle

Retention is organised in **successive phases**. This lifecycle determines your retention rules.

| Phase                        | Purpose                    | Access                    | Example duration                     |
| ---------------------------- | -------------------------- | ------------------------- | ------------------------------------ |
| **Active use**               | Operational use            | Broad (business team)     | Duration of contract + execution     |
| **Intermediate archiving**   | Proof / defence of a right | Restricted (need-to-know) | Legal limitation period (e.g. 5 yrs) |
| **Final archiving** (public) | Historical interest        | Very restricted           | Transfer / selection by archives     |
| **Anonymisation**            | Statistics / research      | Non-identifying data      | Unlimited if truly irreversible      |
| **Deletion**                 | End of lifecycle           | —                         | At the end of the phases             |

{% hint style="info" %}
📄 Your national data protection authority's guidance on retention periods typically covers: record keeping, reference documents, archiving/disposal procedures, instructions to processors, etc.
{% endhint %}

***

### 🧭 How to determine them (methodology)

1. **Clarify the purpose** → What are you actually doing with the data? What is it used for?
2. **Map the phases** → Active use → intermediate archiving → anonymisation/deletion
3. **Identify the legal bases and references** → Sector-specific laws and regulations, DPA guidance, internal reference frameworks
4. **Set a clear rule** → "**X years after \[event]**, then **archive Y years**, then **delete**" → or "**as long as…**, then **Z years after / \[criterion]**"
5. **Organise implementation** → **Automatic** or **managed** purge, logging, proof of execution
6. **Inform and document** → Privacy notice (Art. 13–14), record (Art. 30), internal policy

{% hint style="info" %}
If there is **no clear reference**, choose a period **proportionate to the purpose** and document the reasoning (accountability).
{% endhint %}

***

### 🧪 Example rules (to be adapted)

| Context         | Data                            | Synthetic rule                                                       |
| --------------- | ------------------------------- | -------------------------------------------------------------------- |
| B2B prospects   | Identity, contact, opt-in trace | **3 years** after last active contact, then **deletion**             |
| HR – Candidates | CVs, cover letters, interviews  | **2 years** after last contact with the candidate, unless objection  |
| Customers       | Contract, invoicing             | Contract + **5 years** (proof), then **archiving/deletion**          |
| CCTV            | Images                          | **30 days max**, except incident (evidentiary procedure)             |
| Cookies         | Identifiers, preferences        | Duration consistent with the consent banner and **proof of consent** |

> These values vary according to applicable texts, your sector and your risks: **document your choices**.

***

### 👥 Who should be involved?

* **Business owner of the processing**: operational needs, triggering events
* **DPO / Legal**: compliance, applicable texts, balance of rights/freedoms
* **CISO / IT**: purge, anonymisation, access restriction, logs
* **Processors**: compliant execution of **written instructions**

***

### ✅ Controlling implementation (audits)

* Periodically verify: relevance of periods, purge execution, archiving access, anonymisation
* Log operations: disposal records, purge reports, logs
* Review upon any **change of purpose, legal basis or provider**

***

### 🧰 Implementation in Dastra

#### 1) In the **record**

* Enter a **readable rule** per dataset: "_3 years after last active contact (prospect), then deletion_"
* Add the **triggering criterion** (e.g. "date of last CRM activity", "contract end date")
* Link **references** (legal text, internal framework)

#### 2) **Automate/manage** the purge

* Schedule **recurring tasks** (reviews, purges, proof extractions)
* Use **workflows** and **reminders** for deadlines

#### 3) **Proof**

* Store disposal records, purge reports, scripts and execution tickets in the processing activity's **document management** section

***

### 🔐 Intermediate archiving & security

* Restrict access (RBAC, compartmentalisation)
* Log consultations
* Logical separation (archive vault/zone)
* Encrypt where relevant
* Plan **reversibility** with processors

***

### 🧪 Anonymisation vs pseudonymisation

* **Anonymisation**: irreversible → **outside GDPR scope** if truly non-re-identifiable
* **Pseudonymisation**: reversible with key → **still personal data** → Document the method, test **re-identifiability**, account for **auxiliary data**.

***

### 🤖 AI & retention periods

For **AI systems**, define separate retention periods for:

* **Training** (datasets, versions),
* **Validation / testing**,
* **Inference logs** (traceability, transparency),
* **Evaluation sets** (bias, robustness).

Link these periods to your **AI systems register** to ensure GDPR / AI Act consistency.

***

{% hint style="success" %}
**Good practice:** Write _actionable_ rules ("**X years after \[event]** → **purge** / **anonymisation**"), test them on a limited scope, then roll out broadly. Dastra helps you **document**, **schedule** and **prove** execution.
{% endhint %}

***

### 📘 For more information

{% content-ref url="../../features/editer-le-registre/remplir-le-questionnaire/categorie-de-donnees.md" %}
[categorie-de-donnees.md](../../features/editer-le-registre/remplir-le-questionnaire/categorie-de-donnees.md)
{% endcontent-ref %}

{% content-ref url="../../features/planifier/" %}
[planifier](../../features/planifier/)
{% endcontent-ref %}

�������������������������������������������������������������������������������������������
