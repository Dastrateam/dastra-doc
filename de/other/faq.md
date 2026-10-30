---
description: >-
  Die FAQ jedes Dastra-Moduls an einem Ort und Antworten auf allgemeine Fragen:
  Logos, Import eines bestehenden Verzeichnisses, Löschen einer
  Verarbeitungstätigkeit, fehlende Elemente und der lokale Speicher des
  Browsers.
---

# FAQ

Diese Seite ist der Einstieg zu den in der Dokumentation beantworteten Fragen. Sie listet die FAQ jedes Moduls auf und beantwortet danach die allgemeinen Fragen.

## FAQ der Module

* [FAQ Erste Schritte](../getting-started/setup/faq.md): Teams und Organisationseinheiten als Stakeholder, Export und Import von Organisationseinheiten, Änderung des Datenschutzbeauftragten und Verwaltung der Inhaber der Organisation.
* [FAQ Allgemeine Funktionen](../features/general/faq.md): Datenkategorien importieren.
* [FAQ KI-Assistent](../features/general/ai-assistant/faq.md): Datenschutz und Daten, Qualität und Zuverlässigkeit, Konfiguration und Zugriff sowie die KI-Verordnung.
* [FAQ Verarbeitungsverzeichnis](../features/ropa/faq.md): Änderungsverlauf, Löschen, Datenkategorien im Lesemodus, Sammeländerungen bei Stakeholdern, Duplizieren in einen anderen Mandanten, Typwechsel und Fehlermeldungen.
* [FAQ Fragebögen](../features/questionnaires/faq.md): DSFA für mehrere Verarbeitungstätigkeiten, E-Mail-Vorlagen, externe Befragte, vorgeschlagene Aufgaben, Veröffentlichen von Vorlagen, Fehlermeldungen und Grenzen.
* [FAQ Risiken](../features/risks/faq.md): das fehlende Menü, ein Risiko zum nächsten Schritt verschieben, anfängliches, Restrisiko und aktuelles Risiko, die Risikoskala ändern.
* [FAQ Aufgaben](../features/tasks/faq.md): Aufgaben einem Projekt zuordnen, eine Aufgabe löschen, den Arbeitsaufwand erfassen und nachfassen.
* [FAQ Anfragen](../features/requests/faq.md): E-Mails zum Abschluss, der sichere Bereich der anfragenden Person und die E-Mail-Prüfung, Länge von Nachrichten und Cookies auf der Erfassungsseite.
* [FAQ Zapier](../features/integrations/zapier/faq.md): vertraglicher Status von Zapier, wer den Vertrag unterzeichnet, und die Dokumentation zur Zuverlässigkeit.

Bei Problemen statt Fragen siehe [Bekannte Probleme](known-problems.md) und die [bekannten Probleme bei SSO](../features/settings/sso/known-problems.md).

## Wie ändere ich das Logo der Organisation in Dastra?

Die Organisation hat kein Logo. Das Bild oben rechts auf dem Bildschirm, neben Ihrem Namen und dem Namen der Organisation, ist das Bild Ihres Nutzerkontos. Um es zu ändern, öffnen Sie oben rechts Ihr Profilmenü, klicken Sie auf **Nutzerprofil** und laden Sie ein neues Bild hoch.

Wie Sie das in den Exporten verwendete Logo anpassen, lesen Sie bei der nächsten Frage.

## Wie ändere ich das Logo des Mandanten in Dastra?

Öffnen Sie die Mandanteneinstellungen und dann den Bereich **Design und Marke**. Sie können ein quadratisches und ein rechteckiges Logo hochladen und die **Markenfarbe** und die **Akzentfarbe** wählen. Mit diesen Elementen passen Sie die Exporte von Dastra an Ihre Marke an.

Dieser Bereich ist den Inhabern der Organisation vorbehalten.

## Wie importiere ich mein Verarbeitungsverzeichnis im CNIL-Format?

Sie können ein bestehendes Verarbeitungsverzeichnis im CNIL-Format in Dastra importieren. Der Import umfasst mehrere Schritte:

1. Importieren Sie die Bezeichnungen der Verarbeitungstätigkeiten.
2. Importieren Sie die Datenkategorien.
3. Importieren Sie die Stakeholder.
4. Importieren Sie die Sicherheitsmaßnahmen.
5. Stellen Sie in den Verarbeitungstätigkeiten die Verknüpfungen zwischen diesen Objekten her.

