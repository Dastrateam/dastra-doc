# Docusign integration

Dastra integrates natively with DocuSign, the electronic signature solution. You send a document for signature, track the signature status and find it up to date directly from the **Contracts & policies** module.

## Install the integration

1. Open **Workspace settings** > **Integrations**, then click the **Docusign** card.

   <figure><img src="../../.gitbook/assets/contracts-docusign-1.png" alt="The integrations catalog with the Docusign card"><figcaption><p>Select Docusign in the integrations</p></figcaption></figure>
2. On the contracts use case, click **Add integration**.
3. At the **Connection** step, create the connection: Dastra redirects you to the Docusign authentication to link your Docusign account with Dastra.
4. At the configuration step, enter **Account ID** and **Account Base URI**. You find them in your Docusign account, on the [Apps and Keys](https://apps.docusign.com/admin/apps-and-keys) page.

   <figure><img src="../../.gitbook/assets/contracts-docusign-2.png" alt="The configuration step with the Account ID and Account Base URI fields"><figcaption><p>The keys to enter in Dastra, taken from your Docusign account</p></figcaption></figure>
5. Save. Dastra checks the account with Docusign.

The installation is complete: Docusign signature is available in the signature window of your documents. How connections and use cases work in general is described in [Connections, use cases and field mapping](../integrations/connections.md).

## Send a document for signature

To send a document, you need:

* a signer whose stakeholder has a valid email address;
* at least one attachment to sign, in PDF, DOC or DOCX format;
* a subject for the invitation email.

In the **Add signature** window, choose **Sign with Docusign®** (see [Sign a document](sign.md)). If the integration is not installed, the window shows the **Install integration** button, which opens its settings.

### Sending options

Fill in the following fields:

* **Select the signers whose signature you want to record.**: the signers to send the request to. A stakeholder without an email address, or who has already signed, cannot be selected. The **Refresh** button reloads the list after a change.
* **Choose attachments added to the signature request**: the PDF, DOC or DOCX files sent for signature. All valid attachments are ticked by default.
* **Invitation email subject**: the subject of the email sent to the signers (80 characters at most).
* **Give detailed instructions for signing the document**: an optional text, included in the invitation email and visible to the signer in the Docusign interface.

Two optional settings complete the request:

* **Add automatically signature placement**: available when all attachments are PDF files. For each signer, Dastra displays the text to insert in the document where they must sign, for example `[Signature Signer name]`. The signature is positioned on that text.
* **Add automatically initials to each document page**: available when signature placement is on.

Click **Send** to send the request. The signers receive an invitation email from Docusign.

## Track the signature

Once the request is sent, the signature status is synchronized with your document and updated whenever it changes on the Docusign side. In the **Signers - Signatories** tab, the signer's row shows **Pending signature** until they sign.

<figure><img src="../../.gitbook/assets/contracts-docusign-4.png" alt="A signer row with the Pending signature status"><figcaption><p>A pending signature</p></figcaption></figure>
