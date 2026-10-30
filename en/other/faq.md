---
description: >-
  Answers to frequently asked questions about using Dastra: logos, importing an
  existing record, deleting a processing activity, missing items and the
  browser's local storage.
---

# Frequently asked questions

## How to change the organization logo in Dastra?

The organization has no logo. The image displayed at the top right of the screen, next to your name and the organization name, is the image of your user account. To change it, open your profile menu at the top right, click **User profile** and upload a new image.

To customize the logo used in exports, see the next question.

## How to change the workspace logo in Dastra?

Open the workspace settings, then the **Design** section. You can upload a square logo and a rectangle logo, and choose the **Brand color** and the **Secondary color**. These elements adapt Dastra exports to your brand.

This section is reserved for the organization's owners.

## How to import my record of processing activities in the CNIL format?

You can import an existing record of processing activities in the CNIL format into Dastra. The import takes several steps:

1. Import the names of the processing activities.
2. Import the datasets.
3. Import the stakeholders.
4. Import the security measures.
5. Create the links between these objects in the processing activities.

For the import of processing activities, see [Export / import the record](../features/ropa/export-import.md). To get help importing your record, [contact support](../getting-started/support/request.md).

## How to delete a processing activity?

Deletion takes two steps, to prevent deletions by mistake. First move the processing activity to the recycle bin with **Move to recycle bin**. Then display the recycle bin with **View recycle bin** in the filters, and choose **Delete** to delete it permanently, or **Restore** to put it back in the record.

The full procedure is described in the [Frequently asked questions](../features/ropa/faq.md#how-to-delete-a-processing-activity) of the record.

## I can't find some items, what can I do?

If you can't find an item you should have access to, it may be hidden for one of the following reasons:

1. A filter is active and restricts the display. The number of active filters appears in brackets on the button, for example "(1)". Click **Reset filters**.

   <figure><img src="../.gitbook/assets/other-faq-1.png" alt="Record list with an active filter and the Reset filters (1) button"><figcaption><p>An active filter restricts the list</p></figcaption></figure>
2. The item is linked to an organizational unit you can't access, or for which you don't have the necessary rights. Contact your workspace manager.
3. The item is in the recycle bin, so it no longer appears in the default list. Click **Filters** and tick **View recycle bin**.

   <figure><img src="../.gitbook/assets/ropa-faq-3.png" alt="Filters panel of the record with the View recycle bin option"><figcaption><p>Displaying the recycle bin</p></figcaption></figure>
4. Incorrect settings are saved in your browser. To check, open Dastra in a private browsing window. If the problem disappears, clear your browser's local storage with the procedure in the next question.

## How to clear the browser's local storage?

Local storage (localStorage) holds data that the browser keeps so that Dastra works and remembers your settings, such as your filters. If you have a display problem, support may ask you to clear it.

You can also use the **Reset preference data** button in your user profile, described in [Known problems](known-problems.md).

### Google Chrome

1. Open the browser menu, then **More tools** > **Developer tools** (F12).
2. Open the **Application** tab, then **Storage** > **Local storage**.
3. Right-click the Dastra address and choose **Clear**.
4. Refresh the page (F5).

### Mozilla Firefox

1. Open the browser menu, then **More tools** > **Web Developer** > **Developer Tools** (F12).
2. Open the **Storage** tab, then **Local Storage**.
3. Right-click the Dastra address and choose **Delete All**.
4. Refresh the page (F5).