Zum Import von Verarbeitungstätigkeiten siehe [Verzeichnis exportieren / importieren](../features/ropa/export-import.md). Wenn Sie Hilfe beim Import Ihres Verzeichnisses benötigen, [wenden Sie sich an den Support](../getting-started/support/request.md).

## Wie lösche ich eine Verarbeitungstätigkeit?

Das Löschen erfolgt in zwei Schritten, damit nichts versehentlich gelöscht wird. Verschieben Sie die Verarbeitungstätigkeit zuerst mit **In den Papierkorb verschieben** in den Papierkorb. Zeigen Sie dann in den Filtern mit **Papierkorb anzeigen** den Papierkorb an und wählen Sie **Löschen**, um sie endgültig zu löschen, oder **Wiederherstellen**, um sie wieder in das Verzeichnis aufzunehmen.

Das vollständige Vorgehen steht in der [FAQ zum Verzeichnis](../features/ropa/faq.md#wie-loscht-man-eine-verarbeitungstatigkeit).

## Ich finde bestimmte Elemente nicht. Was kann ich tun?

Wenn Sie ein Element nicht finden, auf das Sie Zugriff haben sollten, kann es aus einem der folgenden Gründe ausgeblendet sein:

1. Ein Filter ist aktiv und schränkt die Anzeige ein. Die Anzahl der aktiven Filter steht in Klammern auf der Schaltfläche, zum Beispiel „(1)“. Klicken Sie auf **Filter löschen**.

   <figure><img src="../.gitbook/assets/other-faq-1.png" alt="Liste des Verzeichnisses mit einem aktiven Filter und der Schaltfläche Filter löschen (1)"><figcaption><p>Ein aktiver Filter schränkt die Liste ein</p></figcaption></figure>
2. Das Element ist mit einer Organisationseinheit verknüpft, auf die Sie keinen Zugriff haben oder für die Ihnen die nötigen Rechte fehlen. Wenden Sie sich an die Verantwortlichen Ihres Mandanten.
3. Das Element befindet sich im Papierkorb und erscheint deshalb nicht mehr in der Standardliste. Klicken Sie auf **Filter** und aktivieren Sie **Papierkorb anzeigen**.

   <figure><img src="../.gitbook/assets/ropa-faq-3.png" alt="Bereich Filter des Verzeichnisses mit der Option Papierkorb anzeigen"><figcaption><p>Den Papierkorb anzeigen</p></figcaption></figure>
4. Fehlerhafte Einstellungen sind in Ihrem Browser gespeichert. Öffnen Sie zur Prüfung Dastra in einem privaten Browserfenster. Wenn das Problem verschwindet, leeren Sie den lokalen Speicher Ihres Browsers nach dem Vorgehen der nächsten Frage.

## Wie leere ich den lokalen Speicher des Browsers?

Der lokale Speicher (localStorage) enthält Daten, die der Browser aufbewahrt, damit Dastra funktioniert und sich Ihre Einstellungen merkt, zum Beispiel Ihre Filter. Bei einem Anzeigeproblem kann der Support Sie bitten, ihn zu leeren.

Sie können auch die Schaltfläche **Präferenzdaten zurücksetzen** in Ihrem Nutzerprofil verwenden, die unter [Bekannte Probleme](known-problems.md) beschrieben ist.

### Google Chrome

1. Öffnen Sie das Browsermenü und dann **Weitere Tools** > **Entwicklertools** (F12).
2. Öffnen Sie den Tab **Application** und dann **Storage** > **Local storage**.
3. Klicken Sie mit der rechten Maustaste auf die Dastra-Adresse und wählen Sie **Clear**.
4. Aktualisieren Sie die Seite (F5).

### Mozilla Firefox

1. Öffnen Sie das Browsermenü und dann **Weitere Tools** > **Web-Entwickler** > **Entwicklertools** (F12).
2. Öffnen Sie den Tab **Speicher** und dann **Lokaler Speicher**.
3. Klicken Sie mit der rechten Maustaste auf die Dastra-Adresse und wählen Sie **Alles löschen**.
4. Aktualisieren Sie die Seite (F5).
