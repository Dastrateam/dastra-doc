---
description: Learn how to monitor risks in Dastra.
---

# 4. Monitor

Once the risk is treated, make sure it is followed over time and spot any change. In the risk page, the **Monitoring** step is named **Treated** when the response type is **Mitigation and controls**; for another option, it carries the name of that option.

## Follow the control points

With the **Mitigation and controls** option, the section shows two indicators: the **Completion** as a percentage and the **Score** in points out of the maximum. Control points are grouped by influence: those that reduce severity and those that reduce likelihood, each with its percentage.

<figure><img src="../../../.gitbook/assets/risks-monitor-1.png" alt="Monitoring step of a risk: completion, score and control points grouped by severity and likelihood"><figcaption><p>The control points of a risk and its remediation</p></figcaption></figure>

1. Click **Assign control points** to choose the control points of the risk type.
2. On the control point concerned, click **New questionnaire**.
3. Choose the answer, enter the **Implementation date**, and add a description and files in **Send implementation proofs** if needed.
4. Click **Submit response**.

Every response is kept: the **Activity history** button of the control point lists them, and the most recent one is the current response. If the control point is assessed on a recurring basis, Dastra notifies you when the chosen number of days has elapsed.

## Effect on the current risk

After each new response, Dastra recalculates the remediation rate, then the current risk: {Current risk} = {Initial risk} - ({Initial risk} - {Residual risk}) \* {Remediation rate}. The closer the remediation gets to 100%, the closer the current risk gets to the residual risk. The calculation is detailed in the [glossary](../glossary.md).

## Follow changes over time

The module **Overview** and the workspace dashboard track how risks change: average initial, current and residual risk, average remediation, number of risks per step. The heatmap shows the initial, residual or current risk. **Reporting** details the minimum, average and maximum scores per object.

<figure><img src="../../../.gitbook/assets/risks-monitor-2.png" alt="Risk overview with the indicators and the heatmap of the current risk"><figcaption><p>The risk dashboard tracks changes over time</p></figcaption></figure>

## Archive a risk

When a risk has disappeared, click **Archive the risk**. The risk moves to the **Archive** step: you can still read it, but you can no longer edit it. To put it back under monitoring, click **Cancel** in the archive section. Only the risk owner can archive a risk or cancel its archiving.
