---
description: >-
  A compliance project tracks how one or more frameworks are applied to a scope
  of your organization, from design to the final audit.
---

# Projects

A compliance project tracks how one or more frameworks are applied to a scope of your organization. It groups requirements, controls, tests, risks and audits, and moves forward in phases, from scoping to the final audit.

This page covers creating a project, its six phases, the phase assistant and navigation. Each phase is described in detail on the following pages:

* [Project design](design.md): frameworks, requirements, controls and risks to import;
* [Project implementation](implement.md): tests, risk assessment, connectors;
* [Compliance monitoring](monitoring.md): evidence, test campaigns, statement of applicability export;
* [Audits](audits.md): internal audits and final audits.

## Open the projects

In the menu, click **Compliance** then **Projects**. The side menu has two groups:

* **Compliance Projects**: **All projects** lists the projects of the workspace;
* **My tasks**: the items assigned to you, across all projects (see below).

## Create a project

1. In **All projects**, click **Create a project**.
2. Enter the project **Title** (200 characters at most).
3. Choose the **Scope** (required). If it does not exist yet, click **Create a scope** in the list to define it without leaving the dialog. See [Scopes](../scopes.md).
4. Click **Next**.
5. In **Assign users to project**, add the people allowed to manage the project and give each one the **Accountable** or **Informed** role. You are added by default with the **Accountable** role.
6. Click **Add**.

The project opens on its overview, in the **Scope** phase.

{% hint style="info" %}
Creating or editing a project requires write access to operational compliance.
{% endhint %}

<figure><img src="../../../.gitbook/assets/compliance-projects-list-1.png" alt="List of compliance projects with the Create a project button and the My tasks side menu"><figcaption></figcaption></figure>

## Project phases

A project goes through six phases. The current phase is highlighted on the overview, and each phase shows its objective when you hover over it.

| Phase | Objective | Page |
| --- | --- | --- |
| **Scope** | Define the compliance perimeter, that is, the organizational units concerned. This usually happens when the project is created. | [Scopes](../scopes.md) |
| **Design** | Define the frameworks to apply (GDPR, ISO, etc.), including their requirements, controls and risks. You can use the Dastra templates or your own frameworks. | [Project design](design.md) |
| **Implementation** | Define how compliance is carried out: tests, risk assessment, owners and possible automations. | [Project implementation](implement.md) |
| **Monitoring** | Collect evidence across the whole project using test campaigns and make sure as many controls as possible pass. This is the day-to-day run phase. | [Compliance monitoring](monitoring.md) |
| **Internal audit** | Perform a first internal audit to check that everything is correctly implemented before the final audit. | [Audits](audits.md) |
| **Final audit** | Perform the certification audit on each framework you have implemented. | [Audits](audits.md) |

<figure><img src="../../../.gitbook/assets/compliance-projects-overview-1.png" alt="Project overview with the six phases, the assistant and the list of frameworks"><figcaption></figcaption></figure>

### Change phase

Phases are not locked: you can move to any of them, forward or backward.

1. On the overview, click the phase you want.
2. Confirm in the **Would you like to move the project to this status ?** dialog.

Some features are enabled or disabled depending on the phase, and all your work is kept. When you act outside the recommended phase, Dastra shows a warning without blocking you:

* changing evidence outside the **Monitoring** phase;
* launching a test campaign outside the **Monitoring** phase;
* creating an audit outside an audit phase, or a certification audit outside the **Final audit** phase.

### Follow the assistant checklist

At the top of the overview, the assistant recalls the **Objective** of the phase and shows a **Checklist** for the current phase. Each step has an action button that opens the relevant screen.

| Phase | Checklist steps |
| --- | --- |
| **Scope** | Define project scope |
| **Design** | Add at least one framework; add controls to project; add risks to project |
| **Implementation** | Configure at least one control; configure automated tests; assess your risks; assign owners to tests |
| **Monitoring** | Validate at least one test; make sure 80% of tests are passing |
| **Internal audit** | Configure your first internal compliance audit; finalize at least one audit |
| **Final audit** | Launch at least one final audit per framework; finalize one of your final/certification audit |

When every step is done, the **Move to phase : …** button appears to move to the next phase, after the same confirmation.

To hide the assistant, click its cross (**Hide assistant**). The **Display assistant** button brings it back.

## Navigate a project

The side menu of a project shows the scope, the title (click it to edit) and the project users, then gives access to these tabs:

| Group | Tabs |
| --- | --- |
| **Project** | **Overview**, **Requirements**, **Audits** |
| **Controls & tests** | **Controls**, **Tests**, **Test campaigns** |
| **Risks** | **Risks**, **Threats** |

The task and comment buttons of the menu let you follow the project with other users. The **⋯** menu offers:

* **Settings**: edit the title, the description and the scope;
* **History**: review the changes made to the project;
* **Export**: export the project as PDF, DOCX, JSON, HTML or Markdown;
* **Move to recycle bin**: archive the project. An archived project is read-only: **Restore** makes it editable again and **Delete** removes it permanently.

## Follow your tasks

The **My tasks** group of the side menu gathers what is assigned to you, across all projects. It is the daily workspace of test owners and auditors. A user who cannot open the project list lands directly on **My tests** when opening **Compliance**.

| View | Content |
| --- | --- |
| **My tests** | The tests you own, with their statistics. Filter by test campaign to open a campaign and add your evidence. |
| **My controls** | The controls you own. |
| **My risks** | The risks you own. |
| **My audits** | The audits where you are an auditor. Click an audit to assess it. |
| **My test campaigns** | The test campaigns, which you can filter by status and by framework. |

See also [Validate tests](monitoring.md#validating-tests).

## Display a project in the Trust center

The Trust center can display a summary of all the frameworks of a compliance project, with the information of the latest audit and the related attachments. The option is enabled in the Trust center configuration: see [Configure your Trust center](../../trust-center/configuration/README.md).
