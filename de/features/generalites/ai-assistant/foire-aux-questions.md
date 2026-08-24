# Häufig gestellte Fragen

### Vertraulichkeit und Daten

**Werden meine Daten zum Trainieren der KI-Modelle verwendet?**

Nein. Die von Dastra verwendeten Modelle sind vortrainiert und werden auf Microsoft Azure gehostet. Ihre Daten werden niemals zum Trainieren, Feintuning oder Verbessern der Basismodelle verwendet, weder von Microsoft, OpenAI, Mistral noch von Dritten. Diese Garantie ist vertraglich festgelegt.

***

**Werden die Daten meines Workspace ohne mein Wissen an das Modell übermittelt?**

Nein. Dastra übermittelt nur die für die angeforderte Generierung strikt erforderlichen Informationen: den von Ihnen eingegebenen Text und gegebenenfalls die Felder des Objekts, an dem Sie arbeiten (Verarbeitung, KI-System, Betroffenenanfrage usw.). Andere Datensätze Ihres Workspace, Ihre Anmeldedaten und Sitzungsmetadaten werden niemals einbezogen. Für Details nach Funktion konsultieren Sie die Seite Wie funktioniert es?.

***

**Wo werden die von Dastra verwendeten KI-Modelle gehostet?**

Für die Familien OpenAI, Mistral und Open Source werden die Modelle auf der Microsoft Azure-Infrastruktur in Frankreich gehostet. Ihre Daten werden nicht an die eigenen Server von OpenAI oder Mistral übertragen. Dastra nutzt ausschließlich die verwalteten Azure-Dienste.

Wenn Sie einen **Custom AI Provider** mit Ihrem eigenen API-Schlüssel konfigurieren, hängt das Hosting vom gewählten Anbieter ab.

***

**Werden meine Prompts nach der Generierung aufbewahrt?**

Die Azure-Modelle sind zustandslos (_stateless_): Die Prompts und Ergebnisse werden nicht zwischen zwei Anfragen im Modell gespeichert. Sie werden auch nicht zu kommerziellen Wiederverwendungszwecken protokolliert.

**Ausnahme:** Azure unterhält einen automatisierten Missbrauchserkennungsmechanismus. Wenn ein Inhalt gemeldet wird, kann eine Stichprobe vorübergehend in einem kundenspezifisch isolierten Bereich zur Überprüfung aufbewahrt werden. Für Ressourcen, die im EWR bereitgestellt werden (was bei Dastra der Fall ist), befinden sich die menschlichen Prüfer ebenfalls im EWR. Diese Aufbewahrung ist außergewöhnlich.

***

**Wer kann die an den KI-Assistenten gerichteten Aufrufe in meiner Organisation sehen?**

Die Administratoren Ihres Workspace haben Zugriff auf die **KI-Aufrufprotokolle** (90 Tage Verlauf) über **Einstellungen > KI-Assistent > KI-Aufrufprotokolle**. Diese Protokolle zeigen Datum, Status, Operationstyp, verwendetes Modell, Dauer und den Nutzer, der die Generierung ausgelöst hat. Der Inhalt der Prompts und Antworten wird dort nicht angezeigt.

***

**Wird der KI-Assistent vom DPA (Auftragsverarbeitungsvertrag) von Dastra abgedeckt?**

Ja. Die Nutzung des KI-Assistenten erfolgt im Rahmen des bestehenden Vertrags zwischen Ihrer Organisation und Dastra. Microsoft Azure ist Auftragsverarbeiter zweiten Grades, gebunden durch die vertraglichen Verpflichtungen von Azure in Bezug auf den Datenschutz. Für weitere Details verweisen wir auf Ihren Dastra-DPA oder kontaktieren Sie unser Team.

***

### Qualität und Zuverlässigkeit

**Kann man den von der KI generierten Ergebnissen vertrauen?**

Die generierten Ergebnisse sind Ausgangspunkte, keine endgültigen Antworten. Sie beschleunigen Ihre Dokumentationsarbeit, ersetzen aber nicht das Urteil eines Experten. Alle generierten Inhalte müssen von einer qualifizierten Person überprüft und validiert werden, bevor sie verwendet werden, insbesondere für Compliance-Analysen, Datenschutzerklärungen und Antworten auf Betroffenenanfragen.

***

**Was ist eine Funktion in der Beta-Phase?**

Einige KI-Funktionen werden als Beta-Version veröffentlicht: Sie sind funktionsfähig, werden aber weiterhin verbessert. Die Ergebnisse können weniger konstant sein als bei stabilen Funktionen und sollten mit erhöhter Aufmerksamkeit behandelt werden.

Aktuell in der Beta-Phase: die Compliance-Analyse der Verarbeitungen und die Compliance-Analyse der KI-Systeme.

***

**Kann die KI bei rechtlichen Fragen falsch liegen?**

Ja. Der KI-Assistent ist kein Jurist. Die generierten Inhalte, Compliance-Analysen, Hinweise, Risikobewertungen, sind Denkhilfen basierend auf den in Ihrem Workspace gespeicherten Informationen. Sie stellen keine Rechtsberatung dar und können die Expertise eines Datenschutzbeauftragten oder eines spezialisierten Beraters nicht ersetzen.

