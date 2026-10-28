---
description: Funktionsweise der Nachrichtenvorlagen
---

# Nachrichtenvorlagen

## Anpassung der Nachrichtenvorlagen

Um Ihre Zeit zu optimieren und die Effizienz zu steigern, können Sie Nachrichtenvorlagen konfigurieren, die in den Modulen von Dastra wiederverwendet werden können.

### Verfügbare Arten von Nachrichtenvorlagen

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration31.png" alt=""><figcaption></figcaption></figure>

Die Vorlagentypen sind wie folgt:

*   **Nachricht in Betroffenenanfragen**

    Beim Austausch mit den Antragstellern können Sie Vorlagen speichern, um Zeit zu sparen. Zum Beispiel eine Vorlage für die Empfangsbestätigung der Anfrage.
*   **Aufgabe**

    Sie können den Inhalt der Aufgabenbeschreibung anpassen. Ideal, um bei sich wiederholenden Aufgaben Zeit zu sparen. Zum Beispiel, wenn Sie jemanden bitten, Informationen zu einer Datenverarbeitung einzugeben, können Sie dieselbe Nachrichtenvorlage wiederverwenden.
*   **Audits**

    Sie können die Einladungen zur Beantwortung eines Audits anpassen. Verwenden Sie hier eine Vorlage, um dieselbe Nachricht für alle Ihre Befragten einzugeben. Zum Beispiel können Sie Ihre Auftragsverarbeiter einladen, einen Überprüfungsaudit über die ordnungsgemäße Anwendung des Auftragsverarbeitungsvertrags auszufüllen, basierend auf einer Vorlage, die dem Image Ihrer Organisation entspricht.
*   **Eine Verarbeitung vervollständigen**

    Sie können einen Dastra-Nutzer einladen, eine Datenverarbeitung ab einem bestimmten Schritt zu vervollständigen. Schreiben Sie die Vorlage einmal oder wählen Sie eine Vorlage je nach Qualität des Empfängers (Jurist, IT-Leiter usw.), um Zeit zu sparen.
*   **Eine Datenschutzverletzung vervollständigen**

    Sie können einen Dastra-Nutzer einladen, eine Datenschutzverletzung ab einem bestimmten Schritt zu vervollständigen. Schreiben Sie die Vorlage einmal oder wählen Sie eine Vorlage je nach Qualität des Empfängers (Jurist, IT-Leiter usw.), um Zeit zu sparen.

### Erstellung der Vorlage

Die Vorlagenerstellung erfolgt entweder über die Mandant-Einstellungen oder direkt am Ort der Nachricht.

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration32.png" alt=""><figcaption><p>Erstellung über die Mandant-Einstellungen</p></figcaption></figure>

Klicken Sie auf Vorlage erstellen

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration33.png" alt=""><figcaption><p>Oberfläche zur Vorlagenerstellung</p></figcaption></figure>

Vergessen Sie nicht, Ihre Arbeit zu speichern!

### Benutzerdefinierte Variablen in den Vorlagen

Dastra ermöglicht es Ihnen, **die Vorlage automatisch mit benutzerdefinierten Variablen zu füllen**.

Das bedeutet, dass Sie automatisch Informationen zum mit der Vorlage verknüpften Objekt in den Text der Nachrichtenvorlage einfügen können.

Zum Beispiel kann in der Einladung zur Beantwortung eines Audits automatisch das Fälligkeitsdatum eines Audits übernommen werden.

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration34.png" alt=""><figcaption><p>Die benutzerdefinierten Felder der Einladungsnachricht zur Audit-Beantwortung</p></figcaption></figure>

Sie können so einfach dynamische Felder direkt in die Vorlage einfügen. Als Sprache für die Vorlagenerstellung verwenden wir die LiquidJS-Syntax.

