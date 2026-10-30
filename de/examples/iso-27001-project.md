---
description: >-
  Begleiten Sie die Brightmoor Retail Group durch ein ISO-27001-Compliance-Projekt
  in Dastra, vom Framework und vom Scope bis zur Testkampagne und zu den Audits.
---

# ISO-27001-Projekt

Die Brightmoor Retail Group möchte für ihren Onlineshop die Zertifizierung nach ISO/IEC 27001 erreichen. Emma Walsh, die Datenschutzbeauftragte, leitet das Projekt, und Liam O'Connor verfolgt es. Dieses Beispiel führt durch die sechs Phasen eines Compliance-Projekts, mit den echten Bildschirmen und Bezeichnungen der Anwendung.

Dastra bereitet die Arbeit vor und verfolgt sie. Das Zertifikat selbst stellt eine akkreditierte Zertifizierungsstelle außerhalb von Dastra aus.

## Der Weg im Überblick

| Phase | Was Brightmoor tut | Referenz |
| --- | --- | --- |
| **Scope** | Legt einen Scope fest und erstellt das Projekt | [Scopes](../features/compliance/scopes.md), [Projekte](../features/compliance/projects/README.md) |
| **Design** | Fügt das Framework ISO 27001 hinzu und importiert seine Kontrollen und Risiken | [Projektgestaltung](../features/compliance/projects/design.md) |
| **Implementierung** | Schließt nicht zutreffende Kontrollen aus, weist Inhaber zu, konfiguriert Tests | [Projektimplementierung](../features/compliance/projects/implement.md) |
| **Überwachung** | Führt eine Testkampagne durch und sammelt Nachweise | [Compliance-Überwachung](../features/compliance/projects/monitoring.md) |
| **Internes Audit** | Auditiert das Framework und meldet Lücken | [Audits](../features/compliance/projects/audits.md) |
| **Abschlussaudit** | Hält den Stand der Compliance vor der Zertifizierung fest | [Audits](../features/compliance/projects/audits.md) |

## 1. Das Framework vorbereiten

Ein Framework enthält die Anforderungen, Kontrollen, Tests, Risiken und Bedrohungen eines Standards. Brightmoor geht von der Dastra-Vorlage aus.

1. Öffnen Sie im Menü **Compliance** > **Bibliothek** > **Frameworks**.
2. Klicken Sie auf **Ein Framework erstellen** und wählen Sie dann **Basierend auf einer Vorlage**.
3. Suchen Sie nach ISO 27001 und wählen Sie die Vorlage aus. Prüfen Sie die in den Details angezeigte Anzahl der Anforderungen, Kontrollen, Risiken und Bedrohungen.
4. Bestätigen Sie den Import.

Das Framework liegt nun in der Bibliothek und ist bearbeitbar. Das Erstellen verbraucht einen Framework-Credit des Kontos (siehe [Import und Dastra-Vorlagen](../features/compliance/library/frameworks/import.md)).

## 2. Den Scope festlegen

Der Scope beantwortet eine Frage: Welche Organisationseinheiten deckt das Projekt ab? Brightmoor zertifiziert nur den Onlineshop.

1. Öffnen Sie **Compliance** > **Scope** und erstellen Sie einen Scope mit dem Namen „Online shop“.
2. Wählen Sie die Organisationseinheiten „Group IT“ und „E-commerce“ aus. Ein Scope braucht mindestens eine Einheit.

## 3. Das Projekt erstellen

1. Öffnen Sie **Compliance** > **Projekte**, dann **Alle Projekte**, und klicken Sie auf **Projekt erstellen**.
2. Geben Sie „ISO 27001 certification“ als **Titel** ein und wählen Sie den **Geltungsbereich** „Online shop“. Klicken Sie auf **Weiter**.
3. Fügen Sie unter **Weisen Sie Nutzer dem Projekt zu** Emma Walsh mit der Rolle **Genehmiger** und Liam O'Connor mit der Rolle **Informiert** hinzu. Klicken Sie auf **Hinzufügen**.

Das Projekt öffnet sich auf seiner Übersicht in der Phase **Scope**. Der Assistent oben zeigt die **Checkliste** der Phase, und die Schaltfläche **Move to phase** erscheint, sobald alle Schritte erledigt sind.

## 4. Phase Design: die Kontrollen importieren

Verschieben Sie das Projekt in die Phase **Design** und folgen Sie der Checkliste.

1. Fügen Sie das Framework ISO 27001 zum Projekt hinzu. Behalten Sie die vorausgewählte Version unter **Zu installierende Version** bei.
2. Importieren Sie alle Kontrollen des Frameworks. Die Kontrollen sind standardmäßig als umgesetzt markiert, und ihre Tests werden mit dem Status **Beweis fehlt** angehängt.
3. Fügen Sie die Risiken des Frameworks zum Projekt hinzu. Sie sind die Grundlage der anfänglichen Risikobewertung.

