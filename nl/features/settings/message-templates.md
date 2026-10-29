---
description: >-
  Maak herbruikbare berichtsjablonen voor verzoeken van betrokkenen, taken,
  vragenlijsten, verwerkingsactiviteiten en datalekken.
---

# Berichtsjablonen

Berichtsjablonen besparen u tijd: u schrijft ze één keer en gebruikt ze opnieuw in de modules van Dastra. Open **Instellingen voor werkruimte** > **Modellen** om ze te beheren. Deze menuvermelding is zichtbaar voor gebruikers met het schrijfrecht op berichtsjablonen, voor alle items of voor hun eigen items.

## Soorten berichtsjablonen

Elk soort sjabloon heeft zijn eigen tabblad op de pagina. De tabbladen die u ziet, hangen af van de modules in uw abonnement.

<figure><img src="../../.gitbook/assets/settings-message-templates-1.png" alt="De lijst met berichtsjablonen met de tabbladen per soort en de knop Maak een sjabloon"><figcaption><p>De lijst met berichtsjablonen, tabblad Bericht voor het uitoefenen van rechten</p></figcaption></figure>

* **Bericht voor het uitoefenen van rechten**: om tijd te besparen bij uw uitwisselingen met aanvragers. Bijvoorbeeld een sjabloon om de ontvangst van een verzoek te bevestigen.
* **Taak**: om de inhoud van een taakbeschrijving aan te passen, bijvoorbeeld wanneer u regelmatig iemand vraagt details over een verwerkingsactiviteit in te vullen.
* **Uitnodiging voor audits**: om de uitnodigingen om een vragenlijst te beantwoorden aan te passen. Hetzelfde bericht gaat naar al uw respondenten. U kunt bijvoorbeeld uw verwerkers uitnodigen een vragenlijst in te vullen waarmee de toepassing van de verwerkersovereenkomst wordt gecontroleerd.
* **Verwerking bericht uitnodiging**: om een Dastra-gebruiker vanaf een stap uit te nodigen een verwerkingsactiviteit aan te vullen. Schrijf het sjabloon één keer of bereid één sjabloon per soort ontvanger voor (jurist, IT-directeur enzovoort).
* **Datalek**: om op dezelfde manier een Dastra-gebruiker vanaf een stap uit te nodigen een datalek aan te vullen.

## Een sjabloon aanmaken

U maakt een sjabloon aan vanuit de instellingen voor de werkruimte of vanaf de plek waar u het bericht schrijft.

Vanuit de instellingen:

1. Open **Instellingen voor werkruimte** > **Modellen** en klik op het tabblad van het soort sjabloon dat u nodig hebt.
2. Klik op **Maak een sjabloon**.
3. Vul de **Naam** van het sjabloon in (maximaal 150 tekens) en de **Body van de template** (maximaal 9.000 tekens).
4. Schakel **Wilt u dit sjabloon delen met alle gebruikers van uw werkruimte?** in als alle gebruikers van de werkruimte het sjabloon mogen gebruiken.
5. Sla het sjabloon op.

<figure><img src="../../.gitbook/assets/settings-message-templates-2.png" alt="Het paneel voor het aanmaken van een sjabloon met de naam, de inhoud en de deeloptie"><figcaption><p>Een sjabloon aanmaken</p></figcaption></figure>

## Gedeelde en privésjablonen

De lijst toont per sjabloon of het gedeeld of privé is, met het aantal keren dat het is gebruikt. Een gedeeld sjabloon is beschikbaar voor alle gebruikers van de werkruimte. Een privésjabloon is alleen zichtbaar voor de maker.

Om slechts één van de twee weer te geven, gebruikt u het filter boven de lijst (**Alles**, **Gedeeld**, **Privé**). Voor het bewerken of verwijderen van een gedeeld sjabloon is het schrijfrecht op berichtsjablonen nodig; voor een privésjabloon volstaat het recht op uw eigen items.

## Sjablonen importeren en exporteren

De pijl van de knop **Maak een sjabloon** opent twee acties:

* **Importeren**: importeert sjablonen uit een bestand.
* **Exporteren**: exporteert de sjablonen van het getoonde soort in CSV-, XLSX-, JSON- of Markdown-indeling.

## Aangepaste variabelen in sjablonen

Dastra kan het sjabloon automatisch invullen met variabelen. U kunt in de tekst van het sjabloon gegevens opnemen over het object waaraan het is gekoppeld. In de uitnodiging om een vragenlijst te beantwoorden kunt u bijvoorbeeld de uiterste datum opnemen.

