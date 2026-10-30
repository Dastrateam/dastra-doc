---
description: >-
  Berechnen Sie ein Risiko Schritt für Schritt auf der Standardskala 5×5 und auf
  der CNIL-Skala 4×4 und sehen Sie dann, wie der Score einer
  Datenschutzverletzung berechnet wird.
---

# Risiko-Scoring

Dieses Beispiel bewertet ein Risiko der Brightmoor Retail Group zweimal auf zwei Skalen und bewertet dann eine Datenschutzverletzung. Die beiden Berechnungen unterscheiden sich: Der Score eines Risikos ist ein Produkt, der Score einer Datenschutzverletzung eine Summe.

## Das Risiko

Brightmoor identifiziert das Risiko „Loss of customer payment data“ bei der Verarbeitungstätigkeit „Online order management“. Im Abschnitt **Risikobewertung** wählt Emma Walsh, die Datenschutzbeauftragte, einen **Schweregrad** und eine **Wahrscheinlichkeit** für das anfängliche Risiko und dann für das Restrisiko, sobald die Kontrollen eingerichtet sind. Den Bildschirm sehen Sie unter [Bewerten](../features/risks/process/assess.md).

Der Score eines Risikos ist **Schweregrad × Wahrscheinlichkeit**. Der Höchstwert einer Skala ist das Produkt ihrer beiden höchsten Stufen. Dastra zeigt den Score als „Score / Höchstwert“ und in einigen Ansichten als Prozentsatz des Höchstwerts.

## Auf der Standardskala 5×5

Die Standardskala **Standard-Risikoskala** hat fünf Stufen pro Achse.

| Stufe | Schweregrad | Wahrscheinlichkeit |
| --- | --- | --- |
| 1 | Vernachlässigbar | Sehr unwahrscheinlich |
| 2 | Gering | Unwahrscheinlich |
| 3 | Mittel | Möglich |
| 4 | Hoch | Wahrscheinlich |
| 5 | Extrem | Extrem |

Brightmoor bewertet das anfängliche Risiko mit dem Schweregrad **Hoch** (4) und der Wahrscheinlichkeit **Möglich** (3). Kartenzahlungen werden von einem externen Dienstleister verarbeitet, doch die Bestelldatenbank enthält die letzten Ziffern und die Rechnungsadresse. Nach den Kontrollen (Verschlüsselung, Zugriffsprüfungen) sinkt die Restwahrscheinlichkeit auf **Sehr unwahrscheinlich** (1).

| Risiko | Schweregrad | Wahrscheinlichkeit | Berechnung | Score | Prozentsatz | Zelle der Matrix |
| --- | --- | --- | --- | --- | --- | --- |
| Anfänglich | 4 | 3 | 4 × 3 | 12 / 25 | 48 % | rot |
| Rest | 4 | 1 | 4 × 1 | 4 / 25 | 16 % | grün |

<figure><img src="../.gitbook/assets/examples-risk-1.png" alt="Abschnitt Risikobewertung mit dem anfänglichen Risiko und dem Restrisiko auf der Matrix 5 mal 5"><figcaption><p>Das Risiko auf der Standardskala</p></figcaption></figure>

Der Prozentsatz ist der Score geteilt durch den Höchstwert (25), gerundet. Die Farbe der Zelle stammt aus der Matrix der Skala: Bei fünf Stufen ist die Zeile der Schweregrad, von oben gezählt, und die Spalte die Wahrscheinlichkeit.

