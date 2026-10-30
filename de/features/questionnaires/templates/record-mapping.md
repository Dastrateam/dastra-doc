---
description: >-
  Nutzen Sie die Antworten eines Fragebogens, um einen Eintrag anzulegen oder
  einen bestehenden zu aktualisieren: unterstützte Objekte, Variablen,
  Fragetypen, die Schaltfläche zum Zusammenführen und die Fehlermeldungen.
---

# Ein Verzeichnis aus den Antworten befüllen

Ein Fragebogen eines Erstellungstyps kann seine Antworten in einen Eintrag von Dastra umwandeln: eine Verarbeitungstätigkeit, ein Asset, ein KI-System und so weiter. Ist die Antwort mit einem bestehenden Eintrag verknüpft, lassen sich die Antworten stattdessen in ihn zusammenführen. Jede Frage ist über ihren **Namen der Variablen** an ein Feld des Eintrags gebunden.

Diese Seite richtet sich an die Personen, die die Vorlagen erstellen. Befragte sehen nichts von der Zuordnung.

Einen vollständigen Fall mit einem KI-System finden Sie unter [Fragebogenantworten in einem Verzeichnis](../../../examples/questionnaire-to-record.md).

## Welche Objekte befüllt werden können

Nur die Erstellungstypen des Felds **Art des Fragebogens** tragen ein Datenmodell. Die anderen Typen, etwa die DSFA, die Anbieterbewertung oder der Standardfragebogen, haben keines.

| Art des Fragebogens | Eintrag |
| --- | --- |
| Data processing project | Verarbeitungstätigkeit |
| Data breach creation request | Datenschutzverletzung |
| Asset creation | Asset |
| Contract creation | Vertrag |
| AI System creation | KI-System |
| Stakeholder creation | Stakeholder |

Die integrierten Vorlagen dieser Typen sind sofort einsatzbereit (siehe [Eine Fragebogenvorlage erstellen](README.md)). Sie können auch eine eigene Vorlage erstellen und einen dieser Typen wählen.

## Modellvalidierung und die Liste der Variablen

Das Modell eines Typs ist die Beschreibung der Felder des Eintrags: ihr Name, ihre Art (Text, Datum, feste Werteliste, Liste von Elementen) und ihre maximale Länge. Die Liste der Variablen liest dieses Modell.

So ordnen Sie eine Frage zu:

1. Öffnen Sie die Vorlage und dann die Frage.
2. Aktivieren Sie **Möchten Sie den Namen der Variablen anpassen (nur für fortgeschrittene Nutzer)?**.
3. Geben Sie unter **Name der Variablen** den Namen des Felds ein oder klicken Sie auf **Bitte wählen Sie eine zuzuordnende Variable aus**.
4. Klicken Sie in der Liste auf das Feld. Das Fenster zeigt für jedes Feld **Name**, **Name der Variablen**, **Mögliche Werte** und **Max**. Eine Markierung **Pflichtfeld** kennzeichnet die Felder, ohne die der Eintrag nicht auskommt.

Die Wahl eines Felds füllt den Variablennamen und die maximale Länge aus. Bei einem Feld mit fester Werteliste, zum Beispiel der Risikostufe eines KI-Systems, erzeugt sie außerdem die Antworten der Frage, eine pro Wert, und der Variablenname jeder Antwort ist der Wert, den Dastra erwartet. Behalten Sie diese Variablennamen unverändert bei.

Ein Variablenname besteht aus Buchstaben, Ziffern, Bindestrichen und Unterstrichen und muss in der Vorlage eindeutig sein.

{% hint style="info" %}
Eine Frage, deren Variablenname zu keinem Feld des Eintrags passt, wird beim Anlegen des Eintrags ignoriert. Nur das Modell des Typs entscheidet, welche Namen gültig sind: Geben Sie die Namen genau so ein, wie die Liste sie zeigt, mit derselben Groß- und Kleinschreibung.
{% endhint %}

<figure><img src="../../../.gitbook/assets/examples-questionnaire-1.png" alt="Fenster Bitte wählen Sie eine zuzuordnende Variable aus mit den Feldern eines KI-Systems"><figcaption><p>Die für ein KI-System angebotenen Variablen</p></figcaption></figure>

## Fragetypen und Felder

Die Liste bietet nur die Felder an, die zum Typ der Frage passen.

