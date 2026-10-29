---
description: >-
  Import your existing record of AI systems into Dastra from a CSV or Excel
  file, with the expected format for each column.
---

# Import your AI systems

If you already have a record of AI systems, import it into Dastra instead of entering everything by hand.

1. Click **AI governance** in the sidebar, then **Record of AI systems**.
2. In the top right-hand corner, open the menu of the **Create an AI system** button and click **Import**.
3. On the page that opens, add your file at the bottom of the page.

<figure><img src="../../.gitbook/assets/ai-systems-import-1.png" alt="Menu of the Create an AI system button with the Create from library, Import and Export actions"><figcaption><p>The Import action in the menu of the record of AI systems</p></figcaption></figure>

For the details of the procedure, see [Import your data (Excel, Csv, JSON)](../general/import.md).

## File format

The file contains a header row with the column names described below. All columns are optional except `Label`.

Enumeration columns expect exactly the values of the "Allowed values" column. Case does not matter. A value that matches none of the allowed values is ignored.

| Column | Description | Type | Constraints | Allowed values |
| --- | --- | --- | --- | --- |
| `Label` | System name | Text | Required, 1 to 120 characters | Free text |
| `Ref` | Internal reference | Text | 50 characters at most | Free text |
| `Description` | System description | Text | 4,000 characters at most | Free text |
| `State` | System state | `AiSystemState` | | `Draft`, `Cancelled`, `Pending`, `Active` |
| `RiskLevel` | Risk level | `AiSystemRiskLevel` | | `Low`, `Medium`, `High`, `Unacceptable` |
| `RiskLevelJustification` | Justification of the risk level | Text | | Free text |
| `BenefitLevel` | Business value level | `AiSystemBenefitLevel` | | `Low`, `Medium`, `High` |
| `BenefitLevelJustification` | Justification of the business value | Text | | Free text |
| `DateArchived` | Date moved to the recycle bin | Date | Formats `DD-MM-YYYY` or `DD/MM/YYYY` | Date |
| `DateCreation` | Creation date | Date | Same format | Date |
| `DateUpdate` | Last update date | Date | Same format | Date |
| `DateDeployment` | Deployment date | Date | Same format | Date |
| `DateRetirement` | Retirement date | Date | Same format | Date |
| `TransparencyNoticeDone` | A transparency notice has been provided | Boolean | | `true` or `false` |
| `TransparencyNoticeHtml` | Content of the notice | Text | | HTML |

### Match with the labels shown in the application

The values in the file are the technical names, not the labels displayed in the application. Do not write the on-screen label in the file.

| Column | Value in the file | Label displayed |
| --- | --- | --- |
| `State` | `Draft` | Draft |
| `State` | `Pending` | Pending |
| `State` | `Active` | Active |
| `State` | `Cancelled` | Cancelled |
| `RiskLevel` | `Low` | Minimal |
| `RiskLevel` | `Medium` | Limited |
| `RiskLevel` | `High` | High |
| `RiskLevel` | `Unacceptable` | Unacceptable |
| `BenefitLevel` | `Low` | Low |
| `BenefitLevel` | `Medium` | Moderate |
| `BenefitLevel` | `High` | High |

## Example row

```
"Internal ChatGPT","SYS-001","Internal documentation assistant model","Active","Medium","Moderate risks with responsible use","High","Very high business value","01/02/2024","15/01/2024","01/03/2024","20/03/2024","","false","<p>This AI system is used to assist employees in drafting internal documents.</p>"
```

## Ready-to-use header template

Copy this line into a blank `.csv` file:

```
Label,Ref,Description,State,RiskLevel,RiskLevelJustification,BenefitLevel,BenefitLevelJustification,DateArchived,DateCreation,DateUpdate,DateDeployment,DateRetirement,TransparencyNoticeDone,TransparencyNoticeHtml
```
