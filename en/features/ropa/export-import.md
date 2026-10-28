---
description: Learn how to export and import a complete existing record into Dastra.
---

# Export / import the record

## Record export

To export the entire record, open the record of processing activities, click the arrow on the right of the **Create data processing** button, then select **Export**.

<figure><img src="../../.gitbook/assets/ropa-export-import-1.png" alt="Create data processing menu with the Export entry"><figcaption><p>Record drop-down menu with the export feature</p></figcaption></figure>

In the window that opens, **Choose an export format**: PDF, Word, HTML, CSV, Excel, JSON or Markdown. For PDF, Word and HTML, also **Choose an export type** (**Complete**, **Article 30 GDPR**, **Standard information notice** or **Data retention policy**). Then click **Download file**. That's it, your record is exported!

Depending on the format, additional options are available, for example:

* **Group by areas** (PDF, Word, HTML), to group the processing activities by organizational unit
* **Export Progress, quality and sensitivity indicators** and **Export associated tasks** (PDF and HTML, Complete type)
* **Complex table (Multi-sheets)** (Excel)
* **Use native column names or reports (recommended for importing data)** and **Export custom fields**, which lets you choose the columns to export (CSV and Excel)
* **Export for customer/data controller**, to produce an export for one of your clients only, without the other clients' data

PDF, Word and HTML exports include up to 500 processing activities, and CSV, Excel, JSON and Markdown exports up to 10,000. A warning appears in the window if your selection is larger.

For a large record, the JSON export is prepared in the background: you can keep working, a notification keeps you informed of its progress and the file downloads as soon as it is ready.

### Article 30 GDPR format

The Article 30 GDPR format corresponds to what the GDPR requires: the export only contains the fields that Article 30 makes mandatory in the record of processing activities. The information contained is:

* Name of the processing activity, and the identity of the controller (or processor), its representative and its DPO
* Purposes (without legal basis)
* Categories of data subjects and of personal data, and retention periods
* Recipients and possible transfers outside the EU
* Security measures

### Complete format

The complete format is the native Dastra format: you export all the fields that make up the processing activity.

{% hint style="info" %}
You can also export only one or several processing activities of the record, instead of the whole record. To do this, tick the boxes on the left of the processing activities concerned, then click **Select a batch action** and **Export**. To export a single processing activity, you can also use **Export** in the menu at the end of its row.
{% endhint %}

## Record import

Click the arrow on the right of the **Create data processing** button, then select **Import**. The **Import data processings** window offers three formats:

* **Complex excel workbook**: import your processing activities from an Excel workbook made up of several sheets (Beta)
* **CSV**: import your processing activities from a CSV file
* **JSON**: import processing activities previously exported from Dastra in JSON format, for example from another workspace

<figure><img src="../../.gitbook/assets/ropa-export-import-2.png" alt="Import data processings window with the Complex excel workbook, CSV and JSON options"><figcaption><p>Choosing the import format</p></figcaption></figure>

### Import with the complex Excel workbook

Importing an existing record can be tedious if you have many processing activities. The complex Excel workbook lets you import your processing activities in bulk, in one go. Dastra recognizes the data in the workbook to create the processing activities and the associated repositories.

1. Choose **Complex excel workbook**.
2. Click **Download the file template** and fill it in with your data.
3. Select the **Organizational unit** in which the processing activities will be created.
4. Drop your completed file to start the import.

{% hint style="info" %}
No organizational unit is created during the import. Data from fields that are not part of the template is placed in the HTML description fields.
{% endhint %}

### Standard import, step by step

To avoid filling in each processing activity by hand and to handle every possible record format, Dastra has designed a methodology based on the principle of **splitting the record into data domains**. Thus, 7 steps are recommended to import an entire existing record into Dastra.

{% hint style="info" %}
These steps, which are not mandatory, are nevertheless strongly recommended, especially when the record contains many processing activities.
{% endhint %}

Don't hesitate to consult our library of data processing templates: [https://www.dastra.eu/en/data-processing/referentials](https://www.dastra.eu/en/data-processing/referentials)

The import page works the same way for every step. It is described in detail in [Import your data (Excel, Csv)](../general/import.md).

