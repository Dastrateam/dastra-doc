---
description: >-
  Ein Nutzer sieht eine Verarbeitung oder einen Tab nicht oder erhält einen
  403-Fehler? Verstehen Sie, wie Rollen, Teams und Organisationseinheiten
  bestimmen, was er sehen kann.
---

# Warum sieht ein Nutzer eine Verarbeitung nicht?

Zwei Nutzer mit derselben Rolle sehen nicht unbedingt dieselben Elemente. In Dastra hängt der Zugriff von **zwei Ebenen** ab, die sich addieren:

1. **Seine Rollen**: Sie bestimmen, was der Nutzer in jedem Modul tun kann (Lesen, Schreiben, Erstellen, Exportieren …) und in welchen Mandanten.
2. **Die Organisationseinheiten, auf die er Zugriff hat**: Sie bestimmen, in welchem Bereich (Einheit, Abteilung) der Nutzer Elemente sehen und bearbeiten kann.

Fehlt eine der beiden Ebenen, erscheint das Element nicht oder es wird die Zugriffsfehlermeldung „Ressource nicht verfügbar (403)“ angezeigt.

## 1. Rollen prüfen

* **Inhaber** der Organisation haben Zugriff auf alle aktiven Mandanten, alle Organisationseinheiten und alle Berechtigungen.
* Alle anderen Nutzer haben nur die Berechtigungen der **ihnen zugewiesenen Rollen**, Mandant für Mandant. Eine Rolle kann einem bestimmten Mandanten oder allen Mandanten zugewiesen werden.
* Eine Rolle ohne angekreuzte Berechtigung gewährt keinerlei Zugriff.
* Ein Nutzer kann mehrere Rollen kumulieren.

Prüfen Sie unter **Mandanteneinstellungen** > **Nutzer** (des betreffenden Mandanten), welche Rollen zugewiesen sind, und anschließend unter **Konfiguration der Organisation** > **Rollen und Berechtigungen**, dass das gewünschte Modul mindestens die Berechtigung **Lesen** hat. Siehe [Rollen und Berechtigungen](../../features/settings/roles.md).

{% hint style="info" %}
Die Berechtigung **Lesen/Schreiben eigener Elemente** gewährt nur Zugriff auf Elemente, die dem Nutzer zugewiesen sind, nicht auf alle Elemente des Moduls.
{% endhint %}

## 2. Zugriff auf die Organisationseinheit prüfen

Jede Verarbeitung ist einer Organisationseinheit zugeordnet. Hat der Nutzer keinen Zugriff auf diese Einheit, sieht er deren Verarbeitungen nicht, auch nicht mit der richtigen Rolle.

Die Zugriffsregeln lauten:

* Standardmäßig ist eine Organisationseinheit für **alle** Nutzer des Mandanten **zugänglich**: In ihren Berechtigungen erscheint die Meldung „Jeder ist berechtigt, das Element anzuzeigen oder zu bearbeiten.“
* Sobald Sie **Berechtigungen** für eine Einheit **festlegen** (zugelassene Nutzer oder Teams), haben nur die aufgeführten Nutzer und die Mitglieder der aufgeführten Teams Zugriff.
* **Untergeordnete** Einheiten **erben** die Berechtigungen der übergeordneten Einheit (angezeigt als „Erbschaft“), solange sie keine eigenen haben. Legt eine untergeordnete Einheit eigene Berechtigungen fest, ersetzen diese die der übergeordneten Einheit.

Um diese Regeln einzusehen oder zu ändern, öffnen Sie **Mandanteneinstellungen** > **Organisationseinheiten** und wählen Sie im Menü der betreffenden Einheit **Festlegen der Berechtigungen für**. Diese Aktion ist Nutzern mit dem Recht für die erweiterte Verwaltung vorbehalten.

{% hint style="warning" %}
Häufige Ursache: Ein Team wurde bei einer übergeordneten Einheit hinzugefügt, und der Nutzer gehört nicht zu diesem Team. Er verliert dann den Zugriff auf alle untergeordneten Einheiten, die keine eigenen Berechtigungen haben. Prüfen Sie, welchen [Teams](teams.md) er angehört.
{% endhint %}

## Kurze Checkliste

| Symptom | Zu prüfen |
|---|---|
| Keine Verarbeitung sichtbar oder ein Tab fehlt | Ist in diesem Mandanten eine Rolle mit der Berechtigung **Lesen** für das Modul zugewiesen? |
| Nur einige Verarbeitungen sind sichtbar | Zugriff auf Organisationseinheiten, Vererbung von der übergeordneten Einheit, Teammitgliedschaft |
| Ein Kollege mit derselben Rolle sieht mehr Elemente | Er gehört wahrscheinlich einem für die Einheit zugelassenen Team an, Sie nicht |
| Die Speichern-Schaltfläche ist ausgegraut | Fehlende Berechtigung **Schreiben** (bzw. **Erstellen** für ein neues Element) |
| Fehler „Ressource nicht verfügbar (403)“ | Zugriff auf die Organisationseinheit des Elements oder keine Rolle in diesem Mandanten |

Wenn alles korrekt ist und das Element unsichtbar bleibt, wenden Sie sich an den Dastra-Support und nennen Sie Mandant, Nutzer und betroffenes Element.
