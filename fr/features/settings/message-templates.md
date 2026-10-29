---
description: >-
  Créez des modèles de messages réutilisables dans les demandes d'exercice des
  droits, les tâches, les questionnaires, les traitements et les violations de
  données.
---

# Modèles de messages

{% embed url="https://youtu.be/3UtQuceFXqo" %}

Les modèles de messages vous font gagner du temps : vous les rédigez une fois et vous les réutilisez dans les modules de Dastra. Pour les gérer, ouvrez **Réglages espace de travail** > **Modèles**. Cette entrée du menu est visible pour les utilisateurs qui disposent de la permission d'écriture sur les modèles de messages, pour tout ou pour leurs propres éléments.

## Types de modèles de messages

Chaque type de modèle correspond à un onglet de la page. Les onglets affichés dépendent des modules inclus dans votre offre.

<figure><img src="../../.gitbook/assets/settings-message-templates-1.png" alt="La liste des modèles de messages avec les onglets par type et le bouton Créer modèle"><figcaption><p>La liste des modèles de messages, onglet Message de demande d'ex. de droits</p></figcaption></figure>

* **Message de demande d'ex. de droits** : pour gagner du temps lors des échanges avec les demandeurs. Par exemple, un modèle d'accusé de réception de la demande.
* **Tâche** : pour personnaliser le contenu de la description d'une tâche, par exemple quand vous demandez régulièrement à quelqu'un de renseigner des éléments sur un traitement.
* **Invitation aux questionnaires** : pour personnaliser les invitations à répondre à un questionnaire. Le même message est envoyé à tous vos répondants. Par exemple, vous pouvez inviter vos sous-traitants à renseigner un questionnaire de vérification de l'application du contrat de sous-traitance.
* **Message d'invitation traitement** : pour inviter un utilisateur de Dastra à compléter un traitement à partir d'une étape. Rédigez le modèle une fois, ou prévoyez un modèle par type de destinataire (juriste, DSI, etc.).
* **Violation de données** : pour inviter un utilisateur de Dastra à compléter une violation de données à partir d'une étape, de la même manière.

## Créer un modèle

Vous pouvez créer un modèle depuis les réglages de l'espace de travail ou depuis l'endroit où vous rédigez le message.

Depuis les réglages :

1. Ouvrez **Réglages espace de travail** > **Modèles** et cliquez sur l'onglet du type de modèle voulu.
2. Cliquez sur **Créer modèle**.
3. Saisissez le **Nom** du modèle (150 caractères au maximum) et son **Corps du modèle** (9 000 caractères au maximum).
4. Pour que tous les utilisateurs de l'espace de travail puissent utiliser le modèle, activez l'option **Souhaitez vous partager ce modèle avec tous les utilisateurs de votre espace de travail ?**
5. Enregistrez le modèle.

<figure><img src="../../.gitbook/assets/settings-message-templates-2.png" alt="Le panneau de création d'un modèle avec le nom, le corps du modèle et l'option de partage"><figcaption><p>La création d'un modèle</p></figcaption></figure>

## Modèles partagés et privés

La liste indique pour chaque modèle s'il est **Partagé** ou **Privé**, ainsi que son nombre d'utilisations. Un modèle partagé est disponible pour tous les utilisateurs de l'espace de travail. Un modèle privé n'est visible que par son créateur.

Pour n'afficher que l'un des deux, utilisez le filtre au-dessus de la liste (**Tout**, **Partagé**, **Privé**). La modification et la suppression d'un modèle partagé demandent la permission d'écriture sur les modèles de messages ; pour un modèle privé, la permission sur ses propres éléments suffit.

## Importer et exporter des modèles

La flèche du bouton **Créer modèle** ouvre deux actions :

* **Importer** : importe des modèles depuis un fichier.
* **Exporter** : exporte les modèles du type affiché, aux formats CSV, XLSX, JSON ou Markdown.

## Variables personnalisées dans les modèles

Dastra peut remplir automatiquement le modèle avec des variables. Vous reprenez ainsi dans le texte du modèle des informations sur l'objet auquel il est lié. Par exemple, dans l'invitation à répondre à un questionnaire, vous pouvez reprendre la date d'échéance.

