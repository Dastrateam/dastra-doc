---
description: >-
  Häufig gestellte Fragen zum KI-Assistenten von Dastra: Datenschutz,
  Zuverlässigkeit, Konfiguration und Konformität mit dem KI-Verordnung.
---

# Häufig gestellte Fragen

## Datenschutz und Daten

**Werden meine Daten zum Trainieren von KI-Modellen verwendet?**

Nein. Die von Dastra verwendeten Modelle sind vortrainiert und werden auf Microsoft Azure gehostet. Ihre Daten werden niemals zum Trainieren, Feinabstimmen oder Verbessern der Basismodelle verwendet, weder von Microsoft, OpenAI, Mistral noch von Dritten. Diese Garantie ist vertraglich festgelegt.

***

**Werden die Daten meines Mandanten ohne mein Wissen an das Modell gesendet?**

Nein. Dastra übermittelt nur die Informationen, die für die angeforderte Erstellung unbedingt erforderlich sind: den von Ihnen eingegebenen Text und gegebenenfalls die Felder des Objekts, an dem Sie arbeiten (Verarbeitungstätigkeit, KI-System, Anfrage zur Ausübung von Rechten usw.). Andere Einträge Ihres Mandanten, Ihre Zugangsdaten und Sitzungsmetadaten sind niemals enthalten. Die einzige Ausnahme: Wenn Sie beim Erstellen einer Verarbeitungstätigkeit die Option **Vorhandene Komponenten nutzen** aktivieren, werden die Bezeichnungen vorhandener Sicherheitsmaßnahmen, Assets und Datenfelder gesendet, damit der Assistent sie wiederverwenden kann. Eine Aufschlüsselung nach Funktion finden Sie auf der Seite [Funktionsweise](how-it-works.md).

***

**Wo werden die von Dastra verwendeten KI-Modelle gehostet?**

Für die Familien OpenAI, Mistral und Open Source werden die Modelle auf der Infrastruktur von Microsoft Azure in Frankreich gehostet. Ihre Daten laufen nicht über die eigenen Server von OpenAI oder Mistral. Dastra nutzt ausschließlich verwaltete Azure-Dienste.

Wenn Sie einen **benutzerdefinierten KI-Anbieter** mit Ihrem eigenen API-Schlüssel konfigurieren, hängt das Hosting vom gewählten Anbieter ab.

***

**Werden meine Prompts nach der Erstellung aufbewahrt?**

Azure-Modelle sind zustandslos: Prompts und Ergebnisse werden zwischen zwei Anfragen nicht im Modell gespeichert. Sie werden auch nicht für eine kommerzielle Wiederverwendung protokolliert.

**Ausnahme:** Azure unterhält einen automatisierten Mechanismus zur Erkennung von Missbrauch. Wird ein Inhalt gemeldet, kann eine Stichprobe zu Prüfzwecken vorübergehend in einer kundenspezifisch isolierten Umgebung aufbewahrt werden. Für Ressourcen, die im EWR bereitgestellt werden (was bei Dastra der Fall ist), befinden sich auch die beteiligten menschlichen Prüfer im EWR. Diese Aufbewahrung bleibt die Ausnahme.

***

**Wer kann die KI-Aufrufe in meiner Organisation einsehen?**

Die Inhaber der Organisation können das Nutzungsprotokoll der KI (Verlauf von 90 Tagen) unter **Organisationseinstellungen** > **KI-Assistent**, Karte **AI usage**, Tab **Logs (90 days)** einsehen. Es zeigt Datum, Status, Art des Vorgangs, Modellname, verbrauchte Credits, Dauer und den Nutzer, der die Erstellung ausgelöst hat. Der Inhalt der Prompts und der Antworten wird nicht angezeigt.

***

**Ist der KI-Assistent durch den AVV (Auftragsverarbeitungsvertrag) von Dastra abgedeckt?**

Ja. Die Nutzung des KI-Assistenten fällt unter den bestehenden Vertragsrahmen zwischen Ihrer Organisation und Dastra. Microsoft Azure handelt als Unterauftragsverarbeiter und ist an die vertraglichen Datenschutzverpflichtungen von Azure gebunden. Weitere Einzelheiten finden Sie in Ihrem Dastra-AVV, oder wenden Sie sich an unser Team.

***

## Qualität und Zuverlässigkeit

**Kann man den von der KI erstellten Ergebnissen vertrauen?**

