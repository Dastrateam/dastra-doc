---
description: Hoe berichtsjablonen werken
---

# Berichtensjablonen

## Berichtsjablonen aanpassen



Om tijd te besparen en de efficiëntie te verhogen, kunt u berichtsjablonen instellen voor hergebruik in Dastra-modules.



### Typen berichtsjablonen beschikbaar&#x20;

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

De sjabloontypen zijn als volgt:

**Bericht in verzoeken om rechten**

    Wanneer je omgaat met aanvragers, kun je tijd besparen door sjablonen op te slaan. Bijvoorbeeld een sjabloon voor het bevestigen van de ontvangst van het verzoek.
* Taak

    U kunt de inhoud van een taakbeschrijving aanpassen. Ideaal om tijd te besparen op repetitieve taken. Als je bijvoorbeeld iemand vraagt om gegevens in te vullen voor een gegevensverwerkingstaak, kun je dezelfde berichtsjabloon &#x20 hergebruiken;
* Uitnodigingen

    Je kunt uitnodigingen om te reageren op een audit personaliseren. Gebruik hier een sjabloon om hetzelfde bericht in te voeren voor al je respondenten. U kunt bijvoorbeeld uw onderaannemers uitnodigen om een audit uit te voeren om de correcte toepassing van het onderaannemingscontract te controleren met behulp van een sjabloon die is gemaakt naar het beeld van uw organisatie.
* Een behandeling voltooien

    U kunt een Dastra-gebruiker uitnodigen om een gegevensverwerkingsstap te voltooien. Schrijf het sjabloon eenmalig of selecteer een sjabloon op basis van de kwaliteit van de ontvanger (advocaat, IT-afdeling, enz.) om tijd te besparen;
* **Volledig een gegevensinbreuk**

    U kunt een Dastra-gebruiker uitnodigen om een gegevensinbreuk te voltooien vanuit één stap. Schrijf het sjabloon één keer of selecteer een sjabloon op basis van de kwaliteit van de ontvanger (advocaat, CIO, enz.) om tijd te besparen &#x20;



### Sjablonen maken

Sjablonen worden gemaakt vanuit de werkruimte-instellingen of vanuit de berichtlocatie.&#x20;

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption><p>Maken vanuit werkruimte-instellingen</p></figcaption></figure>

Klik op Sjabloon maken

<figure><img src="../../.gitbook/assets/image (4) (1) (2).png" alt=""><figcaption><p>Sjablooninterface maken</p></figcaption></figure>

Vergeet niet uw werk op te slaan!

### Aangepaste variabelen in sjablonen

Met Dastra kunt u **automatisch het sjabloon vullen met aangepaste variabelen**.&#x20;

Dit betekent dat u automatisch informatie over het object dat gekoppeld is aan het sjabloon kunt opnemen in de tekst van het berichtsjabloon &#x20;

Zo is het bijvoorbeeld mogelijk om in de uitnodiging om te reageren op een audit automatisch de vervaldatum van een audit op te nemen &#x20;

<figure><img src="../../.gitbook/assets/image (2) (1) (2).png" alt=""><figcaption><p>Aangepaste velden in het bericht voor de uitnodiging om te reageren op een audit</p></figcaption></figure>



Dit maakt het eenvoudig om dynamische velden direct aan de sjabloon toe te voegen. Als taal voor het maken van sjablonen gebruiken we de liquidJS.&#x20 synthax;

