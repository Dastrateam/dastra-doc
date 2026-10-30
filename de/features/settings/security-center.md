---
description: >-
  Legen Sie die Sicherheitsregeln Ihrer Organisation fest (Passworterneuerung,
  automatische Abmeldung, starke Authentifizierung, IP- und E-Mail-Domain-Filter)
  und sehen Sie die Sicherheitsprotokolle und den Aktivitätsverlauf ein.
---

# Sicherheit der Organisation und Sicherheitsprotokolle

Diese Seite richtet sich an die Inhaber der Organisation. Sie beschreibt die Seite **Sicherheit** der Organisationseinstellungen, auf der Sie die Sicherheitsregeln festlegen, die für alle Nutzer Ihrer Organisation gelten, und die beiden Protokollseiten, mit denen Sie verfolgen, was in ihr geschieht.

## Die Seite Sicherheit öffnen

Klicken Sie in der oberen Leiste auf das Zahnradsymbol (**Organisationseinstellungen**) und dann im linken Menü auf **Sicherheit**. Die Seite ist nur für die Inhaber der Organisation sichtbar. Sie setzt den Tarif **Entreprise** voraus: Bei einem anderen Tarif zeigt die Seite die Meldung **This feature is reserved for the plan: Entreprise**.

<figure><img src="../../.gitbook/assets/settings-security-center-1.png" alt="Die Seite Sicherheit der Organisationseinstellungen mit ihren Karten"><figcaption><p>Die Seite Sicherheit, mit einer Karte pro Regel</p></figcaption></figure>

Jede Karte gilt, sobald Sie sie ändern: Es gibt keine Schaltfläche zum Speichern.

## Richtlinie zur Passwortaktualisierung

Die Karte **Richtlinie zur Passwortaktualisierung** legt eine Lebensdauer für Passwörter fest: **90 Tage**, **180 Tage** oder **365 Tage**. Wählen Sie **Unbestimmt**, um die Richtlinie auszuschalten.

Die Richtlinie gilt für die internen Nutzer Ihrer Organisation, die sich nicht per SSO anmelden. Externe Nutzer sind nicht betroffen. Ist die Lebensdauer abgelaufen, wird der Nutzer bei der nächsten Anmeldung aufgefordert, ein neues starkes Passwort zu erstellen.

## Aufbewahrung von Sicherheitsprotokollen

