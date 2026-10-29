# Glossary of terms

These are the terms used in the risk management module.

* **Likelihood (probability):** the evaluation of how often a risk occurs. It is a score evaluated empirically, from 1 to 5 with the default scale. Each level corresponds to a frequency of occurrence of the risk. The app shows it under the label **likelihood**.
* **Severity (impact):** the evaluation of the consequence of a dreaded event on the organization. The app shows it under the label **Severity**.
* **Initial (or inherent) risk:** the theoretical risk associated with the activity, before any control measure (internal control). It is calculated by multiplying the initial impact by the initial probability.
* **Residual risk:** the risk remaining after the implementation of control measures (internal control). It is calculated by multiplying the residual impact by the residual probability.
* **Current risk:** the level of risk at a given moment, according to the remediation level of your control points. It is calculated as follows: {Current risk} = {Initial risk} - ({Initial risk} - {Residual risk}) \* {Remediation rate}. Without any response to control points, the current risk equals the initial risk.
* **Dreaded event:** the uncertain event that is characterized by its frequency and severity. It is the consequence of the occurrence of a risk.
* **Risk type:** groups a dreaded event, its threats, its sources, its control points and a pre-assessment. You reuse it on as many objects as needed.
* **Risk:** the combination of a risk type and its evaluation (impact and probability) on an object: organizational unit, processing activity, stakeholder (for example a processor), asset or AI system. Threats (the events at the origin of the dreaded event) and sources (who or what can cause them) complete the description.
* **Control point:** (or risk management system). Complying with the control points is the way to bring the current risk toward the residual risk. In Dastra, the list of control points is attached to the risk type.
* **Remediation (remediation rate):** the share of control measures actually in place for a risk. It is calculated as follows: the sum of the points of the current response of each control point, divided by the sum of the maximum points of each control point, rounded up to the next percent. **Not applicable** responses are excluded from the calculation, and a control point without a response counts zero points. For example, with three control points whose responses are worth only 0 or 1 point, two compliant control points out of three give a remediation rate of 67%.
