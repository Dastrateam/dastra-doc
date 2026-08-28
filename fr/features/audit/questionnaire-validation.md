---
description: >-
  Comprendre le processus de validation d’un questionnaire dans Dastra :
  approbations des validateurs, validation finale, demande de révision et
  annulation.
---

# Valider un questionnaire

La validation est l’étape de revue qui suit la finalisation d’un questionnaire par ses répondants. Elle permet aux validateurs désignés de contrôler chaque réponse, de demander des corrections si nécessaire, puis d’approuver et de publier le questionnaire.

## Le cycle de vie d’une réponse

1. **En attente de répondants / Démarré** — les répondants complètent le formulaire.
2. **En attente de validation** — dès que tous les répondants **requis** ont cliqué sur **Finaliser**, la réponse bascule dans cet état et les validateurs reçoivent une notification.
3. **Validé** — après approbation de tous les validateurs requis et validation finale.

Trois issues sont possibles depuis l’état « En attente de validation » : **valider**, **demander une révision** (retour aux répondants) ou **annuler** le questionnaire.

{% hint style="info" %}
Si aucun bouton n’est actionnable, vérifiez que la réponse est bien en « En attente de validation ». Toutes les actions de validation sont bloquées dans les autres statuts.
{% endhint %}

## Qui valide ?

Les validateurs sont définis à la planification du questionnaire (voir [Planifier un questionnaire](planifier-un-audit.md)), dans la section **Responsables** :

* **Approbateurs requis** — tous doivent approuver le questionnaire avant qu’il puisse être validé. Au moins un approbateur requis est obligatoire.
* **Approbateurs optionnels** — activez l’option « Ajouter des approbateurs optionnels » pour convier des relecteurs dont l’approbation est suivie mais **n’est pas bloquante**.

Seuls ces utilisateurs peuvent approuver, valider, demander une révision ou annuler la réponse.

{% hint style="success" %}
Vous pouvez désactiver entièrement cette étape à la planification avec l’option « Désactiver l’étape d’approbation ». La réponse est alors publiée directement dès la finalisation par les répondants.
{% endhint %}

## L’écran de revue

Depuis la réponse, cliquez sur **« Revoir et valider le questionnaire »**. L’écran de revue reprend la structure du questionnaire : navigation par sections à gauche, questions et réponses au centre, actions de validation à droite.

### Qualifier chaque réponse

Chaque question peut recevoir un statut d’évaluation :

* **Pas de statut** — question non qualifiée (statut par défaut, non bloquant)
* **Validé** — la réponse est acceptée
* **Besoin de révision** — la réponse doit être complétée ou corrigée
* **Non validé** — la réponse est rejetée

Un sélecteur situé en haut de chaque section permet d’appliquer le même statut à toutes les questions affichées d’un seul geste.

Pour chaque question, vous pouvez également :

* **Ajouter une annotation** — échange interne avec les répondants et les autres validateurs
* **Ajouter une tâche** — alimente directement le plan d’actions
* **Compléter la justification** de la réponse et **joindre une pièce jointe**
* **Qualifier un risque** lorsque la question y est associée

{% hint style="warning" %}
Si au moins une question est marquée « Besoin de révision » ou « Non validé », l’approbation et la validation sont bloquées : utilisez **« Demander révision »** pour renvoyer le questionnaire aux répondants.
{% endhint %}

## Approuver le questionnaire

Chaque validateur donne son approbation individuellement, via le bouton **« Approuver le questionnaire »** :

* Vous pouvez saisir des **commentaires de revue** : ils sont conservés et **repris dans l’export du rapport**.
* Une **notification par e-mail** est envoyée aux validateurs qui n’ont pas encore approuvé.

Le panneau **« Approbations requises (n/total) »** récapitule l’état de chaque validateur (approuvé avec la date, ou « En attente d’approbation »), ainsi qu’un bloc séparé « Approbations optionnelles » le cas échéant. Les commentaires de revue de chaque validateur y sont consultables.

Deux actions complémentaires :

* **Révoquer mon approbation** — retire votre approbation tant que le questionnaire n’est pas validé.
* Si vous êtes le **dernier validateur requis** à approuver, Dastra vous propose immédiatement d’enchaîner sur la validation et la publication.

## Valider et publier

Le bouton **« Valider le questionnaire »** n’est actif que lorsque **tous les approbateurs requis ont approuvé** et qu’aucune question n’est marquée comme à corriger. La fenêtre de validation affiche :

* le rappel du nombre de questions validées sur le total ;
* l’état des approbations ;
* pour un **PIA / AIPD**, l’option de **reporter la date de l’analyse d’impact sur le traitement lié** ;
* l’option d’envoyer une **notification** aux parties prenantes.

La réponse passe alors au statut **« Validé »** avec sa date de publication, et vous êtes redirigé vers son rapport. Vous pouvez ensuite [exporter le rapport](exporter-un-rapport.md), générer un plan d’actions ou fusionner les réponses avec l’objet lié (voir [Piloter les questionnaires](piloter-les-questionnaires.md)).

## Demander une révision

L’action **« Demander révision »** renvoie le questionnaire aux répondants :

* la réponse repasse en « En cours » et une **nouvelle échéance** est calculée à partir du délai du modèle (30 jours par défaut) ;
* **toutes les approbations déjà données sont réinitialisées** ;
* un **tour de correction** est comptabilisé dans l’historique de la réponse ;
* une notification est envoyée à chaque répondant, avec votre message de revue — que vous pouvez rédiger librement ou pré-remplir depuis un modèle d’e-mail.

Lorsque les répondants finalisent à nouveau, le cycle de validation reprend depuis le début.

## Annuler le questionnaire

L’action **« Annuler le questionnaire »** met fin au cycle sans publication. Un commentaire facultatif permet d’expliquer le motif ; il est conservé dans l’historique et visible par les répondants. Les approbations sont réinitialisées et la réponse prend le statut **« Annulé »** : elle n’est plus modifiable et n’est pas compilée dans les résultats.

## Suivre les questionnaires à valider

Les questionnaires qui attendent votre approbation sont regroupés dans « En attente de ma validation » depuis vos questionnaires, et signalés par le badge « En attente de validation » dans les listes et le reporting.
