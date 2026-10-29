---
description: >-
  Erstellen und verwalten Sie die API-Schlüssel Ihrer Organisation: Mandant,
  Ablauf, Berechtigungen, Zugriff auf den MCP-Server.
---

# API-Schlüssel verwalten

Diese Seite erklärt, wofür die API-Schlüssel von Dastra verwendet werden und wie Sie sie erstellen und verwalten. Nur die Inhaber der Organisation haben Zugriff darauf.

## Verwendung von API-Schlüsseln

* **Einen Dastra-API-Client erstellen**, um Daten außerhalb der Anwendung abzurufen oder zu ändern. Dieser Client kann Server-zu-Server (Client credential) oder JavaScript (Authorization code) sein. Weitere Informationen finden Sie in der [Dokumentation zur Authentifizierung bei der Dastra-API](../../api/authentication.md).
* **Ein Widget für Betroffenenanfragen konfigurieren** (nur öffentlicher Schlüssel). Lesen Sie die [Dokumentation zu den Formularen für Betroffenenanfragen](../requests/widget.md).
* **Ein Cookie-Widget konfigurieren** (nur öffentlicher Schlüssel). Lesen Sie die [Dokumentation zu Cookies](../cookies/banner/configure.md).
* **Ein KI-Tool mit dem Dastra-MCP-Server verbinden**. Lesen Sie die [Dokumentation zum MCP-Server](../general/ai-assistant/mcp.md).

## Wo Sie API-Schlüssel verwalten

Klicken Sie in der oberen Leiste auf das Zahnradsymbol (**Organisationseinstellungen**) und dann im linken Menü auf **API-Schlüssel & MCP**. Die direkte Adresse lautet [https://app.dastra.eu/general-settings/api](https://app.dastra.eu/general-settings/api).

Die Seite hat drei Tabs:

* **API keys**: die Liste der Schlüssel. Für jeden Schlüssel werden der Name, die letzte Verwendung (**Never**, wenn der Schlüssel noch nie verwendet wurde) und der Mandant angezeigt. Das Kennzeichen **Expired** markiert einen Schlüssel, dessen Ablaufdatum überschritten ist, und das Kennzeichen `MCP` einen Schlüssel mit Zugriff auf den MCP-Server.
* **MCP Server**: verbindet ein KI-Tool mit dem Dastra-MCP-Server. Siehe [Der MCP-Server](../general/ai-assistant/mcp.md).
* **tenantId & workspaceId**: die Kennung der Organisation (**TENANT ID**) und jedes Mandanten (**WORKSPACE ID**), mit einer Schaltfläche zum Kopieren. API-Aufrufe, die diese Kennungen verlangen, verwenden sie.

## Einen API-Schlüssel erstellen

1. Klicken Sie im Tab **API keys** auf **Erstellen Sie einen neuen API-Schlüssel**.
2. Geben Sie den **Name** des Schlüssels ein.
3. Um den Schlüssel auf einen Mandanten zu beschränken, wählen Sie ihn unter **Auswahl eines bestimmten Mandanten**. Wenn Sie keinen wählen, gilt der Schlüssel für **Alle Mandanten**.
4. Wählen Sie den **Expiration**: **Unlimited**, 30 Tage, 180 Tage, 365 Tage oder **Custom date**.
5. Antworten Sie bei **Möchten Sie alle Zugriffsberechtigungen für diesen API-Schlüssel gewähren?** mit **Ja** für einen Schlüssel ohne Einschränkungen oder mit **Nein**, um nur die Berechtigungen anzukreuzen, die der Schlüssel verwenden darf.
6. Klicken Sie auf **Erstellen**.

<figure><img src="../../.gitbook/assets/settings-api-keys-1.png" alt="Das Fenster zum Erstellen eines API-Schlüssels mit Name, Mandant, Ablauf und Berechtigungen"><figcaption><p>Einen API-Schlüssel erstellen</p></figcaption></figure>

Das Panel **API key details** öffnet sich. Es zeigt:

* den öffentlichen Schlüssel (`client_id`) und den privaten Schlüssel (`client_secret` oder API-Schlüssel), der maskiert ist und aus dem Panel kopiert werden kann;
* die Schaltfläche **Erneuern Sie den privaten Schlüssel**, die einen neuen privaten Schlüssel erzeugt, ohne den API-Schlüssel zu löschen;
* den Mandanten, den Zugriff auf den MCP-Server, die letzte Verwendung und den Ablauf des Schlüssels;
* die **Permissions** des Schlüssels, die Sie mit der Schaltfläche zum Bearbeiten anpassen können;
* die erlaubten CORS-Herkunftsadressen und die erlaubten Weiterleitungs-URIs, die Sie ausfüllen, wenn Sie die API in JavaScript mit OAuth2 (Authorization code) verwenden.

<figure><img src="../../.gitbook/assets/settings-api-keys-2.png" alt="Das Panel mit den Details eines API-Schlüssels, der private Schlüssel ist maskiert"><figcaption><p>Die Details eines API-Schlüssels</p></figcaption></figure>

{% hint style="info" %}
Der Ablauf und der Zugriff auf den MCP-Server werden bei der Erstellung des Schlüssels gewählt und lassen sich danach nicht mehr ändern. Um eines von beiden zu ändern, erstellen Sie einen neuen Schlüssel.
{% endhint %}

## Einen Schlüssel mit dem MCP-Server verwenden

Wenn Ihr Tarif den MCP-Server enthält (Dastra AI Pro), bietet das Fenster zur Erstellung die Option **Allow this key to access the MCP server (requires a specific workspace)** an. Schalten Sie sie ein und wählen Sie einen Mandanten: Der MCP-Server lehnt einen Schlüssel ohne diese Option oder ohne Mandant ab. Zugelassene Schlüssel tragen in der Liste das Kennzeichen `MCP`. Siehe [Der MCP-Server](../general/ai-assistant/mcp.md).

## Einen Schlüssel ersetzen oder löschen

{% hint style="warning" %}
Bewahren Sie Ihre API-Schlüssel sicher auf. Der private Schlüssel darf niemals veröffentlicht werden.

Wenn die Sicherheit Ihres API-Schlüssels gefährdet ist, klicken Sie im Detailpanel auf **Erneuern Sie den privaten Schlüssel** oder löschen Sie den Schlüssel in der Liste (Dreipunktmenü > **Löschen**) und erstellen Sie einen neuen.
{% endhint %}