Die erstellten Ergebnisse sind Ausgangsvorschläge, keine endgültigen Antworten. Sie beschleunigen Ihre Dokumentationsarbeit, ersetzen aber nicht das Urteil von Fachleuten. Alle erstellten Inhalte müssen vor der Verwendung von einer qualifizierten Person geprüft und bestätigt werden, insbesondere Compliance-Analysen, Datenschutzerklärungen und Antworten auf Anfragen betroffener Personen.

***

**Was ist eine Beta-Funktion?**

Einige KI-Funktionen werden als Beta veröffentlicht: Sie sind einsatzbereit, werden aber weiter verfeinert. Die Ergebnisse können weniger konsistent sein als bei stabilen Funktionen und sollten mit besonderer Sorgfalt behandelt werden.

Derzeit in der Beta: die Compliance-Analyse von Verarbeitungstätigkeiten und die Compliance-Analyse von KI-Systemen.

***

**Kann die KI bei rechtlichen Fragen Fehler machen?**

Ja. Der KI-Assistent ist kein Rechtsanwalt. Erstellte Inhalte wie Compliance-Analysen, Hinweise und Risikobewertungen sind eine Entscheidungshilfe auf Grundlage der in Ihrem Mandanten erfassten Informationen. Sie stellen keine Rechtsberatung dar und können die Expertise eines Datenschutzbeauftragten oder einer spezialisierten Rechtsberatung nicht ersetzen.

***

## Konfiguration und Zugriff

**Wie wähle ich das verwendete KI-Modell aus?**

Der Inhaber der Organisation öffnet **Organisationseinstellungen** > **KI-Assistent** und wählt die **Familie von KI-Modellen**: OpenAI (Standard), Mistral, Open Source oder den benutzerdefinierten KI-Anbieter (im Feld **Maßgeschneiderte KI-Modelle**). Für jede Familie werden je nach Komplexität der Aufgabe automatisch drei Modellstufen verwendet (Fast, Smart, Large context).

***

**Kann ich meinen eigenen KI-Anbieter anbinden?**

Ja, mit der Familie des benutzerdefinierten KI-Anbieters. Jeder Anbieter, der mit dem OpenAI-API-Standard kompatibel ist, kann angebunden werden: OpenAI, Anthropic (Claude), Google (Gemini), Mistral, Azure AI Foundry oder ein selbst gehostetes LLM. Konfigurieren Sie Ihre Zugangsdaten unter **Organisationseinstellungen** > **KI-Assistent** im Block **Anmeldedaten des KI-Anbieters**.

{% hint style="warning" %}
Bei einem benutzerdefinierten KI-Anbieter gelten die in dieser Dokumentation beschriebenen Azure-Garantien nicht mehr. Die Daten unterliegen der Richtlinie Ihres Anbieters.
{% endhint %}

***

**Kann ich den KI-Assistenten für meine Organisation deaktivieren?**

Die Anwendung hat keinen Schalter, um den KI-Assistenten zu deaktivieren: Seine Verfügbarkeit hängt vom Tarif Ihrer Organisation ab. Die KI-Funktionen werden Modul für Modul freigeschaltet (Verarbeitungstätigkeiten und Referenzdaten, Compliance, Risiken, Datenschutzvorfälle, Fragebögen, Verträge, Betroffenenanfragen, Analysen). In einem Modul, das Ihr Tarif nicht enthält, sind die KI-Schaltflächen ausgegraut. Um diesen Umfang zu ändern, wenden Sie sich an unser Team.

Eine Einstellung liegt in der Hand der Administratoren: die **Automatische KI-Analyse von Beweismitteln**, standardmäßig aktiviert, die Sie pro Mandant unter **Mandanteneinstellungen** > **Compliance** ausschalten.

***

**Ist der KI-Assistent in allen Dastra-Tarifen verfügbar?**

Nein. Der KI-Assistent, jede seiner Funktionen pro Modul, KI-Agenten und der MCP-Server sind Tarifoptionen. Wenden Sie sich an unser Team, um den Umfang Ihres Tarifs zu erfahren.

***

**Was sind KI-Credits?**

KI-Credits sind die Maßeinheit für den Verbrauch des KI-Assistenten in Ihrer Organisation. Jeder Aufruf einer KI-Funktion verbraucht eine bestimmte Anzahl Credits, die von der verwendeten Modellstufe (Fast, Smart oder Large context) und der Menge der verarbeiteten Daten abhängt.

