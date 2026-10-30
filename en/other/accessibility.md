---
description: >-
  Dastra’s digital accessibility policy, applied reference standards, and
  continuous improvement approach.
---

# Accessibility

## Commitment

Dastra is committed to making its digital services accessible to everyone, in compliance with international standards and applicable regulatory requirements.

Accessibility is integrated into our overall compliance and continuous improvement approach.

## Applicable standards and frameworks

Our accessibility approach is based on the following standards:

* **WCAG 2.1 (levels A and AA)** published by the W3C
* **EN 301 549**, the European standard defining accessibility requirements for digital products and services
* **RGAA**, the French operational implementation of WCAG within the national regulatory framework

WCAG defines 50 success criteria at levels A and AA.

RGAA provides a structured methodological framework to assess compliance of HTML (HTML4, XHTML1, HTML5), CSS, and JavaScript content through a set of control criteria and technical tests.

The RGAA methodology includes 106 criteria, each with multiple tests. Some rely on specific implementation techniques to limit interpretation margins.

Certain tests, particularly for dynamic interface components developed in JavaScript, require verification using assistive technologies (screen readers, keyboard navigation) within a reference environment combining browser and operating system.

Native mobile applications, software, and other specific environments are assessed directly against the relevant requirements of EN 301 549.

## Accessibility audit

A first RGAA 4.1.1 audit was carried out internally on October 16, 2025, on three pages accessible to the general public:

* The cookie banner, as displayed on www.dastra.eu
* The public page of the data subject request form
* The Privacy Hub

Internal interfaces, which require authentication, are not part of this initial scope. The audit does not produce an overall compliance rate: only these three pages were assessed.

| Page | Compliant criteria | Non-compliant criteria | Not applicable criteria |
| --- | --- | --- | --- |
| Cookie banner | 47 | 5 | 54 |
| Data subject request form | 43 | 11 | 52 |
| Privacy Hub | 56 | 3 | 47 |

Criteria 7.1 and 7.2 (display without JavaScript) are reported on all three pages. The audit considers them not applicable for the banner, which sets no cookie without JavaScript, and for the form.

## Improvement plan

Fixes are delivered progressively in the development cycles. To date, they cover:

* Criterion 3.3 (colors in interface components)
* Criterion 12.6 (navigation landmarks)
* Criterion 9.3 (list markup) and criteria 11.5 and 11.6 (field groups with a legend) on the request form

The remaining work covers:

* Keyboard navigation on the data subject request form (criteria 7.3 and 7.4)
* The label of the form's language selector (criterion 11.1)

The audit also recommends more precise text alternatives (criterion 1.1), more explicit error messages (criterion 11.11) and, for the cookie banner, placing it first in the tab order (criterion 10.7).

### Color contrast

Criterion 3.2 (text contrast) depends on the colors each customer chooses in their design settings. Contrast therefore remains the customer's responsibility: check that the colors you choose give a contrast ratio of at least 4.5:1 for body text.

## Compliance status

Last updated: October 30, 2026.

* The initial RGAA audit is complete, on three pages.
* The fixes listed above are delivered. The remaining work is still to be done.
* The detailed accessibility statement is not published yet. It will be published once the main fixes are deployed.

## Report an accessibility issue

If you encounter difficulty accessing any content or functionality, you can contact us at:

contact@dastra.eu

We are committed to responding as quickly as possible.
