---
description: >-
  Erstellen Sie automatisch Objekte in Dastra aus E-Mails, die an dedizierten
  Erfassungsadressen eingehen.
---

# E-Mail-Adressen für Datenerfassung

Diese Integration erstellt automatisch Objekte in Dastra aus E-Mails, die an dedizierten Erfassungsadressen eingehen. Dastra stellt diese Adressen bereit und macht aus jeder eingehenden E-Mail ein Objekt.

Einer Erfassungsadresse können fünf Arten von Objekten zugeordnet werden:

* Aufgaben;
* Verarbeitungstätigkeiten;
* Betroffenenanfragen;
* Verträge;
* Datenschutzvorfälle.

## Eine Erfassungsadresse einrichten

Für die Installation ist die Berechtigung zur Verwaltung der Integrationen im Mandanten erforderlich. Sie können pro Objektart und pro Mandant nur eine Erfassungsadresse haben.

1. Öffnen Sie **Mandanteneinstellungen** > **Integrationen** und klicken Sie auf die Karte **Incoming mail data collection**.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-1.png" alt="Der Katalog der Integrationen mit der Karte Incoming mail data collection"><figcaption><p>Die Karte Incoming mail data collection in den Integrationen</p></figcaption></figure>
2. Suchen Sie in der Liste der vorkonfigurierten Anwendungsfälle die Objektart, die Sie befüllen möchten, und klicken Sie auf **Integration hinzufügen**.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-2.png" alt="Die Liste der fünf Anwendungsfälle für Erfassungsadressen, jeweils mit der Schaltfläche Integration hinzufügen"><figcaption><p>Ein Anwendungsfall pro Objektart</p></figcaption></figure>
3. Wählen Sie im Panel, das sich öffnet, bei Bedarf die **Zielorganisationseinheit** der erstellten Objekte. Wenn Sie dieses Feld leer lassen, werden die Objekte in der Standard-Organisationseinheit erstellt.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-3.png" alt="Das Konfigurationspanel mit dem Feld Zielorganisationseinheit und der Schaltfläche Speichern"><figcaption><p>Die Ziel-Organisationseinheit wählen</p></figcaption></figure>
4. Klicken Sie auf **Speichern**. Dastra schließt die Installation ab und zeigt die zu verwendende E-Mail-Adresse an.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-4.png" alt="Das Panel mit der erzeugten Erfassungsadresse und der Schaltfläche zum Kopieren"><figcaption><p>Die erzeugte Erfassungsadresse</p></figcaption></figure>

Um eine Erfassungsadresse zu entfernen, öffnen Sie das Panel des Anwendungsfalls erneut und klicken Sie auf **Löschen**. Die Adresse wird freigegeben und empfängt keine E-Mails mehr.

## Funktionsweise

* Jede E-Mail, die an einer Erfassungsadresse eingeht, erstellt in Dastra ein Objekt der zugeordneten Art.
* Das Objekt wird in der Organisationseinheit erstellt, die bei der Installation gewählt wurde.
* Der Betreff der E-Mail wird zum Namen des Objekts.
* Der Text der E-Mail wird zur Beschreibung des Objekts.
* Die Anhänge der E-Mail werden unter den unten beschriebenen Bedingungen zu Anhängen des Objekts.

## Anhänge

Ein Anhang wird beibehalten, wenn:

* seine Dateiendung gültig ist. Zulässig sind `7z`, `csv`, `doc`, `docx`, `eml`, `epub`, `gif`, `htm`, `html`, `jpeg`, `jpg`, `json`, `md`, `msg`, `ods`, `odg`, `odp`, `odt`, `pdf`, `png`, `ppt`, `pptx`, `rar`, `rtf`, `svg`, `txt`, `xls`, `xlsm`, `xlsx` und `zip`;
* er mindestens 5 KB groß ist, falls es sich um ein Bild handelt (jpg, png, gif usw.). Diese Grenze verhindert, dass irrelevante Bilder wie Logos in E-Mail-Signaturen hinzugefügt werden.

## Die von einer Erfassungsadresse erstellten Objekte finden

Die betroffenen Objekte haben ein Feld **Quelle** oder **Herkunft der Erfassung**. Um es in einer Tabelle anzuzeigen, fügen Sie die entsprechende Spalte hinzu.

Alle Objekte, die aus einer Erfassungsadresse erstellt wurden, tragen außerdem das Tag **Incoming email**, das Ihnen beim Wiederfinden hilft.

## Erfolgsbenachrichtigung

Wenn nach dem Eingang einer E-Mail ein Objekt erstellt wird, sendet Dastra automatisch eine E-Mail-Benachrichtigung an die Adresse, die die Integration ausgelöst hat. Diese E-Mail bestätigt, dass das Objekt in Dastra erstellt wurde.

Die Bestätigungs-E-Mail wird in der Standardsprache des Mandanten verfasst, in dem die Integration installiert ist (Mandanteneinstellungen, Standardsprache).

## Ihre bestehenden E-Mails automatisch an Dastra weiterleiten

Wenn Sie bereits eine dedizierte Adresse für Betroffenenanfragen haben (zum Beispiel `privacy@yourcompany.com`), müssen Sie sie nicht ersetzen. Richten Sie in Ihrem Mailserver eine Weiterleitungsregel ein, die eingehende E-Mails an die Erfassungsadresse von Dastra umleitet.

Die E-Mails gelangen dann ohne manuelle Aktion direkt in Dastra, und Ihre Ansprechpartner verwenden weiterhin Ihre gewohnte Adresse.

### Mit Microsoft Exchange / Office 365

Öffnen Sie das **Exchange Admin Center** > **Nachrichtenfluss** > **Regeln** und klicken Sie auf **+ Regel hinzufügen**. Konfigurieren Sie die Regel wie folgt:

1. Bedingung: **Der Absender befindet sich** > **Außerhalb der Organisation**. Sie können einen Filter auf Stichwörter im Betreff hinzufügen, um nur die relevanten Anfragen umzuleiten (zum Beispiel, wenn der Betreff das Wort Anfrage oder Löschung enthält).
2. Aktion: **Die Nachricht umleiten an**. Geben Sie dann die im vorherigen Schritt erzeugte Erfassungsadresse von Dastra ein.
3. Modus: **Erzwingen**.

{% hint style="info" %}
Mit Betreff-Filtern leiten Sie nur bestimmte Arten von Anfragen (Löschung, Auskunft, Übertragbarkeit usw.) an die passende Erfassungsadresse um und behalten die übrigen Nachrichten in Ihrem gewohnten Posteingang.
{% endhint %}

{% hint style="warning" %}
Stellen Sie sicher, dass Ihre Regel keine Weiterleitungsschleife erzeugt, falls die Dastra-Adresse selbst E-Mails umleitet. Verwenden Sie die Bedingung „Von außerhalb der Organisation empfangen“, um Schleifen zu verhindern.
{% endhint %}

### Mit Google Workspace (Gmail)

Fügen Sie in der **Google Admin-Konsole** > **Apps** > **Google Workspace** > **Gmail** > **Routing** eine Regel für eingehendes Routing mit der Aktion **Route ändern** hinzu und geben Sie dann die Erfassungsadresse von Dastra ein.
