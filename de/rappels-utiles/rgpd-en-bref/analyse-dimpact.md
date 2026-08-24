---
description: Erfahren Sie, was eine Datenschutz-Folgenabschätzung ist.
---

# Datenschutz-Folgenabschätzung (DSFA / DPIA)

### 📖 Was ist eine DSFA?

Die **Datenschutz-Folgenabschätzung (DSFA)**, vorgesehen durch [Artikel 35 der DSGVO](https://dsgvo-gesetz.de/art-35-dsgvo/), ist ein **Compliance-Mechanismus**, der darauf abzielt:

* **Risiken** für die Rechte und Freiheiten der betroffenen Personen **zu identifizieren und zu minimieren**,
* Die **Compliance** mit der DSGVO **nachzuweisen**,
* Und den **Datenschutz durch Technikgestaltung** von Anfang an zu integrieren (_Privacy by Design_).

> ⚖️ Die DSFA bezieht sich auf die **Risiken für die Personen**, nicht auf die Risiken für die Organisation.

**DSFA = DPIA = PIA = Privacy Impact Assessment = Datenschutz-Folgenabschätzung**

***

### 🧩 Die drei Bestandteile einer DSFA

Eine DSFA ist in drei große Schritte gegliedert:

1. 📝 **Beschreibung der Verarbeitung**\
   → Ziele, Kontext, Stakeholder, Technologien, betroffene Daten.
2. ⚖️ **Bewertung der Notwendigkeit und Verhältnismäßigkeit**\
   → Analyse der rechtlichen Compliance: Zwecke, Rechtsgrundlagen, Betroffenenrechte, Speicherdauern usw.
3. 🔐 **Untersuchung der Risiken und Sicherheitsmaßnahmen**\
   → Identifizierung der Risiken für die Privatsphäre und Bestimmung der technischen und organisatorischen Maßnahmen zur Risikominderung.

> 📘 Die DSFA ist zugleich **juristisch**, **technisch** und **organisatorisch**: Sie bindet das gesamte Projektteam ein.

***

### 🎯 Ziel der DSFA

Die DSFA ermöglicht einer Organisation:

* Ihre **Compliance nachzuweisen** (Accountability-Prinzip),
* **Risiken und Compliance-Kosten vorauszusehen**,
* **Entwurfsentscheidungen** zu dokumentieren,
* Das **Vertrauen** der Nutzer, Kunden oder Beschäftigten **zu gewährleisten**.

***

### 🔍 Wann ist eine DSFA erforderlich?

Eine DSFA ist **verpflichtend**, wenn eine Verarbeitung ein **hohes Risiko** für die Rechte und Freiheiten der betroffenen Personen **mit sich bringt**.

#### Beispiele betroffener Verarbeitungen:

* Intelligente Videoüberwachung,
* Automatische Profilbewertung (Scoring),
* Massenhafte Erhebung von Gesundheitsdaten,
* Einsatz von Biometrie oder KI für personenbezogene Daten.

{% hint style="info" %}
Verarbeitungen, die mindestens **2 der folgenden Kriterien** (EDSA) aufweisen, gelten als mit hohem Risiko behaftet:

* Bewertung oder Scoring,
* Automatisierte Entscheidungsfindung mit rechtlicher Wirkung,
* Systematische Überwachung,
* Sensible Daten,
* Großer Umfang,
* Datenabgleich,
* Schutzbedürftige Personen,
* Innovativer Einsatz (KI, IoT, Big Data),
* Verweigerung eines Rechts oder einer Dienstleistung,
* Datenübermittlungen außerhalb der EU.
{% endhint %}

***

### 🕐 Wann soll sie durchgeführt werden?

Die DSFA muss **vor der Umsetzung der Verarbeitung** durchgeführt werden, idealerweise bereits in der Entwurfsphase.\
Sie stellt eine konkrete Anwendung des Prinzips **Privacy by Design** dar.

Sie muss außerdem:

* **Regelmäßig aktualisiert werden** (alle 3 bis 5 Jahre),
* **Bei wesentlichen Änderungen** der Verarbeitung **überarbeitet werden**,
* In Dastra **mit Ihrem Verarbeitungsverzeichnis verknüpft werden** für eine kontinuierliche Überwachung.

![Ein iterativer Prozess](<../../.gitbook/assets/Ein iterativer Prozess.png>)

> 🔁 Die DSFA ist ein **iterativer Prozess**: Sie begleitet den gesamten Lebenszyklus der Verarbeitung.

***

### ⚙️ Wie wird eine DSFA durchgeführt?

#### 1. Notwendigkeit und Verhältnismäßigkeit der Verarbeitung bewerten

Stellen Sie sich die richtigen Fragen:

* Sind die **Verarbeitungszwecke** bestimmt und legitim?
* Ist die **Rechtsgrundlage** klar?
* Sind die Daten **minimiert**, korrekt und aktuell?
* Sind die **Speicherdauern** begrenzt?
* Sind die **betroffenen Personen** ordnungsgemäß informiert?

#### 2. Den Schutz der Betroffenenrechte prüfen

* Transparente Information, klare Einwilligung, Recht auf Auskunft, Löschung, Widerspruch.
* Verträge mit Auftragsverarbeitern.
* Garantien bei internationalen Datenübermittlungen.
* Vorgesehene Korrekturmaßnahmen im Falle eines Datenschutzvorfalls.

#### 3. Risiken für die Privatsphäre analysieren

Für jedes **befürchtete Ereignis**:

* Die möglichen **Auswirkungen** auf die betroffenen Personen identifizieren (Beeinträchtigung der Privatsphäre, Ruf, Diskriminierung…).
* Die **Schwere** und **Eintrittswahrscheinlichkeit** des Risikos einschätzen.
* Die **vorhandenen oder geplanten Schutzmaßnahmen** bestimmen.
* Das **Restrisiko** bewerten und gegebenenfalls **ergänzende Maßnahmen** vorschlagen.

{% hint style="success" %}
💡 Endziel: Ein **akzeptables Restrisiko** erreichen, das dokumentiert und begründet ist.
{% endhint %}

***

### 🧠 Wer sollte einbezogen werden?

| Stakeholder                 | Rolle in der DSFA                                                   |
| --------------------------- | ------------------------------------------------------------------- |
| **Verantwortlicher**        | Trägt die Verantwortung für die DSFA und steuert deren Durchführung |
| **Datenschutzbeauftragter** | Berät, validiert die Methodik und bewertet die Restrisiken          |
| **CISO / IT-Leitung**       | Bringt die technische Expertise und Sicherheitsmaßnahmen ein        |
| **Fachabteilungen**         | Liefern die operativen Details der Verarbeitung                     |
| **Auftragsverarbeiter**     | Übermitteln die für die Bewertung erforderlichen Informationen      |
| **Betroffene Personen**     | Können in bestimmten Fällen konsultiert oder vertreten werden       |

> 👥 Die DSFA ist ein kollaborativer Ansatz – sie bindet sowohl Juristen als auch operative Mitarbeiter ein.

***

### 🤖 DSFA und künstliche Intelligenz

Die **KI-Verordnung** führt eine spezifische Pflicht zur **Dokumentation und Bewertung von KI-Systemen** mit hohem Risiko ein.\
Organisationen müssen darin aufnehmen:

* Die Herkunft der Trainingsdaten,
* Robustheits- und Bias-Tests,
* Vorgesehene menschliche Kontrollen,
* Transparenzmaßnahmen.

Dastra ermöglicht es, jede **DSFA** mit einem **KI-System** zu verknüpfen, um eine **übergreifende Compliance DSGVO / KI-Verordnung** sicherzustellen.

***

### 🧰 Bewährte Praktiken in Dastra

* Zentralisieren Sie alle Ihre DSFAs im **Modul "Verarbeitungsverzeichnis"**,
* Nutzen Sie die **vordefinierten Risikomodelle** (EDSA, Aufsichtsbehörden, ISO 29134),
* Arbeiten Sie mit den Teams über **Kommentare und Workflows** zusammen,
* Exportieren Sie Ihre DSFAs als **PDF** für Audits,
* Planen Sie **automatische Überprüfungserinnerungen**.

{% hint style="success" %}
💡 Dastra führt Sie Schritt für Schritt durch die Durchführung der DSFA, dank eines interaktiven Modells und bereits integrierter Bibliotheken von Bedrohungen und Maßnahmen.
{% endhint %}

***

### 📘 Weiterführende Informationen

🎥 Webinar "Wie Sie die DSFA-Phase mit einem Tool angehen"
