---
description: Lernen Sie, Benachrichtigungen in Dastra zu verwalten.
---

# Benachrichtigungen

### 🧭 Übersicht

In Dastra ermöglichen Ihnen Benachrichtigungen, über wichtige Aktivitäten im Zusammenhang mit Ihren Verarbeitungen, Audits, Aufgaben oder Rechteausübungsanfragen informiert zu bleiben.

Es gibt **zwei Arten von Benachrichtigungen**:

1. **Das Benachrichtigungszentrum** — direkt in die Anwendung integriert
2. **E-Mail-Benachrichtigungen** — nach Ihren Präferenzen anpassbar

***

### 🔔 Benachrichtigungszentrum (in der Anwendung)

Das Benachrichtigungszentrum fasst die Warnungen zusammen, die über das **Glocken**-Symbol oben rechts auf Ihrem Bildschirm sichtbar sind.

* Für alle Nutzer des Mandanten zugänglich
* Nicht anpassbar (gemeinsam für den gesamten Mandanten)
* Enthält allgemeine Benachrichtigungen über die letzten Aktivitäten: Erstellung, Änderung oder Löschung von Elementen

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration2.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Beispiel: „Eine neue Datenverarbeitung wurde in Ihrem Mandanten erstellt."
{% endhint %}

***

### ✉️ E-Mail-Benachrichtigungen (anpassbar)

Jeder Nutzer kann die zu empfangenden E-Mail-Benachrichtigungen über sein Nutzerprofil auswählen.

#### 🔧 So passen Sie Ihre Benachrichtigungen an

1. Klicken Sie auf Ihren **Avatar** oben rechts in Dastra
2. Wählen Sie **Benachrichtigungszentrum**
3. Aktivieren oder deaktivieren Sie die Kategorien nach Ihren Bedürfnissen
4. Speichern Sie Ihre Präferenzen

{% hint style="info" %}
E-Mail-Benachrichtigungen sind ideal, um über Aktionen benachrichtigt zu werden, die eine schnelle Reaktion erfordern (Audits, Anfragen, Datenschutzverletzungen usw.)
{% endhint %}

***

**🔐 Voraussetzung: Die Berechtigung „Benachrichtigung" in der Rolle**

Die Anpassung der E-Mail-Benachrichtigungen funktioniert nur, wenn die Rolle des Nutzers dies erlaubt.

In der Rollenkonfiguration (**Einstellungen → Rollen**) verfügt jedes Modul über ein Kontrollkästchen **Benachrichtigung**. Wenn dieses Kontrollkästchen nicht aktiviert ist, erhalten Nutzer mit dieser Rolle keine E-Mail-Benachrichtigungen für dieses Modul — unabhängig von ihren persönlichen Präferenzen.

{% hint style="info" %}
Die Rolle öffnet oder schließt das Recht auf Benachrichtigung. Der Nutzer kann anschließend seine Präferenzen verfeinern — aber nur im Rahmen dessen, was seine Rolle erlaubt.
{% endhint %}

### 📚 Benachrichtigungskategorien

Die E-Mail-Benachrichtigungen sind nach **Kategorien** organisiert.\
Jede Kategorie enthält mehrere Unter-Ereignistypen, die individuell aktiviert werden können.

| Kategorie                         | Beispiel für Benachrichtigung                     | Anpassbar? |
| --------------------------------- | ------------------------------------------------- | ---------- |
| **Datenverarbeitungen**           | Eine Verarbeitung wurde geändert oder gelöscht    | ✅          |
| **Rechteausübungsanfragen (DSR)** | Eine neue Anfrage wurde zugewiesen                | ✅          |
| **Datenschutzverletzungen**       | Eine Verletzung wurde gemeldet oder abgeschlossen | ✅          |
| **Aufgaben**                      | Sie wurden einer Aufgabe zugewiesen               | ✅          |
| **Audits**                        | Eine Antwort wurde validiert/abgelehnt            | ✅          |
| **Audit-Vorlagen**                | Eine Vorlage wurde aktualisiert                   | ✅          |
| **Kommentare**                    | Jemand hat Sie erwähnt (@)                        | ✅          |
| **Einwilligung / Cookies**        | Eine Änderung am Banner wurde vorgenommen         | ✅          |
| **Berichte / Analysen**           | Ein neuer Bericht ist verfügbar                   | ✅          |
| **Marketing / Push**              | Produktkommunikationen oder Dastra-Neuigkeiten    | ✅          |

***

### ⚠️ Automatische Benachrichtigungen

Bestimmte Benachrichtigungen gelten als **systemisch**: Sie werden automatisch gesendet, auch wenn Sie die entsprechende Kategorie deaktiviert haben.

Diese Benachrichtigungen werden als wesentlich für die Zusammenarbeit erachtet:

* Einladung zu einem **Audit**
* **Zuweisung** zu einer Aufgabe oder einer Anfrage
* **Direkte Erwähnung** in einem Kommentar (@Ihr-Name)
* Einladung zur Vervollständigung des **Verarbeitungsverzeichnisses**
* Sofortiger Versand einer **geplanten Einladung** (falls Option aktiviert)

***

### 💬 Best Practices

Gut zu wissen

* Aktivieren Sie E-Mails für Aktivitäten, die eine Handlung Ihrerseits erfordern (Audits, DSR, Verletzungen).
* Konsultieren Sie regelmäßig die **Glocke** für die Gesamtüberwachung des Mandanten.
* Überprüfen Sie Ihren **Ordner „Benachrichtigungen"** in Ihrem E-Mail-Postfach, wenn Sie bestimmte Nachrichten nicht mehr zu erhalten glauben.
* Für einen Datenschutzbeauftragten: Alle Kategorien aktivieren.
* Für einen Mitarbeiter: Aufgaben, Kommentare und Audits bevorzugen.

***

### ❓FAQ

#### Ich erhalte meine Benachrichtigungen nicht mehr, was tun?

Überprüfen Sie Ihre Präferenzen in Ihrem **Nutzerprofil → Benachrichtigungszentrum**.\
Stellen Sie außerdem sicher, dass die E-Mails von Dastra nicht in den Ordner „Werbung" oder „Spam" umgeleitet werden.

{% hint style="info" %}
Achtung: Sie erhalten keine Benachrichtigung für Elemente, die Sie selbst betreffen.
{% endhint %}

#### Kann ich eine monatliche Zusammenfassung erhalten?

Sie können eine monatliche Zusammenfassung der Aktivitäten Ihres Mandanten erhalten. Klicken Sie auf die Benachrichtigung: **Präferenzen: Anmeldung zum monatlichen Bericht**

***

### 🔗 Siehe auch

* [Ihr Nutzerprofil einrichten](../../getting-started/setup/parametrer-votre-profil-utilisateur.md)
* [Rollen und Berechtigungen konfigurieren](roles-et-permissions.md)
* [Ihre Audits verfolgen](../audit/)
