---
description: Erfahren Sie, was Speicherdauern sind.
---

# Speicherdauer

## Definition

Die **Speicherdauern** gehören zu den Grundprinzipien des Schutzes personenbezogener Daten. Sie ergeben sich aus dem Grundsatz der **Speicherbegrenzung** (Artikel 5 Absatz 1 Buchstabe e DSGVO) und tragen zum **Recht auf Löschung** bei.

Wichtige Artikel:

* **Artikel 5 DSGVO** (Speicherbegrenzung);
* **Artikel 30** (Dokumentation im Verzeichnis);
* **Artikel 13 und 14** (Information der betroffenen Personen).

Konkret müssen Sie für jede Verarbeitungstätigkeit festlegen:

* eine **feste Dauer** (oder eine Reihe von Dauern je Phase),
* und/oder ein **objektives Kriterium** für ihre Berechnung (z. B. „+3 Jahre nach dem letzten aktiven Kontakt“).

***

## Der Lebenszyklus der Daten

Die Aufbewahrung gliedert sich in **aufeinanderfolgende Phasen**. Dieser Lebenszyklus bestimmt Ihre Regeln zur Speicherdauer.

| Phase | Zweck | Zugriff | Beispiel für die Dauer |
| --- | --- | --- | --- |
| **Aktive Nutzung** | Operative Nutzung | Breit (Fachabteilung) | Vertragslaufzeit + Durchführung |
| **Zwischenarchivierung** | Nachweis / Verteidigung eines Rechts | Eingeschränkt (Kenntnis nur bei Bedarf) | Gesetzliche Verjährungsfrist (z. B. 5 Jahre) |
| **Endarchivierung** (öffentlich) | Historisches Interesse | Sehr eingeschränkt | Übergabe / Auswahl durch die Archive |
| **Anonymisierung** | Statistik / Forschung | Nicht identifizierende Daten | Unbegrenzt, wenn wirklich unumkehrbar |
| **Löschung** | Ende des Lebenszyklus | Nicht anwendbar | Am Ende der Phasen |

{% hint style="info" %}
Die Leitlinien Ihrer nationalen Datenschutzbehörde zu Speicherdauern behandeln in der Regel: die Führung von Verzeichnissen, Referenzdokumente, Verfahren zur Archivierung und Vernichtung, Weisungen an Auftragsverarbeiter usw.
{% endhint %}

***

## Wie Sie die Speicherdauern festlegen (Methode)

1. **Den Zweck klären**: Was tun Sie tatsächlich mit den Daten? Wofür werden sie verwendet?
2. **Die Phasen abbilden**: Aktive Nutzung → Zwischenarchivierung → Anonymisierung / Löschung
3. **Rechtsgrundlagen und Referenzen ermitteln**: Branchenspezifische Gesetze und Vorschriften, Leitlinien der Aufsichtsbehörde, interne Referenzrahmen
4. **Eine klare Regel festlegen**: „**X Jahre nach \[Ereignis]**, dann **Y Jahre archivieren**, dann **löschen**“ oder „**solange…**, dann **Z Jahre nach \[Kriterium]**“
5. **Die Umsetzung organisieren**: **Automatische** oder **gesteuerte** Löschung, Protokollierung, Nachweis der Ausführung
6. **Informieren und dokumentieren**: Datenschutzerklärung (Art. 13–14), Verzeichnis (Art. 30), interne Richtlinie

{% hint style="info" %}
Gibt es **keine klare Referenz**, wählen Sie eine **dem Zweck angemessene** Dauer und dokumentieren Sie die Begründung (Rechenschaftspflicht).
{% endhint %}

***

## Beispielregeln (anzupassen)

| Kontext | Daten | Kurzregel |
| --- | --- | --- |
| B2B-Interessenten | Identität, Kontaktdaten, Nachweis des Opt-ins | **3 Jahre** nach dem letzten aktiven Kontakt, dann **Löschung** |
| Personal, Bewerber | Lebensläufe, Anschreiben, Gespräche | **2 Jahre** nach dem letzten Kontakt mit dem Bewerber, außer bei Widerspruch |
| Kunden | Vertrag, Rechnungsstellung | Vertrag + **5 Jahre** (Nachweis), dann **Archivierung / Löschung** |
| Videoüberwachung | Bilder | **höchstens 30 Tage**, außer bei einem Vorfall (Beweisverfahren) |
| Cookies | Kennungen, Präferenzen | Dauer im Einklang mit dem Cookie-Banner und dem **Nachweis der Einwilligung** |