| Fragetyp | Angebotene Felder | Was der Eintrag erhält |
| --- | --- | --- |
| Kurztext, Langtext, Texteditor | Textfelder | Den eingegebenen Text |
| Datum, Datum und Uhrzeit | Datumsfelder | Das Datum. Ein ungültiges Datum bleibt leer |
| Einfachauswahlliste, Einzelauswahl | Felder mit fester Werteliste | Den Variablennamen der gewählten Antwort oder ihre Bezeichnung, wenn sie keinen hat |
| Mehrfachauswahlliste, Mehrfachauswahl | Alle Felder außer `id` | Die Liste der Variablennamen der gewählten Antworten |
| Liste mit mehreren Feldern | Listenfelder | Ein Element pro Zeile. Die Variablennamen der Unterfragen sind die Eigenschaften eines Elements |
| Zahl, Bereichsauswahl, Einfaches Kontrollkästchen, Land, Tags-Auswahl | Alle Felder außer `id` | Den eingegebenen Wert. Bei der Tags-Auswahl die Liste der Tags |

Bei den Typen ohne Filter wählen Sie das Feld selbst: Nehmen Sie eines von derselben Art wie die Antwort.

Der Fragetyp **Dateien** wird keinem Feld zugeordnet. Mit den Antworten gesendete Dokumente können beim Anlegen des Eintrags in den Dateimanager übertragen werden (siehe unten).

## Native Fragen

Eine native Frage ist eine Frage einer integrierten Erstellungsvorlage, die an ein Feld des Eintrags gebunden ist. Ihr Typ, ihr Variablenname, ihre Grenzen und ihre Antworten sind gesperrt: Nur die Administratoren von Dastra können sie ändern, damit die Zuordnung korrekt bleibt. Fügen Sie neben den nativen Fragen eigene hinzu, um andere Felder zu befüllen.

## Ein benutzerdefiniertes Feld befüllen

Ein benutzerdefiniertes Feld wird durch einen Variablennamen befüllt, der aus `custom_` gefolgt vom technischen Namen des Felds besteht.

1. Klicken Sie in der Seitenleiste auf **Mandanteneinstellungen**, dann auf **Benutzerdefinierte Felder** und wählen Sie das Modul des Eintrags.
2. Klicken Sie auf das Feld. Der technische Name ist der **Name der Variablen (Slug)**, zum Beispiel `business_owner`. Er ist nach der Erstellung schreibgeschützt.
3. Setzen Sie in der Frage den Variablennamen auf `custom_business_owner`.

Benutzerdefinierte Felder stehen nicht in der Liste **Bitte wählen Sie eine zuzuordnende Variable aus**: Geben Sie den ganzen Namen ein. Die Optionen der Felder finden Sie unter [Benutzerdefinierte Felder](../../general/custom-fields.md).

Wählen Sie einen Fragetyp, der zum Typ des Felds passt:

| Typ des benutzerdefinierten Felds | Fragetyp |
| --- | --- |
| Text, Textbereich, Rich Text | Kurztext, Langtext, Texteditor |
| Zahl (ganze Zahl), Zahl (Dezimalzahl) | Zahl |
| Datum, Datum mit Uhrzeit | Datum, Datum und Uhrzeit |
| Optionsfeld, Einzelauswahl | Einfachauswahlliste, Einzelauswahl |
| Kontrollkästchen, Mehrfachauswahl | Mehrfachauswahlliste, Mehrfachauswahl |
| Boolean | Einfaches Kontrollkästchen |

Beim Anlegen des Eintrags gelten zwei Regeln:

* Ein technischer Name, der zu keinem benutzerdefinierten Feld des Mandanten für diese Art von Eintrag passt, wird ohne Fehler verworfen: Die Antwort wird nicht gespeichert. Prüfen Sie die Schreibweise und das Präfix `custom_`;
* ein Wert, den das Feld nicht akzeptiert, stoppt das Anlegen mit einer Meldung, die das Feld nennt, zum Beispiel wenn das Feld erforderlich und die Antwort leer ist oder wenn eine Liste zu wenige oder zu viele Elemente hat.

## Den Eintrag anlegen oder zusammenführen

Die Schaltfläche erscheint in der Antwort des Fragebogens, wenn:

* die Antwort veröffentlicht ist, also validiert und nicht archiviert;
* die Vorlage von einem Erstellungstyp ist.

