---
description: >-
  Vier Workflow-Regeln der Brightmoor Retail Group: neue Anfragen zuweisen,
  Aufgaben in einem Team verteilen, Microsoft Teams bei einer Verletzung mit
  hohem Risiko alarmieren und eine HTTP-Anfrage senden.
---

# Workflow-Rezepte

Jedes Rezept ist eine [Workflow-Regel](../features/settings/workflow-rules.md) der Brightmoor Retail Group: ein Auslöser, Bedingungen und Aktionen für eine Objektart. Um eine davon zu erstellen, öffnen Sie **Automatisierungen** > **Workflow-Regeln**, klicken Sie auf **Erstellen Sie eine Workflow-Regel**, wählen Sie **Von Grund auf** und geben Sie dann den **Namen der Regel** und den **Elementtyp** ein. Schalten Sie die Regel nach dem Speichern mit dem Schalter **Status** ein.

Lassen Sie **Führen Sie den Workflow einmal pro Element aus (empfohlen).** bei den Rezepten eingeschaltet, die auf eine Erstellung oder eine Änderung reagieren, damit ein Element nie zweimal verarbeitet wird.

## Rezept 1: neue Anfragen zuweisen

Ziel: Jede neue Anfrage einer betroffenen Person hat von der ersten Minute an einen Bearbeiter, je nach der Tochtergesellschaft, die sie erhalten hat.

### Auslöser

Elementtyp: **Anfrage**. Auslöser: **Aktion**, Ereignis **Erstellung**.

### Bedingungen

Eine Regel hat bis zu fünf Bedingungen, und jede trägt ihre eigenen Aktionen. Wählen Sie für jede **Einige Bedingungen anwenden**:

| Bedingung | Feld | Wert |
| --- | --- | --- |
| 1 | **Organisationseinheit** | Brightmoor Germany |
| 2 | **Organisationseinheit** | Brightmoor UK |
| 3 | **Organisationseinheit** | Brightmoor Retail Group |

Eine Anfrage hat kein Feld für das Land. Die Organisationseinheit der Anfrage ist der übliche Ersatz für das Land einer Tochtergesellschaft. Um nach Sprache zu verteilen, verwenden Sie stattdessen das Feld **Sprache**, und um nach ausgeübtem Recht zu verteilen, **Rechte der betroffenen Person** (zum Beispiel Löschung).

### Aktionen

Klicken Sie in jeder Bedingung auf **+** und wählen Sie **Zugewiesenen Nutzer definieren**, dann einen Nutzer: Sophie Becker für Bedingung 1, Liam O'Connor für Bedingung 2 und Emma Walsh für Bedingung 3. Bei einer Anfrage füllt diese Aktion den **Bearbeiter** aus.

### Ergebnis

Eine von der deutschen Tochtergesellschaft erhaltene Anfrage wird Sophie Becker zugewiesen, sobald sie erstellt wird. In der Regel listet der **Verlauf** jede verarbeitete Anfrage mit ihrem Status auf, und **Ausführen** wendet die Regel von Hand auf eine Anfrage an, die vor der Regel erstellt wurde.

## Rezept 2: Aufgaben in einem Team verteilen

Ziel: Die neuen Aufgaben gleichmäßig auf die Mitglieder des Datenschutz-Teams verteilen.

### Auslöser

Elementtyp: **Aufgabe**. Auslöser: **Aktion**, Ereignis **Erstellung**.

### Bedingungen

**Gilt für alle Elemente**: Jede neue Aufgabe ist betroffen. Um die Regel einzugrenzen, wählen Sie **Einige Bedingungen anwenden** und filtern Sie nach einem Feld wie einem Tag.

### Aktionen

Fügen Sie **Zugewiesenen Nutzer definieren** hinzu, wählen Sie **Bitte wählen Sie einen Nutzer aus dem Team aus.** und wählen Sie das Team unter **Bitte wählen Sie ein Team aus**. Ein Nutzer des Teams wird nach dem Round-Robin-Verfahren ausgewählt: Jedes Mal, wenn die Regel ausgelöst wird, kommt das nächste Mitglied an die Reihe, und auf das letzte folgt wieder das erste.

<figure><img src="../.gitbook/assets/examples-workflow-1.png" alt="Designer der Workflow-Regel mit der Aktion Zugewiesenen Nutzer definieren, die einen Nutzer aus einem Team auswählt"><figcaption><p>Die Round-Robin-Zuweisung</p></figcaption></figure>

### Ergebnis

Die erste Aufgabe geht an das erste Mitglied des Teams, die zweite an das nächste und so weiter. Das gewählte Mitglied steht in **Zugewiesen an**. Wie Sie das Team erstellen, lesen Sie unter [Teams erstellen und zuweisen](../getting-started/setup/teams.md). Hat das Team kein Mitglied, schlägt die Ausführung fehl und erscheint im Verlauf als Fehler.

