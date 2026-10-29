---
description: >-
  The results of the RGAA accessibility audit of the cookie management banner
  and the points to fix.
---

# RGAA compliance

This page presents the results of the latest accessibility audit of the cookie management banner, carried out against the French general accessibility improvement framework (RGAA).

## Audit of October 16, 2025

* **Framework**: RGAA 4.1.1.
* **Type of audit**: internal audit (initial visit) of the banner as displayed on www.dastra.eu.
* **Result**: 47 criteria compliant, 5 not compliant and 54 not applicable.

{% hint style="info" %}
The audit grid does not calculate an overall compliance rate. This audit is not a declaration of full compliance of the banner.
{% endhint %}

## Non-compliant points

| Criterion | Finding | Follow-up |
| --- | --- | --- |
| 3.2 Text contrast | Body text, gray on a white background, has a contrast of 3.98:1 where 4.5:1 is required. The "Notre politique de cookies" link, orange on white, is also concerned. | Depends on the colors chosen in the banner settings. See below. |
| 3.3 Colors of interface components | Bold words use the same color as body text. | The grid says "corrigé" (fixed). The SDK of version 3.0.0 displays bold words in a darker shade than body text. |
| 7.1 and 7.2 Display without JavaScript | The banner does not appear without JavaScript. | The auditor notes that, without JavaScript, no cookie is set: there is then no consent to collect. |
| 12.6 Navigation landmarks | The link to the cookie policy is not inside a navigation landmark. | The grid says "corrigé" (fixed). The SDK of version 3.0.0 places this link in a `<nav>` element, on the welcome screen and on the preferences screen. |

The audit also recommends placing the banner first in the tab order (criterion 10.7, compliant).

### Contrast: your settings matter

The colors of the banner text and links come from the settings of each banner: **Main text color** and **Primary color** in the **Templating of the banner** section. Contrast is therefore your choice: Dastra cannot guarantee it for every banner. Check that text and links have a contrast of at least 4.5:1 with the background. See [Set up the cookie consent banner](banner/configure.md).

## 2021 report

The previous audit dates from March 16, 2021. It covers the RGAA 4.1 grid, it is written in French and it predates several changes to the banner (Global Privacy Control, the "Continue without accept" button, shapes of the floating button). It remains available as a historical reference.

{% file src="../../.gitbook/assets/audit-rgaa.zip" %}
Download the 2021 RGAA audit report
{% endfile %}