Sie ist nur für den Inhaber der Antwort aktiviert.

* Ohne verknüpften Eintrag heißt die Schaltfläche **Anlegen**, gefolgt von der Art des Eintrags. Sie öffnet eine Vorschau des aus den Antworten aufgebauten Eintrags. Wählen Sie die **Organisationseinheit** (bei Assets und Stakeholdern nicht abgefragt), behalten Sie die Option zur Übertragung der Dateien in den Dateimanager bei oder entfernen Sie sie, und klicken Sie auf **Erstellen**. Der Eintrag wird angelegt und mit der Antwort verknüpft.
* Bei einem verknüpften Eintrag heißt die Schaltfläche **Daten zusammenführen**. Verknüpfen Sie den Eintrag beim Planen des Fragebogens unter **Gegenstand der Antwort** (siehe [Einen Fragebogen planen](../schedule.md#den-fragebogen-mit-anderen-objekten-in-dastra-verknupfen)), nachdem Sie **Verwandtes Thema** in der Vorlage auf die Art des Eintrags gesetzt haben. Die Vorschau öffnet sich auf dieselbe Weise, und die Schaltfläche heißt **Erstellen und Zusammenführen des Bestehenden**.

Mit **Erstellen und Zusammenführen des Bestehenden** baut Dastra aus den Antworten einen temporären Eintrag auf, mit der Bezeichnung gefolgt von „(From Questionnaire)“, und öffnet das Zusammenführungsfenster mit dem bestehenden und dem temporären Eintrag. Sie wählen Feld für Feld die Werte, die Sie behalten. Die Dateien werden übertragen, sobald Sie das Zusammenführen bestätigen. Verlassen Sie das Fenster, ohne zusammenzuführen, wird der temporäre Eintrag gelöscht, und nichts ändert sich.

Nichts wird automatisch zusammengeführt: Die Antworten aktualisieren einen Eintrag nie von selbst. Das Zusammenführen ist immer die Handlung einer Person.

<figure><img src="../../../.gitbook/assets/examples-questionnaire-2.png" alt="Seite der Zusammenführungsanfrage mit der Vorschau des KI-Systems und der Schaltfläche Erstellen und Zusammenführen des Bestehenden"><figcaption><p>Die Zusammenführungsanfrage einer Antwort</p></figcaption></figure>

## Fehlermeldungen

| Meldung oder Symptom | Ursache | Lösung |
| --- | --- | --- |
| This audit template type has no model validation configured | Der Typ der Vorlage gehört nicht zu den sechs Erstellungstypen und hat daher kein Modell. Die Meldung erscheint, wenn Sie auf **Bitte wählen Sie eine zuzuordnende Variable aus** klicken | Ändern Sie die **Art des Fragebogens** auf einen Erstellungstyp oder geben Sie die Variablennamen von Hand ein, wenn die Vorlage nur Antworten sammelt |
| Die Liste **Bitte wählen Sie eine zuzuordnende Variable aus** ist leer | Kein Feld des Eintrags passt zum Fragetyp, zum Beispiel eine Frage vom Typ Datum bei einem Eintrag ohne Datum | Ändern Sie den Fragetyp oder wählen Sie einen Typ ohne Filter |
| You need at least a slug name | Der Variablenname ist leer | Füllen Sie **Name der Variablen** aus |
| The variable name {slug} is present in another question | Zwei Fragen verwenden denselben Variablennamen | Geben Sie jeder Frage einen eigenen Namen |
| Die Schaltfläche **Anlegen** oder **Daten zusammenführen** fehlt | Die Antwort ist nicht veröffentlicht, ist archiviert oder die Vorlage ist nicht von einem Erstellungstyp | Validieren Sie die Antwort, stellen Sie sie wieder her oder prüfen Sie den Typ |
| Die Schaltfläche ist ausgegraut | Sie sind nicht der Inhaber der Antwort | Fragen Sie den Inhaber |
| Ein Feld im neuen Eintrag ist leer | Der Variablenname passt nicht zum Feld, oder das benutzerdefinierte Feld existiert nicht | Vergleichen Sie ihn mit der Liste und mit dem technischen Namen |
| Das Anlegen stoppt mit einer Meldung, die ein Feld nennt | Der Wert ist für das Feld nicht gültig | Korrigieren Sie die Antwort und versuchen Sie es erneut |