Hier is de volledige handleiding: [tags ](https://liquidjs.com/tags/overview.html)en [filters](https://liquidjs.com/filters/overview.html).&#x20;

Om statussen te vertalen kun je de getTranslation custom filter als volgt gebruiken \{{data | getTranslation: ''\}}. Voorbeeld: \{{data | getTranslation: 'dataSubjectRequestStates'\}}

### Details van variabele velden :&#x20;

#### Rechten oefening verzoekbericht :&#x20;

- Titel verzoek

- Gesloten door (closedByUser)

- Organisatorische eenheid (gebied)

- Gemaakt door (maker)

- Gebruiker

- Taal (locale)

- Gearchiveerd

- Gearchiveerd op (gearchiveerdeDatum)

- OnderwerpCategorie

- Complex verzoek

- Datum gesloten (dateClosed)

- Aanvullende (interne) informatie (omschrijving)

- Verzoek bericht (message)

- E-mailadres (email)

- Telefoonnummer (phoneNumber)

- Voornaam (givenName)

- Achternaam (familyName)

- Bijgewerkt op (dateUpdate)

- Ref. id (refId)

- Gebruikers-ID (userId)

- Reden voor afsluiting (closedReason)

- Beschrijving van de afsluiting (closedReasonDescription)

- Vervaldatum (expiryTime)

- Adres (address)

- Postcode (zipCode)

- Stad (city)

- Land (countryCode)

- Valideringsdatum e-mail (emailValidationDate)

- Gevalideerde e-mail (mailValidated)

- Url bron (referrerUrl)

- IdentiteitGevalideerd

- Identiteitsvalidatiedatum (dateIdentityValidated)

- Verzoek id (requestId)

- Status (state)

- Datum (dateCreation)

- Stap (workFlowStep)

- Collectie kanaal (channel)

- Soorten rechten (purposes)

- Berichten (nbMessages)

- Resterende dagen (remainingDays)

- Sluitingstijd (dagen) (closingTime)

- Tags (Tags)



#### Beschrijving van een taak:&#x20;

- Project (project)

- Iteratie (iteratie)

- Opdracht (order)

- Eigenaar (owner)

- Organisatorische eenheid (area)

- Gemaakt door (creator)

- Resterende dagen (remainingDays)

- Eindtijd (dagen) (closingTime)

- Aantal subtaken (nbSubTasks)

- Aantal subtaken gesloten (nbSubTasksClosed)

- Id (id)

- Interne referentie (ref)

- Gearchiveerd (archived)

- Naam (label)

- Beschrijving (descriptionHtml)

- Geassocieerd met (objectType)

- Status (status)

- Uiterste datum (deadline)

- Startdatum (startDate)

- Gesloten op (dateClosed)

- Geactiveerd op (dateActivated)

- Gemaakt op (dateCreation)

- Bijgewerkt op (dateUpdate)

- Bron (source)

- test (customFields.test)

- LIste (customFields.liste)

- Eenvoudige checkbox (customFields.case_eenvoudige_checkbox)

-  Tags (tags)

- WorkFlowStap (workFlowStep)

- Prioriteit (priority)

- Toegewezen aan (assignedToUser)



#### Uitnodigingen om een controlevragenlijst in te vullen :&#x20;

- Model (template)

- Datum volgende audit (dateNextAudit)

- Duur van de audit (auditDurationDays)

- Aantal correcties (nbCorrections)

- Aantal validaties (nbValidations)

- Dagen voor volgende audit (nextAuditDaysRemaining)

- Id (id)

- Naam (label)

- Oude versie (isRevision)

- Versie naam (revisionDescription)

- Gearchiveerd (archived)

- Verouderd (isOverdue)

- Organisatorische eenheid (area)

- Bijgewerkt op (dateUpdate)

- Gearchiveerd op (archivedDate)

- Score (readiness)

- Punten (score)

- Voltooiingspercentage (%) (completionRate)

- Aantal antwoorden (nbAnswers)

- Aantal vragen (nbQuestions)

- Eigenaars (owners)

- Respondenten (respondants)

- Actieplan gegenereerd op (actionPlanDate)

- Status (status)

- Startdatum (startDate)

- Afgerond op (responseDate)

- Datum gepubliceerd (publishedDate)

- Gemaakt op (dateCreation)

- Bijgevoegd object (objectLabel)

- Uiterste datum (deadline)



#### Uitnodigingen om een behandeling te voltooien:&#x20;

Organisatorische eenheid (area)

Stap (workflowStep)

Id (id)

Bron (source)

Naam (label)

Status (status)

Aangemaakt op (dateCreation)

Datum gearchiveerd (dateArchived)

Gearchiveerd (archived)

Versiebeschrijving (versionDescription)

Type (processingType)

Organisatorische eenheid (areaId)

Activa (assets)

Interne referentie (ref)

Verwerkingsstatus (processingState)

Documentatie (descriptionHtml)

Tags (tags)
 
Eigenaar verwerking (owner)

Belanghebbenden (stakeHolders)

PIA vereist (isDPIARequired)

PIA datum (dpiaDate)

Is vrijgesteld van PIA (dpiaExemption)

Ontvangers (recipients)

Voor de verwerking verantwoordelijken / klanten (dataControllers)

Gegevensreeksen (dataRetentionRules)

Doeleinden (purposes)

Maatregelen (securityMeasures)

Categorieën van betrokkenen (personCategories)

AIPD (customFields.aipd)

Progressie (%) (progression)

Kwaliteit (%) (quality)

Gevoeligheid (%) (sensitivity)

Gemaakt door (creatorUser)

Plaatsingsdatum (dateDeployment)

Publicatiedatum (datePublication)

Laatste wijziging (dateUpdate)

Beschrijving (description)



#### Uitnodiging om een overtreding te voltooien:&#x20;

Naam (label)

ID (id)

Locatie van gegevens (location)

Verlies van vertrouwelijkheid (access)

Verlies van integriteit (integrity)

Verlies van beschikbaarheid (availability)

Oorzaak (reason)

Bron (source)

Betrokken onderaannemers (processorInvolved)

Verwerkers (processors)

Gevoelige gegevens (sensitiveData)

Waarschijnlijkheidsscore (probabilityScore)

Impact score (impactScore)

Score (score)

RisicoLevel (riskLevel)

Volume gegevensrecords (dataVolume)

Gegevensondersteuning (dataSupport)

Communicatie uitgevoerd (communicationDone)

Reden voor geen communicatie (noCommunicationReason)

Periode (period)

Begindatum (startDate)

Einddatum (endDate)

Datum bevinding (findingDate)

Uiterste datum voor kennisgeving aan de toezichthoudende autoriteit (notificationDueTime)

Exploitant (operator)

Stap (workFlowStep)

Organisatorische eenheid (area)

Gemaakt op (dateCreation)

Bijgewerkt op (dateUpdate)

Post-mortem gedaan (postMortemDone)

Tags (tags)

Opmerkingen (complementaryInformations)

Datum gesloten (dateClosed)

Datum gearchiveerd (dateArchived)

Gemaakt door (creator)
