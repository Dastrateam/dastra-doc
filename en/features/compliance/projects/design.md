---
description: >-
  The design phase is the starting point of your compliance project.
---

# Project design

The **Design** phase lets you define the **organizational scope** of the project, select the **applicable frameworks** and automatically initialize the associated controls, tests and risks.

This step lays the foundations of the project and determines the quality of monitoring in the following phases. For an overview of the phases, see [Projects](README.md).

***

<figure><img src="../../../.gitbook/assets/image-432.png" alt="The phases of the compliance project, with the Scope phase in progress"><figcaption></figcaption></figure>

## 1. Creating the project and defining the scope

When creating the project, an **organizational scope** must be selected.\
The scope groups together one or more organizational units and determines **the scope of application of the compliance project**.

{% columns %}
{% column %}
Once the project is created, the scope is displayed in the project header and used throughout the compliance cycle.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image-490.png" alt="Project creation window with the title and the scope"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## 2. Assigning users to the project

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image-491.png" alt="Project creation window with the user assignment"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
The design phase also allows you to **designate the users authorized to manage the project**.

* Each user can be assigned a role: **Accountable** or **Informed**.
* These users will be entitled to steer the project's controls, tests and audits.
{% endcolumn %}
{% endcolumns %}

***

<figure><img src="../../../.gitbook/assets/image-433.png" alt="The phases of the compliance project, with the Design phase"><figcaption></figcaption></figure>

## 3. Adding compliance frameworks

A compliance project is based on one or more **frameworks** (standards, internal or custom referentials).

Adding a framework allows you to import:

* the **requirements**,
* the **controls**,
* the **tests**,
* and the associated **risks**.

<figure><img src="../../../.gitbook/assets/image-434.png" alt="Selection of a framework to add to the project"><figcaption></figcaption></figure>



Only the published versions of a framework are offered. When several published versions exist, choose the version in the **Version to install** list displayed next to the framework name; the current version is preselected.

The project remains attached to the installed version. When it is no longer the current version, the framework card in the project overview displays the **Update available** badge. Moving to another version is done manually with the **Update the framework version** action, which is not possible while an audit is in progress in the project (see [Framework versions](../library/frameworks/versions.md)).

Several frameworks can be added successively to the same project.

***

## 4. Sharing controls across frameworks

When several frameworks are added to the project, Dastra automatically detects the **common controls**.

* A control shared between several frameworks **is imported only once**.
* Its implementation simultaneously covers all the associated requirements.
* This makes it possible to increase compliance coverage without multiplying actions.

<figure><img src="../../../.gitbook/assets/image-435.png" alt="Import of the controls shared between several frameworks"><figcaption></figcaption></figure>

***

## 5. Selecting the controls to import

When adding a framework, several options are offered:

* import **all the controls** of the framework,
* import **only certain controls**,
* or **not import any controls** in order to implement them manually.

<figure><img src="../../../.gitbook/assets/image-437.png" alt="Choice of the controls to import with the framework"><figcaption></figcaption></figure>

This flexibility makes it possible to adapt the project to the organization's maturity.

***

## 6. Initializing controls and tests

{% columns %}
{% column %}
Once the frameworks are imported:

* The **selected controls** are automatically added to the project.
* They are considered **implemented by default**.
* The **associated tests** are also attached to the controls.

At this stage:

* the tests are set to the **"missing evidence"** status,
* no evidence has been collected yet.
{% endcolumn %}

{% column %}
<div align="center"><img src="../../../.gitbook/assets/image-438.png" alt="Project overview with the imported frameworks"></div>
{% endcolumn %}
{% endcolumns %}

***

## 7. Preparing the risk analysis

The **risks from the frameworks** can be selected during the import.

They constitute:

* the basis for the **initial risk assessment**,
* the reference point for calculating the **residual risk** after the controls are applied.

<figure><img src="../../../.gitbook/assets/image-439.png" alt="Risk matrix of the project"><figcaption></figcaption></figure>

***

## Removing a framework from the project

On the project **Overview**, the **⋯** menu of a framework card offers **Detach framework**. Dastra then removes from the project the controls, tests, risks and threats attached only to that framework. A control that the project still applies through another framework is kept.

Removal is not possible while an audit of that framework is not archived (see [Audits](audits.md)).

***

## Result of the Design phase

At the end of the design phase, the project has:

* a clearly defined scope,
* identified owners,
* the applicable frameworks imported,
* shared controls ready to be monitored,
* initialized tests,
* and a structured risk base.

The project is then ready to enter the next phase: **Implementation**.