Das aktuelle Risiko liegt dazwischen. Nach jeder Antwort auf einen Kontrollpunkt berechnet Dastra es mit dieser Formel neu: aktuelles Risiko = anfängliches Risiko − (anfängliches Risiko − Restrisiko) × Abhilfequote. Bei einer Abhilfequote von 50 % ist das aktuelle Risiko 12 − (12 − 4) × 0,5 = 8. Siehe [Auswirkung auf das aktuelle Risiko](../features/risks/process/monitor.md#auswirkung-auf-das-aktuelle-risiko).

## Auf der CNIL-Skala 4×4

Brightmoor beschließt, die vierstufige Skala der CNIL-Methode für Datenschutz-Folgenabschätzungen zu verwenden. Unter **Mandanteneinstellungen** > **Risikomanagement** wird eine Skala mit dem **Risikoskalamodell** **4 levels - Classic DPIA** erstellt und mit **Dieses Raster speichern und aktivieren** aktiviert (siehe [Die Risikoskala konfigurieren](../features/risks/process/assess.md#die-risikoskala-konfigurieren)).

| Stufe | Schweregrad | Wert | Wahrscheinlichkeit | Wert |
| --- | --- | --- | --- | --- |
| 1 | Vernachlässigbar | 10.000 € | Sehr unwahrscheinlich | 25 % |
| 2 | Gering | 50.000 € | Unwahrscheinlich | 50 % |
| 3 | Mittel | 100.000 € | Möglich | 75 % |
| 4 | Hoch | 1.000.000 € | Wahrscheinlich | 100 % |

<figure><img src="../.gitbook/assets/examples-risk-2.png" alt="Editor der Risikoskala mit der vierstufigen Matrix der CNIL-Vorlage"><figcaption><p>Die Skala 4 levels - Classic DPIA</p></figcaption></figure>

Die Werte sind die Standardwerte der Vorlage. Sie sind wie die Bezeichnungen bearbeitbar.

Dieselbe Bewertung, Schweregrad **Hoch** (4) und Wahrscheinlichkeit **Möglich** (3), ergibt jetzt:

| Risiko | Schweregrad | Wahrscheinlichkeit | Berechnung | Score | Prozentsatz | Zelle der Matrix |
| --- | --- | --- | --- | --- | --- | --- |
| Anfänglich | 4 | 3 | 4 × 3 | 12 / 16 | 75 % | rot |
| Rest | 4 | 1 | 4 × 1 | 4 / 16 | 25 % | orange |

Der Score ist identisch, aber der Höchstwert ist niedriger, sodass dasselbe Risiko mehr wiegt: 75 % statt 48 %, und das Restrisiko ist orange statt grün. Deshalb bittet Dastra um eine Bestätigung, bevor eine andere Skala aktiviert wird, wenn Risiken existieren, und deshalb sollten Sie die Skala wählen, bevor Sie Ihre ersten Risiken erfassen (siehe die [FAQ](../features/risks/faq.md)).

## Eine Datenschutzverletzung

Das Modul Vorfälle verwendet die Risikoskalen nicht. Beantworten Sie im Schritt **Risikoanalyse** einer Datenschutzverletzung **Wurde bereits eine Risikoanalyse durchgeführt?** mit **Nein** und wählen Sie dann zwei Bewertungen von 1 bis 4:

* **Identifizierung der betroffenen Personen**: wie leicht sich Personen anhand der Daten identifizieren lassen;
* **Auswirkungen auf die betroffenen Personen**: die Folgen für sie.

Die Bezeichnungen der vier Werte sind **1 - Vernachlässigbar**, **2 - Begrenzt**, **3 - Wichtig** und **4 - Maximal**. Der Score der Verletzung ist ihre **Summe**, von 2 bis 8, und legt die **Risikostufe** fest:

| Summe der beiden Bewertungen | Risikostufe | Von Dastra angezeigte Folge |
| --- | --- | --- |
| 2 und 3 | Geringes Risiko | Eine Meldung an die Aufsichtsbehörde und eine Mitteilung an die Personen sind nicht erforderlich |
| 4 und 5 | Mittleres Risiko | Sie müssen die Aufsichtsbehörde benachrichtigen |
| 6 bis 8 | Hohes Risiko | Meldung an die Aufsichtsbehörde und Mitteilung an die betroffenen Personen sind verpflichtend |

Brightmoor stellt fest, dass ein Kundenexport einige Stunden lang in einem falsch konfigurierten Speicherbereich lesbar war. Er enthält Namen, E-Mail-Adressen und Bestellhistorien.

| Fall | Identifizierung | Auswirkung | Berechnung | Score | Risikostufe |
| --- | --- | --- | --- | --- | --- |
| Export nur der Bestellnummern | 2 | 1 | 2 + 1 | 3 | Geringes Risiko |
| Export der Namen ohne Kontaktdaten | 3 | 1 | 3 + 1 | 4 | Mittleres Risiko |
| Export der Kundendatei | 4 | 2 | 4 + 2 | 6 | Hohes Risiko |

Im dritten Fall würde ein Produkt 4 × 2 = 8 ergeben, doch Dastra addiert die Bewertungen: 4 + 2 = 6. Das ist bereits ein **Hohes Risiko**, sodass die Meldung an die Aufsichtsbehörde und die Mitteilung an die betroffenen Personen verpflichtend sind. Den Schritt und den 72-Stunden-Zähler sehen Sie unter [Einen neuen Datenschutzvorfall dokumentieren](../features/incidents/document-breach.md#schritt-risikoanalyse).

{% hint style="info" %}
Steht **Wurde bereits eine Risikoanalyse durchgeführt?** auf **Ja**, erfassen Sie Ihre eigene Analyse und wählen die Stufe selbst unter **Fazit der Risikoanalyse: Geschätzte Risikostufe**. Die von Ihnen gewählte Stufe ersetzt die berechnete.
{% endhint %}
