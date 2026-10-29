# FAQ

## Do requesters receive an email notification when a request is closed?

By default, no email is sent. The closure notification goes to the requester only if you select the **Send a notification to** box (followed by the requester's email address) in the closing dialog. The box appears only when the request has an email address, and it is greyed out when the requester has already been notified.

<figure><img src="../../.gitbook/assets/requests-faq-1.png" alt="The request closing dialog with the notification box selected"><figcaption><p>The notification box in the closing dialog</p></figcaption></figure>

{% hint style="info" %}
Select this option when you want to inform the data subject that their request has been resolved. It is good practice, and it helps you demonstrate that you met the GDPR response deadline.
{% endhint %}

***

## How long does the requester keep access to the secure space after closure?

Once the request is closed, the requester keeps access to their secure space (exchange history, documents sent) for **60 days**. During this period, they can still send a message to the person handling the request through the conversation interface.

After 60 days, access is revoked automatically.

## How does the requester's email verification work?

When a request is submitted from the public form, the requester receives a confirmation email containing a **validation link** and a **6-digit code**. The request is only taken into account once the address has been validated.

* The link and the code are valid for **24 hours**. This duration cannot be configured.
* After several incorrect code entries (4), further attempts are **blocked for 30 minutes**.
* If the deadline is exceeded, the requester must submit a new request.

## Why can't a requester submit a new request?

The same requester (same email address) cannot submit a second request of the **same type** in the same workspace while the previous one, submitted less than 24 hours ago, has not been closed.

## What is the maximum length of a message in a request?

Messages exchanged with the requester, the public form message and closure reasons are limited to **3,000 characters**. A message can contain up to **20 attachments**.

***

## Does the request collection page set cookies? Do I need a consent banner?

No. The Dastra widget page (URL of the form `https://api.dastra.eu/v1/client/data-subject-request/page?id=…`) sets **only one cookie**: `acaAffinity`.

This is a **load-balancing** cookie (Azure Application Gateway). Its only function is to keep the server session stable by routing requests to the same backend node. It lasts for the **session**, is secure (`Secure`, `HttpOnly`) and falls under the **consent exemption** of Article 5(3) of the ePrivacy Directive, confirmed by the CNIL guidelines (cookies strictly necessary for the operation of the service).

No consent banner is required on this page.

{% hint style="success" %}
Audit carried out on 27 April 2026: 0 analytics cookies, 0 advertising cookies, 0 third-party trackers detected. The third-party resources loaded (Bootstrap from cdnjs.cloudflare.com, the Poppins font from fonts.bunny.net, the SDK from cdn.dastra.eu) set no cookies.
{% endhint %}

***

## Must the `acaAffinity` cookie appear in our cookie register?

Yes, for the sake of complete documentation, even though it is exempt from consent. Here is the recommended entry:

| Field            | Value                                        |
| ---------------- | -------------------------------------------- |
| Name             | `acaAffinity`                                |
| Domain           | `api.dastra.eu`                              |
| Category         | Technical / Strictly necessary               |
| Purpose          | Load balancing: server session stability     |
| Duration         | Session (deleted when the browser is closed) |
| Issuer           | Dastra (processor)                           |
| Legal basis      | ePrivacy exemption: strictly necessary       |
| Consent required | No                                           |
