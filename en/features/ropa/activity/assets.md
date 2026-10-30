---
description: >-
  List the assets, internal or external to the organization, that support the
  processing activity.
---

# Assets

This is where you list the assets, internal or external to the organization (applications, software, resources, buildings, etc.), that support the execution of the processing activity.

_For example, if you use CRM software, add it to this list._

This information, **which is not mandatory for the register**, allows you to **map the application chain linking the data together**.

**The objective is to help you control the data carriers and link your assets to your data catalog.**

You can thus specify the types of data processed through this processing activity.

NB: Assets are not necessarily linked to processors. For example, it can be **software installed on your own server, without any intervention of its editor in the processing of personal data**.

## Link assets to the processing activity

1. In the **Assets** section, click **Attach asset**.
2. Search for the assets to link and select them. If an asset does not exist yet, click **Add an asset** to create it.

The linked assets are listed in a table. For each asset, you can:

* click **Add a description** to describe the role of this asset in this processing activity;
* click **Sync data** to import the asset's data into the processing activity (see below);
* use the **...** menu to **Edit** the asset or **Delete** it from the processing activity.

## Sync the asset data with the processing activity

An asset can already be documented in your data mapping, with its editor, its datasets and its security measures. Instead of entering this information again, you can copy it into the processing activity.

1. On the asset's row, click **Sync data**. The **Sync asset data with data processing** window lists the elements that would be added to the processing activity:
   * **Asset's editor to add as a processor**, with its transfer countries;
   * **Dataset related to this asset**;
   * **Subject categories** of the selected datasets;
   * the security measures of the asset.
2. Select the elements to add, or check **Select all**.
3. Click **Add**.

The selected elements are added to the corresponding sections of the processing activity: the editor becomes a recipient of the **Processors** category in the **Recipients** section, the datasets are added to the **Datasets** section, the subject categories to the **Data subject** section and the security measures to the **Measures** section. If a country is set for the asset or its editor, a transfer to this country is also added to the recipient: check it in the **Recipients** section.

The asset's row shows whether its data is **Synced**, **Not synced**, or when it was last synced if the asset has changed since.