## Rezept 3: einen Microsoft-Teams-Kanal bei einer Verletzung mit hohem Risiko alarmieren

Ziel: Den Datenschutzkanal sofort warnen, wenn eine Datenschutzverletzung die Risikostufe Hoch erreicht, weil dann die Aufsichtsbehörde und die betroffenen Personen informiert werden müssen.

Voraussetzung: Die [Microsoft-Teams-Integration](../features/integrations/microsoft-teams.md) ist im Mandanten installiert und aktiviert. Ohne sie wird die Aktion nicht angeboten.

### Auslöser

Elementtyp: **Datenschutzverletzung**. Auslöser: **Aktion**, Ereignis **Erstellung oder Änderung**: Die Risikostufe existiert erst, wenn die Risikoanalyse ausgefüllt ist, also nach der Erstellung.

### Bedingungen

Wählen Sie **Einige Bedingungen anwenden** und setzen Sie das Feld **Points** auf einen Wert größer oder gleich 6. **Points** ist der Score der Verletzung, die Summe der beiden Bewertungen der Risikoanalyse, und 6 ist die Schwelle der Risikostufe Hoch (siehe [Risiko-Scoring](risk-scoring.md)). Das Feld **Risiko** selbst wird in Bedingungen nicht angeboten.

{% hint style="info" %}
Eine Verletzung, deren Stufe von Hand unter **Fazit der Risikoanalyse: Geschätzte Risikostufe** festgelegt wurde, behält ihren Score, sodass die Regel dem Score folgt und nicht der von Ihnen gewählten Stufe.
{% endhint %}

### Aktionen

Fügen Sie **Eine Teams-Benachrichtigung senden** hinzu und füllen Sie aus:

* **Titel der Karte**: `High risk data breach: {{label}}`;
* **Nachricht**: `Score {{score}}. Check the notification deadline to the supervisory authority.`;
* **Einen Link zum Objekt in die Karte aufnehmen**: eingeschaltet, was der Standard ist.

Geben Sie `{{` in ein Feld ein, um die Variablen der Datenschutzverletzung aufzulisten.

### Ergebnis

Im Teams-Kanal, der mit dem Webhook verknüpft ist, erscheint eine Karte mit einem Link zur Verletzung. Es gibt keinen Empfänger zu wählen: Der Kanal ist der in der Integration konfigurierte. Diese Aktion lässt sich ohne Teams-Kanal nicht ausprobieren, weshalb dieses Rezept keinen Screenshot hat.

## Rezept 4: eine HTTP-Anfrage senden

Ziel: Bei jeder eingehenden Anfrage ein Ticket im Service Desk von Brightmoor anlegen.

Voraussetzung: Die Integration [HTTP / Benutzerdefinierte API](../features/integrations/custom-http.md) ist unter **Mandanteneinstellungen** > **Integrationen** aktiviert, mit einer Verbindung zum Service Desk (API-Schlüssel, Basic-Zugangsdaten oder OAuth 2.0). Das Hinzufügen dieser Aktion setzt die Berechtigung **Integrationen** voraus.

### Auslöser

Elementtyp: **Anfrage**. Auslöser: **Aktion**, Ereignis **Erstellung**.

### Bedingungen

**Gilt für alle Elemente**.

### Aktionen

Fügen Sie **Send an HTTP request** hinzu und füllen Sie aus:

* **Method**: POST. **URL**: `https://servicedesk.brightmoor.example/api/tickets`.
* Tab **Authentication**: die Verbindung des Service Desk. Die Zugangsdaten bleiben in der Verbindung, nie in der Regel.
* Tab **Body**: das Format **JSON**, mit dieser Vorlage:

```
{
  "summary": "{{title}}",
  "reference": "{{refId}}",
  "origin": "Dastra"
}
```

Klicken Sie auf **Test the request**. **Preview** rendert die URL, die Header und den Body anhand einer echten Anfrage des Mandanten, ohne etwas zu senden. **Send the request** führt den echten Aufruf aus und zeigt die Antwort des Service Desk. **Generate with AI** entwirft die Anfrage aus einer Anweisung und der Nutzlast, die der Service Desk erwartet.

<figure><img src="../.gitbook/assets/examples-workflow-2.png" alt="Aktion Send an HTTP request mit der Methode POST, der URL und dem JSON-Body"><figcaption><p>Die Aktion HTTP-Anfrage</p></figcaption></figure>

### Ergebnis

Der Service Desk erhält für jede neue Anfrage ein Ticket. Der gerenderte Body muss gültiges JSON sein: Andernfalls wird nichts gesendet, und die Ausführung wird als Fehler protokolliert. Jeder Aufruf wird in den Integrationsprotokollen nachverfolgt. Das Deaktivieren der Integration oder das Löschen der Verbindung deaktiviert die Regel.
