---
description: >-
  Ein Nutzer sieht eine Verarbeitung oder einen Tab nicht oder erhält einen
  403-Fehler? Verstehen Sie, wie Rollen, Teams und Organisationseinheiten
  bestimmen, was er sehen kann.
---

# Warum sieht ein Nutzer eine Verarbeitung nicht?

Zwei Nutzer mit derselben Rolle sehen nicht unbedingt dieselben Elemente. In Dastra hängt der Zugriff von **zwei Ebenen** ab, die sich addieren:

1. **Seine Rollen**: Sie bestimmen, was der Nutzer in jedem Modul tun kann (Lesen, Schreiben, Erstellen, Exportieren …) und in welchen Arbeitsbereichen.
2. **Die Organisationseinheiten, auf die er Zugriff hat**: Sie bestimmen, in welchem Bereich (Einheit, Abteilung) der Nutzer Elemente sehen und bearbeiten kann.

Fehlt eine der beiden Ebenen, erscheint das Element nicht oder es wird eine Zugriffsfehlermeldung (403, „Ressource nicht zugänglich") angezeigt.

## 1. Rollen prüfen

* **Eigentümer** der Organisation haben Zugriff auf alle aktiven Arbeitsbereiche, alle Organisationseinheiten und alle Berechtigungen.
* Alle anderen Nutzer haben nur die Berechtigungen der **ihnen zugewiesenen Rollen**, Arbeitsbereich für Arbeitsbereich. Eine Rolle kann einem bestimmten Arbeitsbereich oder allen Arbeitsbereichen zugewiesen werden.
* Eine Rolle ohne angekreuzte Berechtigung gewährt keinerlei Zugriff.
* Ein Nutzer kann mehrere Rollen kumulieren.

Prüfen Sie unter **Einstellungen > Nutzer** (des betreffenden Arbeitsbereichs), welche Rollen zugewiesen sind, und anschließend unter **Konfiguration > Rollen und Berechtigungen**, dass das gewünschte Modul mindestens die Berechtigung **Lesen** hat. Siehe [Rollen und Berechtigungen](../../features/settings/roles-et-permissions.md).

{% hint style="info" %}
Die Berechtigung **Lesen/Bearbeiten eigener Elemente** gewährt nur Zugriff auf Elemente, die dem Nutzer zugewiesen sind, nicht auf alle Elemente des Moduls.
{% endhint %}

## 2. Zugriff auf die Organisationseinheit prüfen

Jede Verarbeitung ist einer Organisationseinheit zugeordnet. Hat der Nutzer keinen Zugriff auf diese Einheit, sieht er deren Verarbeitungen nicht – auch nicht mit der richtigen Rolle.

Die Zugriffsregeln lauten:

* Standardmäßig ist eine Organisationseinheit für **alle** Nutzer des Arbeitsbereichs **zugänglich**: In ihren Berechtigungen erscheint die Meldung „Jeder darf das Element anzeigen oder bearbeiten".
* Sobald Sie **Berechtigungen** für eine Einheit **festlegen** (zugelassene Nutzer oder Teams), haben nur die aufgeführten Nutzer und die Mitglieder der aufgeführten Teams Zugriff.
* **Untergeordnete** Einheiten **erben** die Berechtigungen der übergeordneten Einheit (angezeigt als „Geerbt"), solange sie keine eigenen haben. Legt eine untergeordnete Einheit eigene Berechtigungen fest, ersetzen diese die der übergeordneten Einheit.

Um diese Regeln einzusehen oder zu ändern, öffnen Sie **Einstellungen > Organisationseinheiten** und wählen Sie im Menü der betreffenden Einheit **Berechtigungen festlegen für …**. Diese Aktion ist Nutzern mit dem Recht für die erweiterte Verwaltung vorbehalten.

{% hint style="warning" %}
Häufige Ursache: Ein Team wurde bei einer übergeordneten Einheit hinzugefügt, und der Nutzer gehört nicht zu diesem Team. Er verliert dann den Zugriff auf alle untergeordneten Einheiten, die keine eigenen Berechtigungen haben. Prüfen Sie, welchen [Teams](creer-puis-affectez-des-equipes.md) er angehört.
{% endhint %}

## Kurze Checkliste

| Symptom | Zu prüfen |
|---|---|
| Keine Verarbeitung sichtbar oder ein Tab fehlt | Ist in diesem Arbeitsbereich eine Rolle mit der Berechtigung **Lesen** für das Modul zugewiesen? |
| Nur einige Verarbeitungen sind sichtbar | Zugriff auf Organisationseinheiten, Vererbung von der übergeordneten Einheit, Teammitgliedschaft |
| Ein Kollege mit derselben Rolle sieht mehr Elemente | Er gehört wahrscheinlich einem für die Einheit zugelassenen Team an, Sie nicht |
| Die Speichern-Schaltfläche ist ausgegraut | Fehlende Berechtigung **Schreiben** (bzw. **Erstellen** für ein neues Element) |
| 403-Fehler „Ressource nicht zugänglich" | Zugriff auf die Organisationseinheit des Elements oder keine Rolle in diesem Arbeitsbereich |

Wenn alles korrekt ist und das Element unsichtbar bleibt, wenden Sie sich an den Dastra-Support und nennen Sie Arbeitsbereich, Nutzer und betroffenes Element.
