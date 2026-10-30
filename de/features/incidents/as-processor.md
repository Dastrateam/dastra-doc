---
description: >-
  Verwalten Sie Datenschutzvorfälle, bei denen Ihre Organisation nach der DSGVO
  als Auftragsverarbeiter handelt.
---

# Datenschutzvorfälle als Auftragsverarbeiter

Das Modul Vorfälle von Dastra passt sich der Rolle Ihrer Organisation im Vorfall an: Verantwortlicher oder Auftragsverarbeiter. Diese Rolle bestimmt die geltenden Pflichten und welche Schritte im Formular angezeigt werden.

## Ihre Rolle bei der Erstellung angeben

Beim Erstellen eines Vorfalls fragt das Fenster **Sind Sie im Zusammenhang mit diesem Vorfall als Auftragsverarbeiter tätig?** mit zwei Antworten:

* **Nein** (Standard): Sie behandeln den Vorfall als Verantwortlicher. Es gilt der Standardablauf: Meldung an die Aufsichtsbehörde, Mitteilung an die betroffenen Personen, Risikoanalyse.
* **Ja**: Sie behandeln den Vorfall als Auftragsverarbeiter. Sie müssen die Aufsichtsbehörde nicht selbst benachrichtigen: Das ist Sache des Verantwortlichen.

<figure><img src="../../.gitbook/assets/violations-create-subprocessor.png" alt="Fenster zum Erstellen eines Vorfalls mit der Frage zur Rolle als Auftragsverarbeiter, Ja ausgewählt"><figcaption><p>Geben Sie bei der Erstellung an, ob Ihre Organisation als Auftragsverarbeiter handelt</p></figcaption></figure>

Wie Sie den Vorfall Schritt für Schritt erstellen, lesen Sie unter [Einen neuen Datenschutzvorfall dokumentieren](document-breach.md).

{% hint style="info" %}
Artikel 33 Absatz 2 DSGVO: Der Auftragsverarbeiter meldet dem Verantwortlichen jede Verletzung des Schutzes personenbezogener Daten unverzüglich, nachdem sie ihm bekannt geworden ist. Der Auftragsverarbeiter ist nicht verpflichtet, die Aufsichtsbehörde direkt zu benachrichtigen: Diese Pflicht liegt beim Verantwortlichen.
{% endhint %}

## Unterschiede im Formular

Wenn Sie die Frage zur Rolle mit **Ja** beantworten, ändert sich das Formular wie folgt:

| Element | Verantwortlicher | Auftragsverarbeiter |
| --- | --- | --- |
| Schritt **Benachrichtigung** (Aufsichtsbehörde) | Angezeigt | Ausgeblendet |
| Schritt **Mitteilung** | Mitteilung an die betroffenen Personen | Mitteilung an die Verantwortlichen, mit dem Tab **Verantwortliche für die Datenverarbeitung** |

Die übrigen Schritte bleiben gleich. Im Schritt **Risikoanalyse** erinnert ein Hinweis daran, die betreffenden Verantwortlichen über die erforderlichen Maßnahmen zu informieren, damit sie entsprechend handeln können.

Im Verzeichnis unterscheidet der Filter **Rolle** die als Auftragsverarbeiter behandelten Vorfälle von denen, die als Verantwortlicher behandelt werden, und die Seite **Statistiken** zeigt die **Aufteilung nach Rollen**.

## Den Verantwortlichen, die Ihre Kunden sind, Mitteilung machen

Der Schritt **Mitteilung** eines Vorfalls als Auftragsverarbeiter hat zwei Tabs.

Beantworten Sie im Tab **Mitteilung** die Frage **Haben Sie sich an die Verantwortlichen für die Verarbeitungen gewandt?** mit **Nicht zutreffend**, **Ja** oder **Nein**. Klicken Sie bei **Ja** auf **Eine Mitteilung hinzufügen**, um jede Nachricht mit ihrem Datum zu erfassen. Nennen Sie bei **Nein** die Gründe unter **Aus welchen Gründen haben Sie die Verantwortlichen für die Verarbeitung nicht informiert?**.

Der Tab **Verantwortliche für die Datenverarbeitung** listet die vom Vorfall betroffenen Verantwortlichen unter Ihren Kunden auf. Sie können:

* einen Verantwortlichen mit **RT zuordnen** zuordnen;
* die Verantwortlichen mit **RTs synchronisieren** automatisch importieren;
* bei jedem **Nachricht gesendet** und **Notifizierte Behörde** aktivieren;
* die Liste für Ihre Compliance-Akte mit **RTs exportieren** exportieren.

<figure><img src="../../.gitbook/assets/incidents-as-processor-1.png" alt="Schritt Mitteilung eines Vorfalls als Auftragsverarbeiter, Tab Verantwortliche für die Datenverarbeitung"><figcaption><p>Der Tab Verantwortliche für die Datenverarbeitung mit den Aktionen RT zuordnen, RTs synchronisieren und RTs exportieren</p></figcaption></figure>

### Die Verantwortlichen synchronisieren

Sind dem Vorfall Verarbeitungstätigkeiten zugeordnet (Schritt **Verarbeitungen**), findet Dastra anhand dieser Tätigkeiten die Verantwortlichen unter Ihren Kunden und fügt sie der Liste hinzu. Klicken Sie auf **RTs synchronisieren**, um den Vorgang zu starten. Ist noch keine Verarbeitungstätigkeit und kein KI-System verknüpft, bittet Dastra Sie, zuerst welche zu verknüpfen.

## Bewährte Vorgehensweisen

* Benachrichtigen Sie die Verantwortlichen unter Ihren Kunden, sobald Ihnen der Vorfall bekannt wird. Die DSGVO setzt dem Auftragsverarbeiter keine feste Frist, anders als die 72 Stunden, die der Verantwortliche für die Meldung an die Behörde hat, doch eine schnelle Reaktion ist entscheidend.
* Halten Sie Datum und Uhrzeit jeder an die Verantwortlichen gesendeten Mitteilung fest.
* Bewahren Sie die Empfangsbestätigungen und Antworten im Schritt **Dokumentation** des Vorfalls auf.
