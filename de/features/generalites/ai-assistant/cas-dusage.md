# Anwendungsfälle

{% hint style="warning" %}
**Hinweis zur Qualität der generierten Inhalte**: Alle vom Assistenten generierten Inhalte sind lediglich Vorschläge. Sie müssen von einer qualifizierten Person überprüft und aktualisiert werden, bevor sie verwendet werden. Dastra übernimmt keine Gewähr für die Qualität der vorgeschlagenen Informationen.
{% endhint %}

### Datenverarbeitungen

#### Verarbeitung generieren

Generieren Sie schnell eine Datenverarbeitung im von Dastra erwarteten Format aus einer kurzen Beschreibung. Der Assistent schlägt Ihnen einen Namen, einen oder mehrere Datensätze mit ihren Feldern, eine Speicherdauer, Sicherheitsmaßnahmen, Empfänger und eine Beschreibung vor.

1. Klicken Sie auf **Verarbeitung erstellen** > **Mit KI-Assistent generieren**
2. Geben Sie eine kurze Beschreibung Ihrer Verarbeitung ein
3. Klicken Sie auf **Weiter** und warten Sie einen Moment
4. Auf dem Zusammenfassungsbildschirm nehmen Sie Ihre Korrekturen vor und klicken Sie auf **Erstellen**

#### Datensatz generieren

1. Gehen Sie auf die Seite **Datensätze**
2. Klicken Sie auf **Datensatz erstellen** > **Mit KI-Assistent erstellen**
3. Geben Sie eine kurze Beschreibung Ihres Datensatzes ein
4. Klicken Sie auf **Weiter** und warten Sie einen Moment
5. Auf dem Zusammenfassungsbildschirm nehmen Sie Ihre Korrekturen vor und klicken Sie auf **Erstellen**

#### Datenschutzerklärung generieren

1. Gehen Sie auf die Bearbeitungsseite einer Verarbeitung
2. Im Abschnitt **11. Dokumentation** klicken Sie auf **Datenschutzerklärung generieren**
3. Wählen Sie das gewünschte Format — Sie können die Anweisungen anpassen, indem Sie **Benutzerdefiniert** auswählen
4. Klicken Sie auf **Generieren**, dann kopieren oder fügen Sie den Text in Ihre Dokumentation ein

#### Compliance-Analyse einer Verarbeitung generieren

Der Assistent kann eine bestehende Verarbeitung analysieren und eine Bewertung ihrer Compliance hinsichtlich der dokumentarischen Anforderungen der DSGVO erstellen.

{% hint style="info" %}
**Funktion in der Beta-Phase**: Die Ergebnisse können weniger konstant sein als bei einer stabilen Funktion und sollten mit erhöhter Aufmerksamkeit behandelt werden. Diese Analyse ist eine Entscheidungshilfe, keine Rechtsberatung.
{% endhint %}

***

### Fragebögen (DSFA, Risikoanalyse...)

#### KI-gestützte Antwort generieren

1. Gehen Sie in die Rubrik **Fragebögen** und wählen Sie die gewünschte Vorlage (z. B.: DSFA der CNIL)
2. Klicken Sie auf **Fragebogen planen**
3. Wählen Sie **KI-gestützte Antwort**
4. Geben Sie die Verarbeitung an, die als Quelle dienen soll, oder geben Sie benutzerdefinierte Anweisungen ein
5. Sobald die Antwort generiert ist, nehmen Sie Ihre Korrekturen direkt im Fragebogen vor

#### Fragebogenvorlage generieren&#x20;

1. Gehen Sie in die Rubrik **Fragebögen** und klicken Sie auf Fragebogenvorlage erstellen.
2. Wählen Sie **Aus KI erstellen**
3. Geben Sie eine Beschreibung des Fragebogens (300 Wörter) und einen Typ an
4. Passen Sie die Anzahl der Abschnitte und Fragen an
5. Klicken Sie auf **Generieren**

***

### Betroffenenanfragen

#### Antwort auf eine Anfrage generieren

Generieren Sie Antworten in mehreren Sprachen mit Anpassungsoptionen (Länge, formeller oder informeller Ton usw.).

1. Öffnen Sie eine in Bearbeitung befindliche Betroffenenanfrage
2. Füllen Sie die Informationen bis zum Schritt **Kommunikation / Übermittlung** aus
3. Klicken Sie auf **Mit KI generieren** — der Assistent generiert eine Antwort basierend auf folgenden Informationen:
   * Vor- und Nachname des Antragstellers
   * Nachricht der Anfrage
   * Zu verwendende Sprache
   * Name des Workspace
   * Verarbeitungszwecke
   * Name des Bearbeiters der Anfrage
   * Datum der Anfrage und Anzahl der verbleibenden Tage
   * Status und Kennung der Anfrage
