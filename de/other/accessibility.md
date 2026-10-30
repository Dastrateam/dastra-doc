---
description: >-
  Richtlinie zur digitalen Barrierefreiheit von Dastra, angewandte
  Referenzstandards und kontinuierlicher Verbesserungsansatz.
---

# Barrierefreiheit

## Engagement

Dastra verpflichtet sich, seine digitalen Dienste für alle zugänglich zu machen, in Übereinstimmung mit internationalen Standards und den geltenden regulatorischen Anforderungen.

Die Barrierefreiheit ist Teil unseres umfassenden Ansatzes für Compliance und kontinuierliche Verbesserung.

## Anwendbare Standards und Rahmenwerke

Unser Ansatz zur Barrierefreiheit beruht auf den folgenden Standards:

* **WCAG 2.1 (Stufen A und AA)**, veröffentlicht vom W3C
* **EN 301 549**, die europäische Norm, die die Barrierefreiheitsanforderungen für digitale Produkte und Dienste festlegt
* **RGAA**, die französische operative Umsetzung der WCAG im nationalen Regelungsrahmen

Die WCAG definieren 50 Erfolgskriterien auf den Stufen A und AA.

Das RGAA bietet einen strukturierten methodischen Rahmen, um die Konformität von HTML-Inhalten (HTML4, XHTML1, HTML5), CSS und JavaScript anhand von Prüfkriterien und technischen Tests zu bewerten.

Die RGAA-Methodik umfasst 106 Kriterien mit jeweils mehreren Tests. Einige beruhen auf bestimmten Umsetzungstechniken, um den Interpretationsspielraum zu begrenzen.

Bestimmte Tests, insbesondere für dynamische, in JavaScript entwickelte Oberflächenkomponenten, erfordern eine Überprüfung mit assistiven Technologien (Screenreader, Tastaturnavigation) in einer Referenzumgebung aus Browser und Betriebssystem.

Native mobile Anwendungen, Software und andere spezifische Umgebungen werden unmittelbar anhand der einschlägigen Anforderungen der EN 301 549 bewertet.

## Barrierefreiheitsaudit

Ein erstes RGAA-4.1.1-Audit wurde am 16. Oktober 2025 intern an drei öffentlich zugänglichen Seiten durchgeführt:

* Das Cookie-Banner, wie es auf www.dastra.eu angezeigt wird
* Die öffentliche Seite des Formulars für Anfragen betroffener Personen
* Der Privacy Hub

Interne Oberflächen, die eine Authentifizierung erfordern, gehören nicht zu diesem ersten Umfang. Das Audit ergibt keine Gesamtkonformitätsquote: Es wurden nur diese drei Seiten bewertet.

| Seite | Konforme Kriterien | Nicht konforme Kriterien | Nicht anwendbare Kriterien |
| --- | --- | --- | --- |
| Cookie-Banner | 47 | 5 | 54 |
| Formular für Anfragen betroffener Personen | 43 | 11 | 52 |
| Privacy Hub | 56 | 3 | 47 |

Die Kriterien 7.1 und 7.2 (Anzeige ohne JavaScript) werden für alle drei Seiten gemeldet. Das Audit stuft sie für das Banner, das ohne JavaScript kein Cookie setzt, und für das Formular als nicht anwendbar ein.

## Verbesserungsplan

Korrekturen werden schrittweise in den Entwicklungszyklen ausgeliefert. Bisher betreffen sie:

* Kriterium 3.3 (Farben in Oberflächenkomponenten)
* Kriterium 12.6 (Navigationsbereiche)
* Kriterium 9.3 (Listenauszeichnung) sowie die Kriterien 11.5 und 11.6 (Feldgruppen mit Legende) im Anfrageformular

Die noch offenen Arbeiten betreffen:

* Die Tastaturnavigation im Formular für Anfragen betroffener Personen (Kriterien 7.3 und 7.4)
* Die Beschriftung der Sprachauswahl des Formulars (Kriterium 11.1)

Das Audit empfiehlt außerdem präzisere Textalternativen (Kriterium 1.1), eindeutigere Fehlermeldungen (Kriterium 11.11) und, für das Cookie-Banner, es als Erstes in die Tabulatorreihenfolge zu setzen (Kriterium 10.7).

### Farbkontrast

Kriterium 3.2 (Textkontrast) hängt von den Farben ab, die jeder Kunde in seinen Design-Einstellungen wählt. Der Kontrast bleibt daher in der Verantwortung des Kunden: Prüfen Sie, dass die gewählten Farben für den Fließtext ein Kontrastverhältnis von mindestens 4,5:1 ergeben.

## Stand der Konformität

Letzte Aktualisierung: 30. Oktober 2026.

* Das erste RGAA-Audit an drei Seiten ist abgeschlossen.
* Die oben genannten Korrekturen sind ausgeliefert. Die verbleibenden Arbeiten stehen noch aus.
* Die ausführliche Barrierefreiheitserklärung ist noch nicht veröffentlicht. Sie wird veröffentlicht, sobald die wichtigsten Korrekturen bereitgestellt sind.

## Ein Barrierefreiheitsproblem melden

Wenn Sie Schwierigkeiten beim Zugriff auf Inhalte oder Funktionen haben, erreichen Sie uns unter:

contact@dastra.eu

Wir verpflichten uns, so schnell wie möglich zu antworten.
