---
description: Dastra integriert sich in alle Ihre Tools
---

# Integrationen

## Einführung

Dastra verbindet sich mit den Tools, die Ihre Teams bereits nutzen: Importieren Sie Ihr Anwendungsinventar aus Ihrem ITAM oder Ihrer CMDB, synchronisieren Sie Anfragen betroffener Personen mit Ihrem Ticketsystem, senden Sie Benachrichtigungen in Ihre Kollaborationskanäle, streamen Sie Ihre Sicherheits-Audit-Protokolle an Ihr SIEM oder hängen Sie Dateien aus Ihren Cloud-Laufwerken an. Native Konnektoren decken die gängigsten Tools ab, Zapier alles andere.

Der Integrations-Marktplatz steht unter **Mandanteneinstellungen** > **Integrationen** Ihres Mandanten zur Verfügung. Er listet alle verfügbaren Integrationen auf und lässt sich nach Kategorie und nach dem jeweiligen Dastra-Objekt filtern, mit einem Umschalter **Alle / Installiert**.

## Wie native Integrationen funktionieren

Jede native Integration beruht auf drei Konzepten:

* **Anwendungsfälle**: jede Integration stellt einen oder mehrere Anwendungsfälle bereit (zum Beispiel _Anwendungen als Assets importieren_ oder _Anfragen betroffener Personen synchronisieren_). Anwendungsfälle werden unabhängig voneinander installiert, aktiviert, konfiguriert und deinstalliert.
* **Verbindungen**: eine Verbindung speichert, wie sich Dastra beim externen Tool authentifiziert: Zugangsdaten, die Dastra verschlüsselt speichert, oder eine delegierte OAuth-Autorisierung. Sie können mehrere Verbindungen zum selben Tool anlegen (zum Beispiel eine Produktions- und eine Sandbox-Instanz) und wählen, auf welche sich jeder Anwendungsfall stützt. Verbindungen zeigen ihren Zustand an und können jederzeit getestet werden.
* **Feld-Mapping**: bei Import-Anwendungsfällen wählen Sie für jedes Dastra-Feld das externe Feld, das es befüllt, mit Standardwerten, Wertumwandlung für geschlossene Listen (Status, Lebenszyklusphasen usw.) und KI-gestützten Vorschlägen.

Import-Konnektoren synchronisieren einmal täglich und auf Abruf mit **Synchronisierung starten**. Jede Ausführung wird in den Integrationsprotokollen nachverfolgt, mit der Anzahl der erstellten, aktualisierten, markierten und fehlerhaften Elemente.

<figure><img src="../../.gitbook/assets/integrations-catalog.png" alt="Der Integrations-Marktplatz mit den verfügbaren Integrationen"><figcaption></figcaption></figure>

Die Einzelheiten finden Sie unter [Verbindungen, Anwendungsfälle und Feld-Mapping](connections.md).

## Verfügbare Integrationen

