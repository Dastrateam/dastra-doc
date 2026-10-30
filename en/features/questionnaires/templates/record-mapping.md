---
description: >-
  Use the answers of a questionnaire to create a record or update an existing
  one: supported objects, variables, question types, the merge button and the
  error messages.
---

# Fill a record from the answers

A questionnaire of a creation type can turn its answers into a record of Dastra: a processing activity, an asset, an AI system and so on. When the response is linked to an existing record, the answers can be merged into it instead. Each question is tied to a field of the record by its **variable name**.

This page is for the people who build the templates. Respondents see nothing of the mapping.

For a complete case with an AI system, see [Questionnaire answers in a record](../../../examples/questionnaire-to-record.md).

## Which objects can be filled

Only the creation types of the **Questionnaire type** field carry a data model. The other types, such as the DPIA, the vendor assessment or the standard questionnaire, have none.

| Questionnaire type | Record |
| --- | --- |
| Data processing project | Processing activity |
| Data breach creation request | Data breach |
| Asset creation | Asset |
| Contract creation | Contract |
| AI System creation | AI system |
| Stakeholder creation | Stakeholder |

The built-in templates of these types are ready to use (see [Create a questionnaire template](README.md)). You can also build your own template and choose one of these types.

## Model validation and the variable list

The model of a type is the description of the fields of the record: their name, their kind (text, date, fixed list of values, list of items) and their maximum length. The variable list reads this model.

To map a question:

1. Open the template, then the question.
2. Check **Would you like to customize the variable name (for experts users only)?**.
3. In **Variable's name**, type the name of the field, or click **Select a variable to map**.
4. In the list, click the field. The window shows **Name**, **Variable's name**, **Possible values** and **Max** for each field. A **Required** mark flags the fields the record cannot do without.

Choosing a field fills the variable name and the maximum length. For a field with a fixed list of values, for example the risk level of an AI system, it also creates the answers of the question, one per value, and the variable name of each answer is the value Dastra expects. Keep these variable names unchanged.

A variable name uses letters, digits, hyphens and underscores, and must be unique in the template.

{% hint style="info" %}
A question whose variable name matches no field of the record is ignored when the record is created. Only the model of the type decides which names are valid: type the names exactly as the list shows them, with the same case.
{% endhint %}

<figure><img src="../../../.gitbook/assets/examples-questionnaire-1.png" alt="Select a variable to map window listing the fields of an AI system"><figcaption><p>The variables offered for an AI system</p></figcaption></figure>

## Question types and fields

The list only offers the fields that suit the type of the question.

| Question type | Fields offered | What the record receives |
| --- | --- | --- |
| Short text, Long text, Text editor | Text fields | The text entered |
| Date, Date & time | Date fields | The date. An invalid date is left empty |
| Unique choice list, Single select | Fields with a fixed list of values | The variable name of the chosen answer, or its label if it has none |
| Multi choice list, Multiple select | All fields, except `id` | The list of the variable names of the chosen answers |
| List with multiple fields | List fields | One item per row. The variable names of the sub-questions are the properties of an item |
| Number, Range selector, Simple checkbox, Country, Tags select | All fields, except `id` | The value as entered. For Tags select, the list of the tags |

You choose the field yourself for the types with no filter: pick one of the same kind as the answer.

The **Files** question type is not mapped to a field. Documents sent with the answers can be transferred to the file manager when the record is created (see below).

## Native questions

A native question is a question of a built-in creation template that is bound to a field of the record. Its type, its variable name, its limits and its answers are locked: only the administrators of Dastra can change them, so that the mapping stays correct. Add your own questions next to the native ones to fill other fields.

## Fill a custom field

A custom field is filled by a variable name made of `custom_` followed by the technical name of the field.

1. In the sidebar, click **Workspace settings**, then **Custom fields**, and choose the module of the record.
2. Click the field. The technical name is the **Variable name (slug)**, for example `business_owner`. It is read-only after the creation.
3. In the question, set the variable name to `custom_business_owner`.

Custom fields are not in the **Select a variable to map** list: type the whole name. See [Custom fields](../../general/custom-fields.md) for the field options.

Choose a question type that matches the field type:

| Custom field type | Question type |
| --- | --- |
| Text, Text area, Rich text | Short text, Long text, Text editor |
| Number (integer), Number (decimal) | Number |
| Date, Date with time | Date, Date & time |
| Radio, Single select | Unique choice list, Single select |
| Check box, Multi select | Multi choice list, Multiple select |
| Boolean | Simple checkbox |

Two rules apply when the record is created:

* a technical name that matches no custom field of the workspace for this type of record is dropped without an error: the answer is not saved. Check the spelling and the `custom_` prefix;
* a value that the field does not accept stops the creation with a message naming the field, for example when the field is required and the answer is empty, or when a list has too few or too many items.

## Create or merge the record

The button appears in the response of the questionnaire when:

* the response is published, that is validated and not archived;
* the template is of a creation type.

It is enabled for the owner of the response only.

* Without a linked record, the button is **Creation request**, followed by the type of record. It opens a preview of the record built from the answers. Choose the **Organizational unit** (not asked for assets and stakeholders), keep or clear the option to transfer the files to the file manager, and click **Create**. The record is created and linked to the response.
* With a linked record, the button is **Merge request**. Link the record when you schedule the questionnaire, in **Subject linked to the response** (see [Schedule a questionnaire](../schedule.md#linking-the-questionnaire-to-other-objects-in-dastra)), after setting **Related to** on the template to the type of the record. The preview opens the same way, and the button is **Create and merge**.

With **Create and merge**, Dastra builds a temporary record from the answers, with the label followed by "(From Questionnaire)", and opens the merge window with the existing record and the temporary one. You choose, field by field, the values to keep. The files are transferred once you confirm the merge. If you leave the window without merging, the temporary record is deleted and nothing changes.

Nothing is merged automatically: the answers never update a record on their own. The merge is always an action of a person.

<figure><img src="../../../.gitbook/assets/examples-questionnaire-2.png" alt="Merge request page with the preview of the AI system and the Create and merge button"><figcaption><p>The merge request of a response</p></figcaption></figure>

## Error messages

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| This audit template type has no model validation configured | The template type is not one of the six creation types, so it has no model. It appears when you click **Select a variable to map** | Change the **Questionnaire type** to a creation type, or type the variable names by hand if the template only collects answers |
| The **Select a variable to map** list is empty | No field of the record suits the question type, for example a Date question on a record without date | Change the question type, or choose a type with no filter |
| You need at least a slug name | The variable name is empty | Fill in **Variable's name** |
| The variable name {slug} is present in another question | Two questions use the same variable name | Give each question its own name |
| The button **Creation request** or **Merge request** is missing | The response is not published, is archived or the template is not of a creation type | Validate the response, restore it, or check the type |
| The button is grayed out | You are not the owner of the response | Ask the owner |
| A field is empty in the new record | The variable name does not match the field, or the custom field does not exist | Compare it with the list and with the technical name |
| The creation stops with a message naming a field | The value is not valid for the field | Fix the answer, then try again |
