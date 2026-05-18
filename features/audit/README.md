---
description: Apprenez à réaliser des questionnaires et des AIPD avec Dastra.
---

# Questionnaires et AIPD

## Introduction

En tant qu'organisation, vous avez besoin de réaliser des analyses d'impact relatives à la protection des données (AIPD) et de vous assurer du niveau de conformité de vos traitements. Le module Questionnaires de Dastra vous permet de collecter toutes les informations nécessaires au pilotage de votre conformité : AIPD, questionnaires des sous-traitants, questionnaires de conformité, questionnaires de sécurité, etc.

Avec le module Questionnaires de Dastra, vous pouvez :

* Créer des questionnaires, dont des AIPD
* Lier vos questionnaires à des actifs, des traitements, des acteurs, des mesures, violations, demandes d'exercice de droits et risques
* Notifier automatiquement les participants
* Répondre au questionnaire avec une interface simple et intuitive
* Suivre la validation des questionnaires
* Évaluer les risques
* Générer un plan d'actions

{% hint style="info" %}
Dans Dastra, les AIPD sont considérées comme un **modèle de questionnaire** particulier.
{% endhint %}

## Tutoriel utilisateur : les questionnaires

{% embed url="https://www.youtube-nocookie.com/embed/IHevXHniVvk" %}

## Comment accéder au module Questionnaires ?

Pour accéder au module Questionnaires, cliquer sur l'icône "Questionnaires" à gauche de l'écran.

<figure><img src="../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

Le module est organisé en trois onglets :

* **Modèles de questionnaires** : gérez et créez vos modèles de questionnaires
* **Voir les questionnaires** : consultez l'ensemble des questionnaires planifiés et leurs réponses
* **Mes réponses** : accédez aux questionnaires auxquels vous avez été invité à répondre

## Créer un modèle de questionnaire

Depuis l'onglet "Modèles de questionnaires", cliquez sur le bouton **"Créer un modèle"**. Quatre méthodes de création sont disponibles :

* **Questionnaires automatisés** : choisissez un modèle prédéfini depuis la bibliothèque Dastra. Le modèle peut être personnalisé après sélection.
* **Créer depuis l'IA** : générez un modèle de questionnaire à l'aide de l'assistant IA de Dastra.
* **Questionnaire personnalisé** : construisez votre propre modèle depuis zéro avec l'éditeur de modèles.
* **Importer un fichier** : importez un modèle existant au format JSON, Excel ou CSV.

### La bibliothèque de modèles Dastra

En sélectionnant "Questionnaires automatisés", vous accédez à la bibliothèque par défaut de Dastra, qui inclut des modèles d'AIPD, de PIA (CNIL, ICO, EDPB), de TIA, de LIA, d'audits sous-traitants, et bien d'autres.

{% hint style="info" %}
Pour les PIA, une option complémentaire est disponible : **importer votre PIA depuis l'outil de la CNIL** en cliquant sur "Importer votre PIA CNIL". Le PIA CNIL doit être exporté au format .json — une très grande partie des éléments sera reprise automatiquement dans Dastra.
{% endhint %}

## Planifier un questionnaire

Une fois le modèle prêt, cliquez sur le bouton **"Planifier un questionnaire"**. Quatre modes de planification sont proposés :

* **Questionnaire express** : répondez vous-même immédiatement, sans configuration supplémentaire.
* **Campagne de questionnaire** : invitez des utilisateurs internes, des équipes ou des parties prenantes externes à répondre. Chaque répondant reçoit un email avec un lien personnalisé vers son espace de réponse en ligne.
* **Lien d'invitation** : générez un lien partageable vers le questionnaire, sans envoi d'invitations individuelles.
* **Réponse assistée par IA** : gagnez du temps en laissant l'IA de Dastra pré-remplir une réponse au questionnaire, que vous pourrez ensuite revoir et ajuster.

{% hint style="info" %}
Il est possible de relancer les répondants qui n'ont pas encore répondu.
{% endhint %}

## Suivre les réponses

Depuis l'onglet **"Voir les questionnaires"**, sélectionnez un modèle pour accéder à son tableau de bord de réponses :

* **Réponses** : liste de toutes les réponses avec leur statut (en attente, publié, en retard), leur score et l'objet lié
* **Tableau détaillé** : comparaison côte à côte de toutes les réponses par catégorie et score, utile pour benchmarker plusieurs entités ou traitements
* **Stats** : statistiques agrégées sur l'ensemble des réponses du modèle
* **Détails** : configuration et métadonnées du questionnaire

### Reporting d'une réponse

En ouvrant une réponse individuelle, vous accédez à une vue de reporting détaillée comprenant :

* **Statut** : progression de "En attente de répondants" à "Démarré", "En attente de validation" et "Publié"
* **Score** : score total du répondant sur le maximum de points
* **Complétion** : nombre de questions répondues sur le total
* **Temps de réponse** : durée de complétion du questionnaire
* **Signalements** : réponses automatiquement marquées comme nécessitant attention
* **Analyse des résultats** : blocs d'analyse générés automatiquement (niveau de conformité, évaluation des risques, etc.)
* **Score par catégories** : visualisé sous forme de radar ou de graphique en barres

### Analyse IA (bêta)

Depuis la vue de reporting d'une réponse, vous pouvez déclencher une **analyse IA** qui fournit :

* Un score global de conformité ou de risque
* Un résumé écrit des principaux constats
* Une analyse par critères (complétude, base légale, mesures de sécurité, etc.)
* Des tâches suggérées pour combler les lacunes identifiées

{% hint style="warning" %}
L'analyse IA est une fonctionnalité bêta. Les résultats doivent être interprétés avec prudence et revus par un professionnel qualifié.
{% endhint %}

## Valider et publier une réponse

Une fois la réponse examinée, cliquez sur **"Revoir et valider le questionnaire"** pour la passer au statut "Publié". Cette action est disponible pour les responsables du questionnaire.

{% hint style="info" %}
Si vous ne pouvez pas valider une réponse, vérifiez que le répondant a bien cliqué sur le bouton "Finaliser" pour soumettre ses réponses. Sans cette étape, la réponse reste en "En attente de validation".
{% endhint %}

## Générer un plan d'actions

Depuis la vue de reporting d'une réponse, vous pouvez générer automatiquement un plan d'actions basé sur les réponses fournies. Les tâches sont suggérées selon la configuration du modèle et peuvent être ajoutées directement au module de gestion des tâches de Dastra.

## Aller plus loin

{% content-ref url="creez-un-modele-daudit/" %}
[creez-un-modele-daudit](creez-un-modele-daudit/)
{% endcontent-ref %}

{% content-ref url="planifier-un-audit.md" %}
[planifier-un-audit.md](planifier-un-audit.md)
{% endcontent-ref %}

{% content-ref url="rapport-daudit.md" %}
[rapport-daudit.md](rapport-daudit.md)
{% endcontent-ref %}

{% content-ref url="../la-gestion-des-risques/" %}
[la-gestion-des-risques](../la-gestion-des-risques/)
{% endcontent-ref %}
