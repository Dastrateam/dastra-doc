---
description: Learn how to scan cookies placed on your website.
---

# Cookies scanning

DASTRA allows you to scan the cookies placed on your website thanks to its **cookie scanning** functionality, directly integrated into its "Cookie consent widget" module.

## Access the "scan cookies" function Dastra

You must first log into your Dastra workspace. To learn how to do this, go to the following page:

{% content-ref url="/broken/pages/-LvaGKB4EL4Jf4xLoJUG" %}
[Broken link](/broken/pages/-LvaGKB4EL4Jf4xLoJUG)
{% endcontent-ref %}

Then, you must go to the "Consent to cookies" module, and click on the "New widget" button.

<figure><img src="../../../.gitbook/assets/settings-sso-openid-card-status.png" alt=""><figcaption><p>Icon of the "Cookies" module</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/screenshot-2023-02-20-174103.png" alt=""><figcaption><p>Click on the "New widget" button</p></figcaption></figure>

A new screen appears. You are in the "Cookie Scan" section.

<figure><img src="../../../.gitbook/assets/screenshot-2023-02-20-174229.png" alt=""><figcaption></figcaption></figure>

## Scan the cookies placed on your website

Once in the "Scan cookies" section, simply enter the domain name of your website in the space reserved, and click on "Submit".

<figure><img src="../../../.gitbook/assets/screenshot-2023-02-20-174330.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Your domain name must include the entire prefix "https: // www." to be taken into account by our engine. Websites without SSL are not eligible to the scan feature.
{% endhint %}

Wait a few seconds, and that's it, the cookies placed on your website are identified!

![Scanning is in progress](<../../../.gitbook/assets/settings-org-units-create-department-button.png>)

Once the cookies placed on your website are scanned, you can proceed to their classification.

{% content-ref url="classifiez-les-cookies-par-categories-de-consentement.md" %}
[classifiez-les-cookies-par-categories-de-consentement.md](classifiez-les-cookies-par-categories-de-consentement.md)
{% endcontent-ref %}

***



## Handle unclassified cookies

The scan compares the detected cookies with the Dastra service library. A cookie that matches no service is an unclassified cookie: it is not linked to any service, it is never displayed in the public banner, and visitors therefore cannot consent to it.

In the scan results, a warning badge shows the number of unclassified cookies (for example "3 unclassified cookies") next to the scan summary. These cookies are grouped in the **Unclassified cookies** tab, next to the **Services**, **Found cookies** and **Cookies breakdown** tabs.

<figure><img src="../../../.gitbook/assets/cookies-scan-unclassified-cookies-tab.png" alt="Unclassified cookies tab in the scan results"><figcaption><p>The "Unclassified cookies" tab of the scan results, with the badge showing their number</p></figcaption></figure>

Select one or more cookies using the checkboxes (the header checkbox selects the whole list), then choose one of the available actions.

### Add cookies to an existing service

1. Select the cookies, then click **Add to an existing service**.
2. In the **Target service** field, choose the service to link the cookies to.
3. Confirm.

All selected cookies are added to the service at once. A cookie already present in the service (same name and same domain) is not added a second time.

### Create a service from a selection

1. Select the cookies, then click **Create a new service**.
2. The service form opens, pre-filled from the most frequent domain among the selected cookies (service name, domain and logo) and containing the selected cookies.
3. Review the suggested information, in particular the purpose of the service, then save.

Only the cookies kept in the service leave the list of unclassified cookies.

### Delete cookies

Select the cookies, click **Delete**, then confirm. The cookies are removed from the list of unclassified cookies.

### Remove a cookie from a service

In the **Services** tab of the scan results, expand the cookie list of a service, then click the trash icon next to the cookie (tooltip "Remove from this service"). The cookie is detached from the service and moves to the **Unclassified cookies** tab.

After each action, the tab counters, the badge and the breakdown chart are updated immediately.

### Handle unclassified cookies from the banner editor

You do not need to handle every cookie before creating the banner: unhandled cookies remain attached to the banner and can be handled later. In the banner editor, the title of the **Services** section shows the number of unclassified cookies, and the **Unclassified cookies** tab of this section offers the same actions: **Delete**, **Add to an existing service** and **Create a new service**.

When all cookies are linked to a service, the tab displays the message "All cookies are classified".

### Rescan an existing banner

In the **Services** tab of the banner editor, click **Website scanning** to scan the site again. In the results, a green check mark (tooltip "Already in your configuration") flags the services already declared in the banner. Detected cookies that match the cookies of a service already declared, including a custom service, are linked to that service and do not appear among the unclassified cookies.

{% hint style="warning" %}
Unclassified cookies are never displayed in the public banner. Link every cookie actually placed by your website to a service so that visitors can consent to it.
{% endhint %}

***

## Limitations and best practices

### Cookies set after consent (opt-in services)

By default, a cookie scanner browses your site without giving consent. Cookies that are only placed after opt-in (analytics, marketing, etc.) are never triggered and therefore cannot be detected.

**Exception: if the Dastra SDK is already integrated on your site**, the scanner is able to bypass the consent banner and collect all cookies actually placed — including those from opt-in services. In that case, the scan produces a complete result without any manual intervention.

If the Dastra SDK is not yet in place on the scanned site, opt-in services will need to be **added manually** via the service library.

### Manually added services — excess cookies

When you add a service from the Dastra library (e.g. Google Analytics, Meta Pixel), Dastra imports the full list of cookies that service *can* place across all its possible configurations. Your implementation likely only uses a subset of those.

It is recommended to **remove cookies that your specific implementation does not actually place**. Declaring cookies you do not use is misleading to visitors and may raise questions during a compliance audit.

To identify which cookies to keep, cross-reference the automated scan results (which detect what is actually placed) with the list imported from the library, and remove entries that do not appear in the scan.
