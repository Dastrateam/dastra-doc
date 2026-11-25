---
description: >-
  Formulieren Sie Ihre Anfragen an Dastra AI so, dass die Antworten vollständig und belegt sind: fünf Grundsätze, Beispielanfragen und die Prüfung einer Antwort.
---

# Wirksame Anfragen formulieren

Dastra AI antwortet aus Ihrem Mandanten, die Antwort ist also nur so genau wie die Anfrage. Nennen Sie die Einträge, die Sie meinen, sagen Sie, was Sie zurückbekommen möchten, und bitten Sie im Bearbeitungsmodus darum, zuerst nachzusehen, bevor es handelt. Diese Seite zeigt fünf Grundsätze, Beispielanfragen und die Prüfung einer Antwort.

Die Beispiele wurden in einem Demo-Mandanten getestet, dem eines fiktiven Händlers, der Brightmoor Retail Group. Ersetzen Sie seine Eintragsnamen durch Ihre eigenen. Die Anfragen wurden auf Englisch getestet, die deutschen Formulierungen sind Übersetzungen.

## Fünf Grundsätze

### Den Umfang mit den Wörtern der App benennen

Nennt eine Anfrage eine Gruppe von Einträgen, die Dastra nicht als solche kennt, muss der Assistent raten, welche Sie meinen. Zählen Sie die Einträge auf oder verwenden Sie die Wörter der App: Verarbeitungstätigkeit, Betroffenenanfrage, Organisationseinheit.

| Statt | Schreiben Sie |
| --- | --- |
| `Vergleichen Sie die Speicherdauern unserer Marketing-Verarbeitungstätigkeiten und markieren Sie die, die nicht stimmig wirken. Antworten Sie als Tabelle.` Der Assistent wählte drei Tätigkeiten und ließ andere derselben Art aus. | `Vergleichen Sie die Speicherdauern dieser Verarbeitungstätigkeiten: Newsletter and promotional emails, Newsletter campaigns, Targeted advertising and retargeting, Personalised product recommendations und Brightmoor Rewards loyalty programme. Zeigen Sie die Aufbewahrungsregel und die Speicherdauer jeder Tätigkeit in einer Tabelle und markieren Sie die, die nicht stimmig wirken.` Fünf Zeilen, jede mit ihrer Aufbewahrungsregel und einer Markierung. |
| `Fügen Sie den Tag „Reviewed 2026“ zu den Verarbeitungstätigkeiten von Brightmoor UK Ltd hinzu.` Der Assistent las „Entität“ als Namen eines Eintrags und schlug eine unzusammenhängende Tätigkeit vor. | `Fügen Sie den Tag „Reviewed 2026“ zu den Verarbeitungstätigkeiten der Abteilung Legal & Compliance der Brightmoor Retail Group hinzu.` Bearbeitungsmodus. Der Assistent fand die Organisationseinheit, sah, dass der Tag nicht existierte, und stoppte an einer Genehmigungskarte, um ihn zu erstellen. |

### Den Beleg verlangen, nicht das bloße Urteil

Eine Ja-Nein-Frage wird aus einer Markierung im Verzeichnis beantwortet. Verlangen Sie die Daten dahinter und dann die Markierung.

| Statt | Schreiben Sie |
| --- | --- |
| `Welche Verarbeitungstätigkeiten verarbeiten Gesundheitsdaten oder andere sensible Daten und haben keine DSFA?` Zwei richtige Tätigkeiten, aber nur aus der Markierung für sensible Daten, und keine Gesundheitsdaten identifiziert. | `Listen Sie alle Verarbeitungstätigkeiten mit ihren Datenkategorien auf und geben Sie an, ob eine DSFA erfasst ist. Markieren Sie dann die, die besondere Datenkategorien verarbeiten, etwa Gesundheitsdaten, und keine DSFA haben. Antworten Sie als Tabelle.` Jede Tätigkeit in einer Tabelle, dieselben zwei markiert, und der Grund: Eine verknüpfte Datenkategorie enthält Krankschreibungen. |

### Kontext mit `@` geben oder den Eintrag öffnen

Auf einem Eintrag geht der Assistent von dem aus, was der Eintrag enthält: seine Zähler, seine verknüpften Maßnahmen und Dienstleister. Zwei Wege, ihm diesen Kontext zu geben:

* Öffnen Sie den Eintrag und drücken Sie **Strg+J** (**Cmd+J** auf dem Mac). Der Eintrag wird über dem Nachrichtenfeld angehängt. Das Fenster öffnet die vorherige Unterhaltung wieder: Klicken Sie zuerst auf **Neue Unterhaltung**.
* Geben Sie `@` und einige Buchstaben des Eintragsnamens ein und wählen Sie dann die Zeile. Die Erwähnung wird in Ihrer Nachricht zu einem Chip. Das Menü listet Einträge und Dokumente auf, manchmal mit ähnlichen Namen: Wählen Sie die Zeile des richtigen Typs.

Die [Beispiele zum Analysieren](#beispielanfragen-nach-ziel) unten nutzen beide Wege.

### Das Format verlangen, dann in derselben Unterhaltung nachfassen

Sagen Sie, wie die Antwort aussehen soll: eine Tabelle, die Spalten, die Reihenfolge, eine Zeilenzahl. Verfeinern Sie dann in derselben Unterhaltung. Eine Folgefrage nutzt die vorherige Liste weiter, statt neu zu suchen, sodass die neue Antwort mit ihr stimmig bleibt.

1. `Listen Sie die nicht abgeschlossenen Betroffenenanfragen mit Typ, Antragsteller und Fälligkeitsdatum auf, die älteste zuerst.`
2. `Gruppieren Sie sie jetzt nach Anfragetyp und zählen Sie sie.`

### Erst finden, dann handeln

Im Bearbeitungsmodus liefert eine Anfrage, die aus einer allgemeinen Beschreibung etwas erstellt, ein allgemeines Ergebnis. Bitten Sie den Assistenten, zuerst aufzulisten, was fehlt, und dann auf dieser Liste zu handeln.

| Statt | Schreiben Sie |
| --- | --- |
| `Erstellen Sie einen Aktionsplan mit drei Aufgaben, um die Verarbeitungstätigkeit „Supplier and contract management“ zu vervollständigen.` Die Aufgaben waren allgemeine Aufgaben der Lieferantenverwaltung und verfehlten die Lücken des Eintrags. | `Listen Sie zuerst auf, was in der Verarbeitungstätigkeit „Supplier and contract management“ fehlt. Erstellen Sie dann einen Aktionsplan mit einer Aufgabe für jede der drei wichtigsten Lücken.` Bearbeitungsmodus. Drei Aufgaben mit hoher Priorität, die zu den Lücken passen: Speicherdauern, Inventar der personenbezogenen Daten und Zwecke, Empfänger und Übermittlungen. |

Jede Änderung im Bearbeitungsmodus stoppt an einer Karte **Genehmigung erforderlich**: siehe [Die Genehmigungskarte lesen](#die-genehmigungskarte-lesen).

## Beispielanfragen nach Ziel

Jede der folgenden Anfragen wurde getestet. Der Modus ist der, in dem sie getestet wurde. Auch die Anfragen der Grundsätze oben sind Beispiele: der Vergleich der Speicherdauern und die Frage zu sensiblen Daten für das Analysieren und Finden, der Tag und der Aktionsplan für das Ändern von Einträgen.

| Ziel | Schreiben Sie | Modus |
| --- | --- | --- |
| Finden | `Listen Sie die nicht abgeschlossenen Betroffenenanfragen mit Typ, Antragsteller und Fälligkeitsdatum auf, die älteste zuerst.` | **Frage** |
| Einen Eintrag analysieren | `Fassen Sie diese Verarbeitungstätigkeit in fünf Zeilen zusammen und listen Sie dann auf, was zu ihrer Vervollständigung fehlt.` Aus dem Fenster, das auf der Verarbeitungstätigkeit „Supplier and contract management“ geöffnet ist. | **Frage** |
| Einen Eintrag analysieren | `@Online order management Welche Sicherheitsmaßnahmen würden Sie für diese Verarbeitung erwarten, die noch nicht verknüpft sind?` Die Erwähnung ist ein Chip. | **Frage** |
| Nachfassen | `Behalten Sie nur die, die dieses Jahr erstellt wurden.` In der Unterhaltung der obigen Liste. | **Frage** |
| Nachfassen | `Gruppieren Sie sie jetzt nach Anfragetyp und zählen Sie sie.` In derselben Unterhaltung. | **Frage** |
| Entwerfen | `Entwerfen Sie eine Antwort auf die Anfrage 2BEX36WB, auf Englisch, in förmlichem Ton, die bestätigt, dass wir sie erhalten haben und innerhalb eines Monats antworten werden.` Nichts wird gesendet oder gespeichert: Kopieren Sie den Entwurf mit **Kopieren**. | **Frage** |
| Ein Artefakt erstellen | `Zeichnen Sie ein Diagramm der Datenflüsse der Verarbeitungstätigkeit Online order management.` Die Antwort verweist auf ein [Artefakt](artifacts.md). | **Frage** |
| Eine Funktion ausführen | `/dpo_opinion`, dann in derselben Unterhaltung: `Diese Nachricht ist die Anfrage, heute gestellt von Emma Walsh, DSB. Frage: Kann diese Verarbeitungstätigkeit veröffentlicht bleiben, obwohl ihre Aufbewahrungsregel und ihre Felder für personenbezogene Daten fehlen?` Auf der Verarbeitungstätigkeit „Supplier and contract management“. | **Frage** |

## Die Antwort prüfen und steuern

### Die Schritte und die Quellen lesen

Unter einer Antwort sagt Ihnen eine Zeile wie **3 Verwendete(s) Tool(s)**, was der Assistent getan hat. Klicken Sie auf **Tools anzeigen**, um die Schritte zu sehen, zum Beispiel **Einträge durchsuchen** oder **Eintrag lesen**. Passen die Schritte nicht zu dem, was Sie meinten, formulieren Sie den Umfang neu.

Einträge werden in der Antwort genannt, nicht verlinkt: In einer Tabelle sind die Zeilen einfacher Text. Suchen Sie den Namen im Verzeichnis, um den Eintrag zu öffnen.

Der Assistent sagt auch, was er nicht feststellen konnte. In den Tests merkte er an, dass eine „nicht verknüpfte“ Maßnahme nicht beweist, dass sie „nicht umgesetzt“ ist, dass Fälligkeitsdaten in UTC angegeben sind und dass die Wege eines Diagramms über die erfassten Zwecke hinaus Richtwerte sind. Lesen Sie diese Sätze: Sie sagen Ihnen, was Sie prüfen sollten.

{% hint style="info" %}
Eine Antwort ist ein Vorschlag zur Prüfung, keine Schlussfolgerung. Siehe [KI als Ausgangspunkt, nicht als endgültige Antwort](README.md#ki-als-ausgangspunkt-nicht-als-endgultige-antwort).
{% endhint %}

### Die Genehmigungskarte lesen

Im Bearbeitungsmodus zeigt der Assistent vor jeder Änderung eine Karte **Genehmigung erforderlich** an. Sie nennt das Werkzeug, zum Beispiel **Erstellung eines Tags** oder **Erstellung eines Aktionsplans**. Klicken Sie auf **Argumente anzeigen**, um genau zu sehen, was gesendet werden soll: die Einträge, die Bezeichnungen, die Aufgaben.

**Ablehnen** ändert nichts. Der Assistent bestätigt es („es wurden keine Aufgaben erstellt“) und bietet an, die Anfrage zu überarbeiten. Senden Sie eine weitere Nachricht, während eine Karte wartet, gilt die Karte nicht mehr. Die Möglichkeiten der Karte sind unter [Der Modus Frage und der Bearbeitungsmodus](README.md#der-modus-frage-und-der-bearbeitungsmodus) beschrieben.

### Die Antwort bewerten

Klicken Sie unter einer Antwort auf **Richtige Antwort** oder **Falsche Antwort**. Bei **Falsche Antwort** öffnet sich ein Fenster, in dem Sie sagen können, was falsch war. Dastra speichert die Bewertung und den Kommentar mit der Nachricht.

## Gut zu wissen

* Prüfen Sie den Modus, bevor Sie senden. Für Nutzer, die bearbeiten dürfen, ist der Modus standardmäßig **Bearbeiten**. Wechseln Sie zu **Frage** für eine Frage, die nichts ändern darf.
* Beginnen Sie für ein neues Thema eine neue Unterhaltung. Das Fenster öffnet die vorherige Unterhaltung wieder: Klicken Sie oben im Fenster auf **Neue Unterhaltung**. Eine Folgefrage arbeitet mit der vorherigen Antwort, ein neues Thema braucht sie nicht.
* Prüfen Sie die Zeile, die Sie im Menü `@` wählen. Es mischt Einträge und Dokumente, und ein Dokument kann einen Namen haben, der dem eines Eintrags nahekommt.
* Eine Funktion braucht ihre Angaben in der Nachricht. `/dpo_opinion` allein fragt nur nach der Anfrage: wer sie gestellt hat, wann und die Frage.

## Eine wiederkehrende Anfrage in eine Funktion verwandeln

Tippen Sie dieselbe Anfrage oft neu ein, speichern Sie sie als Funktion und rufen Sie sie mit `/` auf. Eine Funktion bewahrt Ihre Formulierung, und Ihr Team kann sie teilen. Siehe [Funktionen](agents/skills.md).