| Integration | Funktion | Dokumentation |
| --- | --- | --- |
| **ServiceNow** | Importiert die Geschäftsanwendungen Ihrer CMDB als Assets und hält sie täglich synchron | [ServiceNow](servicenow.md) |
| **SAP LeanIX** | Importiert Ihre Fact Sheets vom Typ Application als Assets und hält sie täglich synchron | [SAP LeanIX](sap-leanix.md) |
| **Jira** | Erstellt und verfolgt Anfragen betroffener Personen aus Ihrem Jira-Projekt und sendet Ihre Aufgaben als synchron gehaltene Tickets an Jira (Status, Zuständiger, zugeordnete Felder) | [Jira](jira.md) |
| **Filerskeepers** | Integriert Ihre Filerskeepers-Aufbewahrungsrichtlinien in Dastra | [Filerskeepers](filerskeepers.md) |
| **Microsoft Teams** | Veröffentlicht die Benachrichtigungen Ihrer Workflow-Regeln als Karten in einem Teams-Kanal | [Microsoft Teams](microsoft-teams.md) |
| **HTTP / Custom API** | Ruft aus Ihren Workflow-Regeln jede externe API mit einer benutzerdefinierten HTTP-Anfrage auf, mit Methode, URL, Headern und einem aus dem Datensatz erzeugten JSON- oder XML-Body | [HTTP / Benutzerdefinierte API](custom-http.md) |
| **Slack** | Benachrichtigt Nutzer auf Slack, wenn sie in einem Kommentar erwähnt werden | [Slack](#slack) |
| **Docusign** | Sendet Ihre Verträge zur elektronischen Signatur an Ihre Dienstleister | [Integration mit Docusign](../contracts/docusign.md) |
| **OneDrive & SharePoint / Google Drive** | Hängt Dateien aus Ihrem OneDrive, Ihren SharePoint-Bibliotheken oder Ihrem Google Drive an Ihre Stakeholder, Sicherheitsmaßnahmen, Verarbeitungstätigkeiten, Aufgaben, Vorfälle usw. an | [OneDrive/SharePoint- und Google-Drive-Integrationen](../settings/cloud-storage.md) |
| **Office 365 / Gmail** | Sendet Dastra-E-Mails aus Ihrem eigenen Postfach | [SMTP-Konfiguration](../settings/smtp/README.md) |
| **Eingehende E-Mails** | Wandelt die E-Mails, die an eine dedizierte Erfassungsadresse gesendet werden, in Aufgaben, Anfragen, Datenschutzverletzungen, Verträge oder Verarbeitungstätigkeiten um | [E-Mail-Adressen für Datenerfassung](../settings/mailboxes.md) |
| **SIRENE (INSEE)** | Füllt die Angaben Ihrer Stakeholder aus dem französischen Unternehmensregister aus | [SIRENE (INSEE)](#integration-sirene-insee) |
| **KI-Anbieter** | Verbindet jeden OpenAI-kompatiblen KI-Anbieter mit dem Dastra-Assistenten | [Funktionsweise](../general/ai-assistant/how-it-works.md) |
| **Single Sign-on (SSO)** | Ermöglicht Ihren Nutzern die Anmeldung mit Ihrem eigenen Identitätsanbieter | [Single Sign On (SSO)](../settings/sso/README.md) |
| **SIEM-Streaming** | Streamt Ihre Sicherheits-Audit-Ereignisse in Echtzeit an Ihr SIEM | [SIEM-Streaming](../settings/siem.md) |
| **Zapier** | Verbindet Dastra über automatisierte Workflows mit Tausenden von Anwendungen | [Zapier](zapier/README.md) |

Einige Integrationen gelten für Ihre gesamte Organisation statt für einen Mandanten: Single Sign-on, SIEM-Streaming, Office 365 / Gmail und der KI-Anbieter. Ihre Kachel im Marktplatz führt Sie zu den entsprechenden Organisationseinstellungen, wo sie von einem Kontoinhaber konfiguriert werden.

## Zapier: alles andere verbinden

Zapier ist ein Online-Automatisierungstool, das Ihre Anwendungen und Dienste ohne Code verbindet. Ein **Zap** ist ein automatisierter Workflow aus einem **Trigger** und einer oder mehreren **Aktionen**: Tritt das Trigger-Ereignis ein, werden die Aktionen ausgeführt.

Auf Seiten von Dastra kann Zapier auf zwei Trigger (_neue Anfrage einer betroffenen Person erstellt_ und _neue Aufgabe erstellt_) reagieren und sechs Aktionen ausführen: eine Aufgabe erstellen, einen Stakeholder erstellen, eine Anfrage einer betroffenen Person erstellen, einen Stakeholder mit einer bestehenden Verarbeitungstätigkeit verknüpfen, einen Stakeholder suchen sowie einen Stakeholder finden oder erstellen. Sie können also von einem Ereignis in Dastra ausgehen, um in einer Drittanwendung zu handeln, oder von einem Ereignis einer Drittanwendung, um in Dastra zu handeln.

Vorkonfigurierte Vorlagen (Salesforce, Zoho, Trello, Google Sheets, Excel, Outlook, Azure DevOps …) stehen auf der [Dastra-Seite im Zapier-Katalog](https://zapier.com/apps/dastra/integrations) bereit, und im Zap-Editor erstellen Sie Ihren eigenen Workflow von Grund auf. Siehe die Seite [Zapier](zapier/README.md) und ihre [häufig gestellten Fragen](zapier/faq.md).

## Slack

Die Slack-Integration tut genau eine Sache: Wird ein Nutzer in einem Kommentar mit der Syntax @Benutzername erwähnt, sendet ihm der Dastra-Bot eine Direktnachricht auf Slack. Die Nachricht zeigt, wer den Nutzer erwähnt hat, den Text des Kommentars und die Art des verknüpften Objekts, mit einer Schaltfläche **View in Dastra**.

1. Öffnen Sie **Mandanteneinstellungen** > **Integrationen** und wählen Sie **Slack** aus.
2. Klicken Sie im Anwendungsfall für Erwähnungen auf **Integration hinzufügen**.
3. Wählen Sie im Schritt **Anmelden** die Option **Verbindung hinzufügen** und klicken Sie dann auf **Registrieren und anmelden**. Dastra leitet Sie zu Slack weiter, um die Anwendung in Ihrem Slack-Workspace zu autorisieren.

Die Verbindung genügt: Dieser Anwendungsfall hat keinen Konfigurationsschritt. Dastra fragt bei Slack die Berechtigungen ab, Nachrichten zu senden sowie Nutzer und ihre E-Mail-Adresse zu lesen.

{% hint style="info" %}
Dastra findet den Slack-Nutzer anhand seiner E-Mail-Adresse. Ein Nutzer, dessen E-Mail-Adresse in Dastra mit keinem Konto Ihres Slack-Workspace übereinstimmt, erhält keine Nachricht.
{% endhint %}

## Integration SIRENE (INSEE)

Die Integration SIRENE (INSEE) fragt das französische Unternehmensregister ab, um die Angaben eines Stakeholders auszufüllen. Sie wird von Dastra verwaltet: Es sind keine Zugangsdaten einzugeben, und sie deckt nur in Frankreich eingetragene Unternehmen ab.

1. Öffnen Sie **Mandanteneinstellungen** > **Integrationen** und wählen Sie **Sirene / Insee** aus.
2. Klicken Sie auf **Integration hinzufügen**. Die Integration wird sofort aktiviert.

Anschließend erscheint im Formular eines Stakeholders vom Typ **Juristische Person** neben dem Feld **Name der Organisation** eine Suchschaltfläche (**Suche in der SIRET-Datenbank**). Geben Sie den Namen des Unternehmens ein, starten Sie die Suche und klicken Sie dann beim passenden Unternehmen auf **Bitte auswählen**. Dastra füllt den Namen, die Registrierungsnummer (SIREN) und die Postanschrift aus.

## Sicherheit und Datenschutz

* Zugangsdaten und Token der Integrationen werden verschlüsselt gespeichert, nie von der API zurückgegeben und gelöscht, wenn Sie eine Integration deinstallieren oder einen Mandanten löschen.
* OAuth-Abläufe validieren ihre Callbacks streng, und die Endpunkte für eingehende Webhooks sind in der Anzahl der Aufrufe begrenzt.
* Integrationen sind auf einen Mandanten beschränkt: Daten eines Mandanten sind nie aus einem anderen sichtbar.
* Von einer Integration erstellte Datensätze (Assets, Anfragen usw.) gehören zu Ihrem Mandanten und bleiben erhalten, wenn die Integration deinstalliert wird.

## Weitere Anforderungen

Wenn keine Integration Ihrem Bedarf entspricht, können Sie mit der [Dastra-REST-API](../../api/configuration.md) eigene Skripte und Konnektoren entwickeln, und Sie können über den Support beim Dastra-Team eine Konnektor-Anfrage einreichen.
