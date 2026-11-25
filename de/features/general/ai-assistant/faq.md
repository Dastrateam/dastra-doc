---
description: >-
  Häufig gestellte Fragen zu Dastra AI: Datenschutz, Zuverlässigkeit,
  Konfiguration und KI-Verordnung.
---
# Häufig gestellte Fragen

## Datenschutz und Daten

{% hint style="warning" %}
**Bleu-Angebot.** Die Antworten dieses Abschnitts, die Azure beschreiben (Hosting der Modelle, kein Training, Speicherung von Prompts, Missbrauchserkennung, Unterauftragsverarbeiter zweiter Stufe), gelten nicht für [Bleu](../../../security/bleu.md): Die KI-Funktionen werden dort von Mistral AI ausgeführt, einem französischen Unternehmen außerhalb des Bleu-Perimeters. Zu den geltenden vertraglichen Zusagen wenden Sie sich an Ihren Dastra-Vertrag oder an unser Team.
{% endhint %}

<details>

<summary>Werden meine Daten zum Trainieren von KI-Modellen verwendet?</summary>

Nein. Die von Dastra verwendeten Modelle sind vortrainiert und werden auf Microsoft Azure gehostet. Ihre Daten werden niemals zum Trainieren, Feinabstimmen oder Verbessern der Basismodelle verwendet, weder von Microsoft, OpenAI, Mistral noch von Dritten. Diese Garantie ist vertraglich festgelegt.

</details>

<details>

<summary>Werden die Daten meines Mandanten ohne mein Wissen an das Modell gesendet?</summary>

Nein. Dastra übermittelt nur die Informationen, die für die angeforderte Erstellung unbedingt erforderlich sind: den von Ihnen eingegebenen Text und gegebenenfalls die Felder des Objekts, an dem Sie arbeiten (Verarbeitungstätigkeit, KI-System, Anfrage zur Ausübung von Rechten usw.). Andere Einträge Ihres Mandanten, Ihre Zugangsdaten und Sitzungsmetadaten sind niemals enthalten. Die einzige Ausnahme: Wenn Sie beim Erstellen einer Verarbeitungstätigkeit die Option **Vorhandene Komponenten nutzen** aktivieren, werden die Bezeichnungen vorhandener Sicherheitsmaßnahmen, Assets und Datenfelder gesendet, damit der Assistent sie wiederverwenden kann. Eine Aufschlüsselung nach Funktion finden Sie auf der Seite [Funktionsweise](how-it-works.md).

</details>

<details>

<summary>Wo werden die von Dastra verwendeten KI-Modelle gehostet?</summary>

Für die Familien OpenAI, Mistral und Open Source werden die Modelle auf der Infrastruktur von Microsoft Azure in Frankreich gehostet. Ihre Daten laufen nicht über die eigenen Server von OpenAI oder Mistral. Dastra nutzt ausschließlich verwaltete Azure-Dienste.

Wenn Sie einen **benutzerdefinierten KI-Anbieter** mit Ihrem eigenen API-Schlüssel konfigurieren, hängt das Hosting vom gewählten Anbieter ab.

</details>

<details>

<summary>Werden meine Prompts nach der Erstellung aufbewahrt?</summary>

Azure-Modelle sind zustandslos: Prompts und Ergebnisse werden zwischen zwei Anfragen nicht im Modell gespeichert. Sie werden auch nicht für eine kommerzielle Wiederverwendung protokolliert.

**Ausnahme:** Azure unterhält einen automatisierten Mechanismus zur Erkennung von Missbrauch. Wird ein Inhalt gemeldet, kann eine Stichprobe zu Prüfzwecken vorübergehend in einer kundenspezifisch isolierten Umgebung aufbewahrt werden. Für Ressourcen, die im EWR bereitgestellt werden (was bei Dastra der Fall ist), befinden sich auch die beteiligten menschlichen Prüfer im EWR. Diese Aufbewahrung bleibt die Ausnahme.

