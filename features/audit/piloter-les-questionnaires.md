---
description: >-
  Apprenez à piloter les réponses aux questionnaires et à analyser les résultats
  dans Dastra.
---

# Piloter les questionnaires

## Tableau de bord des réponses

Depuis l'onglet **"Voir les questionnaires"**, sélectionnez un modèle pour accéder à son tableau de bord de réponses. Il propose quatre vues :

* **Réponses** : liste de toutes les réponses avec leur statut (en attente, publié, en retard), leur score et l'objet lié
* **Tableau détaillé** : comparaison côte à côte de toutes les réponses par catégorie et score — utile pour benchmarker plusieurs entités ou traitements
* **Stats** : statistiques agrégées sur l'ensemble des réponses du modèle
* **Détails** : configuration et métadonnées du questionnaire

## Reporting d'une réponse individuelle

En ouvrant une réponse, vous accédez à une vue de reporting détaillée :

* **Statut** : progression de "En attente de répondants" → "Démarré" → "En attente de validation" → "Publié"
* **Score** : score total sur le maximum de points
* **Complétion** : nombre de questions répondues sur le total
* **Temps de réponse** : durée de complétion du questionnaire
* **Signalements** : réponses automatiquement marquées comme nécessitant attention selon la configuration du modèle
* **Analyse des résultats** : blocs d'analyse générés automatiquement (niveau de conformité, évaluation des risques, etc.)
* **Score par catégories** : visualisé sous forme de radar ou de graphique en barres

## Analyse IA (bêta)

Depuis la vue de reporting d'une réponse, déclenchez une **analyse IA** pour obtenir :

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
Si vous ne pouvez pas valider une réponse, vérifiez que le répondant a bien cliqué sur le bouton **"Finaliser"**. Sans cette étape, la réponse reste en "En attente de validation".
{% endhint %}

## Fusionner les réponses avec l'objet attaché

Après avoir complété un questionnaire lié à un objet Dastra (traitement, actif, acteur, etc.), il est possible de **fusionner les réponses collectées avec les données de cet objet**.

Cette action met à jour directement les champs correspondants de l'objet à partir des informations saisies dans le formulaire, sans nouvelle saisie manuelle.

Pour lancer la fusion  :

1. Ouvrez la réponse complétée au questionnaire.
2. Cliquez sur **"Fusionner les réponses avec l'objet"**.
3. Confirmez les champs à mettre à jour dans l'objet cible.

Cette fonctionnalité est particulièrement utile dans les scénarios de collecte externe via les Privacy hubs, où des tiers (fournisseurs, sous-traitants) renseignent des informations qui doivent ensuite être reflétées dans vos registres internes.

<figure><img src="../../.gitbook/assets/image (275).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (278).png" alt=""><figcaption></figcaption></figure>

## Générer un plan d'actions

Depuis la vue de reporting d'une réponse, cliquez sur **"Générer un plan d'actions"** pour créer automatiquement des tâches basées sur les réponses fournies. Les tâches sont suggérées selon la configuration du modèle et ajoutées directement au module de gestion des tâches de Dastra.
