---
description: >-
  Inventarisieren Sie die Software, Server und anderen Medien, die Ihre
  personenbezogenen Daten enthalten, beschreiben Sie jedes Asset und erstellen
  Sie daraus eine Verarbeitungstätigkeit.
---

# Assets

Assets sind die Elemente, die Ihnen bei der Verwaltung von Daten helfen: Datenträger, Räumlichkeiten sowie materielle und immaterielle Ausstattung. Diese Referenzliste führt die Assets auf, die zur Organisation gehören oder außerhalb von ihr liegen (Anwendungen, Ressourcen, Gebäude usw.).

Erfassen Sie hier die Anwendungen, die Software und andere Elemente, die als Datenträger dienen. Wenn Sie zum Beispiel eine Software zur Verwaltung von Kundenbeziehungen wie ein CRM nutzen, fügen Sie sie dieser Liste hinzu. So behalten Sie die Kontrolle über Ihre Datenträger und verknüpfen sie mit Ihrem Datenkatalog.

{% hint style="info" %}
Assets sind nicht zwangsläufig mit Auftragsverarbeitern verknüpft. Ein Asset kann zum Beispiel eine Software sein, die auf Ihrem eigenen Server installiert ist, ohne dass ihr Herausgeber in die Verarbeitung personenbezogener Daten eingreift.
{% endhint %}

## Ein Asset hinzufügen

Um ein Asset hinzuzufügen, haben Sie folgende Möglichkeiten:

* von einer Vorlage ausgehen: Klicken Sie auf den Pfeil neben der Schaltfläche **Asset erstellen** und dann auf **Erstellen Sie auf der Grundlage von Vorlagen**;
* die KI nutzen: Klicken Sie auf die KI-Schaltfläche links von **Asset erstellen** oder wählen Sie im Erstellungsfenster **Erstellen mit KI-Assistent** (diese Option hängt von den Funktionen ab, die für Ihre Organisation aktiviert sind);
* das Asset direkt in der Referenzliste erstellen: Klicken Sie auf **Asset erstellen** und wählen Sie dann **Von Grund auf neu**;
* Assets aus einer Excel-, CSV- oder JSON-Datei importieren: Klicken Sie auf den Pfeil neben der Schaltfläche **Asset erstellen** und dann auf **Importieren**. Siehe [Daten importieren (Excel, CSV)](../../general/import.md);
* das Asset aus einem Fragebogen erstellen: Dafür ist eine Fragebogenvorlage vom Typ **Asset creation** nötig. Siehe [Eine Fragebogenvorlage erstellen](../../questionnaires/templates/README.md).

## Das Asset-Formular ausfüllen

Das Formular eines Assets fasst die folgenden Angaben zusammen.

| Abschnitt | Feld | Inhalt |
| --- | --- | --- |
| **Allgemeine Informationen** | **Name des Assets**, **Interne Referenz** | Der Name des Assets und Ihre interne Referenz. |
| | **Organisationseinheit** | Die Einheit, zu der das Asset gehört. Siehe unten. |
| | **Art des Assets** | Die Art des Assets, erforderlich. |
| | **Inhaber des Assets** | Der Nutzer, der für die Umsetzung des Assets zuständig ist. Der Inhaber wird bevorzugt den mit dem Asset verknüpften Fragebögen und Aufgaben zugewiesen. |
| | **Herausgeber** | Die Organisation, die das Asset herausgibt, hostet oder verwaltet. Sie kann als Auftragsverarbeiter referenziert werden, wenn das Asset in einer Verarbeitungstätigkeit genannt wird. Beispiel: Der Herausgeber von Office 365 ist Microsoft. |
| | **Beschreibung**, **URL der Datenschutzinformation** | Eine freie Beschreibung und die Adresse der Datenschutzinformation des Assets. |
| | **Software-Typ**, **Software-Status**, **Art des Hosts**, **Art der Entwicklung**, **Art der Unterstützung**, **Art der Wartung** | Diese sechs Felder erscheinen, wenn die Art des Assets **Software** ist. |
| **Lokalisierung der Daten** | **Land**, **Adresse**, **Stadt**, **Region**, **Postleitzahl** | Wo sich das Asset befindet. |
| | **Informationen zum Speicherort der Daten** | Freitext, um anzugeben, wo die Daten gehostet werden. |
| **Datensätze** | | Die im Asset enthaltenen Datenkategorien. Speichern Sie das Asset einmal, bevor Sie sie erstellen. |
| **Verbundene Sicherheitsmaßnahmen** | | Die Sicherheitsmaßnahmen des Assets, oft im DPA genannt. Wählen Sie kurze Namen, damit Sie sie von einem Asset zum anderen wiederverwenden können. |

