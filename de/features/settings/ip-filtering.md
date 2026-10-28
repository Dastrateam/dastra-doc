---
description: >-
  Beschränken Sie die Anmeldung bei Dastra auf zugelassene IP-Adressbereiche:
  Geltungsbereich, Funktionsweise, Sperrung und Hinweise.
---

# IP-Filterung

Mit der IP-Filterung können Sie den Zugriff auf Ihre Dastra-Organisation auf eine Liste zugelassener IP-Adressbereiche beschränken (z. B. die Ihrer Büros oder Ihres Unternehmens-VPN). Die Konfiguration erfolgt unter **Konfiguration** > **Sicherheit**.

{% hint style="info" %}
Diese Funktion ist dem Enterprise-Tarif oder einer kostenpflichtigen Option vorbehalten. Wenden Sie sich zur Aktivierung an Ihren Dastra-Ansprechpartner.
{% endhint %}

{% hint style="danger" %}
Eine Warnung weist darauf hin: „Diese Aktion ist nicht umkehrbar". In der Praxis kann eine Filterregel über die Oberfläche weder gelöscht noch deaktiviert werden: **Nur das Administrationsteam von Dastra** kann sie entfernen. Prüfen Sie Ihre Bereiche sorgfältig vor dem Speichern, sonst sperren Sie sich möglicherweise selbst aus.
{% endhint %}

## Regeln definieren

* Die Regeln gelten für die **gesamte Organisation** (nicht für einen einzelnen Arbeitsbereich).
* Jede Regel besteht aus einem Bereich mit einer **Start-** und einer **Endadresse**. Die CIDR-Notation (z. B. `10.0.0.0/24`) wird nicht unterstützt: Wandeln Sie Ihre Netzwerke in Start- und Endadressen um.
* **IPv4- und IPv6**-Adressen werden akzeptiert.
* Die Anzahl der Regeln ist nicht begrenzt.

## Wer ist betroffen?

Die Filterung gilt für **alle Nutzer der Organisation, einschließlich Administratoren**. Es gibt weder eine Ausnahme für Administratoren noch eine Ausnahmeliste.

Sie betrifft alle Anmeldemethoden, da die Prüfung nach der Authentifizierung erfolgt:

* Benutzername und Passwort;
* SSO (SAML 2, OpenID, ADFS, Entra, Okta);
* Passkey;
* Magic Link oder Einladung per E-Mail.

Lokale Dienstkonten, die vom SSO ausgenommen sind, sind **nicht** von der IP-Filterung ausgenommen.

## Wann erfolgt die Prüfung?

Die IP-Adresse wird bei der Anmeldung und bei jeder **Erneuerung des Tokens** geprüft. Eine bereits geöffnete Sitzung wird daher nicht sofort beendet, wenn der Nutzer das Netzwerk wechselt (z. B. vom Büro ins Homeoffice): Sie endet bei der nächsten Token-Erneuerung.

Gültigkeitsdauer der Tokens:

| Sitzungstyp | Gültigkeit des Tokens |
|---|---|
| Webanwendung | 6 Minuten (automatisch erneuert) |
| Standardsitzung | 1 Stunde |
| „Angemeldet bleiben" | 30 Tage |

## Welche IP-Adresse wird berücksichtigt?

Dastra verwendet die öffentliche IP-Adresse, die seine Zugangsinfrastruktur sieht (die Schicht, die Ihre Anfrage vor der Anwendung entgegennimmt). Ein Nutzer, der ein VPN oder einen Unternehmens-Proxy verwendet, wird daher anhand der **Ausgangsadresse** des VPN bzw. Proxys gefiltert: Diese Adresse müssen Sie zulassen.

## Was ein gesperrter Nutzer sieht

Der Nutzer wird auf eine Fehlerseite weitergeleitet mit der Meldung:

> IP Address not allowed — Your IP address is not allowed by your organization. Please contact your account's administrator.

{% hint style="warning" %}
Sperrungen werden **nicht** im Audit-Protokoll erfasst und nicht an das [SIEM-Streaming](siem.md) gesendet.
{% endhint %}

## Was die Filterung nicht abdeckt

| Zugriff | Gefiltert? |
|---|---|
| API-Aufrufe mit einem [API-Schlüssel](api-keys.md) | Nein |
| [SCIM](scim.md) | Nein |
| [SIEM-Streaming](siem.md) und BI-Konnektoren | Nein |
| Externe Fragebogen-Teilnehmer (öffentlicher Link) | Nein |
| Portal für Betroffenenanfragen und Trust Center | Nein, sie haben eigene Einstellungen (siehe [Trust Center – Sicherheit](../trust-center/configuration/security.md)) |

## Dastra-Support

Auch der Dastra-Support unterliegt der Filterung: Er kann von einer nicht zugelassenen Adresse aus nicht mehr auf Ihr Konto zugreifen (Impersonation). Um eine Regel zu löschen oder zu deaktivieren, wenden Sie sich an den Dastra-Support.
