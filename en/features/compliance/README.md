---
description: Manage your compliance with the various frameworks in Dastra.
---

# Compliance

The **Compliance** module of Dastra makes it possible to manage regulatory compliance in a structured, traceable and auditable way, relying on a modular architecture aligned with compliance frameworks.

***

## Navigate the module

In the menu, **Compliance** gives access to four entries:

* **Projects**: the compliance projects, their phases, their audits and your tasks. See [Projects](projects/README.md).
* **Library**: the reusable frameworks, controls, tests, risks and threats. See [Library](library/README.md).
* **Scopes**: the organizational units covered by a project. See [Scopes](scopes.md).
* **Statistics**: the compliance dashboard of the workspace (see below).

***

## Architecture of the Compliance module

The module is based on a logical chain of objects, from regulatory frameworks through to compliance evidence.

<figure><img src="../../.gitbook/assets/mermaid-diagram-2026-01-28-160744.png" alt="Chain of objects of the module: framework, requirements, controls, risk scenarios, tests, evidence and audits"><figcaption></figcaption></figure>

### Frameworks

Examples: GDPR, ISO 27701, ISO 27001, AI Act.

A framework:

* defines the regulatory or normative framework,
* contains a set of applicable requirements.

***

### Requirements

Requirements represent the obligations arising from a framework.\
Examples: access control, authorization management, logging.

Each requirement:

* is attached to a framework,
* is assessed during compliance audits,
* is implemented through one or more controls.

***

### Controls

Controls describe **how** a requirement is applied concretely.\
Examples: periodic access review, authorization procedure.

A control:

* implements a requirement,
* is linked to one or more risk scenarios,
* is verified using tests.

***

### Risk scenarios

Risk scenarios describe the feared events. They appear as **Risks** in the application.\
Example: unauthorized access to sensitive data.

Controls make it possible:

* to prevent or reduce these risks,
* to demonstrate the remediation measures put in place.

***

### Tests

Tests are used to verify the effectiveness of controls.\
Examples: recurring access review, validation delegation.

A test:

* checks one or more controls,
* produces measurable results,
* is supported by evidence.

***

### Test campaigns

Campaigns make it possible to orchestrate tests at scale:

* sending campaigns to teams or clients,
* centralized collection of responses,
* tracking progress and statuses.

***

### Evidence

Evidence demonstrates compliance.\
Examples: policies, procedures, access review reports.

A piece of evidence:

* is associated with a test,
* is used during audits,
* ensures the traceability of controls.

***

### Compliance audits

Audits make it possible to assess the level of compliance:

* internal audits,
* self-assessments,
* preparation for external audits.

They rely on:

* requirements,
* controls,
* the associated tests and evidence.

***

### Overview

The Dastra Compliance module thus makes it possible to:

* structure regulatory requirements,
* connect obligations to risks,
* prove compliance through tested and documented controls,
* efficiently prepare for audits and certifications.

### The multi-framework principle in Dastra

The Dastra Compliance module is **natively multi-framework**.

This means that:

* a given **framework** (GDPR, ISO, AI Act…) contains its own requirements,
* a **requirement** belongs to **one framework**,
* a **control can address several requirements**, including ones from **different frameworks**,
* **tests and evidence** are shared and reusable.

Objective: **avoid duplication** and steer compliance in a cross-cutting way.

***

### Key relationships between objects

* a **framework** contains several **requirements** (1 to N),
* **requirements** and **controls**: N to N relationship,
* **controls** and **tests**: N to N relationship,
* a **test** is supported by several pieces of **evidence** (1 to N),
* **controls** and **risk scenarios**: N to N relationship.

A single control (e.g. access review) can thus:

* satisfy a GDPR requirement,
* satisfy an ISO 27001 requirement,
* reduce several risk scenarios.

Explanatory diagram:

<figure><img src="../../.gitbook/assets/compliance-framework-architecture-diagram.png" alt="Relationships between frameworks, requirements, controls, tests, evidence and risk scenarios"><figcaption></figcaption></figure>

***

## Statistics

**Compliance** > **Statistics** opens the **Compliance Dashboard**, which consolidates all the projects of the workspace. Filter it by **Status** (project phase), **Organizational units** and **Scopes**.

The dashboard contains:

* global indicators. Controls: **Total Controls**, **Passing Controls**, **Not Implemented** and **Orphan Controls** (with no associated requirement). Tests: **Total Tests**, **Passing Tests**, **Failing Tests** and **Missing Evidence**. Audits: **Total Audits**, **Completed Audits** and **Average Readiness**, with the distribution of requirements between **Compliant**, **Partially Compliant**, **Not Compliant** and **Not Applicable**;
* **Framework Progression**: for each framework, the number of projects and the progress of controls, tests, requirements and risks;
* **Projects by Status**: the distribution of projects by phase;
* **Compliance by Scope**: the compliance level of each scope.

<figure><img src="../../.gitbook/assets/compliance-statistics-1.png" alt="Compliance dashboard with the global indicators, the framework progression and the compliance by scope"><figcaption></figcaption></figure>