<figure><img src="../../.gitbook/assets/settings-message-templates-3.png" alt="La liste des champs disponibles dans l'éditeur d'un modèle d'invitation à un questionnaire"><figcaption><p>Les champs disponibles dans l'éditeur du modèle</p></figcaption></figure>

Les modèles utilisent la syntaxe LiquidJS. Le guide complet est disponible ici : [les tags](https://liquidjs.com/tags/overview.html) et [les filtres](https://liquidjs.com/filters/overview.html).

Pour traduire les statuts, utilisez le filtre personnalisé `getTranslation` de cette manière : `{{ data | getTranslation: '' }}`. Par exemple : `{{ data | getTranslation: 'dataSubjectRequestStates' }}`.

Les champs personnalisés de l'espace de travail sont disponibles sous la forme `customFields.<nom de la variable>`, où le nom de la variable est celui défini dans le champ personnalisé (**Nom de la variable (slug)**).

## Détail des champs variables

{% hint style="info" %}
Cette liste est un point de départ : le nom technique entre parenthèses est celui à utiliser dans le modèle, mais les libellés peuvent différer légèrement de ceux affichés dans l'éditeur. Les champs disponibles pour votre espace de travail, champs personnalisés compris, sont ceux que propose l'éditeur du modèle.
{% endhint %}

### Message de demande d'exercice des droits

* Titre de la demande (`title`)
* Fermée par (`closedByUser`)
* Unité organisationnelle (`area`)
* Créé par (`creator`)
* Opérateur (`operator`)
* Langue (`locale`)
* Archivé (`archived`)
* Archivé le (`archivedDate`)
* Catégorie de personne (`subjectCategory`)
* Demande complexe (`complex`)
* Date de fermeture (`dateClosed`)
* Informations complémentaires (interne) (`description`)
* Message de la demande (`message`)
* E-mail (`email`)
* N° de téléphone (`phoneNumber`)
* Prénom (`givenName`)
* Nom (`familyName`)
* Mis à jour le (`dateUpdate`)
* Ref. Id (`refId`)
* Identifiant utilisateur (`userId`)
* Raison de la fermeture (`closedReason`)
* Description de la fermeture (`closedReasonDescription`)
* Date d'expiration (`expiryTime`)
* Address (`address`)
* Code postal (`zipCode`)
* Ville (`city`)
* Pays (`countryCode`)
* Date de validation de l'e-mail (`emailValidationDate`)
* E-mail validé (`mailValidated`)
* Url source (`referrerUrl`)
* Identité validée (`identityValidated`)
* Date de validation de l'identité (`dateIdentityValidated`)
* Id de la demande (`demandId`)
* Statut (`state`)
* Date (`dateCreation`)
* Etape (`workFlowStep`)
* Canal de collecte (`channel`)
* Types de droits (`purposes`)
* Messages (`nbMessages`)
* Jours restants (`remainingDays`)
* Délai de fermeture (jours) (`closingTime`)
* Tags (`tags`)

### Description d'une tâche

* Projet (`project`)
* Iteration (`iteration`)
* Ordre (`order`)
* Propriétaire (`owner`)
* Unité organisationnelle (`area`)
* Créé par (`creator`)
* Jours restants (`remainingDays`)
* Délai de fermeture (jours) (`closingTime`)
* Nombre de sous-tâches (`nbSubTasks`)
* Nombre de sous-tâches fermées (`nbSubTasksClosed`)
* Id (`id`)
* Référence interne (`ref`)
* Archivé (`archived`)
* Nom (`label`)
* Description (`descriptionHtml`)
* Associée à (`objectType`)
* Statut (`state`)
* Date limite (`deadline`)
* Date de début (`startDate`)
* Fermée le (`dateClosed`)
* Activée le (`dateActivated`)
* Créé le (`dateCreation`)
* Mis à jour le (`dateUpdate`)
* Source (`source`)
* Tags (`tags`)
* Etape (`workFlowStep`)
* Priorité (`priority`)
* Assignée à (`assignedToUser`)

### Invitations à répondre à un questionnaire

* Modèle (`template`)
* Date du prochain audit (`dateNextAudit`)
* Durée de l'audit (`auditDurationDays`)
* Nb. corrections (`nbCorrections`)
* Nb validations (`nbValidations`)
* Jours avant le prochain audit (`nextAuditDaysRemaining`)
* Id (`id`)
* Nom (`label`)
* Version ancienne (`isRevision`)
* Version name (`revisionDescription`)
* Archivé (`archived`)
* Dépassé (`isOverdue`)
* Unité organisationnelle (`area`)
* Mis à jour le (`dateUpdate`)
* Archivé le (`archivedDate`)
* Score (`readiness`)
* Points (`score`)
* Taux de completion (%) (`completionRate`)
* Nb. réponses (`nbAnswers`)
* Nb. de questions (`nbQuestions`)
* Responsables (`owners`)
* Répondants (`respondants`)
* Plan d'action généré le (`actionPlanDate`)
* Statut (`state`)
* Date de début (`startDate`)
* Finalisé le (`responseDate`)
* Date de publication (`publishedDate`)
* Créé le (`dateCreation`)
* Objet attaché (`objectLabel`)
* Date limite (`deadline`)

### Invitations à compléter un traitement

* Unité organisationnelle (`area`)
* Etape (`workflowStep.label`)
* Id (`id`)
* Source (`source`)
* Nom (`label`)
* Statut (`state`)
* Créé le (`dateCreation`)
* Date d'archivage (`dateArchived`)
* Archivé (`archived`)
* Version description (`versionDescription`)
* Type (`processingType`)
* Unité organisationnelle (`areaId`)
* Actifs (`assets`)
* Référence interne (`ref`)
* État du traitement (`processingState`)
* Documentation (`descriptionHtml`)
* Tags (`tags`)
* Propriétaire du traitement (`owner`)
* Parties prenantes (`stakeHolders`)
* PIA requis (`isDPIARequired`)
* Date de PIA (`dpiaDate`)
* Est exempté de PIA (`dpiaExemption`)
* Destinataires (`recipients`)
* Responsables de traitement / clients (`dataControllers`)
* Jeux de données (`dataRetentionRules`)
* Finalités (`purposes`)
* Mesures (`securityMeasures`)
* Catégories de personnes concernées (`personCategories`)
* Progression (%) (`progression`)
* Qualité (%) (`quality`)
* Sensibilité (%) (`sensitivity`)
* Créé par (`creatorUser`)
* Date de déploiement (`dateDeployment`)
* Date de publication (`datePublication`)
* Dernière modification (`dateUpdate`)
* Description (`description`)

### Invitations à compléter une violation

* Nom (`label`)
* ID (`id`)
* Localisation des données (`location`)
* Perte de confidentialité (`access`)
* Perte d'intégrité (`integrity`)
* Perte de disponibilité (`availability`)
* Cause (`reason`)
* Source (`source`)
* Sous-traitants impliqués (`processorInvolved`)
* Processors (`processors`)
* Données sensibles (`sensitiveData`)
* Score de probabilité (`probabilityScore`)
* Niveau d'impact (`impactScore`)
* Score (`score`)
* Niveau de risque (`riskLevel`)
* Volume d'enregistrements de données (`dataVolume`)
* Support des données (`dataSupport`)
* Communication effectuée ? (`communicationDone`)
* Raison de l'absence de communication (`noCommunicationReason`)
* Période (`period`)
* Date de début (`startDate`)
* Date de fin (`endDate`)
* Date de constatation (`constatationDate`)
* Délai de notification à l'autorité contrôle (`notificationDueTime`)
* Opérateur (`operator`)
* Etape (`workFlowStep`)
* Unité organisationnelle (`area`)
* Créé le (`dateCreation`)
* Mis à jour le (`dateUpdate`)
* Post-mortem effectué (`postMortemDone`)
* Tags (`tags`)
* Remarques (`complementaryInformations`)
* Date de fermeture (`dateClosed`)
* Date d'archivage (`dateArchived`)
* Créé par (`creator`)
