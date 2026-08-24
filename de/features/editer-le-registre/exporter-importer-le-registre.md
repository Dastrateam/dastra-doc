---
description: >-
  Erfahren Sie, wie Sie ein vollständiges bestehendes Verzeichnis in Dastra
  exportieren und importieren.
---

# Verzeichnis exportieren / importieren

## Der Verzeichnisexport

Um das gesamte Verzeichnis zu exportieren, gehen Sie zum Modul "**Verarbeitungsverzeichnis**", klicken Sie auf den Pfeil oben rechts neben der Schaltfläche zur Erstellung einer Verarbeitung und wählen Sie dann "**Exportieren**".

![Dropdown-Menü des Verzeichnisses mit der Exportfunktion](<../../.gitbook/assets/verzeichnis exportieren.png>)

Wählen Sie dann das Exportformat sowie die gewünschte Exportart (vollständig oder Format Artikel 30) und klicken Sie auf "**Datei herunterladen**". Das war's, Ihr Verzeichnis ist exportiert!

### Format Artikel 30

Das sogenannte Artikel-30-Format entspricht dem, was von der DSGVO gefordert wird. Der Export berücksichtigt die im Sinne der DSGVO obligatorischen Felder. Die DSGVO verpflichtet zur Erstellung des Verarbeitungsverzeichnisses. Die enthaltenen Informationen sind:

* Name der Verarbeitung
* Verarbeitungszwecke (ohne Rechtsgrundlagen)
* Daten und Aufbewahrung
* Empfänger und eventuelle Übermittlungen
* Sicherheitsmaßnahmen

### Vollständiges Format

Das vollständige Format ist das native Format von Dastra. Sie exportieren alle Felder, die das Verarbeitungsblatt bilden.

{% hint style="info" %}
Es ist auch möglich, nur eine oder mehrere Verarbeitungen des Verzeichnisses zu exportieren, anstatt das gesamte Verzeichnis. Wählen Sie dazu die betreffenden Verarbeitungen manuell aus, indem Sie die Kontrollkästchen links im Verzeichnis aktivieren, dann "Sammelaktion wählen" und "Exportieren".
{% endhint %}

## Der Verzeichnisimport

#### Der Import über die komplexe Excel-Tabelle

Der Import eines bestehenden Verzeichnisses kann eine mühsame Aufgabe darstellen, wenn Sie eine große Anzahl von Verarbeitungen haben.

Bei DASTRA haben wir eine Excel-Datei integriert, die es Ihnen ermöglicht, Ihre Verarbeitungen massenhaft und in einem einzigen Schritt zu importieren.

Sie bietet auch den Vorteil, **sämtliche** Ihre **Referenzsysteme** direkt in unserer Plattform zu importieren und zu erstellen, und beschränkt sich nicht auf Verarbeitungen.

So können Sie Ihre _Assets_, Ihre _Datensätze_, Ihre _Stakeholder_, Ihre _Sicherheitsmaßnahmen_ usw. eingeben.

