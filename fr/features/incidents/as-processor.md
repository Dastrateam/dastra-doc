---
description: >-
  Gérez les violations de données dans lesquelles votre organisation intervient
  en tant que sous-traitant au sens du RGPD.
---

# Incidents en tant que sous-traitant

Le module Incidents de Dastra s'adapte au rôle de votre organisation dans l'incident : responsable de traitement ou sous-traitant. Ce rôle détermine les obligations applicables et les étapes affichées dans le formulaire.

## Déclarer son rôle à la création

Lorsque vous créez un incident, la fenêtre pose la question **Dans le cadre de cet incident, êtes-vous sous-traitant ?**, avec deux réponses :

* **Non** (réponse par défaut) : vous traitez l'incident en tant que responsable de traitement. Le parcours est le parcours standard : notification à l'autorité de contrôle, communication aux personnes concernées, analyse de risque.
* **Oui** : vous traitez l'incident en tant que sous-traitant. Vous n'avez pas à notifier directement l'autorité de contrôle : c'est au responsable de traitement de le faire.

<figure><img src="../../.gitbook/assets/violations-create-subprocessor.png" alt="Fenêtre de création d'un incident avec la question sur le rôle de sous-traitant, réponse Oui sélectionnée"><figcaption><p>À la création, indiquez si votre organisation intervient en tant que sous-traitant</p></figcaption></figure>

Pour créer l'incident pas à pas, lisez [Documenter une nouvelle violation de données](document-breach.md).

{% hint style="info" %}
Article 33, paragraphe 2, du RGPD : le sous-traitant notifie toute violation de données personnelles au responsable de traitement dans les meilleurs délais après en avoir pris connaissance. Il n'a pas d'obligation de notification directe à l'autorité de contrôle : cette obligation incombe au responsable de traitement.
{% endhint %}

## Différences dans le formulaire

Lorsque vous répondez **Oui** à la question sur le rôle, le formulaire change comme suit :

| Élément | Responsable de traitement | Sous-traitant |
| --- | --- | --- |
| Étape **Notification** (autorité de contrôle) | Affichée | Masquée |
| Étape **Communication** | Communication aux personnes concernées | Communication aux responsables de traitement, avec l'onglet **Responsables de traitement** |

Les autres étapes restent les mêmes. À l'étape **Analyse de risque**, un rappel indique que vous devez informer les responsables de traitement concernés des actions requises afin qu'ils puissent agir en conséquence.

Dans le registre, le filtre **Type** distingue les incidents traités en tant que sous-traitant de ceux traités en tant que responsable de traitement, et la page **Statistiques** affiche la **Répartition par rôle**.

## Communiquer aux responsables de traitement clients

L'étape **Communication** d'un incident de sous-traitant a deux onglets.

Dans l'onglet **Communication**, répondez à **Avez-vous adressé une communication aux responsables de traitement ?** par **Non applicable**, **Oui** ou **Non**. Avec **Oui**, cliquez sur **Ajouter une communication** pour enregistrer chaque envoi avec sa date. Avec **Non**, indiquez les raisons dans **Pour quelles raisons n'avez-vous pas communiqué aux responsables de traitement ?**.

L'onglet **Responsables de traitement** liste les responsables de traitement clients touchés par l'incident. Vous pouvez :

* rattacher un responsable de traitement avec **Rattacher un RT** ;
* importer automatiquement les responsables de traitement avec **Synchroniser les RT** ;
* cocher, pour chacun, **Communication envoyée** et **Autorité notifiée** ;
* exporter la liste avec **Exporter les RT**, pour votre dossier de conformité.

<figure><img src="../../.gitbook/assets/incidents-as-processor-1.png" alt="Étape Communication d'un incident de sous-traitant, onglet Responsables de traitement"><figcaption><p>L'onglet Responsables de traitement, avec les actions Rattacher un RT, Synchroniser les RT et Exporter les RT</p></figcaption></figure>

### Synchroniser les responsables de traitement

Si des traitements sont liés à l'incident (étape **Traitements**), Dastra retrouve les responsables de traitement clients à partir de ces traitements et les ajoute à la liste. Cliquez sur **Synchroniser les RT** pour lancer l'opération. Si aucun traitement ni système d'IA n'est encore lié, Dastra vous invite à en lier d'abord.

## Bonnes pratiques

* Prévenez vos clients responsables de traitement dès que vous avez connaissance de l'incident. Le RGPD n'impose pas de délai chiffré au sous-traitant, contrairement aux 72 heures laissées au responsable de traitement pour notifier l'autorité, mais la réactivité est essentielle.
* Enregistrez la date et l'heure de chaque communication envoyée aux responsables de traitement.
* Conservez les accusés de réception et les réponses dans l'étape **Documentation** de l'incident.