4. Bearbeiten Sie den vorgeschlagenen Text oder verwenden Sie die Umformulierungsoptionen (kürzen, verlängern, Ton ändern)
5. Klicken Sie auf **Diese Nachricht bestätigen**, fügen Sie gegebenenfalls Anhänge hinzu und klicken Sie dann auf **Senden**

{% hint style="info" %}
Für diese Funktion gilt eine Begrenzung der Aufrufe pro Minute.
{% endhint %}

{% hint style="info" %}
**KI-Verordnung — Artikel 50**: Wenn eine Antwort vom KI-Assistenten generiert wird, gilt die strenge Verpflichtung des Art. 50(1) (die Person darüber zu informieren, dass sie mit einem KI-System interagiert) **nicht**, da keine direkte Interaktion zwischen dem KI-System und der betroffenen Person stattfindet — es ist ein menschlicher Nutzer, der die Antwort überprüft, validiert und sendet. Es wird dennoch empfohlen, die betroffene Person als bewährte DSGVO-Praxis (Art. 5(1)(a) Fairness) zu informieren. Konsultieren Sie die [FAQ](foire-aux-questions.md) für die vollständige Analyse.
{% endhint %}

***

### Assets und Stakeholder

#### Asset generieren

Generieren Sie schnell ein Asset (Software, Tool usw.) im von Dastra erwarteten Format. Der Assistent schlägt Ihnen einen Namen, Links zur Datenschutzrichtlinie des Stakeholders vor und erstellt einen Stakeholder als Herausgeber.

1. Klicken Sie auf **Asset erstellen** > **Mit KI-Assistent generieren**
2. Geben Sie eine Beschreibung oder eine URL der Datenschutzrichtlinie ein
3. Überprüfen und vervollständigen Sie die vorgeschlagenen Informationen vor der Bestätigung

***

### Datenschutzvorfälle

#### Post-Mortem generieren

Ausgehend von einem bestehenden Datenschutzvorfall generiert der Assistent ein strukturiertes Post-Mortem-Dokument mit einer Beschreibung des Vorfalls, den betroffenen Daten und den ergriffenen Maßnahmen.

Greifen Sie auf diese Funktion über die Bearbeitungsseite eines Datenschutzvorfalls im Abschnitt Dokumentation zu.

***

### Verträge

#### Metadaten eines Vertrags extrahieren

Importieren Sie ein Vertragsdokument (PDF oder URL) und lassen Sie den Assistenten automatisch die Metadaten extrahieren: Parteien, Gegenstand, Dauer, Schlüsselklauseln usw.

Greifen Sie auf diese Funktion über das Modul **Verträge** bei der Erstellung oder Bearbeitung eines Vertrags zu.

***

### Benutzerdefinierte Dokumente und Berichte

#### Benutzerdefiniertes Dokument generieren

Geben Sie Ihre eigenen Anweisungen ein und stellen Sie gegebenenfalls einen Quellinhalt bereit. Der Assistent generiert ein strukturiertes Dokument gemäß Ihren Spezifikationen.

#### Benutzerdefinierten Bericht generieren

Beschreiben Sie im Modul **Benutzerdefinierte Berichte** den gewünschten Bericht in natürlicher Sprache. Der Assistent erstellt eine erste Version, die Sie verfeinern können.

***

### KI-Systeme

#### Beschreibung eines KI-Systems generieren

1. Greifen Sie auf das Modul **KI-Systeme** zu
2. Erstellen oder öffnen Sie ein KI-System
3. Klicken Sie im Beschreibungsfeld auf **Mit KI-Assistent generieren**
4. Geben Sie eine freie Beschreibung ein oder geben Sie eine URL an

#### Datenschutzerklärung für ein KI-System generieren

Klicken Sie im Datenblatt eines KI-Systems auf **Hinweis generieren**, um automatisch das Informationsdokument für Nutzer oder betroffene Personen zu erstellen.

#### Risikoanalyse eines KI-Systems generieren

Der Assistent analysiert die im Datenblatt des KI-Systems ausgefüllten Felder und erstellt eine Bewertung der damit verbundenen Risiken.

{% hint style="info" %}
**Funktion in der Beta-Phase**: Mit erhöhter Aufmerksamkeit zu behandeln und vor jeder Entscheidung von einem Experten zu validieren.
{% endhint %}

***

### Referenzrahmen und Kontrollen

#### Vorschläge für Kontrollen, Anforderungen und Tests

Aus einem Compliance-Referenzrahmen im Compliance-Modul kann der Assistent relevante Kontrollen, Anforderungen oder Tests basierend auf dem Kontext des betreffenden Objekts (Name, Beschreibung, zugehöriger Referenzrahmen) vorschlagen.
