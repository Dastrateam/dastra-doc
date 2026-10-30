---
description: Learn how to create generic relationships between elements in Dastra.
---

# Generic relationships

## Definition of a generic relationship

A **generic relationship** is a simple, labeled link between two elements in Dastra. It lets you document connections between objects that the platform does not infer automatically, for example linking an asset to a stakeholder, or a data breach to a risk.

A relationship is defined by:

* a **source object** and a **target object**,
* a **relation label** (optional, for example "Controller" or "Managed by"),
* a **summary** (optional, to add context),
* a **direction**, which can be inverted if needed.

{% hint style="info" %}
One element can be linked to several other elements of different types.
{% endhint %}

## Where to create a generic relationship

You create a relationship from the form of an:

* **asset**,
* **stakeholder**,
* **dataset**,
* **security measure**,
* **data breach**.

The target object can be one of these types, or a **risk** if the risk management module is enabled and you have access to it. A risk does not carry generic relationships itself.

Relationships appear on the **Graphs** page of the **Repositories** module, where they connect the nodes of the graph. See [Repositories](repositories/README.md).

To link processing activities to each other, see [Create relationships between processing activities](../ropa/relationships.md).

## Add a generic relationship

1. Open an element, for example an asset.
2. In the toolbar, click **Linked elements**. The button shows the number of existing links.
3. Click **Add a relationship**, then select the type of object to link: stakeholder, security measure, data breach, asset, dataset or risk.
4. In the dialog:
   * Turn on **Inverse relationship** if the direction should be reversed.
   * Choose **Existing element** to link an element already in Dastra, or **Create element** to create a new one on the fly.
   * With **Existing element**, select the target objects in **Select the attached objects**. With **Create element**, type the name of the new object.
   * Optionally, fill in the **Relation label** and the **Summary**.
5. Click **Add** to save the relationship.

## View relationships

Once created, relationships appear:

* in the **Linked elements** panel of each element, which lists all its direct links;
* in the **Node mapping** and **Mapping of stakeholders** charts of the **Graphs** page, where they are displayed as a network.

## Go further

{% content-ref url="README.md" %}
[.](README.md)
{% endcontent-ref %}
