---
description: Erfahren Sie, was Speicherdauern sind.
---

# Speicherdauer

### 📖 Definition

Die **Speicherdauern** gehören zu den grundlegenden Prinzipien des Datenschutzes.\
Sie ergeben sich aus dem Grundsatz der **Speicherbegrenzung** (Artikel 5.1.e DSGVO) und tragen zum **Recht auf Vergessenwerden** bei.

> 🔗 Schlüsselartikel:\
> – **Art. 5 DSGVO** (Speicherbegrenzung)\
> – **Art. 30 DSGVO** (Dokumentation im Verarbeitungsverzeichnis)\
> – **Art. 13–14 DSGVO** (Information der betroffenen Personen)

Konkret müssen Sie für jede Verarbeitung festlegen:

* eine **feste Dauer** (oder eine Reihe von Dauern je Phase),
* und/oder ein **objektives Kriterium** zur Berechnung (z. B. "+3 Jahre nach dem letzten aktiven Kontakt").

***

### 🔄 Der Lebenszyklus der Daten

Die Aufbewahrung gliedert sich in **aufeinanderfolgende Phasen**. Dieser Zyklus bestimmt Ihre Regeln.

| Phase                       | Zweck                         | Zugang                       | Beispiel für Dauer                     |
| --------------------------- | ----------------------------- | ---------------------------- | -------------------------------------- |
| **Aktive Nutzung**          | Operativer Betrieb            | Umfassend (Fachabteilung)    | Vertragsdauer + Durchführung           |
| **Zwischenarchivierung**    | Nachweis / Rechtsverteidigung | Eingeschränkt (Need-to-know) | Gesetzliche Verjährung (z. B. 5 Jahre) |
| **Dauerhafte Archivierung** | Historisches Interesse        | Sehr eingeschränkt           | Übergabe / Sortierung durch Behörden   |
| **Anonymisierung**          | Statistiken / Forschung       | Nicht identifizierbare Daten | Unbegrenzt wenn irreversibel           |
| **Löschung**                | Ende des Zyklus               | —                            | Nach Ablauf der Phasen                 |

***

### 🧭 Wie werden sie bestimmt (Methode)

1. **Den Zweck klären**\
   → Was machen Sie tatsächlich mit den Daten? Wofür dienen sie?
2. **Die Phasen kartieren**\
   → aktive Nutzung → Zwischenarchivierung → Anonymisierung/Löschung
3. **Rechtsgrundlagen und Referenzen identifizieren**\
   → Gesetze & branchenspezifische Vorschriften, Beschlüsse der Aufsichtsbehörden, Referenzrahmen, Branchenpraktiken
4. **Eine klare Regel festlegen**\
   → "**X Jahre nach \[Ereignis]**, dann **Archivierung Y Jahre**, dann **Löschung**"\
   → oder "**solange…**, dann **Z Jahre nach** / **Kriterium**"
5. **Die Umsetzung organisieren**\
   → **Automatische** oder **gesteuerte** Bereinigung, Protokollierung, Ausführungsnachweise
6. **Informieren und dokumentieren**\
   → Datenschutzinformation (Art. 13–14), Verarbeitungsverzeichnis (Art. 30), interne Richtlinie

{% hint style="info" %}
Wenn es **keine eindeutige Referenz** gibt, wählen Sie eine dem Zweck **angemessene Dauer** und dokumentieren Sie die Analyse (Accountability).
{% endhint %}

***

### 🧪 Beispiele für Regeln (anzupassen)

