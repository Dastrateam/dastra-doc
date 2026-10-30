---
description: Senden Sie Dastra-Workflow-Benachrichtigungen an Ihre Microsoft Teams-Kanäle
---

# Microsoft Teams

### Was macht die Integration?

Die Microsoft Teams-Integration veröffentlicht **Dastra-Workflow-Benachrichtigungen als Karten in einem Microsoft Teams-Kanal**: Wenn eine Workflow-Regel ausgelöst wird (z. B. wenn eine Datenschutzverletzung erstellt wird oder eine Anfrage die Workflow-Phase wechselt), sendet Dastra eine Karte mit einem Titel, einer Nachricht und optional einem Link zum entsprechenden Eintrag in Dastra.

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### Voraussetzungen

Sie benötigen einen Microsoft Teams-Kanal mit einem **eingehenden Webhook, der über die Workflows-App** (Power Automate) erstellt wurde:

1. Öffnen Sie in Teams den Kanal und klicken Sie auf **⋯ > Workflows**.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

\
2\. Suchen Sie nach „Webhook“ und wählen Sie die Vorlage **Webhook-Warnungen an einen Kanal senden** (_Send webhook alerts to a channel_).

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

3. Wählen Sie das Team und den Kanal aus und klicken Sie anschließend auf **Speichern**.

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

4. Klicken Sie auf dem Bestätigungsbildschirm auf **Webhook-Link kopieren** — dies ist die URL, die Sie in Dastra einfügen müssen (im Format `https://prod-XX.westeurope.logic.azure.com/workflows/...`).

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Microsoft hat die klassischen eingehenden Office 365-Webhooks (Kanal-Connectors) im April 2026 eingestellt. Die **Workflows-App** ist die von Microsoft vorgesehene Nachfolgelösung, auf der diese Integration basiert.
{% endhint %}

### Installation

1. Öffnen Sie in Dastra **Mandanteneinstellungen** > **Integrationen** und wählen Sie **Microsoft Teams** aus.
2. Klicken Sie beim Anwendungsfall für Workflow-Benachrichtigungen auf **Integration hinzufügen**.
3. Fügen Sie eine Verbindung hinzu und fügen Sie die **Workflows-Webhook-URL** ein.
4. Klicken Sie auf **Verbinden**. Dastra veröffentlicht sofort eine Testkarte („_Dastra-Testbenachrichtigung_“) im Kanal, um die URL zu validieren.

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Die Webhook-URL muss ein Power-Automate-Endpunkt über HTTPS sein (`*.logic.azure.com`, `*.azure-api.net` oder `*.api.powerplatform.com`). Andere Hosts werden abgelehnt.
{% endhint %}

Um **mehrere Kanäle** zu benachrichtigen, erstellen Sie für jeden Kanal eine eigene Verbindung (jeder Workflows-Webhook ist jeweils nur einem Kanal zugeordnet).

### Benachrichtigungen über eine Workflow-Regel senden

Sobald die Integration installiert und aktiviert ist, steht im Designer für Workflow-Regeln eine neue Aktion zur Verfügung: **Teams-Benachrichtigung senden**.

Konfigurieren Sie sie wie die E-Mail-Benachrichtigungsaktion:

* **Kartentitel** — unterstützt Platzhaltervariablen (z. B. den Namen des Datensatzes).
* **Nachricht** — Rich-Text mit Platzhaltervariablen.
* **Link zum Objekt in die Karte aufnehmen** — fügt der Karte die Schaltfläche **In Dastra anzeigen** hinzu.

Es muss kein Empfänger ausgewählt werden: Die Karte wird in dem Kanal zugestellt, der mit dem Webhook verknüpft ist.

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Die Teams-Aktion wird im Aktionsauswahlmenü nur angezeigt, wenn die Integration im Mandanten installiert und aktiviert ist.
{% endhint %}

### Deinstallation

Wenn Sie die Microsoft Teams-Integration deinstallieren, wird die Webhook-URL gelöscht und alle Workflow-Regeln, die die Teams-Aktion verwenden, werden **automatisch deaktiviert** (nicht gelöscht), um zu verhindern, dass Ihre Regeln Fehler verursachen. Aktivieren Sie sie nach der erneuten Installation der Integration wieder.
