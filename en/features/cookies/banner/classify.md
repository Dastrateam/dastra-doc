---
description: Learn how to classify cookies by consent categories.
---

# Classify cookies by consent categories

In its [draft recommendation](https://www.cnil.fr/fr/la-cnil-lance-une-consultation-publique-sur-son-projet-de-recommandation-cookies-et-autres-traceurs) on cookies and other trackers (in French), the CNIL recommends that you list and categorize the cookies on your website according to whether or not they require consent.

{% hint style="info" %}
For more information on the CNIL recommendations on cookies, read the article "[The CNIL's cookie recommendations explained to your boss](https://www.dastra.eu/fr/article/recommendations-CNIL-cookies-expliquees-a-votre-boss/104)" (in French).
{% endhint %}

In Dastra, the category of a cookie is the category of the service it belongs to: you choose the **purpose** of each service, and all its cookies inherit it. The available categories are:

* **Strictly necessary**: cookies that are exempt from consent by their nature, for example session or consent cookies;
* **Preferences**;
* **Analytic**;
* **Marketing**;
* **Social network**;
* **Other**.

{% content-ref url="purposes.md" %}
[purposes.md](purposes.md)
{% endcontent-ref %}

## Choose the purpose of a service

1. Open the banner: **Cookie consent** > **Banners**, then click the banner.
2. Expand the **Services** section.
3. Click the service to classify. In the **Service infos** tab, choose a value in the **Service's purpose** field.
4. Confirm, then click **Save changes**.

<figure><img src="../../../.gitbook/assets/cookies-classify-1.png" alt="The Services section of the banner editor, with the purpose shown under the name of each service"><figcaption><p>The purpose of each service is shown under its name</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/cookies-classify-2.png" alt="The service form with the Service's purpose field"><figcaption><p>The "Service's purpose" field in the service form</p></figcaption></figure>

A service cannot be saved with the "Unclassified" purpose: choose one of the categories above.

{% hint style="info" %}
You decide case by case whether consent must be requested for a service with the **Request consent for these cookies? (display buttons)** option. It is disabled for the **Strictly necessary** category.
{% endhint %}

{% hint style="warning" %}
A cookie detected by the scan but not linked to any service (unclassified cookie) is never displayed in the public banner. Add it to an existing service or create a service from it: see [Handle unclassified cookies](scan.md#handle-unclassified-cookies).
{% endhint %}

Once all your cookies belong to a service classified by category, you can configure the banner.

{% content-ref url="configure.md" %}
[configure.md](configure.md)
{% endcontent-ref %}