</details>

<details>

<summary>Wer kann die KI-Aufrufe in meiner Organisation einsehen?</summary>

Die Inhaber der Organisation können das Nutzungsprotokoll der KI (Verlauf von 90 Tagen) unter **Organisationseinstellungen** > **KI-Assistent**, Karte **AI usage**, Tab **Logs (90 days)** einsehen. Es zeigt Datum, Status, Art des Vorgangs, Modellname, verbrauchte Credits, Dauer und den Nutzer, der die Erstellung ausgelöst hat. Der Inhalt der Prompts und der Antworten wird nicht angezeigt.

</details>

<details>

<summary>Ist der KI-Assistent durch den AVV (Auftragsverarbeitungsvertrag) von Dastra abgedeckt?</summary>

Ja. Die Nutzung des KI-Assistenten fällt unter den bestehenden Vertragsrahmen zwischen Ihrer Organisation und Dastra. Microsoft Azure handelt als Unterauftragsverarbeiter und ist an die vertraglichen Datenschutzverpflichtungen von Azure gebunden. Weitere Einzelheiten finden Sie in Ihrem Dastra-AVV, oder wenden Sie sich an unser Team.

</details>

***

## Qualität und Zuverlässigkeit

<details>

<summary>Kann man den von der KI erstellten Ergebnissen vertrauen?</summary>

Die erstellten Ergebnisse sind Ausgangsvorschläge, keine endgültigen Antworten. Sie beschleunigen Ihre Dokumentationsarbeit, ersetzen aber nicht das Urteil von Fachleuten. Alle erstellten Inhalte müssen vor der Verwendung von einer qualifizierten Person geprüft und bestätigt werden, insbesondere Compliance-Analysen, Datenschutzerklärungen und Antworten auf Anfragen betroffener Personen.

</details>

<details>

<summary>Was ist eine Beta-Funktion?</summary>

Einige KI-Funktionen werden als Beta veröffentlicht: Sie sind einsatzbereit, werden aber weiter verfeinert. Die Ergebnisse können weniger konsistent sein als bei stabilen Funktionen und sollten mit besonderer Sorgfalt behandelt werden.

Derzeit in der Beta ist die KI-Compliance-Analyse (Schaltfläche **KI-Analyse**), verfügbar für Verarbeitungstätigkeiten, KI-Systeme, Verträge, Assets, Stakeholder und Zusammenfassungen von Fragebogenantworten.

</details>

<details>

<summary>Kann die KI bei rechtlichen Fragen Fehler machen?</summary>

Ja. Der KI-Assistent ist kein Rechtsanwalt. Erstellte Inhalte wie Compliance-Analysen, Hinweise und Risikobewertungen sind eine Entscheidungshilfe auf Grundlage der in Ihrem Mandanten erfassten Informationen. Sie stellen keine Rechtsberatung dar und können die Expertise eines Datenschutzbeauftragten oder einer spezialisierten Rechtsberatung nicht ersetzen.

</details>

***

## Konfiguration und Zugriff

<details>

<summary>Wie wähle ich das verwendete KI-Modell aus?</summary>

Der Inhaber der Organisation öffnet **Organisationseinstellungen** > **KI-Assistent** und wählt die **Familie von KI-Modellen**: OpenAI (Standard), Mistral, Open Source oder den benutzerdefinierten KI-Anbieter (im Feld **Maßgeschneiderte KI-Modelle**). Für jede Familie werden je nach Komplexität der Aufgabe automatisch drei Modellstufen verwendet (Fast, Smart, Large context).

</details>

<details>

<summary>Kann ich meinen eigenen KI-Anbieter anbinden?</summary>

