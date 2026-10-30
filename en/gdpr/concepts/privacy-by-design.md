---
description: >-
  Learn what privacy by design and privacy by default mean and how to apply them
  in Dastra.
---

# Privacy by design and by default

## Introduction

The principles of **privacy by design** and **privacy by default** are at the heart of the **GDPR**, set out in [Article 25](https://gdpr-info.eu/art-25-gdpr/). They aim to ensure that **personal data protection** is integrated **from the design phase of a project**, and that, **by default**, only the personal data necessary for each purpose is processed.

> Objective: prevent risks before they arise and demonstrate compliance at every stage of the data lifecycle.

***

## Key definitions

### Privacy by Design

The data controller anticipates data protection **from the design phase** of a product, service or processing activity.  Action is taken **upfront**, before any data collection or deployment.

### Privacy by Default

By default, only the data **necessary for each purpose** is processed. It must not be made accessible to an indefinite number of people without the data subject's intervention, so sharing or visibility options are **disabled by default**.

### Data minimisation

Process only data that is **adequate, relevant and limited** to the purpose.

### Integrity and confidentiality

Restrict access, ensure **confidentiality, integrity and availability** of data, and log all actions.

### Storage limitation

Plan **from the design phase** for the deletion, anonymization or archiving of data at the end of its useful life.

***

## Implementing Privacy by Design

The approach must be **continuous** and integrated into the **lifecycle of the processing**:

### Key steps:

1. **Identify the project**
   * Any new processing, tool or process change.
   * Alert the DPO from the study phase.
2. **Assess the impacts**
   * Map data and purposes.
   * Identify risks to individuals' rights and freedoms.
   * Launch a **DPIA** if necessary.
3. **Design appropriate measures**
   * Minimisation, compartmentalization, encryption, pseudonymization, logging.
   * Define retention periods, roles and access rights.
   * Plan mechanisms for the exercise of rights.
4. **Document compliance**
   * Include measures in the **record of processing activities**.
   * Keep evidence in the **Documentation** section of the processing activity.
   * Justify decisions (proportionality, technology choices, etc.).
5. **Monitor and improve**
   * Audit processing activities regularly.
   * Update records and action plans.

***

## Typical measures to integrate

| Objective           | Technical or organizational measure                       |
| ------------------- | --------------------------------------------------------- |
| Minimize data       | Selective collection, masking, automatic deletion         |
| Secure data flows   | Encryption, TLS, strong authentication, access management |
| Preserve rights     | Rights management portal (DSR), objection procedures      |
| Ensure transparency | Privacy notices, access logs, clear documentation         |
| Ensure traceability | Processing logs, regular audits                           |
| Control retention   | Purge, anonymization, secure intermediate archiving       |

***

## Link with accountability

**Privacy by Design** flows directly from the [accountability principle (Article 5 GDPR)](https://gdpr-info.eu/art-5-gdpr/). The data controller must be able to **demonstrate compliance at any time**.

> This means: _"Being compliant is not enough: you must be able to prove it."_

***

## Privacy by Design in Dastra

Dastra facilitates the practical implementation of **privacy by design** and **privacy by default** through its integrated modules:

### 1. Identify risks

Use the **creation request questionnaires** of the **Privacy by design** menu for each new project.

***

### 2. Assess and document risks

Conduct **DPIAs** or **risk assessments** for each processing activity.

***

### 3. Plan compliance actions

Assign **remediation tasks** and track their progress and deadlines.

***

### 4. Document in the record

Integrate security and governance measures into your **processing activity forms**, with evidence and logging.

***

## Extension: Privacy by Design and responsible AI

**Privacy by Design** also applies to **AI system governance** (AI Act). Dastra links your **AI systems** to the **processing activities** concerned, assesses compliance and documents **risk control measures**.

***

{% hint style="success" %}
**Good practice:** Anticipate compliance from the design phase: involve the DPO, document decisions, assess risks and integrate privacy safeguards by default. Dastra helps you structure this approach and demonstrate it.
{% endhint %}

***

## For more information

{% content-ref url="security.md" %}
[security-measures.md](security.md)
{% endcontent-ref %}

{% content-ref url="ropa.md" %}
[record-of-processing-activities.md](ropa.md)
{% endcontent-ref %}
