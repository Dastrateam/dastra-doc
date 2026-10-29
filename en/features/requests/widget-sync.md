# Widget synchronization

When several data subject request widgets share a similar configuration (same fields, same texts), you can synchronize them. Designate one widget as the source, sync child widgets from it, then propagate any change in a single click to all linked widgets.

This is particularly useful for organizations that manage several variants of the same widget (for example, an account deletion widget deployed across different applications or geographic markets).

In the application, a widget is a form: open it from **Requests** > **Forms**. The sync buttons are at the top of the form page, next to **Preview**.

## Sync content from another widget

To import the configuration of an existing widget into the current one:

1. Click the sync drop-down button next to **Preview**.
2. Click **Sync content from another form**.
3. In **Source form**, select the source widget.
4. Under **What do you want to sync?**, select the elements to import: **Texts & translations**, **Form fields** and **Design & templating**.
5. Click **Sync**.

<figure><img src="../../.gitbook/assets/requests-widget-sync-1.png" alt="Form page with the sync drop-down button next to the Preview button"><figcaption><p>The sync button, next to Preview, imports the configuration of a source widget</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/consent-widget-sync-form-dialog.png" alt="Sync content from another form dialog"><figcaption><p>Selecting the source widget and the elements to import</p></figcaption></figure>

After the sync, the widget becomes a child of the source widget. The button label changes, and the drop-down now offers **Clear** to remove the link with the source.

## Propagate changes to child widgets

Once you have made changes to the source widget, propagate them in one click to all linked widgets:

1. Click **Propagate changes to linked forms**, followed by the number of child widgets in parentheses.
2. Check the list of child widgets, then select the elements to propagate.
3. Click **Propagate**.

<figure><img src="../../.gitbook/assets/consent-widget-propagate-dialog.png" alt="Propagate to linked forms dialog"><figcaption><p>Pushing changes from the source widget to all its children (texts, fields, design)</p></figcaption></figure>

{% hint style="info" %}
The **Propagate changes to linked forms** button only appears on a widget that has at least one child widget. In that case, the sync button is hidden: a source widget cannot itself be synced from another widget.
{% endhint %}