Ja, mit der Familie des benutzerdefinierten KI-Anbieters. Jeder Anbieter, der mit dem OpenAI-API-Standard kompatibel ist, kann angebunden werden: OpenAI, Anthropic (Claude), Google (Gemini), Mistral, Azure AI Foundry oder ein selbst gehostetes LLM. Konfigurieren Sie Ihre Zugangsdaten unter **Organisationseinstellungen** > **KI-Assistent** im Block **Anmeldedaten des KI-Anbieters**. Der benutzerdefinierte Anbieter gilt für die Erstellungsfunktionen des KI-Assistenten, nicht für Dastra AI (Chat), die Agenten oder den MCP-Server.

{% hint style="warning" %}
Bei einem benutzerdefinierten KI-Anbieter gelten die in dieser Dokumentation beschriebenen Azure-Garantien nicht mehr. Die Daten unterliegen der Richtlinie Ihres Anbieters.
{% endhint %}

</details>

<details>

<summary>Kann ich den KI-Assistenten für meine Organisation deaktivieren?</summary>

Die Anwendung hat keinen Schalter, um den KI-Assistenten zu deaktivieren: Seine Verfügbarkeit hängt vom Tarif Ihrer Organisation ab. Die KI-Funktionen werden Modul für Modul freigeschaltet (Verarbeitungstätigkeiten und Referenzdaten, Compliance, Risiken, Datenschutzvorfälle, Fragebögen, Verträge, Betroffenenanfragen, Analysen). In einem Modul, das Ihr Tarif nicht enthält, sind die KI-Schaltflächen ausgegraut. Um diesen Umfang zu ändern, wenden Sie sich an unser Team. Um Dastra AI einzelnen Nutzern vorzuenthalten, entfernen Sie die Berechtigung **AI Assistant** aus deren Rolle.

Eine Einstellung liegt in der Hand der Administratoren: die **Automatische KI-Analyse von Beweismitteln**, standardmäßig aktiviert, die Sie pro Mandant unter **Mandanteneinstellungen** > **Compliance** ausschalten.

</details>

<details>

<summary>Ist der KI-Assistent in allen Dastra-Tarifen verfügbar?</summary>

Nein. Der KI-Assistent, jede seiner Funktionen pro Modul, der Bearbeitungsmodus, eigene KI-Agenten und der MCP-Server sind Tarifoptionen. Wenden Sie sich an unser Team, um den Umfang Ihres Tarifs zu erfahren.

</details>

<details>

<summary>Was sind KI-Credits?</summary>

