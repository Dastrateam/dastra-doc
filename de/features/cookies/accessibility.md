---
description: >-
  Die Ergebnisse des RGAA-Barrierefreiheitsaudits des Cookie-Banners und die
  zu behebenden Punkte.
---

# RGAA-Konformität

Diese Seite stellt die Ergebnisse des letzten Barrierefreiheitsaudits des Cookie-Banners vor. Es wurde anhand des französischen allgemeinen Referenzrahmens zur Verbesserung der Barrierefreiheit (RGAA) durchgeführt.

## Audit vom 16. Oktober 2025

* **Referenzrahmen**: RGAA 4.1.1.
* **Art des Audits**: internes Audit (Erstbesuch) des Banners, wie es auf www.dastra.eu angezeigt wird.
* **Ergebnis**: 47 Kriterien erfüllt, 5 nicht erfüllt und 54 nicht anwendbar.

{% hint style="info" %}
Das Auditraster berechnet keine Gesamtkonformitätsquote. Dieses Audit ist keine Erklärung der vollständigen Konformität des Banners.
{% endhint %}

## Nicht erfüllte Punkte

| Kriterium | Feststellung | Weiterverfolgung |
| --- | --- | --- |
| 3.2 Textkontrast | Der Fließtext, grau auf weißem Hintergrund, hat ein Kontrastverhältnis von 3,98:1, erforderlich sind 4,5:1. Der Link „Notre politique de cookies“, orange auf weiß, ist ebenfalls betroffen. | Hängt von den in den Banner-Einstellungen gewählten Farben ab. Siehe unten. |
| 3.3 Farben der Oberflächenelemente | Fett gesetzte Wörter haben dieselbe Farbe wie der Fließtext. | Das Raster vermerkt „corrigé“ (behoben). Das SDK der Version 3.0.0 zeigt fett gesetzte Wörter in einem dunkleren Farbton als den Fließtext. |
| 7.1 und 7.2 Anzeige ohne JavaScript | Das Banner erscheint ohne JavaScript nicht. | Der Auditor weist darauf hin, dass ohne JavaScript kein Cookie gesetzt wird: Es gibt dann keine Einwilligung einzuholen. |
| 12.6 Navigationsbereiche | Der Link zur Cookie-Richtlinie befindet sich nicht in einem Navigationsbereich. | Das Raster vermerkt „corrigé“ (behoben). Das SDK der Version 3.0.0 setzt diesen Link in ein `<nav>`-Element, auf dem Begrüßungsbildschirm und auf dem Bildschirm mit den Einstellungen. |

Das Audit empfiehlt außerdem, das Banner an die erste Stelle der Tabulatorreihenfolge zu setzen (Kriterium 10.7, erfüllt).

### Kontrast: Ihre Einstellungen sind entscheidend

Die Farben des Banner-Textes und der Links stammen aus den Einstellungen des jeweiligen Banners: **Hauptfarbe der Texte** und **Primärfarbe** im Abschnitt **Erscheinungsbild und Design**. Der Kontrast ist also Ihre Entscheidung: Dastra kann ihn nicht für jedes Banner garantieren. Prüfen Sie, dass Texte und Links zum Hintergrund einen Kontrast von mindestens 4,5:1 haben. Siehe [Das Cookie-Einwilligungsbanner einrichten](banner/configure.md).

## Bericht von 2021

Das vorherige Audit stammt vom 16. März 2021. Es bezieht sich auf das RGAA-Raster 4.1, ist auf Französisch verfasst und liegt vor mehreren Änderungen am Banner (Global Privacy Control, die Schaltfläche **Ohne Zustimmung fortfahren**, Formen der schwebenden Schaltfläche). Es bleibt als historische Referenz verfügbar.

{% file src="../../.gitbook/assets/audit-rgaa.zip" %}
Bericht des RGAA-Audits von 2021 herunterladen
{% endfile %}