Die Karte **Aufbewahrung von Sicherheitsprotokollen** legt fest, wie lange Dastra die [Sicherheitsprotokolle](#sicherheitsprotokolle) aufbewahrt. Wählen Sie unter **Bitte wählen Sie eine Speicherdauer aus.** eine Dauer: 30 Tage, 90 Tage, 180 Tage (**Empfohlen**), 365 Tage, 730 Tage oder 1.095 Tage.

Dastra löscht die Protokolle, die älter als dieser Zeitraum sind, jede Nacht um 01:00 Uhr. Stimmen Sie die Dauer mit Ihren eigenen Regeln zur Aufbewahrung von Audit-Spuren ab.

## Automatische Abmeldung

Die Karte **Automatische Abmeldung** hat einen Schalter, aktiviert oder **Deaktiviert**. Ist sie aktiviert, werden alle internen Nutzer Ihrer Organisation nach 1 Stunde Inaktivität abgemeldet.

## Starke Authentifizierung erzwingen

Die Karte **Nutzer zur Verwendung einer Zwei-Faktor-Authentifizierung (zweistufige Authentifizierung) verpflichten** hat einen Schalter. Ist er aktiviert, müssen alle internen Nutzer Ihrer Organisation bei ihrer nächsten Anmeldung die Zwei-Faktor-Authentifizierung einrichten. Dastra verwendet das TOTP-Protokoll mit einer Authentifizierungs-App für den zweiten Schritt nach dem Passwort. Wie Sie sie als Nutzer einrichten, lesen Sie unter [Anmelden und Authentifizierung verwalten](../../getting-started/setup/login.md#die-starke-authentifizierung-aktivieren).

## IP-Adressen und E-Mail-Domains filtern

Zwei Karten beschränken, wer sich anmelden kann:

* **Filtern Sie die IP-Adressen der Nutzer** beschränkt den Zugriff auf Bereiche von IP-Adressen. Lesen Sie [IP-Filterung](ip-filtering.md), bevor Sie eine Regel speichern: Sie können sie nicht über die Oberfläche entfernen.
* **Filtern Sie die E-Mail-Domains Ihrer Nutzer** lässt nur Nutzer sich anmelden, deren E-Mail-Adresse zu den aufgeführten Domains gehört. Geben Sie eine Domain wie `dastra.eu` ein und drücken Sie die Eingabetaste. Die Änderung kann einige Minuten brauchen, bis sie wirkt.

Der Domain-Filter ist nicht dasselbe wie der Block **Zugelassene E-Mail-Domains** auf der Seite zum Single Sign-on, der neue Kollegen einem Mandanten zuordnet: siehe [E-Mail-Domains](email-domains.md).

## SIEM-Streaming

Die letzte Karte streamt Ihre Sicherheitsereignisse in Echtzeit an Ihr SIEM. Siehe [SIEM-Streaming](siem.md).

## Sicherheitsprotokolle

Die Sicherheitsprotokolle listen die Sicherheitsereignisse Ihrer Organisation auf. Klicken Sie in der oberen Leiste auf das Zahnradsymbol und dann im linken Menü auf **Sicherheitsprotokolle**. Nur die Inhaber der Organisation können diese Seite öffnen.

<figure><img src="../../.gitbook/assets/settings-security-logs-1.png" alt="Die Seite Sicherheitsprotokolle mit ihren Filtern und der Liste der Ereignisse"><figcaption><p>Die Seite Sicherheitsprotokolle</p></figcaption></figure>

1. Wählen Sie mit der Datumsauswahl einen Zeitraum.
2. Klicken Sie auf **Events**, um einen oder mehrere Ereignistypen auszuwählen, und warten Sie, bis die Liste aktualisiert ist.
3. Lesen Sie die Liste: **Datum**, **Bedeutung**, die Bezeichnung des Ereignisses und der **Nutzer**, der es ausgelöst hat.
4. Klicken Sie auf ein Ereignis oder auf **Details**, um seine Seite zu öffnen. Sie zeigt die Typen, die **Zusammenfassung**, den Nutzer, das Datum und die **Event identifier** in einer **Strukturierten Anzeige** oder einer **Bruttoanzeige**, mit einer Schaltfläche **Kopieren** für die Rohdaten.

Mit **Exportieren** laden Sie die Protokolle des gewählten Zeitraums herunter. **Exportieren (SIEM)** lädt sie in einem Format herunter, das Ihr SIEM liest: **CEF (Common Event Format)**, **Syslog (RFC 5424)** oder **Splunk HEC (JSON)**. Dasselbe Menü öffnet für Organisationen mit dem Tarif Entreprise **Einrichten des Echtzeit-Streamings**. Siehe [SIEM-Streaming](siem.md#manueller-export-aus-den-auditprotokollen).

Dastra bewahrt die Ereignisse für die unter [Aufbewahrung von Sicherheitsprotokollen](#aufbewahrung-von-sicherheitsprotokollen) festgelegte Dauer auf.

## Aktivitätsverlauf

Die Seite **Aktivitätsverlauf**, ebenfalls in den Organisationseinstellungen, listet die Ereignisse der gesamten Organisation auf: Erstellungen, Änderungen, Löschungen und andere Aktionen an den Einträgen, zusätzlich zu den Sicherheitsereignissen. Sie ist für jeden Nutzer sichtbar, der die Organisationseinstellungen öffnet.

1. Wählen Sie einen Zeitraum.
2. Grenzen Sie die Liste mit den Filtern **Mandant**, **Typ**, **Events** und **Nutzer** ein. Klicken Sie auf **Filter löschen**, um sie zu entfernen.
3. Die Ereignisse sind nach Tagen gruppiert. Klicken Sie auf **Mehr anzeigen**, um ältere Ereignisse zu sehen.
4. Klicken Sie auf ein Ereignis, um seine Details zu öffnen, mit denselben strukturierten und rohen Ansichten wie bei den Sicherheitsprotokollen.

Nur die Inhaber der Organisation sehen auf dieser Seite die Schaltfläche **Exportieren**.
