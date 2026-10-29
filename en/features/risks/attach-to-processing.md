---
description: >-
  Dastra lets you map the risks linked to processing activities to quickly
  assess the level of priority and the actions to take on a processing activity.
---

# Attach a risk to a processing activity

## Add a risk to a processing activity

1. Open the processing activity in the record of processing activities.
2. In the row of buttons under the title, click **Risks**. The button shows the number of risks already attached to the processing activity.

<figure><img src="../../.gitbook/assets/risks-attach-1.png" alt="Processing activity page with the Risks button and its counter in the button row"><figcaption><p>The Risks button of a processing activity</p></figcaption></figure>

3. In the panel that opens, click **Create a risk**.

<figure><img src="../../.gitbook/assets/risks-attach-2.png" alt="Risks panel of a processing activity with the matrix, the attached risks and the Create a risk button"><figcaption><p>The Risks panel of a processing activity</p></figcaption></figure>

You land on the risk edit page, with the processing activity and its organizational unit already filled in. Start entering the information about the risk you have identified, as described in [Identify](process/identify.md).

You can also attach a risk to a processing activity from the risk management module: open **Risk management** > **Risks**, choose the **Processing activity** tab and click **Create a risk**.

## View the risks of a processing activity

To see the risks of all your processing activities, open **Risk management** > **Risks** and choose the **Processing activity** tab. Each row shows the risk type, the processing activity concerned and the initial, current and residual risk levels.

<figure><img src="../../.gitbook/assets/risks-list-1.png" alt="List of the risks of the Processing activity tab, with initial, current and residual risks"><figcaption><p>The risks attached to processing activities</p></figcaption></figure>

## Risk level assessment

The risk level is calculated with the following formula:

`Risk level = probability value x impact value`

Dastra shows it in points out of the scale maximum (for example 16/25) and as a percentage. The percentage is calculated with the following formula:

`(impact x probability) / maximum score of the active risk scale`

The maximum score of the scale is 25 with the default 5-level scale (5 x 5), 16 with the 4-level scale and 9 with the 3-level scale. See [Configure the risk scale](process/assess.md#configure-the-risk-scale).

The workspace dashboard contains a **Risk management** module. It shows the averages, as percentages, of the initial, current and residual risk, the average remediation, the number of risks per step (**Total**, **Identified**, **Pending response**) and the breakdown of low, medium and high residual risks. Each average is based on the percentages calculated above.

## Go further

{% content-ref url="../tasks/README.md" %}
[Planning](../tasks/README.md)
{% endcontent-ref %}
