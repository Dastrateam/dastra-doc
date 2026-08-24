---
description: >-
  Erfahren Sie, wie Sie unsere native Integration von Sammel-E-Mail-Postfächern
  nutzen
---

# E-Mail-Adressen für Datenerfassung

### Einführung

Diese Integration ermöglicht die automatische Erstellung von Objekten in Dastra aus E-Mails, die an dedizierte E-Mail-Postfächer eingehen. Dastra stellt diese Postfächer bereit und automatisiert die Umwandlung eingehender E-Mails in Objekte in der Dastra-Anwendung.

5 Objekttypen können diesen Sammel-E-Mail-Postfächern zugeordnet werden:

* **Aufgaben**
* **Datenverarbeitungen**
* **Rechteausübungsanfragen**
* **Verträge**
* **Datenschutzverletzungen**

### Einrichtung eines Sammelpostfachs

Um ein Sammelpostfach für eines der oben aufgeführten Objekte einzurichten, gehen Sie zu den Einstellungen Ihres Mandanten, Tab Integrationen, und wählen Sie die Karte „Sammel-E-Mail-Adresse"

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration20.png" alt=""><figcaption></figcaption></figure>

Wählen Sie dann den Objekttyp aus, für den Sie die Integration einrichten möchten, indem Sie auf „Integration hinzufügen" klicken. Beachten Sie, dass Sie nur ein Sammel-E-Mail-Postfach pro Objekttyp und pro Mandant haben können.

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration21.png" alt=""><figcaption></figcaption></figure>

Sie haben die Möglichkeit, die Ziel-Organisationseinheit der über dieses Sammelpostfach erstellten Objekte bei der Installation der Integration anzugeben. Wenn Sie dieses Feld leer lassen, werden die Objekte in der Standard-Organisationseinheit erstellt.

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration23.png" alt=""><figcaption></figcaption></figure>

Durch Klicken auf „Erstellen" schließt Dastra die Installation der Integration ab und stellt Ihnen die zu verwendende E-Mail-Adresse bereit.

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration22.png" alt=""><figcaption></figcaption></figure>

### Hauptfunktionalitäten

* **Automatische Objekterstellung**: Jede E-Mail, die in einem zugeordneten E-Mail-Postfach eingeht, erstellt ein entsprechendes Objekt in Dastra.
* **Konfiguration der Organisationseinheit**: Sie können bei der Installation eine Ziel-Organisationseinheit definieren. Wenn diese Einheit angegeben ist, wird das Objekt automatisch in dieser Einheit erstellt.
* **Verwaltung der Objektfelder**:
  * **Label**: Der Betreff der E-Mail wird als Name des erstellten Objekts übernommen.
  * **Beschreibung**: Der E-Mail-Text wird für die Beschreibung des erstellten Objekts verwendet.
  * **Anhänge**: Die E-Mail-Anhänge werden als Anhänge des Objekts hinzugefügt, vorbehaltlich der Validierungsbedingungen.

### Verwaltung der Anhänge

Die E-Mail-Anhänge werden als Anhänge des Objekts hinzugefügt, vorausgesetzt:

* **Die Dateierweiterungen sind gültig**: Nur Anhänge mit einer gültigen Dateierweiterung werden beibehalten.

Hier ist die Liste der erlaubten Anhänge: `7z`, `csv`, `doc`, `docx`, `eml`, `epub`, `gif`, `htm`, `html`, `jpeg`, `jpg`, `json`, `md`, `msg`, `ods`, `odg`, `odp`, `odt`, `pdf`, `png`, `ppt`, `pptx`, `rar`, `rtf`, `svg`, `txt`, `xls`, `xlsm`, `xlsx`, `zip`.

* **Die Bilder respektieren eine Mindestgröße**: Für Bilddateien (jpg, png, gif usw.) ist eine Mindestgröße von 5 KB erforderlich. Diese Einschränkung verhindert die Aufnahme nicht relevanter Bilder wie die aus E-Mail-Signaturen.

### Auffinden der über ein Sammelpostfach generierten Objekte

Die von Sammelpostfächern betroffenen Objekte verfügen über ein Feld „Quelle" oder „Sammelursprung", das Sie in den Tabellenansichten anzeigen können, indem Sie die Spalte Quelle / Sammelursprung einblenden.

Alle über ein Sammelpostfach generierten Objekte werden mit dem Tag „eingehende E-Mail" versehen, damit Sie sie bei Bedarf leicht identifizieren können.

### Erfolgsbenachrichtigung

Bei erfolgreicher Erstellung eines Objekts nach Eingang einer E-Mail im Sammelpostfach wird automatisch eine E-Mail-Benachrichtigung an die Adresse gesendet, die die Integration ausgelöst hat. Diese Benachrichtigung bestätigt, dass das Objekt erfolgreich in Dastra erstellt wurde, und bietet damit eine sofortige Bestätigung, dass die Anfrage oder Aktion berücksichtigt wurde.

Die Sprache der Bestätigungs-E-Mail entspricht der Standardsprache des Mandanten, in dem die Integration installiert ist (Einstellungen Ihres Mandanten > Standardsprache).

***

### Bestehende E-Mails automatisch an Dastra weiterleiten

Wenn Sie bereits über eine dedizierte E-Mail-Adresse für Rechteausübungsanfragen verfügen (zum Beispiel `privacy@ihrunternehmen.com`), müssen Sie diese nicht ersetzen. Sie können eine **Weiterleitungsregel** in Ihrem E-Mail-Server konfigurieren, um eingehende E-Mails automatisch an das Dastra-Sammelpostfach weiterzuleiten.

Die E-Mails gelangen so direkt in Dastra ohne manuellen Eingriff, während Ihre gewohnte Adresse für Ihre Kontakte erhalten bleibt.

#### Mit Microsoft Exchange / Office 365

Gehen Sie zum **Exchange Admin Center** > **E-Mail-Fluss** > **Regeln**, dann klicken Sie auf **„+ Regel hinzufügen"**.

Konfigurieren Sie die Regel wie folgt:

1. **Bedingungen**: „Der Absender befindet sich" > „Außerhalb der Organisation" — und filtern Sie optional nach Schlüsselwörtern im Betreff, um nur relevante Anfragen weiterzuleiten (z. B.: der Betreff enthält „Anfrage" oder „Rechte").
2. **Aktion**: „Nachricht weiterleiten an" > geben Sie die im vorherigen Schritt generierte Dastra-Sammeladresse ein.
3. **Modus**: Anwenden (Enforce).

{% hint style="info" %}
Sie können Filter auf den E-Mail-Betreff setzen, um nur bestimmte Anfragentypen (Löschung, Auskunft, Datenübertragbarkeit…) an das entsprechende Dastra-Postfach weiterzuleiten und die übrigen in Ihrem gewohnten Postfach zu behalten.
{% endhint %}

{% hint style="warning" %}
Überprüfen Sie, dass Ihre Regel keine Weiterleitungsschleife erzeugt, falls Ihre Dastra-Adresse selbst E-Mails weiterleitet. Konfigurieren Sie die Bedingung „Von außerhalb der Organisation empfangen", um Schleifen zu vermeiden.
{% endhint %}

#### Mit Google Workspace (Gmail)

In der **Google Admin-Konsole** > **Anwendungen** > **Google Workspace** > **Gmail** > **Routing** fügen Sie eine eingehende Routing-Regel mit der Aktion „Empfänger ändern" hinzu und geben Sie die Dastra-Sammeladresse ein.
