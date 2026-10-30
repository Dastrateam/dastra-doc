---
description: Learn how to manage data breach notifications.
---

# Data breach notifications

## Definition

According to [Article 4.12 of the GDPR](https://gdpr-info.eu/art-4-gdpr/), a **personal data breach** is:

> _A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data transmitted, stored or otherwise processed._

In other words, it is any **security incident**, whether **intentional or accidental**, that compromises:

* **Confidentiality** (unauthorized access, disclosure),
* **Integrity** (alteration, falsification),
* **Availability** (loss, deletion, unavailability).

***

## Typical examples

* Accidental deletion of medical data not saved elsewhere.
* Loss of an unencrypted USB key containing a customer database.
* Server hack exposing email addresses and passwords.
* Email containing personal data sent to the wrong recipient.
* HR information disclosed on an unsecured shared space.

***

## Three main types of breach

| Type                | Description                                | Example                        |
| ------------------- | ------------------------------------------ | ------------------------------ |
| **Confidentiality** | Unauthorized access or disclosure          | Disclosure through phishing     |
| **Integrity**       | Unauthorized modification or falsification | Alteration of a medical record |
| **Availability**    | Accidental loss or destruction             | Data deleted without backup    |

***

## Legal obligations for the data controller

### Notification to the supervisory authority

* **Deadline**: where feasible, no later than 72 hours after becoming aware of the breach. Notification is not required when the breach is unlikely to result in a risk to the rights and freedoms of individuals.
* **Content**:
  * nature of the breach,
  * categories and volume of data involved,
  * likely consequences,
  * measures taken or planned.

> If notification cannot be made within 72 hours, the **delay must be justified**.

Reference: [Article 33 of the GDPR](https://gdpr-info.eu/art-33-gdpr/)

***

### Communication to data subjects

If the breach **presents a high risk to individuals' rights and freedoms**, they must be informed **without undue delay**:

* nature of the breach,
* data affected,
* measures taken,
* recommendations to limit the effects (e.g. change password).

Reference: [Article 34 of the GDPR](https://gdpr-info.eu/art-34-gdpr/)

***

### Mandatory internal documentation

Even when no notification is required, **every breach must be recorded** in an internal register that includes:

* the facts relating to the breach,
* its effects,
* the corrective measures taken.

> This register **demonstrates compliance** (accountability principle).

***

## The breach management cycle

1. **Detection** → Identification of an incident or abnormal behaviour.
2. **Qualification** → Verify whether personal data is involved.
3. **Risk assessment** → Impact on individuals' privacy.
4. **Notification (if required)** → Supervisory authority within 72h, data subjects if high risk.
5. **Remediation** → Corrective and preventive measures.
6. **Documentation** → Entry in the breach register.
7. **Lessons learned** → Organizational or technical adjustments.

***

## Security best practices

* Prepare an **incident management plan** and test it regularly.
* Train teams on **rapid detection and escalation** of incidents.
* Implement **preventive measures** (MFA, network segmentation, backups).
* Use a **centralized register** to track each breach and its resolution.
* Assess severity with a **standardized risk grid** (for example one published by your supervisory authority, or ISO/IEC 27005).

***

## Managing breaches in Dastra

The **Incidents** module of Dastra documents and tracks personal data breaches:

| Step         | Dastra feature                                                                                            |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Declaration  | Breach record in the record of incidents                                                                  |
| Assessment   | Risk level calculated from the probability of identification and the severity of the consequences         |
| Notification | Tracking of the notification to the authority (72-hour countdown) and of the communication to individuals |
| Monitoring   | Related tasks, measures adopted after the incident, post-mortem and history                               |
| Reporting    | **Reporting** page with indicators on incidents                                                           |

***

## Useful resources

* [ICO: reporting a data breach](https://ico.org.uk/for-organizations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/personal-data-breaches/)
* [ENISA: the EU Agency for Cybersecurity](https://www.enisa.europa.eu/)
* [ISO/IEC 27035: information security incident management](https://www.iso.org/standard/60803.html)

***

{% hint style="success" %}
**Good practice:** A quickly reported incident limits the impact, reinforces transparency and demonstrates compliance mastery. Dastra helps you structure and document each step of the process.
{% endhint %}

***

## For more information

{% content-ref url="../../features/incidents/README.md" %}
[Manage data breach notifications](../../features/incidents/README.md)
{% endcontent-ref %}

{% content-ref url="../../features/incidents/document-breach.md" %}
[Report a data breach](../../features/incidents/document-breach.md)
{% endcontent-ref %}
