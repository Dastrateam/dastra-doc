---
description: Learn how to assess the level of a risk with Dastra.
---

# Risk assessment

## Risk assessment

A risk can be evaluated with the following formula:

$$
Risk=Probability∗Impact
$$

Where the **probability** is the frequency of occurrence of a hazardous event and/or a hazardous element, and the **impact** is the severity of the effects and/or the severity of the consequences of this hazardous event.

The impact of a risk is classified by default in 5 levels:

* Negligible,
* Low,
* Medium,
* High,
* Extreme.

The probability of a risk is classified by default in 5 levels:

* Remote,
* Unlikely,
* Possible,
* Likely,
* Extreme.

In the matrix, the impact is called **severity** and the probability **likelihood**.

{% hint style="info" %}
It's possible to customize the risk levels in Dastra.
{% endhint %}

## Risk classification

Depending on their level of probability and impact, risks can be classified into several categories:

* Intolerable risks;
* Risks that must be limited as much as possible;
* Acceptable risks either because the probability and/or the severity of the risk is/are negligible compared to other risks.

Intolerable risks are shown in **red** in Dastra.

Risks that should be limited as much as possible are represented in **yellow** in Dastra.

Acceptable risks are shown in **green** in Dastra.

## Gross risk and net (or residual) risk

A "**gross**" risk is considered without all of the surrounding control systems (organization, various controls, documentation, etc.)

A "**net**" (or residual) risk, on the other hand, is evaluated by taking into account all the systems already in place and effective.

## Visualization of a risk

<figure><img src="../../.gitbook/assets/risks-assess-1.png" alt="Risk assessment section: initial and residual levels, justification and risk matrix"><figcaption><p>A risk and its residual level in the risk matrix</p></figcaption></figure>

## For more information

{% content-ref url="../../features/risks/attach-to-processing.md" %}
[attach-a-risk-to-a-processing-activity.md](../../features/risks/attach-to-processing.md)
{% endcontent-ref %}

{% content-ref url="processors.md" %}
[processor-risks.md](processors.md)
{% endcontent-ref %}
