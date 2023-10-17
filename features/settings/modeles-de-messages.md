---
description: Fonctionnement des modèles de messages
---

# Modèles de messages

## Personnalisation des modèles de messages



Pour optimiser votre temps et gagner en efficacité, vous pouvez paramétrer des modèles de messages à réutiliser dans les modules de Dastra.



### Types de modèles de messages accessibles&#x20;

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

Les types de modèles sont les suivants :

*   **Message dans les demandes d'exercice des droits**

    Lors des échanges avec les demandeurs, vous pouvez enregistrer des modèles pour gagner du temps. Par exemple, un modèle d'accusé réception de la demande.
*   **Tâche**

    Vous pouvez personnaliser le contenu de la description d'une tâche. Idéal pour gagner du temps sur des tâches répétitives. Par exemple, quand vous demandez à quelqu'un de renseigner des éléments sur un traitement de données, vous pouvez réutiliser le même modèle de message.&#x20;
*   **Audits**

    Vous pouvez personnaliser les invitations à répondre à un audit. Utilisez ici un modèle pour inscrire le même message pour tous vos répondants. Par exemple, vous pouvez inviter vos sous-traitants à renseigner un audit de vérification de la bonne application du contrat de sous-traitance à partir d'un modèle créé à l'image de votre organisation.
*   **Compléter un traitement**

    Vous pouvez inviter un utilisateur de Dastra à compléter un traitement de données à partir d'une étape. Ecrivez une fois le modèle ou sélectionnez un modèle en fonction de la qualité du destinataire (juriste, DSI etc.) pour gagner du temps.&#x20;
*   **Compléter une violation de données**

    Vous pouvez inviter un utilisateur de Dastra à compléter une violation de données à partir d'une étape. Ecrivez une fois le modèle ou sélectionnez un modèle en fonction de la qualité du destinataire (juriste, DSI etc.) pour gagner du temps.&#x20;



### Création du modèle

La création de modèle s'effectue soit à partir des réglages de l'espace de travail, soit à partir du lieu du message.&#x20;

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption><p>Création depuis les réglages de l'espace de travail</p></figcaption></figure>

Cliquez sur Créer modèle

<figure><img src="../../.gitbook/assets/image (4) (1) (2).png" alt=""><figcaption><p>Interface de création d'un modèle</p></figcaption></figure>

N'oubliez pas d'enregistrer votre travail !

### Variables personnalisées dans les modèles

Dastra vous permet de **remplir automatiquement le modèle avec des variables personnalisées**.&#x20;

Cela signifie que vous pouvez inclure automatiquement des informations concernant l'objet lié au modèle dans le texte du modèle de message.&#x20;

Par exemple, dans l'invitation à répondre à un audit, il sera possible de reprendre automatiquement la date d'échéance d'un audit.&#x20;

<figure><img src="../../.gitbook/assets/image (2) (1) (2).png" alt=""><figcaption><p>Les champs personnalisés du message d'invitation à répondre à un audit</p></figcaption></figure>



Vous pouvez ainsi ajouter facilement des champs dynamiques directement dans le modèle. En tant que langage de création de modèles, nous utilisons la synthax liquidJS.&#x20;