Sie können [hier](https://docs.google.com/spreadsheets/d/1u_QLMbx9k4fFm7jBrpnt65i8fVfOzYz8/edit?usp=sharing\&ouid=117505938343554554786\&rtpof=true\&sd=true) die Excel-Tabelle zur Datenformatierung herunterladen, die für einen fehlerfreien Import erforderlich ist!

#### Standardimport

Um nicht jede Verarbeitung manuell ausfüllen zu müssen und alle möglichen Verzeichnisformate zu berücksichtigen, hat Dastra eine Methodik entwickelt, die auf dem Prinzip der **Aufteilung des Verzeichnisses in Datenbereiche** basiert. So werden 7 Schritte empfohlen, um ein bestehendes Verzeichnis vollständig in Dastra zu importieren.

{% hint style="info" %}
Diese Schritte sind zwar nicht obligatorisch, werden aber dringend empfohlen, insbesondere wenn das Verarbeitungsverzeichnis viele Verarbeitungen enthält.
{% endhint %}

Zögern Sie nicht, auch unsere Bibliothek von Verarbeitungsvorlagen zu konsultieren: [https://www.dastra.eu/de/data-processing/referentials](https://www.dastra.eu/de/data-processing/referentials)

## Schritt 1: Import der Verarbeitungsbezeichnungen

Um Ihre bestehenden Verarbeitungsbezeichnungen zu importieren, klicken Sie auf den Tab "Daten importieren" im Bereich Verzeichnis, Tab Verzeichnis:

![](../../.gitbook/assets/importz.png)

<figure><img src="../../.gitbook/assets/excel1.png" alt=""><figcaption></figcaption></figure>

Laden Sie dann eine Beispieldatei herunter, wie auf dem Bildschirm angezeigt.

![](../../.gitbook/assets/excel2.png)

Füllen Sie die heruntergeladene Datei mit Ihren Verarbeitungsbezeichnungen in der folgenden Reihenfolge aus:

| Spalte           | Beschreibung              | Mögliche Werte                                      |
| ---------------- | ------------------------- | --------------------------------------------------- |
| Ref              | Interne Referenz (String) |                                                     |
| Processing state | Status der Verarbeitung   | "Study", "BeingDeployed", "InProduction", "Stopped" |
| Label            | Name (String)             |                                                     |
| Description      | Beschreibung (String)     |                                                     |

Unten ein Beispiel einer Datei im geforderten Format, die importiert und per Drag-and-Drop in Dastra importiert werden kann:

{% file src="../../.gitbook/assets/sample-dataprocessing-18.csv" %}

Importieren Sie sie direkt in unsere Oberfläche per Drag-and-Drop und klicken Sie dann auf Fortfahren.

Das war's, Ihre Verarbeitungsbezeichnungen sind importiert!

## Schritt 2: Import des Asset-Referenzsystems

Um Ihre bestehenden Anwendungen/Assets zu importieren, klicken Sie auf den Tab "**Importieren**" im Modul "**Metadaten**", im Tab "**Assets**":

![](<../../.gitbook/assets/Assets importieren.png>)

Laden Sie dann eine Beispieldatei herunter, wie auf dem Bildschirm angezeigt. Füllen Sie die heruntergeladene Datei mit Ihren Anwendungen in der folgenden Reihenfolge aus:

| Spalte                     | Beschreibung                              | Mögliche Werte                          |
| -------------------------- | ----------------------------------------- | --------------------------------------- |
| Description                | Beschreibung (String)                     |                                         |
| Label                      | Name (String)                             |                                         |
| ApplicationState           | Anwendungsstatus (applicationstate)       | "InProduction""InDevelopment""Stopped"  |
| ApplicationType            | Anwendungstyp (applicationtype)           | "Software""WebApp""Saas""Module""Other" |
| HostingType                | Hosting-Typ (hostingtype)                 | "InHouse""OutSourced"                   |
| SupportType                | Support-Typ (supporttype)                 | "InHouse""OutSourced"                   |
| DevelopmentType            | Entwicklungstyp (developmenttype)         | "InHouse""OutSourced"                   |
| HostName                   | Hostname (String)                         |                                         |
| PrivacyByDesignImplemented | Privacy by Design implementiert (Boolean) | "true""false"                           |

Unten ein Beispiel einer Datei im geforderten Format, die importiert und per Drag-and-Drop in Dastra importiert werden kann:

{% file src="../../.gitbook/assets/sample-applications-example.xlsx" %}

Importieren Sie sie direkt in unsere Oberfläche per Drag-and-Drop und klicken Sie dann auf Fortfahren.

Das war's, Ihre Anwendungen sind importiert!

## Schritt 3: Import des Stakeholder-Referenzsystems

Wiederholen Sie das gleiche Verfahren wie zuvor aus dem Modul Metadaten im Tab Stakeholder. Unten ein Beispiel:

Ihr Stakeholder-Referenzsystem verzeichnet alle an einer Verarbeitung beteiligten Interessengruppen. Juristische Personen wie Auftragsverarbeiter, Kunden oder gemeinsame Verantwortliche sowie natürliche Personen wie Ansprechpartner der Verarbeitungen.

Dieses Referenzsystem dient als internes Verzeichnis im Mandanten. Für jeden Stakeholder können Sie einen charakterisierenden Typ definieren. Wenn Sie beispielsweise Ihr Auftragsverarbeiter-Verzeichnis hinzufügen möchten, fügen Sie alle Stakeholder hinzu, und jeder Auftragsverarbeiter muss einer Verarbeitung zugeordnet werden.

## Schritt 4: Import des Referenzsystems für Sicherheitsmaßnahmen

Wiederholen Sie das gleiche Verfahren wie zuvor aus dem Modul Metadaten im Tab Maßnahmen.

## Schritt 5: Import der Datenkategorien

Wiederholen Sie das gleiche Verfahren wie zuvor aus dem Modul Metadaten im Tab Datenkategorien.

## Schritt 6: Import des Datensatz-Referenzsystems

Wiederholen Sie das gleiche Verfahren wie zuvor aus dem Modul Metadaten im Tab Datensätze.

## Schritt 7: Aufbau der Verknüpfungen

Nachdem alle Referenzsysteme importiert wurden, bearbeiten Sie jede Verarbeitung und füllen Sie die Informationen auf Basis der importierten Daten aus, indem Sie der folgenden Anleitung folgen:

{% content-ref url="remplir-le-questionnaire/" %}
[remplir-le-questionnaire](remplir-le-questionnaire/)
{% endcontent-ref %}

Das war's, die Verknüpfungen sind aufgebaut!
