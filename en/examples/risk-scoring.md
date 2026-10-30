---
description: >-
  Compute one risk step by step on the default 5×5 scale and on the CNIL 4×4
  scale, then see how the score of a data breach is calculated.
---

# Risk scoring

This example scores a risk of Brightmoor Retail Group twice, on two scales, then scores a data breach. The two calculations differ: the score of a risk is a product, the score of a data breach is a sum.

## The risk

Brightmoor identifies the risk "Loss of customer payment data" on the processing activity "Online order management". In the **Risk assessment** section, Emma Walsh, the data protection officer, chooses a **Severity** and a **likelihood** for the initial risk, then for the residual risk once the controls are in place. See [Assess a risk](../features/risks/process/assess.md) for the screen.

The score of a risk is **severity × likelihood**. The maximum score of a scale is the product of its two highest levels. Dastra shows the score as "score / maximum" and, in some views, as a percentage of the maximum.

## On the default 5×5 scale

The default scale, **Default risk heatmap**, has five levels for each axis.

| Level | Severity | Likelihood |
| --- | --- | --- |
| 1 | Negligible | Remote |
| 2 | Low | Unlikely |
| 3 | Medium | Possible |
| 4 | High | Likely |
| 5 | Extreme | Extreme |

Brightmoor assesses the initial risk as **High** severity (4) and **Possible** likelihood (3). Card payments are processed by an external provider, but the order database holds the last digits and the billing address. After the controls (encryption, access reviews), the residual likelihood falls to **Remote** (1).

| Risk | Severity | Likelihood | Calculation | Score | Percentage | Matrix cell |
| --- | --- | --- | --- | --- | --- | --- |
| Initial | 4 | 3 | 4 × 3 | 12 / 25 | 48% | red |
| Residual | 4 | 1 | 4 × 1 | 4 / 25 | 16% | green |

<figure><img src="../.gitbook/assets/examples-risk-1.png" alt="Risk assessment section with the initial and residual risks placed on the 5 by 5 matrix"><figcaption><p>The risk on the default scale</p></figcaption></figure>

The percentage is the score divided by the maximum (25), rounded. The colour of the cell comes from the matrix of the scale: with five levels, the row is the severity counted from the top and the column is the likelihood.

The current risk lies between the two. After each response to a control point, Dastra recalculates it with this formula: current risk = initial risk − (initial risk − residual risk) × remediation rate. With a remediation rate of 50%, the current risk is 12 − (12 − 4) × 0.5 = 8. See [Effect on the current risk](../features/risks/process/monitor.md#effect-on-the-current-risk).

## On the CNIL 4×4 scale

Brightmoor decides to use the four-level scale of the CNIL method for privacy impact assessments. In **Workspace settings** > **Risk management**, a scale is created with the **Risk profile template** **4 levels - Classic DPIA** and enabled with **Save and enable the profile** (see [Configure the risk scale](../features/risks/process/assess.md#configure-the-risk-scale)).

| Level | Severity | Value | Likelihood | Value |
| --- | --- | --- | --- | --- |
| 1 | Negligible | 10,000 € | Remote | 25% |
| 2 | Low | 50,000 € | Unlikely | 50% |
| 3 | Medium | 100,000 € | Possible | 75% |
| 4 | High | 1,000,000 € | Likely | 100% |

<figure><img src="../.gitbook/assets/examples-risk-2.png" alt="Risk scale editor with the four-level matrix of the CNIL template"><figcaption><p>The 4 levels - Classic DPIA scale</p></figcaption></figure>

The values are the defaults of the template. They are editable, like the labels.

The same assessment, **High** severity (4) and **Possible** likelihood (3), now gives:

| Risk | Severity | Likelihood | Calculation | Score | Percentage | Matrix cell |
| --- | --- | --- | --- | --- | --- | --- |
| Initial | 4 | 3 | 4 × 3 | 12 / 16 | 75% | red |
| Residual | 4 | 1 | 4 × 1 | 4 / 16 | 25% | orange |

The score is identical, but the maximum is lower, so the same risk weighs more: 75% instead of 48%, and the residual risk is orange instead of green. This is why Dastra asks for a confirmation before enabling another scale when risks exist, and why you should choose the scale before entering your first risks (see the [FAQ](../features/risks/faq.md)).

## A data breach

The incident module does not use the risk scales. In the **Risk assessment** step of a data breach, answer **No** to **Risk assessment done?**, then choose two scores from 1 to 4:

* **Data subject identification probability**: how easy it is to identify people from the data;
* **Impact on data subject**: the consequences for them.

The labels of the four values are **1 - Negligible**, **2 - Limited**, **3 - Important** and **4 - Maximum**. The score of the breach is their **sum**, from 2 to 8, and it sets the **Risk level**:

| Sum of the two scores | Risk level | Consequence displayed by Dastra |
| --- | --- | --- |
| 2 and 3 | Low risk | Notification to the supervisory authority and communication to persons are not necessary |
| 4 and 5 | Medium risk | You must notify the supervisory authority |
| 6 to 8 | High risk | Notification to the supervisory authority and communication to data subjects mandatory |

Brightmoor discovers that a customer export was readable for a few hours in a misconfigured storage space. It contains names, email addresses and order histories.

| Case | Identification | Impact | Calculation | Score | Risk level |
| --- | --- | --- | --- | --- | --- |
| Export of order numbers only | 2 | 1 | 2 + 1 | 3 | Low risk |
| Export of names without contact data | 3 | 1 | 3 + 1 | 4 | Medium risk |
| Export of the customer file | 4 | 2 | 4 + 2 | 6 | High risk |

For the third case, a product would give 4 × 2 = 8, but Dastra adds the scores: 4 + 2 = 6. This is already a **High risk**, so the notification to the supervisory authority and the communication to the data subjects are mandatory. See [Document a new data breach](../features/incidents/document-breach.md#risk-assessment-step) for the step and the 72-hour counter.

{% hint style="info" %}
With **Risk assessment done?** set to **Yes**, you enter your own analysis and choose the level yourself in **Risk assessment conclusion**. The level you choose replaces the calculated one.
{% endhint %}