Fügt Brightmoor später ein weiteres Framework hinzu, etwa die DSGVO, erkennt Dastra die gemeinsamen Kontrollen und importiert sie nur einmal (siehe [Projektgestaltung](../features/compliance/projects/design.md#4.-kontrollen-zwischen-frameworks-gemeinsam-nutzen)).

<figure><img src="../.gitbook/assets/examples-iso-1.png" alt="Übersicht des Projekts ISO 27001 certification mit der Framework-Karte und der Checkliste des Assistenten"><figcaption><p>Das Projekt in der Phase Design</p></figcaption></figure>

## 5. Phase Implementierung: die Kontrollen mit Leben füllen

1. Schließen Sie die Kontrollen aus, die nicht zutreffen. Brightmoor hostet alles in der Cloud, sodass Kontrollen zum eigenen Rechenzentrum außerhalb des Scopes liegen. Setzen Sie im Tab **Kontrollen** den **Status der Überprüfung** auf **Exklusiv** und füllen Sie **Bitte erläutern Sie, warum diese Kontrolle ausgeschlossen werden sollte.** aus. Die Begründung gelangt in die Anwendungserklärung und in die Audits.
2. Weisen Sie Inhaber zu. Klicken Sie im Tab **Anforderungen** auf die Nutzerschaltfläche einer Anforderung. Wählen Sie unter **Weisen Sie allen Kontrollen und Tests einen Inhaber zu** den Inhaber aus und klicken Sie auf **Bestätigen**. Sophie Becker übernimmt die Anforderungen zur Zugriffskontrolle, Noah Martin die Anforderungen zum Betrieb.
3. Konfigurieren Sie die Tests. Legen Sie für jeden Test das Verfahren, die Häufigkeit und den Inhaber fest. Ein Test ist manuell oder über einen Konnektor automatisiert (siehe [Tests](../features/compliance/library/tests.md)).
4. Bewerten Sie die Risiken. Legen Sie im Tab **Risiken** die anfängliche und die Restbewertung jedes Risikos fest und wählen Sie seine Behandlung. Die Ansicht **Kartografie** zeigt die Matrizen des anfänglichen, aktuellen und Restrisikos nebeneinander.

Die Checkliste der Phase lautet **Configure at least one control**, **Configure automated tests**, **Assess your risks** und **Assign owners to tests**.

## 6. Phase Überwachung: die Nachweise sammeln

Verschieben Sie das Projekt in die Phase **Überwachung**. Nachweise, die in einer anderen Phase hinzugefügt werden, lösen eine Warnung aus.

1. Öffnen Sie den Tab **Testkampagnen** und klicken Sie auf **Erstellen Sie eine Testkampagne**.
2. Geben Sie die **Bezeichnung der Kampagne** „First evidence collection“ ein und wählen Sie alle Tests aus, die auf Nachweise warten.
3. Prüfen Sie, dass jeder Test einen Inhaber hat. Fehlt bei einigen einer, warnt Dastra Sie: Verwenden Sie **Tests ohne Inhaber anzeigen**.
4. Starten Sie die Kampagne und klicken Sie auf **Einladungen versenden**, um die Inhaber zu benachrichtigen, bei Bedarf mit einer Nachricht.

Jeder Inhaber öffnet **Meine Tests**, liest das **Testverfahren**, fügt den Nachweis mit **Nachweis hinzufügen** hinzu und klickt auf **Test bestätigen**. Dieselbe Datei kann als Nachweis für mehrere Tests dienen.

Brightmoor verfolgt die Kennzahlen **Teststatus** und **Aktualität der Tests** in der Übersicht. Die Checkliste verlangt mindestens 80 % bestandene Tests vor der nächsten Phase.

ISO/IEC 27001 verlangt eine Anwendungserklärung. Öffnen Sie auf der Framework-Karte das Menü **⋯** und klicken Sie auf **Anwendungserklärung exportieren**. Die XLSX-Datei listet jede Kontrolle mit ihrer Anwendbarkeit, ihrer Begründung und ihrem Umsetzungsstatus auf.

## 7. Internes Audit

Verschieben Sie das Projekt in die Phase **Internes Audit**. ISO/IEC 27001 verlangt interne Audits in planmäßigen Abständen.

1. Klicken Sie im Tab **Audits** auf **Neues Audit erstellen** und wählen Sie das Framework ISO 27001.
2. Geben Sie den **Namen** „ISO 27001 internal audit“ ein, wählen Sie Sophie Becker unter **Auditoren**, setzen Sie die **Audit-Phase** auf **Pre-audit** und füllen Sie **Startdatum** und **Frist** aus.
3. Lassen Sie **Als aktives Audit definieren** eingeschaltet und klicken Sie dann auf **Bestätigen**.
4. Klicken Sie auf **Das Audit abschließen** und bewerten Sie jede Anforderung als **Compliance**, **Teilweise konform**, **Nicht konform** oder **Nicht zutreffend**, mit einem **Kommentar**.
5. Ist der Nachweis eines Tests schwach, klicken Sie auf **Fehler melden**, wählen Sie den **Schweregrad** und beschreiben Sie das Problem. Aktivieren Sie im Tab **Fehlerprüfungen** die gemeldeten Tests und klicken Sie auf **Tests ungültig machen** und dann auf **Re launch a test campaign**, damit die Inhaber ihre Nachweise aktualisieren.
6. Sind alle Anforderungen bewertet, klicken Sie auf **Abschluss der Prüfung** und schreiben Sie die **Abschließende Bewertung des Audits**.

<figure><img src="../.gitbook/assets/examples-iso-2.png" alt="Dashboard des internen Audits ISO 27001 mit seinem Fortschritt und dem Tab Fehlerprüfungen"><figcaption><p>Das Dashboard des internen Audits</p></figcaption></figure>

## 8. Abschlussaudit

Verschieben Sie das Projekt in die Phase **Abschlussaudit** und erstellen Sie ein neues Audit mit der Audit-Phase **Final audit**. Bewerten Sie die Anforderungen anhand der verbesserten Nachweise erneut und schließen Sie dann das Audit ab.

Der Compliance-Anteil pro Framework erscheint in der Projektübersicht und unter **Compliance** > **Statistiken**. Brightmoor exportiert das Audit, um die Nachweise an die Zertifizierungsstelle zu übergeben, und kann das Projekt in seinem Trust Center anzeigen (siehe [Ihr Trust Center konfigurieren](../features/trust-center/configuration/README.md)).
