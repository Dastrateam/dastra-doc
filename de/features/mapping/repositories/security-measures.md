---
description: >-
  Führen Sie die technischen und organisatorischen Maßnahmen auf, die Ihre
  Daten schützen, und ordnen Sie sie Ihren Assets und Verarbeitungstätigkeiten
  zu.
---

# Sicherheitsmaßnahmen

Sicherheitsmaßnahmen sind die technischen oder organisatorischen Vorkehrungen zum Schutz der Daten: Virenschutz, Application Firewall, Zugriffskontrollen, eine Clean-Desk-Richtlinie und so weiter. Im Menü heißt diese Referenzliste **Maßnahmen**.

Erfassen Sie jede Maßnahme einmal mit einem kurzen Namen, damit Sie sie von einem Asset oder einer Verarbeitungstätigkeit zur anderen wiederverwenden können. Diese Angaben stehen oft im DPA, den Sie mit einem Herausgeber unterzeichnet haben.

## Eine Sicherheitsmaßnahme hinzufügen

Öffnen Sie **Metadaten** > **Maßnahmen**. Klicken Sie auf **Eine Maßnahme erstellen** und wählen Sie dann:

* **Create from scratch**, um mit einem leeren Formular zu beginnen;
* **Use a template**, um eine Maßnahme aus der Bibliothek oder aus einem anderen Mandanten zu kopieren;
* **Mit KI generieren**, um die Maßnahme zu beschreiben und den Assistenten einen Entwurf erstellen zu lassen (diese Option hängt von den Funktionen ab, die für Ihre Organisation aktiviert sind).

Der Pfeil neben **Eine Maßnahme erstellen** bietet außerdem **Erstellen Sie auf der Grundlage von Vorlagen**, **Importieren** und **Datenqualitätswerkzeug**. Siehe [Daten importieren (Excel, CSV)](../../general/import.md).

<figure><img src="../../../.gitbook/assets/repositories-security-measures-1.png" alt="Formular einer Sicherheitsmaßnahme mit Name, Typ und Beschreibung"><figcaption><p>Das Formular einer Sicherheitsmaßnahme</p></figcaption></figure>

## Das Formular der Sicherheitsmaßnahme ausfüllen

| Feld | Inhalt |
| --- | --- |
| **Name der Maßnahme** | Der Name der Maßnahme, erforderlich. |
| **Interne Referenz** | Ihre Referenz. |
| **Typ** | Technisch, Organisatorisch, Physisch oder Personen (im Englischen **Technical**, **Organizational**, **Physical** oder **People**). |
| **Die Maßnahme beschreiben** | Eine freie Beschreibung. |
| **Beschreiben Sie das mit der Maßnahme verbundene potenzielle Risiko.** | Wozu die Maßnahme dient und welches potenzielle Risiko sie adressiert. |
| **URL der Dokumentation zur Maßnahme (z. B. auf der Website von CNIL)** | Die Adresse ihrer Dokumentation, zum Beispiel auf der Website der CNIL. |

Sie können [Tags](../../general/tags.md) hinzufügen, und die für Maßnahmen definierten [benutzerdefinierten Felder](../../general/custom-fields.md) erscheinen im Formular.

Die Symbolleiste des Formulars gibt je nach Ihren Berechtigungen und den aktivierten Funktionen Zugriff auf die angehängten Dokumente, Fragebögen und Aufgaben, die mit der Maßnahme verknüpft sind. Sie enthält außerdem:

* **Verknüpfte Elemente**: die [generischen Beziehungen](../relationships.md) der Maßnahme;
* **Verarbeitungen**: die Verarbeitungstätigkeiten, die die Maßnahme verwenden, mit der Schaltfläche **Mit einer Verarbeitung verknüpfen**, um weitere hinzuzufügen;
* **Aktivitätsverlauf**;
* den Workflow-Schritt der Maßnahme, wenn Workflow-Schritte definiert sind.

Das Aktionsmenü des Formulars bietet **Duplizieren**, **Zusammenführen** und **Löschen**.

## Sicherheitsmaßnahmen in der Liste finden

Die Filter sind **Nach Tags filtern** und **Typen**. Aktivieren Sie **Siehe Waisen**, um die Maßnahmen aufzulisten, die weder einem Asset noch einer Verarbeitungstätigkeit zugeordnet sind.

Bei einer Auswahl können Sie **Prozessschritt umschalten**, **Felder bearbeiten**, **Zusammenführen**, **Exportieren** und **Löschen**. Siehe [Elemente zusammenführen](../../general/merge.md).

## Wo Sicherheitsmaßnahmen verwendet werden

* In einem Asset listet der Abschnitt **Verbundene Sicherheitsmaßnahmen** die Maßnahmen des Assets auf. Siehe [Assets](assets.md).
* In einer Verarbeitungstätigkeit wählen Sie die Maßnahmen aus, die die Verarbeitung schützen, und geben ihren Umsetzungsstatus an. Siehe [Sicherheitsmaßnahmen](../../ropa/activity/security.md).

{% hint style="warning" %}
Das Löschen einer Maßnahme entfernt endgültig ihre Verweise in allen Verarbeitungstätigkeiten und Anhängen.
{% endhint %}