Hier ist der vollständige Leitfaden: [die Tags](https://liquidjs.com/tags/overview.html) und [die Filter](https://liquidjs.com/filters/overview.html).

Um Status zu übersetzen, können Sie den benutzerdefinierten Filter getTranslation wie folgt verwenden \{{data | getTranslation: ''\}}. Beispiel: \{{data | getTranslation: 'dataSubjectRequestStates'\}}

### Detail der Variablenfelder:

#### Nachricht für Betroffenenanfragen:

• Titel der Anfrage (title)

• Geschlossen von (closedByUser)

• Organisationseinheit (area)

• Erstellt von (creator)

• Bearbeiter (operator)

• Sprache (locale)

• Archiviert (archived)

• Archiviert am (archivedDate)

• Personenkategorie (subjectCategory)

• Komplexe Anfrage (complex)

• Abschlussdatum (dateClosed)

• Zusätzliche Informationen (intern) (description)

• Nachricht der Anfrage (message)

• E-Mail (email)

• Telefonnummer (phoneNumber)

• Vorname (givenName)

• Nachname (familyName)

• Aktualisiert am (dateUpdate)

• Ref. Id (refId)

• Nutzer-ID (userId)

• Schließungsgrund (closedReason)

• Beschreibung der Schließung (closedReasonDescription)

• Ablaufdatum (expiryTime)

• Adresse (address)

• Postleitzahl (zipCode)

• Stadt (city)

• Land (countryCode)

• E-Mail-Validierungsdatum (emailValidationDate)

• E-Mail validiert (mailValidated)

• Quell-URL (referrerUrl)

• Identität validiert (identityValidated)

• Datum der Identitätsvalidierung (dateIdentityValidated)

• Anfrage-ID (demandId)

• Status (state)

• Datum (dateCreation)

• Schritt (workFlowStep)

• Erfassungskanal (channel)

• Rechtearten (purposes)

• Nachrichten (nbMessages)

• Verbleibende Tage (remainingDays)

• Schließungsfrist (Tage) (closingTime)

• Tags (tags)

#### Aufgabenbeschreibung:

• Projekt (project)

• Iteration (iteration)

• Reihenfolge (order)

• Inhaber (owner)

• Organisationseinheit (area)

• Erstellt von (creator)

• Verbleibende Tage (remainingDays)

• Schließungsfrist (Tage) (closingTime)

• Anzahl Unteraufgaben (nbSubTasks)

• Anzahl geschlossener Unteraufgaben (nbSubTasksClosed)

• Id (id)

• Interne Referenz (ref)

• Archiviert (archived)

• Name (label)

• Beschreibung (descriptionHtml)

• Verknüpft mit (objectType)

• Status (state)

• Frist (deadline)

• Startdatum (startDate)

• Geschlossen am (dateClosed)

• Aktiviert am (dateActivated)

• Erstellt am (dateCreation)

• Aktualisiert am (dateUpdate)

• Quelle (source)

• test (customFields.test)

• Liste (customFields.liste)

• Einfaches Kontrollkästchen (customFields.case\_a\_cocher\_simple)

• Tags (tags)

• Schritt (workFlowStep)

• Priorität (priority)

• Zugewiesen an (assignedToUser)

#### Einladungen zur Beantwortung eines Audit-Fragebogens:

• Vorlage (template)

• Datum des nächsten Audits (dateNextAudit)

• Audit-Dauer (auditDurationDays)

• Anz. Korrekturen (nbCorrections)

• Anz. Validierungen (nbValidations)

• Tage bis zum nächsten Audit (nextAuditDaysRemaining)

• Id (id)

• Name (label)

• Ältere Version (isRevision)

• Versionsname (revisionDescription)

• Archiviert (archived)

• Überfällig (isOverdue)

• Organisationseinheit (area)

• Aktualisiert am (dateUpdate)

• Archiviert am (archivedDate)

• Score (readiness)

• Punkte (score)

• Vervollständigungsrate (%) (completionRate)

• Anz. Antworten (nbAnswers)

• Anz. Fragen (nbQuestions)

• Verantwortliche (owners)

• Befragte (respondants)

• Aktionsplan erstellt am (actionPlanDate)

• Status (state)

• Startdatum (startDate)

• Abgeschlossen am (responseDate)

• Veröffentlichungsdatum (publishedDate)

• Erstellt am (dateCreation)

• Verknüpftes Objekt (objectLabel)

• Frist (deadline)

#### Einladungen zur Vervollständigung einer Verarbeitung:

Organisationseinheit (area)

Schritt (workflowStep)

Id (id)

Quelle (source)

Name (label)

Status (state)

Erstellt am (dateCreation)

Archivierungsdatum (dateArchived)

Archiviert (archived)

Versionsbeschreibung (versionDescription)

Typ (processingType)

Organisationseinheit (areaId)

Assets (assets)

Interne Referenz (ref)

Verarbeitungsstatus (processingState)

Dokumentation (descriptionHtml)

Tags (tags)

Inhaber der Verarbeitung (owner)

Beteiligte (stakeHolders)

DSFA erforderlich (isDPIARequired)

DSFA-Datum (dpiaDate)

Von DSFA befreit (dpiaExemption)

Empfänger (recipients)

Verantwortliche / Kunden (dataControllers)

Datensätze (dataRetentionRules)

Zwecke (purposes)

Maßnahmen (securityMeasures)

Kategorien betroffener Personen (personCategories)

DSFA (customFields.aipd)

Fortschritt (%) (progression)

Qualität (%) (quality)

Sensibilität (%) (sensitivity)

Erstellt von (creatorUser)

Bereitstellungsdatum (dateDeployment)

Veröffentlichungsdatum (datePublication)

Letzte Änderung (dateUpdate)

Beschreibung (description)

#### Einladung zur Vervollständigung einer Verletzung:

Name (label)

ID (id)

Datenlokalisierung (location)

Verlust der Vertraulichkeit (access)

Verlust der Integrität (integrity)

Verlust der Verfügbarkeit (availability)

Ursache (reason)

Quelle (source)

Beteiligte Auftragsverarbeiter (processorInvolved)

Auftragsverarbeiter (processors)

Sensible Daten (sensitiveData)

Wahrscheinlichkeitsscore (probabilityScore)

Auswirkungsniveau (impactScore)

Score (score)

Risikoniveau (riskLevel)

Volumen der Datensätze (dataVolume)

Datenträger (dataSupport)

Kommunikation erfolgt? (communicationDone)

Grund für fehlende Kommunikation (noCommunicationReason)

Zeitraum (period)

Startdatum (startDate)

Enddatum (endDate)

Feststellungsdatum (constatationDate)

Meldefrist an die Aufsichtsbehörde (notificationDueTime)

Bearbeiter (operator)

Schritt (workFlowStep)

Organisationseinheit (area)

Erstellt am (dateCreation)

Aktualisiert am (dateUpdate)

Post-Mortem durchgeführt (postMortemDone)

Tags (tags)

Anmerkungen (complementaryInformations)

Abschlussdatum (dateClosed)

Archivierungsdatum (dateArchived)

Erstellt von (creator)