| Kontext           | Daten                               | Zusammengefasste Regel                                                     |
| ----------------- | ----------------------------------- | -------------------------------------------------------------------------- |
| B2B-Interessenten | Identität, Kontakt, Opt-in-Nachweis | **3 Jahre** nach letztem aktivem Kontakt, dann **Löschung**                |
| HR – Bewerber     | Lebenslauf, Anschreiben, Gespräche  | **2 Jahre** nach letztem Kontakt mit dem Bewerber, sofern kein Widerspruch |
| Kunden            | Vertrag, Rechnungsstellung          | Vertrag + **5 Jahre** (Nachweis), dann **Archivierung**/**Löschung**       |
| Videoüberwachung  | Bilder                              | **Maximal 30 Tage**, außer bei Vorfall (Beweisverfahren)                   |
| Cookies           | Kennungen, Präferenzen              | Dauer gemäß Banner und **Einwilligungsnachweis**                           |

> Diese Werte variieren je nach anwendbaren Rechtstexten, Ihrer Branche und Ihren Risiken: **Dokumentieren Sie Ihre Entscheidungen**.

***

### 👥 Wer sollte einbezogen werden?

* **Fachverantwortlicher der Verarbeitung**: Operativer Bedarf, auslösende Ereignisse
* **Datenschutzbeauftragter / Rechtsabteilung**: Compliance, anwendbare Rechtstexte, Balance zwischen Rechten und Freiheiten
* **Archiv**: Aufbewahrungsfristen, Sortierung, Übergabe, endgültige Bestimmung
* **CISO / IT**: Bereinigung, Anonymisierung, Zugriffsbeschränkung, Protokolle
* **Auftragsverarbeiter**: Konforme Ausführung gemäß **schriftlichen Anweisungen**

***

### ✅ Die Anwendung kontrollieren (Audits)

* Regelmäßig überprüfen: Angemessenheit der Speicherdauern, Durchführung der Bereinigungen, Zugang zur Archivierung, Anonymisierung
* Vorgänge nachverfolgen: Löschprotokolle, Bereinigungsberichte, Logs
* Bei jeder **Änderung von Zweck, Rechtsgrundlage, Dienstleister** überprüfen…

***

### 🧰 Umsetzung in Dastra

#### 1) Im **Verarbeitungsverzeichnis**

* Geben Sie **eine lesbare Regel** pro Datensatz ein:\
  "_3 Jahre nach letztem aktivem Kontakt (Interessent), dann Löschung_"
* Fügen Sie **das auslösende Kriterium** hinzu (z. B. "Datum der letzten CRM-Aktivität", "Vertragsende")
* Verknüpfen Sie **die Referenzen** (Rechtstext, interner Referenzrahmen)

#### 2) Die Bereinigung **automatisieren/steuern**

* Planen Sie **wiederkehrende Aufgaben** (Überprüfungen, Bereinigungen, Nachweisexporte)
* Nutzen Sie **Workflows** und **Erinnerungen** für Fristen

#### 3) **Nachweise**

* Hinterlegen Sie Löschprotokolle, Bereinigungsberichte, Skripte, Ausführungstickets in der **Dokumentenverwaltung** der Verarbeitung

***

### 🔐 Zwischenarchivierung & Sicherheit

* Zugang einschränken (RBAC, Segmentierung)
* Zugriffe protokollieren
* Logisch trennen (Tresor/Archivbereich)
* Bei Bedarf verschlüsseln
* **Reversibilität** bei Auftragsverarbeitern vorsehen

***

### 🧪 Anonymisierung vs. Pseudonymisierung

* **Anonymisierung**: irreversibel → **außerhalb der DSGVO**, wenn tatsächlich nicht re-identifizierbar
* **Pseudonymisierung**: reversibel mit Schlüssel → **weiterhin personenbezogene Daten**\
  → Dokumentieren Sie die Methode, testen Sie die **Re-Identifizierbarkeit**, berücksichtigen Sie **Hilfsdaten**.

***

### 🤖 KI & Speicherdauern

Für **KI-Systeme** definieren Sie separate Dauern für:

* **Training** (Datensätze, Versionen),
* **Validierung / Test**,
* **Inferenz-Logs** (Rückverfolgbarkeit, Transparenz),
* **Evaluierungsdatensätze** (Bias, Robustheit).

Verknüpfen Sie diese Dauern mit Ihrem **Register der KI-Systeme**, um die Kohärenz **DSGVO / KI-Verordnung** sicherzustellen.

***

### 📚 Nützliche Referenzen

* Branchenspezifische Referenzrahmen, Verhaltenskodizes, Tarifverträge

***

### ▶️ Ressourcen & nächste Schritte

Webinar "Speicherdauern: Wie bestimmt man sie?"

***

{% hint style="success" %}
**Gute Praxis:** Formulieren Sie _umsetzbare_ Regeln ("**X Jahre nach \[Ereignis]** → **Bereinigung** / **Anonymisierung**"), testen Sie diese in einem begrenzten Bereich und verallgemeinern Sie dann.\
Dastra hilft Ihnen bei der **Dokumentation**, **Planung** und dem **Nachweis** der Ausführung.
{% endhint %}
