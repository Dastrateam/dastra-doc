---
description: >-
  Der KI-Assistent von Dastra erstellt und ergänzt Elemente Ihres Mandanten aus
  einfachen Beschreibungen, mit Agenten und einem MCP-Server.
---

# KI-Assistent

Mit dem KI-Assistenten von Dastra erstellen und ergänzen Sie Elemente Ihres Mandanten aus einfachen Textbeschreibungen. Er basiert auf generativen KI-Modellen, die auf Azure in Frankreich und im Europäischen Wirtschaftsraum gehostet werden, ohne dass Daten Ihrer Organisation zum Training dieser Modelle verwendet werden.

Die Verfügbarkeit des KI-Assistenten hängt vom Tarif Ihrer Organisation ab, Modul für Modul. In einem Modul, das Ihr Tarif nicht enthält, sind die KI-Schaltflächen ausgegraut. Um den Umfang Ihres Tarifs zu ändern, wenden Sie sich an unser Team.

## KI als Ausgangspunkt, nicht als endgültige Antwort

Der KI-Assistent ist darauf ausgelegt, **Ihre Compliance-Arbeit zu beschleunigen**, nicht menschliche Expertise zu ersetzen. Jeder vom Assistenten erstellte Inhalt, sei es eine Verarbeitungsbeschreibung, eine Datenschutzerklärung oder eine Compliance-Analyse, ist **ein Vorschlag, der vor der Verwendung von einer qualifizierten Person geprüft und bestätigt werden muss**.

Insbesondere gilt:

{% hint style="warning" %}
**KI-generierte Inhalte stellen keine Rechtsberatung dar.** Sie können das Urteil einer Fachperson für Datenschutz oder einer Rechtsberatung nicht ersetzen.

**Compliance-Bewertungen sind Analysehilfen.** Bewertungen und Empfehlungen der KI beruhen ausschließlich auf den in Ihrem Mandanten erfassten Informationen. Sie spiegeln die Qualität dieser Dokumentation wider, nicht eine unabhängige rechtliche Einschätzung.

**Sie behalten die Kontrolle.** Kein KI-Ergebnis wird automatisch angewendet oder mitgeteilt. Jedes Ergebnis erfordert eine bewusste menschliche Handlung, bevor es verwendet wird.
{% endhint %}

## Datenschutz und Vertraulichkeit

Die Daten Ihrer Organisation werden niemals zum Training von KI-Modellen verwendet. Die von Dastra genutzten Modelle werden auf der Infrastruktur von Microsoft Azure in Frankreich gehostet, mit vertraglichen Garantien, die Ihre Daten von jedem Training und jeder Weitergabe an Dritte ausschließen. Alle Einzelheiten finden Sie unter [Funktionsweise](how-it-works.md).

## Wobei der KI-Assistent Sie unterstützen kann

Der Assistent steht in mehreren Modulen der Plattform zur Verfügung:

* **Verarbeitungstätigkeiten**: Beschreibungen, Datenkategorien, Sicherheitsmaßnahmen, Datenschutzerklärungen und Compliance-Analysen erstellen
* **KI-Systeme**: Beschreibungen, Hinweise und Risikoanalysen erstellen
* **Fragebögen**: KI-gestützte Antworten auf DSFA und Risikoanalysen erstellen
* **Betroffenenanfragen**: Antworten in mehreren Sprachen und Sprachregistern entwerfen
* **Assets und Stakeholder**: strukturierte Einträge aus einer URL oder einer freien Beschreibung erstellen
* **Verträge**: Metadaten aus einem importierten Dokument extrahieren
* **Eigene Dokumente und Berichte**: Inhalte nach Ihren eigenen Anweisungen erstellen

Eine Schritt-für-Schritt-Anleitung zu jeder Funktion finden Sie unter [Anwendungsfälle](use-cases.md).

## Dastra AI, Agenten und der MCP-Server

Über die Erstellung von Inhalten hinaus bietet Dastra einen Gesprächsassistenten, **Dastra AI**, den Sie über das Dashboard oder über die Schaltfläche **Dastra AI öffnen** unten rechts auf dem Bildschirm befragen. Sie können außerdem eigene [Agenten](agents/README.md) erstellen, im Chat oder autonom, und Ihre KI-Werkzeuge über den [MCP-Server](mcp.md) mit Dastra verbinden. Diese Funktionen hängen vom Tarif Ihrer Organisation und von den Berechtigungen der einzelnen Nutzer ab.

Alle KI-Funktionen teilen sich das monatliche Kontingent an KI-Credits, das unter [Funktionsweise](how-it-works.md#ki-credits-und-kontingente) beschrieben ist.

## Beta-Funktionen

Einige KI-Funktionen werden als Beta veröffentlicht: Sie sind einsatzbereit, werden aber auf Grundlage des Feedbacks der Nutzer weiter verfeinert. Beta-Funktionen sind in der Oberfläche eindeutig gekennzeichnet.

Bei der Nutzung einer Beta-Funktion gilt:

* Die Ergebnisse können weniger konsistent sein als bei stabilen Funktionen und sollten mit besonderer Sorgfalt behandelt werden.
* Die zugrunde liegenden Prompts und Kriterien werden aktiv verbessert, sodass sich die Ergebnisse zwischen den Versionen ändern können.
* Feedback ist willkommen und hilft Dastra, die Funktion zu verbessern. Nutzen Sie dafür die Feedback-Option in der Oberfläche.

{% hint style="warning" %}
Beta-Funktionen sollten niemals die alleinige Grundlage einer Compliance-Entscheidung sein. Sie sollen eine gründliche menschliche Prüfung unterstützen, nicht ersetzen.
{% endhint %}

**Derzeit in der Beta**: die Compliance-Analyse von Verarbeitungstätigkeiten und die Compliance-Analyse von KI-Systemen.

***

{% content-ref url="how-it-works.md" %}
[Funktionsweise](how-it-works.md)
{% endcontent-ref %}

{% content-ref url="use-cases.md" %}
[Anwendungsfälle](use-cases.md)
{% endcontent-ref %}

{% content-ref url="faq.md" %}
[Häufig gestellte Fragen](faq.md)
{% endcontent-ref %}

{% content-ref url="agents/README.md" %}
[Dastra-KI-Agenten](agents/README.md)
{% endcontent-ref %}

{% content-ref url="mcp.md" %}
[Der MCP-Server](mcp.md)
{% endcontent-ref %}
