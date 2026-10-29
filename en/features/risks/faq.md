# FAQ

## Why does the Risk management menu not appear?

The module must be enabled for your workspace, and your role must include read access to risks. Creating or editing a risk requires write access. Contact your workspace administrator.

## Why can't I move a risk to the next step?

Only the owner of a risk can change its state: validate the assessment, validate the response, archive it or go back to a previous step. The owner's name is shown in the **Identification** section of the risk. To hand the risk over to someone else, change the **Risk owner** in that section.

## What is the difference between initial, residual and current risk?

The initial risk is the risk before any control measure. The residual risk is the one you aim for once the measures are in place. The current risk sits between the two, according to the remediation rate of your control points. The formulas are in the [glossary](glossary.md).

## Why does my current risk not change despite my control points?

Check the following:

* the response type is **Mitigation and controls**: the other options do not calculate a remediation rate;
* the risk has an initial level and a residual level;
* control points are assigned to the risk type and have received a response. A control point without a response counts zero points;
* the responses are not all **Not applicable**: these responses are excluded from the calculation.

## What happens if I change the risk scale?

Enabling another scale changes the statistics of every risk in the workspace, and Dastra asks for a confirmation before doing it. Choose your scale before entering your first risks. See [Configure the risk scale](process/assess.md#configure-the-risk-scale).

## How do I assess the same risk on several processing activities or assets?

Use **Batch risk identification**: select the risk type and all the objects concerned, and Dastra creates one risk per object. See [Risk management](README.md).
