---
description: >-
  Erfahren Sie, wie Sie die Antworten auf Fragebögen steuern und die Ergebnisse
  in Dastra analysieren.
---

# Fragebögen steuern

## Dashboard der Antworten

Wählen Sie in der Registerkarte **"Fragebögen anzeigen"** eine Vorlage aus, um auf deren Antwort-Dashboard zuzugreifen. Es bietet vier Ansichten:

* **Antworten**: Liste aller Antworten mit ihrem Status (ausstehend, veröffentlicht, überfällig), ihrer Bewertung und dem verknüpften Objekt
* **Detaillierte Tabelle**: Seitenweiser Vergleich aller Antworten nach Kategorie und Bewertung — nützlich zum Benchmarking mehrerer Entitäten oder Verarbeitungen
* **Statistiken**: Aggregierte Statistiken über alle Antworten der Vorlage
* **Details**: Konfiguration und Metadaten des Fragebogens

## Reporting einer einzelnen Antwort

Beim Öffnen einer Antwort erhalten Sie eine detaillierte Reporting-Ansicht:

* **Status**: Fortschritt von "Warten auf Befragte" → "Gestartet" → "Warten auf Validierung" → "Veröffentlicht"
* **Bewertung**: Gesamtbewertung bezogen auf die maximale Punktzahl
* **Vollständigkeit**: Anzahl der beantworteten Fragen im Verhältnis zur Gesamtzahl
* **Antwortzeit**: Dauer zum Ausfüllen des Fragebogens
* **Markierungen**: Antworten, die gemäß der Vorlagenkonfiguration automatisch als aufmerksamkeitsbedürftig markiert werden
* **Ergebnisanalyse**: Automatisch generierte Analyseblöcke (Compliance-Niveau, Risikobewertung usw.)
* **Bewertung nach Kategorien**: Visualisiert als Radar- oder Balkendiagramm

## KI-Analyse (Beta)

Lösen Sie aus der Reporting-Ansicht einer Antwort eine **KI-Analyse** aus, um Folgendes zu erhalten:

* Eine Gesamtbewertung der Compliance oder des Risikos
* Eine schriftliche Zusammenfassung der wichtigsten Feststellungen
* Eine Analyse nach Kriterien (Vollständigkeit, Rechtsgrundlage, Sicherheitsmaßnahmen usw.)
* Vorgeschlagene Aufgaben zur Behebung der identifizierten Lücken

{% hint style="warning" %}
Die KI-Analyse ist eine Beta-Funktion. Die Ergebnisse sollten mit Vorsicht interpretiert und von einer qualifizierten Fachperson überprüft werden.
{% endhint %}

## Eine Antwort validieren und veröffentlichen

Sobald die Antwort geprüft wurde, klicken Sie auf **"Fragebogen prüfen und validieren"**, um sie auf den Status "Veröffentlicht" zu setzen. Diese Aktion steht den Verantwortlichen des Fragebogens zur Verfügung.

{% hint style="info" %}
Wenn Sie eine Antwort nicht validieren können, überprüfen Sie, ob der Befragte auf die Schaltfläche **"Abschließen"** geklickt hat. Ohne diesen Schritt bleibt die Antwort im Status "Warten auf Validierung".
{% endhint %}

## Antworten mit dem verknüpften Objekt zusammenführen

Nach dem Ausfüllen eines Fragebogens, der mit einem Dastra-Objekt verknüpft ist (Verarbeitung, Asset, Akteur usw.), ist es möglich, **die gesammelten Antworten mit den Daten dieses Objekts zusammenzuführen**.

Diese Aktion aktualisiert direkt die entsprechenden Felder des Objekts anhand der im Formular eingegebenen Informationen, ohne erneute manuelle Eingabe.

Um die Zusammenführung zu starten:

1. Öffnen Sie die abgeschlossene Antwort des Fragebogens.
2. Klicken Sie auf **"Antworten mit dem Objekt zusammenführen"**.
3. Bestätigen Sie die im Zielobjekt zu aktualisierenden Felder.

Diese Funktion ist besonders nützlich in Szenarien der externen Datenerhebung über Privacy Hubs, in denen Dritte (Lieferanten, Auftragsverarbeiter) Informationen angeben, die anschließend in Ihren internen Verzeichnissen widergespiegelt werden müssen.

<figure><img src="../../.gitbook/assets/image-275.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image-278.png" alt=""><figcaption></figcaption></figure>

## Einen Maßnahmenplan erstellen

Klicken Sie aus der Reporting-Ansicht einer Antwort auf **"Maßnahmenplan erstellen"**, um automatisch Aufgaben basierend auf den gegebenen Antworten zu erstellen. Die Aufgaben werden gemäß der Vorlagenkonfiguration vorgeschlagen und direkt zum Aufgabenmanagement-Modul von Dastra hinzugefügt.