Die Inhaber der Organisation sehen den aktuellen Verbrauch und das verbleibende Guthaben unter **Organisationseinstellungen** > **KI-Assistent**, Karte **Anwendung** ([direkter Link](https://app.dastra.eu/general-settings/ai)).

***

**Was passiert, wenn meine Organisation ihr Credit-Kontingent erreicht?**

Wenn das Kontingent erreicht ist, werden die KI-Funktionen bis zur nächsten Erneuerung vorübergehend ausgesetzt. Ihr Mandant und Ihre Daten bleiben vollständig zugänglich: Nur die KI-Erstellung ist deaktiviert.

Um Ihr Kontingent zu erhöhen oder eine vorzeitige Erneuerung zu beantragen, wenden Sie sich an unser Team.

***

**Gilt das Credit-System auch bei einem benutzerdefinierten KI-Anbieter?**

Nein. Wenn Ihre Organisation einen **benutzerdefinierten KI-Anbieter** konfiguriert, ist das Credit-System von Dastra deaktiviert: Es werden keine Credits gezählt. Der Verbrauch wird direkt von Ihrem Anbieter nach dessen eigenen Abrechnungsbedingungen verwaltet.

***

## KI-Verordnung (EU-Verordnung 2024/1689)

**Unterliegt der KI-Assistent von Dastra dem KI-Verordnung?**

Ja. Der KI-Assistent von Dastra fällt unter die Definition eines KI-Systems im Sinne des KI-Verordnunges (EU 2024/1689). Je nach genutzten Funktionen wird er überwiegend als **System mit begrenztem Risiko** eingestuft, was Transparenzpflichten (Art. 50) nach sich zieht, wenn erstellte Inhalte für natürliche Personen bestimmt sind.

***

**Muss ich betroffene Personen darüber informieren, dass ich KI für die Beantwortung ihrer Anfragen genutzt habe?**

Nicht aufgrund einer strikten Pflicht des KI-Verordnunges, aber es wird als bewährte Vorgehensweise dringend empfohlen.

Artikel 50 Absatz 1 des KI-Verordnunges betrifft KI-Systeme, die **direkt mit** natürlichen Personen **interagieren**. In Dastra ist das nicht der Fall: Ein menschlicher Nutzer (Datenschutzbeauftragter, Rechtsberatung) erstellt den Text, prüft ihn, bestätigt ihn und sendet ihn selbst an die betroffene Person. Es gibt keine direkte Interaktion zwischen dem KI-System und dem Endempfänger, sodass die strikte Pflicht aus Art. 50 Abs. 1 nicht gilt.

{% hint style="info" %}
Die Entwurfsleitlinien des KI-Büros (2025 zur Konsultation der Beteiligten veröffentlicht) bestätigen diese Auslegung ausdrücklich: _„Direct interaction excludes indirect or mediated human interaction where the person is exposed to AI outputs without directly interacting with the system, **for example if customer service representatives use AI assistance tools to help them communicate with natural persons** or if the AI output is not made available to the person by the AI system itself, but by another person disseminating the content.“_ (Abschnitt 3.1.1). Der Anwendungsfall von Dastra entspricht genau diesem Szenario.

Hinweis: Die Pflichten aus Artikel 50 gelten seit dem **2. August 2026**. Die Europäische Kommission hat im Juli 2026 endgültige Leitlinien verabschiedet, die diese Analyse ergänzen können.
{% endhint %}

Dennoch bleibt die Information der betroffenen Person darüber, dass eine Antwort KI-gestützt erstellt wurde, eine **bewährte Vorgehensweise** nach dem Grundsatz von Treu und Glauben und Transparenz der DSGVO (Art. 5 Abs. 1 Buchst. a). Dastra fügt diesen Hinweis nicht automatisch hinzu: Wenn Ihre Organisation ihn aufnehmen möchte, liegt es an Ihnen, dies vor dem Versand zu tun.

***

**Ist Dastra Anbieter oder Betreiber im Sinne des KI-Verordnunges?**

Beides, je nach Anwendungsfall. Wenn Sie die Standardmodelle verwenden (OpenAI, Mistral, Open Source über Azure), ist Dastra der **Anbieter** des KI-Systems und Ihre Organisation der **Betreiber**. Wenn Sie über die Familie des benutzerdefinierten KI-Anbieters Ihren eigenen Anbieter anbinden, handelt Dastra ausschließlich als Compliance-Werkzeug. Ihre Organisation übernimmt dann in Bezug auf ihr eigenes Modell die Rolle des Anbieters und/oder Betreibers.
