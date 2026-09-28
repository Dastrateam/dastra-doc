---
description: >-
  Save your recurring instructions as reusable commands in the Dastra AI chat
---

# Skills

A **skill** is an instruction you save once and then recall with a command, by typing `/` in the conversation. Think of it as a prompt template shared across the organisation.

Skills are managed in **Workspace settings > AI agents > Skills**.

<figure><img src="../../../../.gitbook/assets/ai-agents-competences.png" alt="List of Dastra AI skills"><figcaption><p>The Skills tab, with Dastra's built-in skills</p></figcaption></figure>

***

### Built-in skills

Dastra ships two skills, available in every workspace and not editable:

| Command | What it does |
| --- | --- |
| `/scaffold_agent` | Guides you through designing a custom agent — persona, tools, rules — and saves it once you validate. This is what the **Generate with Dastra AI** option of the agent creation screen triggers. |
| `/dpo_opinion` | Turns the current discussion, or the record you are looking at, into a formal, archivable DPO opinion. |

### Creating your own skill

Click **Create a skill**, then fill in:

* **Name** — the label shown in the command list.
* **Command** — the text typed after the `/`. Lower case, with underscores, and **unique within the organisation**: for example `steering_committee_summary`.
* **Description** — one sentence explaining when to use it. It is shown next to the command in the chat.
* **Prompt** — the instruction sent to the assistant, up to 10,000 characters.
* **Visibility** — keep the skill to yourself, or share it with the other members of the workspace.

### Using a skill

In a Dastra AI conversation, type `/`: the list of available skills appears. Pick one, complete your message if needed, then send.

{% hint style="info" %}
A skill applies to the current conversation, with the agent and the mode (Ask or Edit) currently selected. A skill that needs to modify records therefore requires Edit mode.
{% endhint %}

***

### Skill or agent?

Both let you capitalise on an instruction, but not at the same moment:

* A **skill** is a one-off. You trigger it in the middle of a conversation, on whatever context is at hand.
* An **agent** is permanent. It has its own identity, its own tools, and where relevant its own schedule.

If you keep retyping the same request, create a skill. If you want a specialised counterpart or an automated task, create an [agent](README.md).
