# Request purge rules

{% hint style="info" %}
You need **administrator rights** on the workspace to access this feature.
{% endhint %}

You can **automate the purge of requests moved to the recycle bin** to follow your internal retention policies, and in particular the storage limitation principle of the GDPR.

You define:

* the **scope** of the requests the purge applies to,
* the **purge mode** (deletion or anonymization),
* the **maximum retention period** before the purge runs automatically.

To set it up, open the workspace settings, go to the **Process** section, then **Requests** and the **Purge rules** section.

***

## Requests concerned

The purge applies **only to requests in the recycle bin**. Open, closed or archived requests are not affected.

Every night, Dastra checks requests against their **date of move to the bin**. A request that exceeds the maximum period you set (for example 180 days) is purged. The purge covers:

* requests that have been in the bin for longer than the configured period;
* all request types (access, erasure, objection, etc.);
* all requests, whatever their origin (portal, API, import).

***

## Purge modes

In **Select a purge mode**, choose one of the two modes.

### Delete requests permanently

The requests concerned are **permanently deleted** from Dastra. This action is **irreversible**.

* Personal data and the content of the exchanges are deleted.
* Attachments and related files are erased.
* Audit logs keep only technical metadata (timestamp, user, operation).

### Anonymize requests

The requests stay visible in Dastra, but their **personal data** is replaced with random values unrelated to the requester. This mode keeps a non-identifiable statistical trace for your reports and indicators.

* The fields that hold personal data (last name, first name, email, address, city, postal code) are replaced with generated values, and the text of the request is replaced.
* The exchanged messages and the attachments are deleted.
* Non-identifying metadata (request type, status, dates) is kept for reporting.
* The related activity logs are purged.

<figure><img src="../../../.gitbook/assets/requests-purge-1.png" alt="The Purge rules section with the enable switch, the purge mode choice and the maximum retention period"><figcaption><p>Configuring the purge rules</p></figcaption></figure>

***

## Retention period before purge

In **Maximum retention period for requests in the bin (in days)**, enter the maximum age of a request in the bin before it is purged, for example 180 days. The period is counted from the **date the request was moved to the bin**.

Every night, around 2:30 AM UTC, Dastra retrieves the requests concerned and runs the purge in the selected mode.

***

## Example configuration

* **Purge mode**: Delete requests permanently
* **Maximum period**: 180 days (6 months)

Every night, all requests that have been in the bin for more than 180 days are deleted automatically.

***

## Best practices

* Set a period consistent with your internal request retention policy (for example 5 years, or 1,825 days).
* Choose deletion for a complete erasure.
* Choose anonymization if you want to keep activity statistics.
* Check that **Enable automatic purge of requests in the bin** is turned on: otherwise no purge takes place.