Voici le guide complet ici : [les tags ](https://liquidjs.com/tags/overview.html)et [les filtres](https://liquidjs.com/filters/overview.html).&#x20;

Pour traduire les statuts, vous pouvez utiliser le filtre personnalisé getTranslation de cette manière \{{data | getTranslation: ''\}}. Exemple : \{{data | getTranslation: 'dataSubjectRequestStates'\}}

### Détail des champs variables :&#x20;

#### Message de demande d'exercice des droits :&#x20;

•             Titre de la demande (title)

•             Fermée par (closedByUser)

•             Unité organisationnelle (area)

•             Créé par (creator)

•             Opérateur (operator)

•             Langue (locale)

•             Archivé (archived)

•             Archivé le (archivedDate)

•             Catégorie de personne (subjectCategory)

•             Demande complexe (complex)

•             Date de fermeture (dateClosed)

•             Informations complémentaires (interne) (description)

•             Message de la demande (message)

•             Email (email)

•             N° de téléphone (phoneNumber)

•             Prénom (givenName)

•             Nom (familyName)

•             Mis à jour le (dateUpdate)

•             Ref. Id (refId)

•             Identifiant utilisateur (userId)

•             Raison de la fermeture (closedReason)

•             Description de la fermeture (closedReasonDescription)

•             Date d'expiration (expiryTime)

•             Address (address)

•             Code postal (zipCode)

•             Ville (city)

•             Pays (countryCode)

•             Date de validation de l'email (emailValidationDate)

•             Email validé (mailValidated)

•             Url source (referrerUrl)

•             Identité validée (identityValidated)

•             Date de validation de l'identité (dateIdentityValidated)

•             Id de la demande (demandId)

•             Statut (state)

•             Date (dateCreation)

•             Etape (workFlowStep)

•             Canal de collecte (channel)

•             Types de droits (purposes)

•             Messages (nbMessages)

•             Jours restants (remainingDays)

•             Délai de fermeture (jours) (closingTime)

•             Tags (tags)



#### Description d'une tâche :&#x20;

•             Projet (project)

•             Iteration (iteration)

•             Ordre (order)

•             Propriétaire (owner)

•             Unité organisationnelle (area)

•             Créé par (creator)

•             Jours restants (remainingDays)

•             Délai de fermeture (jours) (closingTime)

•             Nombre de sous-tâches (nbSubTasks)

•             Nombre de sous-tâches fermées (nbSubTasksClosed)

•             Id (id)

•             Référence interne (ref)

•             Archivé (archived)

•             Nom (label)

•             Description (descriptionHtml)

•             Associée à (objectType)

•             Statut (state)

•             Date limite (deadline)

•             Date de début (startDate)

•             Fermée le (dateClosed)

•             Activée le (dateActivated)

•             Créé le (dateCreation)

•             Mis à jour le (dateUpdate)

•             Source (source)

•             test (customFields.test)

•             LIste (customFields.liste)

•             Case à cocher simple (customFields.case\_a\_cocher\_simple)

•             Tags (tags)

•             Etape (workFlowStep)

•             Priorité (priority)

•             Assignée à (assignedToUser)



#### Invitations à répondre à un questionnaire d'audit :&#x20;

•             Modèle (template)

•             Date du prochain audit (dateNextAudit)

•             Durée de l'audit (auditDurationDays)

•             Nb. corrections (nbCorrections)

•             Nb validations (nbValidations)

•             Jours avant le prochain audit (nextAuditDaysRemaining)

•             Id (id)

•             Nom (label)

•             Version ancienne (isRevision)

•             Version name (revisionDescription)

•             Archivé (archived)

•             Dépassé (isOverdue)

•             Unité organisationnelle (area)

•             Mis à jour le (dateUpdate)

•             Archivé le (archivedDate)

•             Score (readiness)

•             Points (score)

•             Taux de completion (%) (completionRate)

•             Nb. réponses (nbAnswers)

•             Nb. de questions (nbQuestions)

•             Responsables (owners)

•             Répondants (respondants)

•             Plan d'action généré le (actionPlanDate)

•             Statut (state)

•             Date de début (startDate)

•             Finalisé le (responseDate)

•             Date de publication (publishedDate)

•             Créé le (dateCreation)

•             Objet attaché (objectLabel)

•             Date limite (deadline)



#### Invitations à compléter un traitement :&#x20;

Unité organisationnelle (area)

Etape (workflowStep)

Id (id)

Source (source)

Nom (label)

Statut (state)

Créé le (dateCreation)

Date d'archivage (dateArchived)

Archivé (archived)

Version description (versionDescription)

Type (processingType)

Unité organisationnelle (areaId)

Actifs (assets)

Référence interne (ref)

État du traitement (processingState)

Documentation (descriptionHtml)

Tags (tags)

Propriétaire du traitement (owner)

Parties prenantes (stakeHolders)

PIA requis (isDPIARequired)

Date de PIA (dpiaDate)

Est exempté de PIA (dpiaExemption)

Destinataires (recipients)

Responsables de traitement / clients (dataControllers)

Jeux de données (dataRetentionRules)

Finalités (purposes)

Mesures (securityMeasures)

Catégories de personnes concernées (personCategories)

AIPD (customFields.aipd)

Progression (%) (progression)

Qualité (%) (quality)

Sensibilité (%) (sensitivity)

Créé par (creatorUser)

Date de déploiement (dateDeployment)

Date de publication (datePublication)

Dernière modification (dateUpdate)

Description (description)



#### Invitation à compléter une violation :&#x20;

Nom (label)

ID (id)

Localisation des données (location)

Perte de confidentialité (access)

Perte d'intégrité (integrity)

Perte de disponibilité (availability)

Cause (reason)

Source (source)

Sous-traitants impliqués (processorInvolved)

Processors (processors)

Données sensibles (sensitiveData)

Score de probabilité (probabilityScore)

Niveau d'impact (impactScore)

Score (score)

Niveau de risque (riskLevel)

Volume d'enregistrements de données (dataVolume)

Support des données (dataSupport)

Communication effectuée ? (communicationDone)

Raison de l'absence de communication (noCommunicationReason)

Période (period)

Date de début (startDate)

Date de fin (endDate)

Date de constatation (constatationDate)

Délai de notification à l'autorité contrôle (notificationDueTime)

Opérateur (operator)

Etape (workFlowStep)

Unité organisationnelle (area)

Créé le (dateCreation)

Mis à jour le (dateUpdate)

Post-mortem effectué (postMortemDone)

Tags (tags)

Remarques (complementaryInformations)

Date de fermeture (dateClosed)

Date d'archivage (dateArchived)

Créé par (creator)
