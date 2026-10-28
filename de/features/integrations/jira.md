---
description: >-
  Jira-Integration zur Synchronisierung von Tickets mit Anfragen zur Ausübung
  von Betroffenenrechten in Dastra
---

# Jira

### Was macht die Integration?

Die Jira-Integration synchronisiert **Jira-Tickets mit Anfragen zur Ausübung von Betroffenenrechten (DSR) in Dastra** – in beide Richtungen:

* **Jira → Dastra**: Wenn ein Ticket im konfigurierten Jira-Projekt erstellt oder aktualisiert wird, erstellt oder aktualisiert Dastra die entsprechende Anfrage und füllt deren Felder entsprechend Ihrem Mapping aus.
* **Dastra → Jira**: Wenn eine Anfrage eine bestimmte Workflow-Phase erreicht, setzt Dastra das verknüpfte Jira-Ticket automatisch auf den Status, den Sie dieser Phase zugeordnet haben.

### Voraussetzungen

* Eine Jira-Cloud-Instanz (z. B. `https://ihr-unternehmen.atlassian.net`) und ein zu synchronisierendes Projekt.
*   Je nach Authentifizierungsmethode:

    * **Basic** — die E-Mail-Adresse eines Jira-Kontos und ein [API-Token](https://id.atlassian.com/manage-profile/security/api-tokens) für dieses Konto.
    * **OAuth** — kein Token muss erstellt werden: Sie melden sich mit Ihrem Atlassian-Konto an und autorisieren Dastra.



Die OAuth-Methode wird in der Liste **Authentifizierungsmethode** angezeigt, sofern sie in Ihrer Dastra-Umgebung verfügbar ist. Andernfalls verwenden Sie ein API-Token.

### Installation

1. Öffnen Sie **Einstellungen > Integrationen** und wählen Sie **Jira** aus.
2. Klicken Sie im DSR-Anwendungsfall auf **Integration hinzufügen**.
3. Fügen Sie eine Verbindung hinzu:
   * **Basic**: Geben Sie die **Instanz-URL**, die **E-Mail-Adresse** und das **API-Token** ein und klicken Sie anschließend auf **Verbinden**.
   * **OAuth**: Geben Sie die **Instanz-URL** ein und klicken Sie anschließend auf **Speichern und verbinden** — Sie werden zu Atlassian weitergeleitet, um Dastra zu autorisieren.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Konfiguration

* **Jira-Projekt** — das zu synchronisierende Projekt.
* **Ticket-Typ** — der Ticket-Typ, der eine Anfrage zur Ausübung von Betroffenenrechten darstellt.
* **Feld-Mapping** — ordnen Sie die Felder einer Dastra-Anfrage den Jira-Feldern zu. Wenn ein Jira-Ticket eine Anfrage erstellt oder aktualisiert, wird jedes Feld mit dem ausgewählten Jira-Wert ausgefüllt. Als Quellen stehen die Jira-Standardfelder (Zusammenfassung, E-Mail-Adresse des Meldenden, Beschreibung, Status) **sowie Ihre benutzerdefinierten Jira-Felder** zur Verfügung. Felder mit festgelegten Werten (Status, Auswahllisten) können im Bereich **Erweitert** in Dastra-Werte umgewandelt werden.
* **DSR-Status mit Jira-Übergängen verknüpfen** — ordnen Sie jeder Phase des DSR-Workflows einen Jira-Status zu. Wenn eine Anfrage diese Phase erreicht, führt Dastra die entsprechende Transition des verknüpften Tickets aus. Lassen Sie eine Phase auf **Keine Transition**, um sie zu ignorieren.
* **Standard-Organisationseinheit** (erforderlich) — die Organisationseinheit, die den von der Integration erstellten Anfragen zugewiesen wird.

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Das Feld **E-Mail** der Anfrage muss zugeordnet werden (oder einen Standardwert erhalten), da es die betroffene Person identifiziert. Ohne dieses Feld kann die Konfiguration nicht gespeichert werden.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### Webhook (Jira → Dastra)

Speichern Sie zunächst die Konfiguration — die URL des eingehenden Webhooks wird verfügbar, sobald die Integration konfiguriert wurde. Im Schritt **Webhook** haben Sie anschließend zwei Möglichkeiten:

* **Manuelle Registrierung** — kopieren Sie die **Webhook-URL** und gehen Sie in Jira zu **Projekteinstellungen > Automation** (oder **Webhooks**). Fügen Sie dort einen Webhook hinzu, der für die Ereignisse _Ticket erstellt_ und _Ticket aktualisiert_ auf diese URL verweist.
* **Automatische Registrierung** — klicken Sie auf **Webhook in Jira registrieren**. Dastra registriert ihn anschließend über die Jira-API für Sie. Dafür benötigt das konfigurierte Konto die globale Berechtigung **Jira administrieren**. Sie können den Webhook später über **Webhook löschen** wieder entfernen.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### Deinstallation

Bei der Deinstallation der Integration werden die gespeicherten Zugangsdaten gelöscht und der in Jira registrierte Webhook entfernt (sofern dieser automatisch registriert wurde). Die von der Integration erstellten Anfragen bleiben erhalten.
