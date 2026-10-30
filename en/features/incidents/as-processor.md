---
description: >-
  Manage data breach incidents in which your organization acts as a processor
  under the GDPR.
---

# Incidents as a processor

The Incidents module of Dastra adapts to your organization's role in the incident: controller or processor. This role determines the applicable obligations and which steps are displayed in the form.

## Declare your role at creation

When you create an incident, the dialog asks **In the case of this data breach, are you a sub processor?**, with two answers:

* **No** (the default): you handle the incident as a controller. The flow is the standard one: notification to the supervisory authority, communication to the data subjects, risk assessment.
* **Yes**: you handle the incident as a processor. You do not have to notify the supervisory authority directly: that is the controller's responsibility.

<figure><img src="../../.gitbook/assets/violations-create-subprocessor.png" alt="Create an incident dialog with the processor question, Yes selected"><figcaption><p>At creation, indicate whether your organization acts as a processor</p></figcaption></figure>

To create the incident step by step, see [Document a new data breach](document-breach.md).

{% hint style="info" %}
Article 33(2) of the GDPR: the processor notifies the controller of any personal data breach without undue delay after becoming aware of it. The processor has no obligation to notify the supervisory authority directly: that obligation rests with the controller.
{% endhint %}

## Differences in the form

When you answer **Yes** to the role question, the form changes as follows:

| Element | Controller | Processor |
| --- | --- | --- |
| **Notification** step (supervisory authority) | Shown | Hidden |
| **Communication** step | Communication to the data subjects | Communication to the data controllers, with the **Data controllers** tab |

The other steps stay the same. In the **Risk assessment** step, a reminder tells you to inform the relevant controllers of the required actions so that they can act accordingly.

In the record, the **Type** filter tells incidents handled as a processor from those handled as a controller, and the **Reporting** page shows the **Role breakdown**.

## Communicate to the data controller clients

The **Communication** step of a processor incident has two tabs.

In the **Communication** tab, answer **Did you notify the relevant data controller(s)?** with **Not applicable**, **Yes** or **No**. With **Yes**, click **Add a communication** to record each message with its date. With **No**, give the reasons in **Why have you not notified the relevant data controller(s)?**.

The **Data controllers** tab lists the client controllers affected by the incident. You can:

* attach a controller with **Attach Data Controllers**;
* import the controllers automatically with **Sync Data Controllers**;
* tick **Communication sent** and **Authority notified** for each one;
* export the list with **Export list**, for your compliance file.

<figure><img src="../../.gitbook/assets/incidents-as-processor-1.png" alt="Communication step of a processor incident, Data controllers tab"><figcaption><p>The Data controllers tab, with the Attach Data Controllers, Sync Data Controllers and Export list actions</p></figcaption></figure>

### Synchronize the data controllers

If processing activities are linked to the incident (**Data processing** step), Dastra finds the client controllers from those activities and adds them to the list. Click **Sync Data Controllers** to start it. If no processing activity or AI system is linked yet, Dastra asks you to link some first.

## Best practices

* Notify your client controllers as soon as you become aware of the incident. The GDPR sets no fixed deadline for the processor, unlike the 72 hours the controller has to notify the authority, but a quick response is essential.
* Record the date and time of each communication sent to the controllers.
* Keep the acknowledgements and replies in the **Documentation** step of the incident.
