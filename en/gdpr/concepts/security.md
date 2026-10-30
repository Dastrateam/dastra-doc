---
description: Learn about security measures under the GDPR.
---

# Security measures

The GDPR (Article 32) requires data controllers and processors to **guarantee the security of personal data** through **appropriate technical and organizational measures**. These measures must be **proportionate to the risks** presented by the processing, the **nature of the data** and the **purposes pursued**.

> Objective: ensure the **confidentiality**, **integrity**, **availability** and **resilience** of systems and data.

***

## A risk-based approach

Before choosing measures, you must:

1. Identify the **elements to protect** (data, systems, flows).
2. Assess the **threats and vulnerabilities** (human error, attack, failure, etc.).
3. Determine the **potential impacts** (loss, disclosure, alteration…).
4. Choose **appropriate measures** to reduce these risks to an acceptable level.

> The GDPR does not prescribe a fixed list of measures: it requires measures that are **appropriate to the risk** (Article 32), taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of the processing. Each organization must **adapt** its approach to its context and be able to **demonstrate** it.

***

## Categories of security measures

### Technical measures

Technical measures act directly on information systems.

| Domain                               | Examples                                                                |
| ------------------------------------ | ----------------------------------------------------------------------- |
| **Access control**                   | Strong authentication (MFA), rights management, logging                 |
| **Encryption**                       | Data at rest and in transit, TLS certificates, managed and renewed keys |
| **Pseudonymisation / anonymization** | Logical separation, hashing, tokens                                     |
| **Backups and resilience**           | Regular backups, restoration tests, redundancy                          |
| **Application security**             | Penetration tests, patches, server hardening                            |
| **Monitoring**                       | SIEM, alerts for abnormal access, incident detection                    |

***

### Organizational measures

Organizational measures structure governance and internal behaviors.

| Domain                     | Examples                                                              |
| -------------------------- | --------------------------------------------------------------------- |
| **Security policy**        | IT charter, information security governance, incident management plan |
| **Training & awareness**   | Internal campaigns, e-learning modules, phishing simulations          |
| **Third-party management** | Contractual clauses, processor audits, regular assessments            |
| **Internal procedures**    | Authorization process, business continuity plan, periodic review      |

***

### Physical measures

Physical measures protect premises, equipment and media.

| Domain                  | Examples                                          |
| ----------------------- | ------------------------------------------------- |
| **Physical access**     | Badge control, CCTV, restricted areas             |
| **Hardware protection** | Safes, secured racks, backup power supplies       |
| **Secure destruction**  | Shredding, certified erasure, IT waste management |

***

## Security management cycle

1. **Identify**: data, systems, vulnerabilities, threats.
2. **Assess**: risks and potential impacts.
3. **Protect**: define and apply security measures.
4. **Monitor**: detect incidents, audit controls.
5. **Improve**: correct, strengthen, document actions.

***

## Security measures in Dastra

In Dastra, you can document, assess and track security measures as part of GDPR and AI Act governance:

* Describe your measures in the **Measures** repository and attach them to processing activities, assets and data breaches.
* Assess risks with the risk management module.
* Plan corrective actions with tasks and track their progress.
* Keep compliance evidence (policies, audits, proof of execution).
* Track your organization's compliance level against frameworks such as ISO 27001, in the **Compliance** module.

***

## Useful resources

* [ICO: guide to data security](https://ico.org.uk/for-organizations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/security/)
* [ISO/IEC 27001: information security management systems](https://www.iso.org/isoiec-27001-information-security.html)
* [ENISA: the EU Agency for Cybersecurity](https://www.enisa.europa.eu/)

***

{% hint style="success" %}
**Good practice:** Every new project, processor or tool must be subject to a risk assessment and an update of the associated measures.
{% endhint %}
