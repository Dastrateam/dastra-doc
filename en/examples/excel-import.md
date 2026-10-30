---
description: >-
  Import five assets of Brightmoor Retail Group from a CSV file: columns,
  mapping, Merge mode with a matching field and a custom field.
---

# Import assets from a spreadsheet

Brightmoor Retail Group keeps its list of systems in a spreadsheet. This example imports it into the **Assets** repository. Part of the list is already in Dastra, so the import must update the existing assets and create the others. The method is the same for processing activities and the other objects: see [Import your data (Excel, Csv)](../features/general/import.md) for the full reference.

## The sample file

Download the file: [examples-assets-import.csv](../.gitbook/assets/examples-assets-import.csv). It is a CSV file with the separator `;` and the UTF-8 encoding, the format the import expects. It holds five rows.

| Column | Content | Possible values |
| --- | --- | --- |
| `Ref` | Internal reference, up to 100 characters | Free text |
| `Label` | Name of the asset, required | Free text |
| `Type` | Category of the asset | `Software`, `Building`, `Network`, `Material`, `Data`, `People`, `Process`, `Algorithm` |
| `Description` | Description | Free text |
| `Address`, `ZipCode`, `City` | Location | Free text |
| `CountryCode` | Country, 2 characters | ISO code, for example `DE` |
| `State` | Status of the asset | `Draft`, `Active` |
| `ApplicationType` | Type of application | `Software`, `WebApp`, `Saas`, `Module`, `Other` |
| `HostingType` | Hosting | `InHouse`, `OutSourced` |
| `ApplicationState` | Life cycle | `InProduction`, `InDevelopment`, `Stopped` |
| `CustomFields.criticality` | A custom field of the workspace | Free text |

The possible values are in English, as in the template. A value that matches none of the choices is replaced with the default value of the column: check them before the import.

In the application, **View columns format** in the import wizard lists the columns and values of your version.

## 1. Create the custom field

The last column feeds a custom field. Create it first.

1. In the sidebar, click **Workspace settings**, then **Custom fields**, and choose the module of the assets.
2. Click **Create a group of fields**, name it "Brightmoor data" and save.
3. Drag a text field into the group. Enter "Criticality" in **Custom field label**.
4. Check that **Variable name (slug)** is `criticality`, then save. The slug cannot be changed afterwards.

A custom field is imported through a column named `CustomFields.` followed by its slug: `CustomFields.criticality`. See [Custom fields](../features/general/custom-fields.md).

## 2. Start the import

1. Open **Data inventory** > **Repositories** > **Assets**.
2. Click the arrow next to the **Add an asset** button, then **Import**.

The wizard offers **Download the file template** if you prefer to start from a blank file.

## 3. Choose Merge mode and the matching field

The asset "Brightmoor customer portal" already exists in the workspace with the reference `BRM-A001`. In the **Conflict handling** group, choose **Merge : Overwrite row matching specific criteria**.

Then choose the **field to use for data matching**. For assets, the matching fields are `Ref` and `Label`. Brightmoor chooses `Ref`, which does not change when an asset is renamed. A row matches a record when the value is strictly identical, uppercase and lowercase included.

With this choice:

* row `BRM-A001` updates the existing asset;
* the four other rows create new assets.

{% hint style="warning" %}
**Merge** replaces the stored values with those of the file. An empty cell keeps the existing value, except in columns with a mandatory choice, such as the type or the status, which then take their default value: always fill them in. The operation cannot be undone.
{% endhint %}

With **Merge**, the custom fields are also updated. A row with an empty `CustomFields.criticality` leaves the stored value unchanged.

To keep the existing asset untouched, choose **Preserve : skip records matching a specific criteria** instead: row `BRM-A001` is skipped.

<figure><img src="../.gitbook/assets/examples-import-2.png" alt="Conflict handling with Merge selected and Ref as matching field"><figcaption><p>Merge mode with the Ref matching field</p></figcaption></figure>

## 4. Send the file and map the columns

1. Click **Upload or drag file here** and choose the CSV file. Dastra reads the first rows.
2. In the **Columns mapping** step, Dastra matches the columns of the file with the columns of the import when the header is identical to the name or the label of the column. The **Data sample** column shows the first values of your file.
3. Use the tabs **All columns**, **Not mapped** and **Mapped** to filter the list. If a header does not match, choose the right column in the list of the row. The mapping of `CustomFields.criticality` appears like the others.
4. The **Continue** button stays disabled while a required column, such as `Label`, has no match.

<figure><img src="../.gitbook/assets/examples-import-1.png" alt="Columns mapping step of the asset import with the sample file"><figcaption><p>The columns of the sample file, matched</p></figcaption></figure>

## 5. Read the result

Click **Continue**. The **Result** screen shows the number of lines processed, created, updated and skipped. For the sample file in Merge mode, expect five lines processed, four assets created and one updated. Click **View** to open the list.

If a row is invalid, for example a `CountryCode` that is not a country, the whole import stops and nothing is saved. The message gives the row concerned, the header counting as row 1. Fix the file and start again.
