---
description: Erfahren Sie, wie Sie Risiken in Dastra identifizieren.
---

# 1. Identifizieren

Bei der Erstellung eines neuen Risikos werden Sie aufgefordert, die Identifikationselemente anzugeben.

![Erster Abschnitt: Identifikation](../../../.gitbook/assets/Risiko1.png)

Ordnen Sie Ihr Risiko einer Organisationseinheit zu (standardmäßig wird die Organisationseinheit der Verarbeitung übernommen, wenn das Risiko an eine Verarbeitung geknüpft ist).

Legen Sie für jedes Risiko einen Inhaber fest. Dieser ist für die Überwachung und Steuerung des Risikos verantwortlich.

Und wählen Sie einen Risikotyp.

> Dastra ermöglicht es Ihnen, ein Referenzsystem für Risikotypen aufzubauen. Dieses Referenzsystem spart Ihnen Zeit und ermöglicht die Wiederverwendung von Risikotypen für andere Assets.

Ihr Risikotyp ist nicht im Referenzsystem vorhanden, kein Problem, fügen Sie ihn direkt über diese Oberfläche hinzu.

#### Einen Risikotyp hinzufügen <a href="#ajouter-un-type-de-risque" id="ajouter-un-type-de-risque"></a>

Durch die Erstellung eines Risikotyps haben Sie die Möglichkeit, diese Informationen wiederzuverwenden, um diesen Risikotyp auf so viele Assets wie gewünscht anzuwenden. Zum Beispiel möchten Sie dasselbe Risiko für mehrere Ihrer Auftragsverarbeiter identifizieren. Sie müssen diesen Risikotyp nur einmal angeben und können ihn dann für jeden Auftragsverarbeiter oder Dienstleister wiederverwenden.

**Identifikation des Risikotyps**

Ein Risiko lässt sich als Kombination aus einem befürchteten Ereignis und einer oder mehreren Bedrohungen für die Verwirklichung dieses befürchteten Ereignisses definieren. Es wird in Bezug auf Wahrscheinlichkeit (Eintrittswahrscheinlichkeit) und Schwere (Auswirkung) gemessen.

![Aufbau eines Risikotyps](../../../.gitbook/assets/Risiko2.png)

**Befürchtetes Ereignis**

Um einen Risikotyp hinzuzufügen, ist es notwendig, das befürchtete Ereignis und seine Auswirkungen zu identifizieren.\
Das befürchtete Ereignis ist die Folge des Eintretens eines Risikos.

Klassischerweise werden 3 Arten von befürchteten Ereignissen im Bereich der Informationssicherheit und/oder des Datenschutzes genannt. Die DSGVO fordert uns übrigens auf, die [Sicherheit](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32016R0679#d1e3428-1-1) personenbezogener Daten nach diesen drei Achsen zu gewährleisten.

* Beeinträchtigung der **Vertraulichkeit**
* Beeinträchtigung der **Verfügbarkeit**
* Beeinträchtigung der **Integrität**

Mit Dastra sind die Möglichkeiten zur Erstellung befürchteter Ereignisse unbegrenzt. Sie können also Ihre eigenen Kategorien befürchteter Ereignisse erstellen. Man kann sich auch einen Industrieunfall, einen Korruptionsakt usw. vorstellen.\
In unserem Ansatz konzentrieren wir uns zunächst auf die Risiken für Informationssysteme.

Für jedes befürchtete Ereignis werden Sie aufgefordert, **die Auswirkungen zu präzisieren**, die dieses auf die Situation haben wird.\
\
&#xNAN;_&#x42;eschreiben Sie in der Beschreibung des befürchteten Ereignisses die Auswirkungen_.

<figure><img src="../../../.gitbook/assets/Risiko3.png" alt=""><figcaption><p>Auswahl des befürchteten Ereignisses</p></figcaption></figure>

Die Auswirkungen können je nach Kontext und Objekt, dessen Risiko behandelt wird, variieren. Bei Risiken im Zusammenhang mit personenbezogenen Daten bestehen die Auswirkungen aus Schäden für die Personen (Identitätsdiebstahl, ungerechtfertigte Anschuldigung, Verlust des Personenstands...).

**Bedrohungen**

Für jedes befürchtete Ereignis müssen die Bedrohung(en) identifiziert werden, die seine Verwirklichung ermöglichen.

Ein Szenario muss vorgestellt werden. Sie können sich vergangene Ereignisse oder Ihre Vorstellungskraft zunutze machen, um vorherzusehen, was passieren könnte.

![Auswahl der Bedrohungen](https://static.dastra.eu/richtextbackoffice/b246b597-189b-4c37-a185-4baff38da515/image.png)

> Dastra bietet Referenzmodelle insbesondere für generische Bedrohungen an. Um diese zu importieren, suchen Sie die generischen Bedrohungen in der Bibliothek, indem Sie als Quelle "Modelle" wählen.

**Quellen**

Die Risikoquellen sind die Elemente, die die Verwirklichung des befürchteten Ereignisses ermöglichen (wer oder was könnte der Ursprung des befürchteten Ereignisses sein?).

Dabei müssen menschliche Quellen berücksichtigt werden: zum Beispiel ein IT-Administrator, ein Cyberangreifer, ein fremder Staat... sowie nicht-menschliche: zum Beispiel Wasser, ein Erdbeben, ein nicht gezielter Computervirus.

![Auswahl der Quellen](https://static.dastra.eu/richtextbackoffice/46bf2632-b74d-433c-9269-825b654de481/image.png)

**Kontrollpunkte**

Für jedes Risiko müssen die bestehenden oder geplanten Maßnahmen bestimmt werden, die das Risiko behandeln. Diese Kontrollpunkte können verschiedener Art sein: Sicherheitsmaßnahmen, technische Maßnahmen, organisatorische Maßnahmen oder auch rechtliche oder funktionale Maßnahmen.

Bei Risiken im Zusammenhang mit der Sicherheit von Informationssystemen werden Standard-Kontrollpunkte in der Norm ISO 27001 identifiziert. Der Leitfaden zur Datensicherheit der CNIL schlägt ebenfalls eine Reihe von Kontrollpunkten im Bereich des Schutzes personenbezogener Daten vor.

![Hinzufügen von Kontrollpunkten](https://static.dastra.eu/richtextbackoffice/aef7c85f-92b5-4c5f-9cb9-17b300b8758c/image.png)

**Vorbewertung**

In einem Risikotyp können Sie eine Risikobewertung einschließen. Diese Bewertung wird im endgültigen Risiko übernommen.\
Die Vorbewertung ermöglicht es Ihnen, bei zukünftigen Risiken, die auf dieser Grundlage basieren, Zeit zu sparen.

Die Bewertung erfolgt in Bezug auf Wahrscheinlichkeit und Auswirkung gemäß der von Ihnen konfigurierten Skala.

Sie können das Anfangsrisiko identifizieren: das ist das theoretische Risiko, das mit der Aktivität verbunden ist. Man kann es auch als das Ausgangsrisiko definieren, vor jeglichen Kontrollmaßnahmen (interne Kontrolle).

Sie können auch das Restrisiko identifizieren: das ist das nach der Umsetzung von Kontrollmaßnahmen (insbesondere der Kontrollpunkte) verbleibende Risiko.

![Vorbewertung der Risiken](https://static.dastra.eu/richtextbackoffice/4a223534-de99-4208-9361-fefbf838557b/image.png)

<br>