### Step 1: Import of processing activity labels

To import your existing processing activity labels, click the arrow on the right of **Create data processing**, select **Import**, then choose **CSV**. The **Data import** page opens.

Click **Download the file template** to get a sample file, and **View columns format** to see the list of expected columns, their rules and their possible values.

<figure><img src="../../.gitbook/assets/ropa-export-import-3.png" alt="Data import page with the Download the file template and View columns format buttons"><figcaption><p>Downloading the file template</p></figcaption></figure>

Fill in the file with your processing activities. The main columns are:

| Column           | Description                                    | Possible values                                     |
| ---------------- | ---------------------------------------------- | --------------------------------------------------- |
| Label            | Name of the processing activity (required)     |                                                     |
| Ref              | Internal reference                             |                                                     |
| Processing state | State of the processing activity               | "Study", "BeingDeployed", "InProduction", "Stopped" |
| Description      | Short description of the processing activity   |                                                     |

Select the **Organizational unit**, then drop your file:

<figure><img src="../../.gitbook/assets/ropa-export-import-4.png" alt="Organizational unit selection and file upload area on the Data import page"><figcaption><p>Choosing the organizational unit before uploading the file</p></figcaption></figure>

Match the columns of your file with the Dastra fields in the **Columns mapping** step, then click **Continue** to run the import.

That's it, your processing activity labels are imported!

### Step 2: Import of the asset repository

To import your existing applications and assets, go to the **Repositories** module, **Assets** tab, click the arrow on the right of **Add an asset**, then select **Import**:

<figure><img src="../../.gitbook/assets/ropa-export-import-5.png" alt="Add an asset menu with the Import entry in the Assets repository"><figcaption><p>Importing assets</p></figcaption></figure>

Then download the file template, fill it in with your assets (use **View columns format** for the list of columns) and import it as in step 1.

That's it, your assets are imported!

### Step 3: Import of the stakeholders repository

Repeat the same procedure from the **Repositories** module, **Stakeholders** tab.

Your stakeholders repository lists all the parties involved in a processing activity: legal entities such as processors, clients or joint controllers, or natural persons such as the contact persons for a processing activity.

This repository serves as an internal directory for the workspace. For each stakeholder, you can define a type that characterizes it. For example, if you want to add your processors, you add them all as stakeholders and then associate each processor with the processing activities concerned.

### Step 4: Import of the security measures repository

Repeat the same procedure from the **Repositories** module, **Measures** tab.

### Step 5: Import of the data glossary

Repeat the same procedure from the **Repositories** module, **Data glossary** tab.

### Step 6: Import of the datasets repository

Repeat the same procedure from the **Repositories** module, **Datasets** tab.

#### Export / import datasets with their data fields

You can export and import your datasets **including their associated data fields**. This makes it easier to migrate an existing data map or to update your data glossary in bulk.

**Exporting datasets with their fields**

From the **Repositories** module, **Datasets** tab:

1. Select the datasets to export, or export the full list
2. Click **Export**
3. Choose the CSV or Excel format and click **Download file**

The exported file includes, for each dataset, its name, description, retention rule and the list of its data fields. In this column, each data field is written as `name#sensitivity#category`, and the data fields are separated by `|`. Turn on **Use native column names or reports (recommended for importing data)** if you plan to re-import the file.

**Importing datasets with their fields**

The import file follows the same format as the export. For each dataset, fill in its data fields in the dedicated column, for example `Last name#Current#CivilStatus|Salary#HighlyPersonalNature#EconomicFinancialData`. During import:

* Data fields that do not yet exist in the data glossary are **created automatically**
* Data fields already present (same name) are **associated** with the dataset without duplication

{% hint style="info" %}
This feature is particularly useful for harmonising the data map between multiple workspaces, or for initialising a new workspace from an existing data map.
{% endhint %}

### Step 7: Construction of links

Now that all the repositories have been imported, edit each processing activity and fill in its information based on the imported data, following the guide below:

{% content-ref url="activity/README.md" %}
[remplir-le-questionnaire](activity/README.md)
{% endcontent-ref %}

That's it, the links are built!