***

### Konfiguration und Zugriff

**Wie wähle ich das verwendete KI-Modell?**

Gehen Sie zu **Einstellungen > KI-Assistent**, um die Modellfamilie auszuwählen: OpenAI (Standard), Mistral, Open Source oder einen benutzerdefinierten Anbieter (Custom AI Provider). Für jede Familie werden drei Modellstufen automatisch je nach Aufgabenkomplexität verwendet (Fast, Smart, Erweiterter Kontext).

***

**Kann ich meinen eigenen KI-Anbieter verbinden?**

Ja, über die Funktion **Custom AI Provider**. Jeder mit dem OpenAI-API-Standard kompatible Anbieter kann verbunden werden: OpenAI, Google (Gemini), Mistral, Microsoft Foundry oder ein selbst gehostetes LLM. Konfigurieren Sie Ihre Anmeldedaten unter **Einstellungen > KI-Assistent > Custom AI Provider**.

{% hint style="warning" %}
Bei einem Custom AI Provider gelten die in dieser Dokumentation beschriebenen Azure-Garantien nicht mehr. Die Daten unterliegen der Richtlinie Ihres Anbieters.
{% endhint %}

***

**Kann ich den KI-Assistenten für meine Organisation deaktivieren?**

Ja. Kontaktieren Sie unser Support-Team, um die Funktion auf Organisationsebene zu deaktivieren. Die Deaktivierung ist global: Es ist nicht möglich, nur bestimmte Prompts zu deaktivieren und andere aktiv zu lassen.

***

**Ist der KI-Assistent in allen Dastra-Plänen verfügbar?**

Ja, der KI-Assistent ist in allen Dastra-Plänen verfügbar. Einige erweiterte Funktionen können bestimmten Bedingungen unterliegen. Kontaktieren Sie unser Team bei Fragen zu Ihrem Plan.

***

### KI-Verordnung (AI Act)

**Unterliegt der KI-Assistent von Dastra der KI-Verordnung?**

Ja. Der KI-Assistent von Dastra fällt unter die Definition eines KI-Systems im Sinne der KI-Verordnung (EU 2024/1689). Je nach verwendeter Funktion fällt er hauptsächlich in die Kategorie **begrenztes Risiko**, was Transparenzpflichten (Art. 50) impliziert, wenn der generierte Inhalt für natürliche Personen bestimmt ist.

***

**Muss ich die betroffenen Personen darüber informieren, dass ich KI verwende, um auf ihre Anfragen zu antworten?**

Nicht als strenge Verpflichtung, aber es wird als bewährte Praxis dringend empfohlen.

Artikel 50(1) der KI-Verordnung zielt auf KI-Systeme ab, **die direkt mit natürlichen Personen interagieren**. Bei Dastra ist dies nicht der Fall: Es ist ein menschlicher Nutzer (Datenschutzbeauftragter, Jurist), der den Text generiert, ihn überprüft, validiert und selbst an die betroffene Person sendet. Es gibt keine direkte Interaktion zwischen dem KI-System und dem Endempfänger — die strenge Verpflichtung des Art. 50(1) gilt daher nicht.

{% hint style="info" %}
Die Entwurfsrichtlinien des AI Office (2025 zur Konsultation veröffentlicht) bestätigen ausdrücklich diese Interpretation: *"die direkte Interaktion schließt indirekte oder vermittelte menschliche Interaktionen aus [...] **zum Beispiel wenn Kundendienstmitarbeiter KI-Assistenztools verwenden, um mit natürlichen Personen zu kommunizieren** oder wenn das Ergebnis der KI nicht vom KI-System selbst, sondern von einer anderen Person, die den Inhalt verbreitet, der Person zur Verfügung gestellt wird."* (Abschnitt 3.1.1). Der Anwendungsfall von Dastra entspricht genau diesem Schema.

Hinweis: Die Verpflichtungen aus Artikel 50 treten am **2. August 2026** in Kraft. Die endgültigen Richtlinien können ergänzende Präzisierungen enthalten.
{% endhint %}

Dennoch bleibt es eine **bewährte Praxis**, die betroffene Person darüber zu informieren, dass eine Antwort KI-gestützt erstellt wurde, gemäß dem Grundsatz der Fairness und Transparenz der DSGVO (Art. 5(1)(a)). Dastra generiert diesen Hinweis nicht automatisch: Wenn Ihre Organisation ihn einfügen möchte, müssen Sie ihn vor dem Versand selbst hinzufügen.

***

**Ist Dastra Anbieter oder Betreiber im Sinne der KI-Verordnung?**

Beides, je nach Anwendungsfall. Wenn Sie die Standardmodelle verwenden (OpenAI, Mistral, Open Source via Azure), ist Dastra **Anbieter** des KI-Systems und Ihre Organisation ist der **Betreiber**. Wenn Sie Ihren eigenen Anbieter über Custom AI Provider verbinden, fungiert Dastra lediglich als Compliance-Tool. Ihre Organisation übernimmt dann die Rolle des Anbieters und/oder Betreibers in Bezug auf ihr eigenes Modell.
