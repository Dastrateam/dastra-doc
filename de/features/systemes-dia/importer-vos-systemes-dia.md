# Ihre KI-Systeme importieren

Sie können Ihr bestehendes Verzeichnis ganz einfach direkt in Dastra hochladen. So müssen Sie nicht alles manuell ausfüllen.

Gehen Sie dazu zur Listenansicht mit dem Titel „KI-Systeme". Öffnen Sie oben rechts das Dropdown-Menü neben der Schaltfläche „Neues KI-System erstellen" und klicken Sie dann auf „Importieren". Eine neue Seite erscheint, auf der Sie unten Ihr bestehendes Verzeichnis hinzufügen können.

<figure><img src="../../.gitbook/assets/KI-Register1.png" alt=""><figcaption></figcaption></figure>

Wir empfehlen Ihnen, die Schritte auf der Seite [Ihre Daten importieren (Excel, CSV, JSON)](../generalites/importer-vos-donnees-excel-csv.md) für weitere Details zu befolgen.

## Importformat der KI-Systeme in Dastra

Dieser Leitfaden beschreibt das erwartete Format für die CSV-Datei zum Import von KI-Systemen in Dastra.

***

### Struktur der CSV-Datei

Die Datei muss eine Kopfzeile enthalten, die den unten beschriebenen Spalten entspricht.\
Alle Felder sind optional, außer **Label**.

***

### Tabelle der Importfelder

> 💡 **Wichtig:** Spalten vom Typ _Enum_ müssen strikt die in der Spalte „Zulässige Werte" angegebenen Werte verwenden.

| **Spalte**                    | **Beschreibung**                  | **Typ**              | **Einschränkungen**                                | **Zulässige Werte**               |
| ----------------------------- | --------------------------------- | -------------------- | -------------------------------------------------- | --------------------------------- |
| **Label**                     | Name des Systems                  | String               | **Pflichtfeld**, 1–120 Zeichen                     | —                                 |
| **Ref**                       | Interne Referenz                  | String               | Optional, max. 50 Zeichen                          | —                                 |
| **Description**               | Beschreibung des Systems          | String               | Optional, max. 4000 Zeichen                        | —                                 |
| **State**                     | Status des Systems                | AiSystemState        | Optional                                           | Draft, Cancelled, Pending, Active |
| **RiskLevel**                 | Risikoniveau                      | AiSystemRiskLevel    | Optional                                           | Low, Medium, High, Unacceptable   |
| **RiskLevelJustification**    | Begründung des Risikoniveaus      | String               | Optional                                           | —                                 |
| **BenefitLevel**              | Nutzwert-Niveau                   | AiSystemBenefitLevel | Optional                                           | Low, Medium, High                 |
| **BenefitLevelJustification** | Begründung des Nutzwerts          | String               | Optional                                           | —                                 |
| **DateArchived**              | Archivierungsdatum                | DateTime             | Optional — Formate: `DD-MM-YYYY` oder `DD/MM/YYYY` | —                                 |
| **DateCreation**              | Erstellungsdatum                  | DateTime             | Optional — gleiches Format                         | —                                 |
| **DateUpdate**                | Aktualisierungsdatum              | DateTime             | Optional — gleiches Format                         | —                                 |
| **DateDeployment**            | Bereitstellungsdatum              | DateTime             | Optional — gleiches Format                         | —                                 |
| **DateRetirement**            | Außerbetriebnahme-Datum           | DateTime             | Optional — gleiches Format                         | —                                 |
| **TransparencyNoticeDone**    | Transparenzhinweis bereitgestellt | Boolean              | Optional                                           | true / false                      |
| **TransparencyNoticeHtml**    | HTML-Inhalt des Hinweises         | String               | Optional, max. 4000 Zeichen                        | —                                 |

***

### Beispiel einer CSV-Zeile

> ✨ _Hier ein vollständiges Beispiel einer korrekt formatierten Zeile:_

```
"ChatGPT interne","SYS-001","Modèle interne d'assistance documentaire","Active","Medium","Usage responsable mais risques modérés","High","Très forte valeur ajoutée pour les équipes","01/02/2024","15/01/2024","01/03/2024","20/03/2024","","false","<p>Cette IA est utilisée pour assister les employés dans la rédaction de documents internes.</p>"
```

***

### Einsatzbereite CSV-Vorlage

> Sie können _diese Vorlage in eine leere `.csv`-Datei kopieren:_

```
Label,Ref,Description,State,RiskLevel,RiskLevelJustification,BenefitLevel,BenefitLevelJustification,Date
```