KI-Credits sind die Maßeinheit für den Verbrauch des KI-Assistenten in Ihrer Organisation. Jeder Aufruf einer KI-Funktion verbraucht Credits aus dem monatlichen Kontingent der Organisation, das mit den Unterhaltungen mit Dastra AI und den Ausführungen von Agenten geteilt wird. Siehe [KI-Credits und Kontingente](how-it-works.md#ki-credits-und-kontingente).

Die Inhaber der Organisation sehen den aktuellen Verbrauch und das verbleibende Guthaben unter **Organisationseinstellungen** > **KI-Assistent**, Karte **Anwendung** ([direkter Link](https://app.dastra.eu/general-settings/ai)).

</details>

<details>

<summary>Was passiert, wenn meine Organisation ihr Credit-Kontingent erreicht?</summary>

Wenn das Kontingent erreicht ist, werden die KI-Funktionen bis zur nächsten Erneuerung vorübergehend ausgesetzt. Ihr Mandant und Ihre Daten bleiben vollständig zugänglich: Nur die KI-Erstellung ist deaktiviert.

Um Ihr Kontingent zu erhöhen oder eine vorzeitige Erneuerung zu beantragen, wenden Sie sich an unser Team.

</details>

<details>

<summary>Gilt das Credit-System auch bei einem benutzerdefinierten KI-Anbieter?</summary>

Nein. Wenn Ihre Organisation einen **benutzerdefinierten KI-Anbieter** konfiguriert, ist das Credit-System von Dastra für die Erstellungsfunktionen des KI-Assistenten deaktiviert: Es werden keine Credits gezählt. Der Verbrauch wird direkt von Ihrem Anbieter nach dessen eigenen Abrechnungsbedingungen verwaltet. Dastra AI und die Agenten nutzen die Modelle von Dastra: Ihre Nachrichten verbrauchen weiterhin das Credit-Kontingent und werden gesperrt, sobald es erreicht ist.

</details>

***

## KI-Verordnung (EU-Verordnung 2024/1689)

<details>

<summary>Unterliegt der KI-Assistent von Dastra der KI-Verordnung?</summary>

Ja. Der KI-Assistent von Dastra fällt unter die Definition eines KI-Systems im Sinne der KI-Verordnung (EU 2024/1689). Je nach genutzten Funktionen wird er überwiegend als **System mit begrenztem Risiko** eingestuft, was Transparenzpflichten (Art. 50) nach sich zieht, wenn erstellte Inhalte für natürliche Personen bestimmt sind.

</details>

<details>

<summary>Muss ich betroffene Personen darüber informieren, dass ich KI für die Beantwortung ihrer Anfragen genutzt habe?</summary>

Nicht aufgrund einer strikten Pflicht der KI-Verordnung, aber es wird als bewährte Vorgehensweise dringend empfohlen.

Artikel 50 Absatz 1 der KI-Verordnung betrifft KI-Systeme, die **direkt mit** natürlichen Personen **interagieren**. In Dastra ist das nicht der Fall: Ein menschlicher Nutzer (Datenschutzbeauftragter, Rechtsberatung) erstellt den Text, prüft ihn, bestätigt ihn und sendet ihn selbst an die betroffene Person. Es gibt keine direkte Interaktion zwischen dem KI-System und dem Endempfänger, sodass die strikte Pflicht aus Art. 50 Abs. 1 nicht gilt.

{% hint style="info" %}
Die Entwurfsleitlinien des KI-Büros (2025 zur Konsultation der Beteiligten veröffentlicht) bestätigen diese Auslegung ausdrücklich: _„Direct interaction excludes indirect or mediated human interaction where the person is exposed to AI outputs without directly interacting with the system, **for example if customer service representatives use AI assistance tools to help them communicate with natural persons** or if the AI output is not made available to the person by the AI system itself, but by another person disseminating the content.“_ (Abschnitt 3.1.1). Der Anwendungsfall von Dastra entspricht genau diesem Szenario.

Hinweis: Die Pflichten aus Artikel 50 gelten seit dem **2. August 2026**. Die Europäische Kommission hat im Juli 2026 endgültige Leitlinien verabschiedet, die diese Analyse ergänzen können.
{% endhint %}

Dennoch bleibt die Information der betroffenen Person darüber, dass eine Antwort KI-gestützt erstellt wurde, eine **bewährte Vorgehensweise** nach dem Grundsatz von Treu und Glauben und Transparenz der DSGVO (Art. 5 Abs. 1 Buchst. a). Dastra fügt diesen Hinweis nicht automatisch hinzu: Wenn Ihre Organisation ihn aufnehmen möchte, liegt es an Ihnen, dies vor dem Versand zu tun.

</details>

<details>

<summary>Ist Dastra Anbieter oder Betreiber im Sinne der KI-Verordnung?</summary>

Beides, je nach Anwendungsfall. Wenn Sie die Standardmodelle verwenden (OpenAI, Mistral, Open Source über Azure), ist Dastra der **Anbieter** des KI-Systems und Ihre Organisation der **Betreiber**. Wenn Sie über die Familie des benutzerdefinierten KI-Anbieters Ihren eigenen Anbieter anbinden, handelt Dastra ausschließlich als Compliance-Werkzeug. Ihre Organisation übernimmt dann in Bezug auf ihr eigenes Modell die Rolle des Anbieters und/oder Betreibers.

</details>
