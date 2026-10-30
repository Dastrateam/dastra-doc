---
description: >-
  Erfassen, unterzeichnen und verfolgen Sie Ihre Verträge, Richtlinien und
  anderen rechtlichen Dokumente direkt in Dastra.
---

# Verträge und Richtlinien

Mit dem Modul **Verträge und Richtlinien** von Dastra erfassen, bearbeiten, unterzeichnen und versionieren Sie Ihre rechtlichen und organisatorischen Dokumente: Verträge, Richtlinien, Hinweise und Vorgehensweisen. Jedes Dokument ist mit den Assets, Stakeholdern und Nutzern verknüpft, die es betrifft. So bleiben Ihre Verpflichtungen konsistent mit Ihrem Verzeichnis und Ihren Referenzen.

## Auf das Modul zugreifen

Ihr Abonnement muss die Funktion für Verträge enthalten. Ist sie in Ihrem Plan aktiv, öffnen Sie in der Seitenleiste **Betrieb** > **Verträge und Richtlinien**. Das Modul hat drei Einträge:

* **Verzeichnis der Verträge und Richtlinien**: die Liste Ihrer Dokumente.
* **Statistiken**: die Kennzahlen und Diagramme des Moduls (siehe [Statistiken](README.md#statistiken)).
* **Dokumentvorlagen**: die Vorlagen, mit denen Dokumente generiert werden (siehe [Vertragsvorlagen](templates.md)). Dieser Eintrag ist für Nutzer mit der Rolle `User` ausgeblendet.

<figure><img src="../../.gitbook/assets/contracts-readme-1.png" alt="Die Seitenleiste mit der geöffneten Gruppe Betrieb, dem Eintrag Verträge und Richtlinien und seinen drei Einträgen"><figcaption><p>Das Modul Verträge und Richtlinien in der Seitenleiste</p></figcaption></figure>

## Dokumenttypen

Jedes Dokument hat einen Typ: **Vertrag**, **Richtlinie**, **Hinweis**, **Vorgehensweise** oder **Sonstiges**. Den Typ wählen Sie beim Erstellen des Dokuments (siehe [Ein Dokument erstellen](declare.md)). Um ihn später zu ändern, klicken Sie auf das Typ-Badge neben dem Titel des Dokuments.

Im Verzeichnis beschränkt der Filter **Typen** die Liste auf einen oder mehrere Typen.

## Das Verzeichnis der Dokumente

Das Verzeichnis listet Ihre Dokumente in einer Tabelle auf, deren Spalten Sie auswählen, zum Beispiel die Version, die Anzahl der Unterschriften, die Anzahl der Anhänge und die Frist. Mit den Filtern finden Sie ein Dokument nach Organisationseinheit, Schritt, Unterschriftenstatus, Typ, Status, Tag oder Nutzer.

Die Schaltfläche **Ein Dokument erstellen** öffnet den Assistenten zur Erstellung (siehe [Ein Dokument erstellen](declare.md)). Der Pfeil rechts daneben öffnet die weiteren Aktionen des Moduls:

* **Importieren**: mehrere Dokumente aus einer Datei importieren.
* **Exportieren**: die Liste exportieren.
* **Regelmäßige Überprüfung (Aktualität) konfigurieren**: festlegen, wie oft Dokumente überprüft werden (siehe [Regelmäßige Überprüfung von Dokumenten](review.md)).
* **E-Mails in Dokumente umwandeln**: Dokumente aus den E-Mails erstellen, die an einer Erfassungsadresse eingehen.
* **Bitte lesen Sie die Dokumentation**: diese Dokumentation öffnen.

<figure><img src="../../.gitbook/assets/contracts-readme-2.png" alt="Das Verzeichnis der Verträge und Richtlinien mit geöffnetem Menü der Schaltfläche Ein Dokument erstellen"><figcaption><p>Das Verzeichnis und die Aktionen der Schaltfläche Ein Dokument erstellen</p></figcaption></figure>

## Import und Export

**Importieren** öffnet den Import-Assistenten für Dokumente. Er steht Nutzern zur Verfügung, die die Berechtigung zum Importieren von Verträgen haben. Der Assistent ist unter [Daten importieren (Excel, CSV)](../general/import.md) beschrieben.

**Exportieren** öffnet ein Fenster, in dem Sie das Format wählen: CSV, XLSX, JSON, PDF, HTML, DOCX oder Markdown. Im Verzeichnis umfasst der Export die Liste. In einem Dokument bietet das Menü der Schaltfläche **Speichern** die Aktion **Exportieren** nur für dieses Dokument an. Mit der Option **Dokumente hinzufügen** nehmen Sie seine Anhänge mit.

## Dokumente aus Ihren E-Mails erstellen

Der Eintrag **E-Mails in Dokumente umwandeln** führt zur Integration von Erfassungs-E-Mail-Adressen. Sobald die Adresse für Verträge angelegt ist, erstellt jede eingehende E-Mail ein Dokument: Der Betreff wird zum Namen, der Text zur Beschreibung, und gültige Anhänge werden dem Dokument hinzugefügt. Für die Einrichtung der Adresse ist die Berechtigung zur Verwaltung von Integrationen erforderlich. Sie ist unter [E-Mail-Adressen für Datenerfassung](../settings/mailboxes.md) beschrieben.

## Statistiken

Der Eintrag **Statistiken** bietet einen Überblick über Ihre Dokumente. Die Kennzahlen oben zeigen die Anzahl der Dokumente für **Verspätet**, **Gesamt**, **Entwürfe** und **Veröffentlicht**. Klicken Sie auf eine Kennzahl, um die zugehörige Liste zu öffnen.

Die Diagramme zeigen:

* **Neue Dokumente**: die Entwicklung der Anzahl der Dokumente im Mandanten und die Anzahl der Dokumente, die an jedem Datum erstellt wurden.
* **Unterzeichner**: die Anzahl der Dokumente pro Unterzeichner.
* **Schritte**: die Anzahl der Dokumente pro Schritt des Prozesses.
* **Tags**: die Anzahl der Dokumente pro Tag.
* **Dokumente nach Organisationseinheiten**: die Anzahl der Dokumente in jeder Organisationseinheit, für jeden Schritt des Prozesses.

Die Schaltfläche **Filter** schränkt die Kennzahlen und Diagramme ein, **Drucken** erstellt eine druckbare Version. Die Kennzahl **Verspätet** beruht auf der Frist Ihrer Dokumente: Tragen Sie sie im Tab **Details** ein (siehe [Details und Anhänge](documents.md)).

<figure><img src="../../.gitbook/assets/contracts-readme-3.png" alt="Die Statistikseite mit den vier Kennzahlen und den Diagrammen"><figcaption><p>Die Statistikseite des Moduls</p></figcaption></figure>