<figure><img src="../../.gitbook/assets/settings-message-templates-3.png" alt="De lijst met velden die beschikbaar zijn in de editor van een uitnodigingssjabloon voor een vragenlijst"><figcaption><p>De velden die beschikbaar zijn in de sjablooneditor</p></figcaption></figure>

Sjablonen gebruiken de syntaxis van LiquidJS. De volledige handleiding vindt u hier: [tags](https://liquidjs.com/tags/overview.html) en [filters](https://liquidjs.com/filters/overview.html).

Om statussen te vertalen, gebruikt u het aangepaste filter `getTranslation` als volgt: `{{ data | getTranslation: '' }}`. Bijvoorbeeld: `{{ data | getTranslation: 'dataSubjectRequestStates' }}`.

De aangepaste velden van de werkruimte zijn beschikbaar als `customFields.<naam van de variabele>`, waarbij de naam van de variabele de naam is die in het aangepaste veld is gedefinieerd (**Naam van de variabele (slug)**).

## Detail van de variabele velden

{% hint style="info" %}
Deze lijst is een uitgangspunt: de technische naam tussen haakjes is die u in het sjabloon gebruikt, maar de labels kunnen enigszins verschillen van die in de editor. De velden die voor uw werkruimte beschikbaar zijn, aangepaste velden inbegrepen, zijn die welke de sjablooneditor aanbiedt.
{% endhint %}

### Bericht voor het uitoefenen van rechten

* Titel van het verzoek (`title`)
* Afgesloten door (`closedByUser`)
* Organisatorische eenheid (`area`)
* Aangemaakt door (`creator`)
* Operator (`operator`)
* Taal (`locale`)
* Gearchiveerd (`archived`)
* Gearchiveerd op (`archivedDate`)
* Categorie van de betrokkene (`subjectCategory`)
* Complex verzoek (`complex`)
* Sluitingsdatum (`dateClosed`)
* Aanvullende informatie (intern) (`description`)
* Bericht van het verzoek (`message`)
* E-mail (`email`)
* Telefoonnummer (`phoneNumber`)
* Voornaam (`givenName`)
* Achternaam (`familyName`)
* Bijgewerkt op (`dateUpdate`)
* Ref.-ID (`refId`)
* Gebruikers-ID (`userId`)
* Reden van sluiting (`closedReason`)
* Beschrijving van de sluiting (`closedReasonDescription`)
* Vervaldatum (`expiryTime`)
* Adres (`address`)
* Postcode (`zipCode`)
* Plaats (`city`)
* Land (`countryCode`)
* Datum van e-mailvalidatie (`emailValidationDate`)
* E-mail gevalideerd (`mailValidated`)
* Bron-URL (`referrerUrl`)
* Identiteit gevalideerd (`identityValidated`)
* Datum van identiteitsvalidatie (`dateIdentityValidated`)
* Verzoek-ID (`demandId`)
* Status (`state`)
* Datum (`dateCreation`)
* Workflowstap (`workFlowStep`)
* Verzamelkanaal (`channel`)
* Soorten rechten (`purposes`)
* Berichten (`nbMessages`)
* Resterende dagen (`remainingDays`)
* Afhandeltijd (dagen) (`closingTime`)
* Labels (`tags`)

### Taakbeschrijving

* Project (`project`)
* Iteratie (`iteration`)
* Volgorde (`order`)
* Eigenaar (`owner`)
* Organisatorische eenheid (`area`)
* Aangemaakt door (`creator`)
* Resterende dagen (`remainingDays`)
* Afhandeltijd (dagen) (`closingTime`)
* Aantal subtaken (`nbSubTasks`)
* Aantal afgesloten subtaken (`nbSubTasksClosed`)
* Id (`id`)
* Interne referentie (`ref`)
* Gearchiveerd (`archived`)
* Naam (`label`)
* Beschrijving (`descriptionHtml`)
* Gekoppeld aan (`objectType`)
* Status (`state`)
* Uiterste datum (`deadline`)
* Startdatum (`startDate`)
* Afgesloten op (`dateClosed`)
* Geactiveerd op (`dateActivated`)
* Aangemaakt op (`dateCreation`)
* Bijgewerkt op (`dateUpdate`)
* Bron (`source`)
* Labels (`tags`)
* Workflowstap (`workFlowStep`)
* Prioriteit (`priority`)
* Toegewezen aan (`assignedToUser`)

### Uitnodigingen voor vragenlijsten

* Sjabloon (`template`)
* Datum van de volgende audit (`dateNextAudit`)
* Duur van de audit (`auditDurationDays`)
* Aantal correcties (`nbCorrections`)
* Aantal validaties (`nbValidations`)
* Dagen tot de volgende audit (`nextAuditDaysRemaining`)
* Id (`id`)
* Naam (`label`)
* Oude versie (`isRevision`)
* Naam van de versie (`revisionDescription`)
* Gearchiveerd (`archived`)
* Achterstallig (`isOverdue`)
* Organisatorische eenheid (`area`)
* Bijgewerkt op (`dateUpdate`)
* Gearchiveerd op (`archivedDate`)
* Score (`readiness`)
* Punten (`score`)
* Voltooiingspercentage (%) (`completionRate`)
* Aantal antwoorden (`nbAnswers`)
* Aantal vragen (`nbQuestions`)
* Eigenaren (`owners`)
* Respondenten (`respondants`)
* Actieplan gegenereerd op (`actionPlanDate`)
* Status (`state`)
* Startdatum (`startDate`)
* Voltooid op (`responseDate`)
* Publicatiedatum (`publishedDate`)
* Aangemaakt op (`dateCreation`)
* Gekoppeld object (`objectLabel`)
* Uiterste datum (`deadline`)

### Uitnodigingen om verwerkingsactiviteiten aan te vullen

* Organisatorische eenheid (`area`)
* Workflowstap (`workflowStep.label`)
* ID (`id`)
* Bron (`source`)
* Naam (`label`)
* Status (`state`)
* Aangemaakt op (`dateCreation`)
* Archiveringsdatum (`dateArchived`)
* Gearchiveerd (`archived`)
* Beschrijving van de versie (`versionDescription`)
* Type (`processingType`)
* Organisatorische eenheid (`areaId`)
* Activa (`assets`)
* Interne referentie (`ref`)
* Status van de verwerking (`processingState`)
* Documentatie (`descriptionHtml`)
* Labels (`tags`)
* Eigenaar van de verwerking (`owner`)
* Stakeholders (`stakeHolders`)
* DPIA vereist (`isDPIARequired`)
* DPIA-datum (`dpiaDate`)
* Vrijgesteld van DPIA (`dpiaExemption`)
* Ontvangers (`recipients`)
* Verwerkingsverantwoordelijken / klanten (`dataControllers`)
* Datasets (`dataRetentionRules`)
* Doeleinden (`purposes`)
* Maatregelen (`securityMeasures`)
* Categorieën van betrokkenen (`personCategories`)
* Voortgang (%) (`progression`)
* Kwaliteit (%) (`quality`)
* Gevoeligheid (%) (`sensitivity`)
* Aangemaakt door (`creatorUser`)
* Datum van ingebruikname (`dateDeployment`)
* Publicatiedatum (`datePublication`)
* Laatst gewijzigd (`dateUpdate`)
* Beschrijving (`description`)

### Uitnodigingen om datalekken aan te vullen

* Naam (`label`)
* ID (`id`)
* Locatie van de gegevens (`location`)
* Verlies van vertrouwelijkheid (`access`)
* Verlies van integriteit (`integrity`)
* Verlies van beschikbaarheid (`availability`)
* Oorzaak (`reason`)
* Bron (`source`)
* Betrokken verwerkers (`processorInvolved`)
* Verwerkers (`processors`)
* Gevoelige gegevens (`sensitiveData`)
* Waarschijnlijkheidsscore (`probabilityScore`)
* Impactniveau (`impactScore`)
* Score (`score`)
* Risiconiveau (`riskLevel`)
* Volume van de gegevensrecords (`dataVolume`)
* Gegevensdrager (`dataSupport`)
* Communicatie uitgevoerd? (`communicationDone`)
* Reden voor het uitblijven van communicatie (`noCommunicationReason`)
* Periode (`period`)
* Startdatum (`startDate`)
* Einddatum (`endDate`)
* Datum van ontdekking (`constatationDate`)
* Termijn voor melding aan de toezichthoudende autoriteit (`notificationDueTime`)
* Operator (`operator`)
* Workflowstap (`workFlowStep`)
* Organisatorische eenheid (`area`)
* Aangemaakt op (`dateCreation`)
* Bijgewerkt op (`dateUpdate`)
* Post-mortem uitgevoerd (`postMortemDone`)
* Labels (`tags`)
* Opmerkingen (`complementaryInformations`)
* Sluitingsdatum (`dateClosed`)
* Archiveringsdatum (`dateArchived`)
* Aangemaakt door (`creator`)