> Diese Werte hängen von den anwendbaren Texten, Ihrer Branche und Ihren Risiken ab: **Dokumentieren Sie Ihre Entscheidungen**.

***

## Einzubindende Personen

* **Fachlich Verantwortlicher der Verarbeitung**: operative Anforderungen, auslösende Ereignisse
* **Datenschutzbeauftragter / Recht**: Konformität, anwendbare Texte, Abwägung der Rechte und Freiheiten
* **CISO / IT**: Löschung, Anonymisierung, Zugriffsbeschränkung, Protokolle
* **Auftragsverarbeiter**: konforme Ausführung der **schriftlichen Weisungen**

***

## Die Umsetzung kontrollieren (Audits)

* Regelmäßig prüfen: Angemessenheit der Dauern, Durchführung der Löschungen, Zugriff auf Archive, Anonymisierung
* Vorgänge protokollieren: Vernichtungsnachweise, Löschberichte, Protokolle
* Bei jeder **Änderung des Zwecks, der Rechtsgrundlage oder des Dienstleisters** überprüfen

***

## Umsetzung in Dastra

### 1) Im **Verzeichnis**

* Erfassen Sie pro Datenkategorie eine **lesbare Regel**: „_3 Jahre nach dem letzten aktiven Kontakt (Interessent), dann Löschung_“
* Ergänzen Sie das **auslösende Kriterium** (z. B. „Datum der letzten CRM-Aktivität“, „Vertragsende“)
* Verknüpfen Sie **Referenzen** (Rechtstext, interner Referenzrahmen)

### 2) Die Löschung **automatisieren / steuern**

* Planen Sie **Aufgaben** (Überprüfungen, Löschungen, Erstellung von Nachweisen)
* Nutzen Sie **Workflow-Regeln** und **regelmäßige Überprüfungen** für die Fristen

### 3) **Nachweis**

* Legen Sie Vernichtungsnachweise, Löschberichte, Skripte und Ausführungstickets im Abschnitt **Dokumente** der Verarbeitungstätigkeit ab

***

## Zwischenarchivierung und Sicherheit

* Zugriff beschränken (RBAC, Kompartimentierung)
* Abrufe protokollieren
* Logische Trennung (Archivtresor / -zone)
* Bei Bedarf verschlüsseln
* Mit den Auftragsverarbeitern die **Umkehrbarkeit** planen

***

## Anonymisierung und Pseudonymisierung

* **Anonymisierung**: unumkehrbar → **außerhalb des Anwendungsbereichs der DSGVO**, wenn die Person wirklich nicht wieder identifizierbar ist
* **Pseudonymisierung**: mit einem Schlüssel umkehrbar → **weiterhin personenbezogene Daten** → Dokumentieren Sie das Verfahren, testen Sie die **Re-Identifizierbarkeit** und berücksichtigen Sie **Zusatzdaten**.

***

## KI und Speicherdauern

Legen Sie für **KI-Systeme** getrennte Speicherdauern fest für:

* **Training** (Datensätze, Versionen),
* **Validierung / Tests**,
* **Inferenzprotokolle** (Nachvollziehbarkeit, Transparenz),
* **Evaluierungsdatensätze** (Verzerrungen, Robustheit).

Verknüpfen Sie diese Dauern mit Ihrem **Register der KI-Systeme**, um die Konsistenz zwischen DSGVO und KI-Verordnung zu sichern.

***

## Nützliche Referenzen

* Leitlinien zur Speicherdauer, die Ihre nationale Aufsichtsbehörde veröffentlicht (zum Beispiel der Leitfaden der CNIL zu Speicherdauern in Frankreich)
* Branchenspezifische Gesetze und Vorschriften, die Mindest- oder Höchstspeicherdauern festlegen
* Verhaltensregeln und Standards Ihrer Branche
* Tarifverträge

***

{% hint style="success" %}
**Bewährte Vorgehensweise:** Formulieren Sie _umsetzbare_ Regeln („X Jahre nach \[Ereignis], dann Löschung oder Anonymisierung“), testen Sie sie in einem begrenzten Bereich und führen Sie sie dann breit ein. Dastra hilft Ihnen, die Ausführung zu **dokumentieren**, zu **planen** und **nachzuweisen**.
{% endhint %}

***

## Weiterführende Informationen

{% content-ref url="../../features/ropa/activity/datasets.md" %}
[Daten und Speicherdauer](../../features/ropa/activity/datasets.md)
{% endcontent-ref %}

{% content-ref url="../../features/tasks/README.md" %}
[Planung](../../features/tasks/README.md)
{% endcontent-ref %}
