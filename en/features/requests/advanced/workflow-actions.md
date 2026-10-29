# Additional actions in automated workflows

Workflow rules automate operations in Dastra. For data subject requests, they offer specific actions that you configure to match your own handling rules. Open **Workflow rules** in the workspace settings, then add an action to a rule that applies to requests.

<figure><img src="../../../.gitbook/assets/requests-workflow-actions-1.png" alt="The list of actions offered for a workflow rule that applies to requests"><figcaption><p>Actions specific to data subject requests</p></figcaption></figure>

## Request-specific actions

* **Send a message to the requester**: sends a message to the requester from the request, with free text or a template.
* **Close the request**: closes the request with a closing reason, and can send the closing notification to the requester.
* **Anonymise the request**: erases the identifying data of the request. The action is irreversible.
* **Move to recycle bin**: moves the request to the recycle bin, where the [purge rules](purge.md) then apply.

## Other useful actions for requests

* **Edit a field**: updates a field of the request.
* **Add a task**: creates a task, for example to have the DPO validate the answer.
* **Send notification**: notifies people about the request.
* **Define owner**: sets the owner of the request.
* **Add tag (s)**: adds tags to the request.
* **Schedule a response to a questionnaire**: plans a questionnaire response.
* **Send an HTTP request**: calls an external service.
* **Execute an AI agent**: runs an AI agent, depending on your plan and your permissions.

{% hint style="info" %}
To learn more about workflows, see [Workflow rules](../../settings/workflow-rules.md).
{% endhint %}