Die für Assets definierten [benutzerdefinierten Felder](../../general/custom-fields.md) werden diesem Formular hinzugefügt.

Die Symbolleiste des Formulars gibt Zugriff auf die angehängten Dokumente, Kommentare, Fragebögen, Aufgaben, Verträge, KI-Systeme und Risiken, die mit dem Asset verknüpft sind, je nach Ihren Berechtigungen und den aktivierten Funktionen. Sie enthält außerdem:

* **Verknüpfte Elemente**: die [generischen Beziehungen](../relationships.md) des Assets mit ihrer Anzahl;
* **Verarbeitungen**: die Anzahl der Verarbeitungstätigkeiten, die das Asset verwenden, und ihre Liste;
* **Aktivitätsverlauf**: die aufeinanderfolgenden Änderungen des Formulars, die Sie wiederherstellen können;
* die regelmäßige Überprüfung des Assets. Siehe [Regelmäßige Überprüfung (Aktualität)](../../regular-review.md).

## Aus einem Asset eine Verarbeitungstätigkeit erstellen

Diese Aktion verwendet die Angaben des Assets wieder, um eine Verarbeitungstätigkeit vorzubereiten, damit Sie sie nicht erneut eingeben müssen.

1. Öffnen Sie das Asset.
2. Klicken Sie im Aktionsmenü des Formulars auf **Erstellen Sie eine Datenverarbeitung aus einem Vermögenswert**.
3. Wenn für dieses Asset Verarbeitungstätigkeiten vorgeschlagen wurden, wählen Sie eine aus der Liste oder klicken Sie auf **Diesen Schritt überspringen**.
4. Geben Sie die **Kennzeichnung der neuen Verarbeitung** ein, wählen Sie die **Zielorganisationseinheit** und klicken Sie dann auf **Weiter**.
5. Wählen Sie die Datenkategorien des Assets aus, die in der Verarbeitungstätigkeit wiederverwendet werden sollen, und klicken Sie dann auf **Weiter**.
6. Prüfen Sie die **Zusammenfassung**: Bezeichnung, Beschreibung, Datenkategorien, Sicherheitsmaßnahmen, Zwecke und betroffene Personen. Klicken Sie auf **Verarbeitung erstellen**.

Um Assets später mit einer bestehenden Verarbeitungstätigkeit zu verknüpfen, siehe die Seite [Assets](../../ropa/activity/assets.md) der Verarbeitungstätigkeit.

## Kopieren, zusammenführen und löschen

Das Aktionsmenü des Formulars bietet **Duplizieren**, **Zusammenführen** und **Löschen**. In der Liste erkennt das **Datenqualitätswerkzeug** doppelte Assets. Siehe [Elemente zusammenführen](../../general/merge.md).

## Ein Asset einer Organisationseinheit zuordnen

Standardmäßig steht ein in Dastra erstelltes Asset der gesamten Organisation zur Verfügung (globaler Geltungsbereich). Sie können ein Asset einer bestimmten Organisationseinheit zuordnen, um seine Sichtbarkeit auf die Nutzer dieser Einheit oder Abteilung zu beschränken.

Wählen Sie dazu beim Erstellen oder Bearbeiten des Assets die Organisationseinheit im Feld **Organisationseinheit** aus. Das Asset ist dann nur für Nutzer sichtbar, die Zugriff auf diese Organisationseinheit haben.
