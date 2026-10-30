---
description: >-
  Erstellen Sie einen Fragebogen zur KI-Verordnung, dessen Antworten die
  Risikostufe, die Rollen und ein benutzerdefiniertes Feld eines KI-Systems bei
  der Brightmoor Retail Group befüllen.
---

# Fragebogenantworten in einem Verzeichnis

Die Brightmoor Retail Group führt ihr KI-System „CV screening assistant“ bereits im Verzeichnis, aber der Eintrag ist unvollständig. Emma Walsh, die Datenschutzbeauftragte, möchte, dass die Person, die das Tool verantwortet, einen Fragebogen zur KI-Verordnung beantwortet, und sie möchte, dass die Antworten das KI-System vervollständigen. Dieses Beispiel erstellt diesen Fragebogen. Die Referenz ist [Ein Verzeichnis aus den Antworten befüllen](../features/questionnaires/templates/record-mapping.md).

Der Fragebogen befüllt vier Felder: den Namen, die Risikostufe, die Rollen von Brightmoor nach der KI-Verordnung und ein benutzerdefiniertes Feld mit dem fachlichen Verantwortlichen.

## 1. Das benutzerdefinierte Feld erstellen

Wählen Sie unter **Mandanteneinstellungen** > **Benutzerdefinierte Felder** das Modul der KI-Systeme und erstellen Sie ein Textfeld mit der Bezeichnung „Business owner“. Öffnen Sie das Feld und lesen Sie seinen **Namen der Variablen (Slug)**: `business_owner`. Er ist nach der Erstellung schreibgeschützt. Siehe [Benutzerdefinierte Felder](../features/general/custom-fields.md).

## 2. Die Vorlage erstellen

1. Erstellen Sie unter **Fragebögen** eine benutzerdefinierte Vorlage mit dem Namen „AI Act intake“.
2. Setzen Sie die **Art des Fragebogens** auf **AI System creation**. Der Typ trägt das Datenmodell eines KI-Systems.
3. Setzen Sie **Verwandtes Thema** auf KI-Systeme, damit jede Antwort mit einem KI-System verknüpft werden kann.

## 3. Die Fragen hinzufügen

Öffnen Sie für jede der folgenden Fragen die Eigenschaften der Frage, aktivieren Sie **Möchten Sie den Namen der Variablen anpassen (nur für fortgeschrittene Nutzer)?** und legen Sie den Variablennamen fest.

| Frage | Fragetyp | Variablenname | Wie er festgelegt wird |
| --- | --- | --- | --- |
| Name of the AI system | Kurztext | `label` | **Bitte wählen Sie eine zuzuordnende Variable aus**, dann die Zeile `label` |
| What is the risk level of this AI system? | Einfachauswahlliste | `riskLevel` | **Bitte wählen Sie eine zuzuordnende Variable aus**, dann die Zeile `riskLevel` |
| What is the role of Brightmoor? | Liste mit mehreren Feldern | `responsibilities` | **Bitte wählen Sie eine zuzuordnende Variable aus**, dann die Zeile `responsibilities` |
| Role (Unterfrage der Liste) | Einfachauswahlliste | `responsibilityType` | Von Hand eingegeben |
| Who owns this AI system in the business? | Kurztext | `custom_business_owner` | Von Hand eingegeben: `custom_` und der technische Name |

Drei Punkte sind zu beachten:

* Bei `riskLevel` erzeugt die Wahl des Felds eine Antwort pro Wert: Low, Medium, High und Unacceptable, mit genau diesen Variablennamen. Benennen Sie die Bezeichnungen nach Belieben um, zum Beispiel Minimal, Limited, High und Unacceptable, und behalten Sie die Variablennamen bei.
* Für die Rollen sind die sechs Werte der KI-Verordnung Provider, Deployer, Distributor, Importer, AuthorizedRepresentative und Manufacturer. Fügen Sie der Unterfrage pro Rolle eine Antwort hinzu, mit dem Wert als Variablennamen der Antwort.
* Das benutzerdefinierte Feld steht nicht in der Liste der Variablen, weshalb sein Name vollständig eingegeben wird.

Speichern Sie die Vorlage.

<figure><img src="../.gitbook/assets/examples-questionnaire-1.png" alt="Fenster Bitte wählen Sie eine zuzuordnende Variable aus mit den Feldern eines KI-Systems"><figcaption><p>Die für ein KI-System angebotenen Variablen</p></figcaption></figure>

## 4. Die Antwort mit dem KI-System verknüpfen und die Antworten einholen

1. Planen Sie den Fragebogen. Wählen Sie unter **Gegenstand der Antwort** das KI-System „CV screening assistant“ aus. Siehe [Einen Fragebogen planen](../features/questionnaires/schedule.md).
2. Liam O'Connor antwortet: Name „CV screening assistant“, Risikostufe **High** (ein Recruiting-Tool ist nach Anhang III der KI-Verordnung eine Hochrisiko-Verwendung), Rolle **Deployer**, fachlicher Verantwortlicher „Sophie Becker, HR“.
3. Die Antwort wird validiert und veröffentlicht.

## 5. Die Antworten in das KI-System zusammenführen

Weil die Antwort mit einem bestehenden KI-System verknüpft ist, sieht ihr Inhaber die Schaltfläche **Daten zusammenführen** (Merge request, AI System).

1. Klicken Sie auf **Daten zusammenführen**. Die Vorschau zeigt das aus den Antworten aufgebaute KI-System. Wählen Sie die **Organisationseinheit** und klicken Sie auf **Erstellen und Zusammenführen des Bestehenden**.
2. Vergleichen Sie im Zusammenführungsfenster das bestehende KI-System mit dem temporären, das „CV screening assistant (From Questionnaire)“ heißt. Behalten Sie die Werte des Fragebogens für `riskLevel`, die Rollen und das benutzerdefinierte Feld und die bestehenden Werte für den Rest.
3. Bestätigen Sie das Zusammenführen.

| Feld | Vorher | Nachher |
| --- | --- | --- |
| Risikostufe | Leer | High |
| Rollen | Keine | Deployer |
| Business owner (benutzerdefiniertes Feld) | Leer | Sophie Becker, HR |

Das KI-System trägt jetzt die Antworten. Vor Schritt 3 wurde nichts geändert: Die Antworten aktualisieren einen Eintrag nie von selbst.

Würde das KI-System nicht existieren, hätte die Antwort keinen verknüpften Eintrag. Die Schaltfläche hieße dann **Anlegen**, und **Erstellen** würde das KI-System im Verzeichnis anlegen.

<figure><img src="../.gitbook/assets/examples-questionnaire-2.png" alt="Seite der Zusammenführungsanfrage mit der Vorschau des KI-Systems und der Schaltfläche Erstellen und Zusammenführen des Bestehenden"><figcaption><p>Die Zusammenführungsanfrage einer Antwort</p></figcaption></figure>
