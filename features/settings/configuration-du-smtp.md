---
description: >-
  Dastra vous permet de router vos emails de notification via votre propre
  serveur d'envoi d'emails
---

# Configuration du SMTP

## Principe de fonctionnement

Par défaut, Dastra route un nombre important de notifications par email pour les services suivants :&#x20;

* [Notifications ](notifications.md)en temps réel (Nouveaux commentaires, tâches, ...)
* Emails d'échanges dans le cadre d'[une demande d'exercice de droits](../gerer-les-exercices-des-droits/)
* Invitation aux [audits](../audit/) pour les répondants
* [Invitations ](../../commencer/commencer/inviter-utilisateurs.md)de nouveaux utilisateurs

Par défaut, Dastra utilise son propre service SMTP.

## Comment configurer votre serveur d'envoi SMTP ?

{% hint style="warning" %}
Attention ! personnaliser le SMTP peut conduire à des instabilités de la plateforme. N'effectuez cette manipulation que si vous êtes certains du bon fonctionnement et de la délivrabilité de votre service d'envoi d'email.
{% endhint %}

### Intérêt de personnaliser le SMTP

Dastra s'efforce d'assurer une disponibilité et une sécurité maximale pour les envois d'emails transactionnels.&#x20;

Cependant, selon votre politique interne de sécurité, vous pouvez être amené à internaliser le routage des emails transactionnels afin de maîtriser les flux de messagerie.

### Prérequis

Vous devez disposer des éléments de configuration de votre serveur SMTP :&#x20;

* Hôte SMTP (ex: smtp.yourservice.com)
* Port SMTP (par défaut, utilisez le port 25)
* Nom d'utilisateur
* Mot de passe
* Une **adresse email de sender valide** (ex: noreply@yourservice.com) : cette adresse doit être correctement validée par votre fournisseur SMTP.

{% hint style="warning" %}
Attention, votre serveur SMTP doit obligatoirement supporter une connexion sécurisée utilisant SSL
{% endhint %}

### Configuration

Rendez-vous sur la [page de configuration du serveur SMTP](https://app.dastra.eu/general-settings/smtp)

Remplissez les champs de formulaire à l'aide des données demandées en [prérequis](configuration-du-smtp.md#prerequis)

![](<../../.gitbook/assets/image (249) (1).png>)

A noter que la connectivité au serveur est automatiquement testé pour s'assurer que les identifiants de connexion au serveurs sont correctes. Un email de test sera automatiquement envoyé à partir de nos serveurs.

### Tests

Une fois que vous avez validé le formulaire, votre serveur SMTP devrait fonctionner.

Vous pouvez vérifier que les emails de notifications proviennent bien de votre serveur SMTP. Pour cela, créez par exemple un commentaire dans un traitement et regardez si vous recevez bien le mail de notification dans votre BAL.

* **Si vous ne recevez pas d'email** : soit vous n'avez pas réussi à déclencher la notification, soit il y a un problème dans la configuration de votre SMTP
* **Si vous recevez un email** : vérifiez que votre SMTP et votre sender figurent bien dans le détail du mail.&#x20;

{% hint style="info" %}
[Comment voir le détail de l'email dans GMAIL](https://support.google.com/mail/answer/29436?hl=fr).&#x20;

[Comment voir le détail de l'email dans Outlook](https://support.microsoft.com/fr-fr/office/afficher-les-en-t%C3%AAtes-de-message-internet-dans-outlook-cd039382-dc6e-4264-ac74-c048563d212c)
{% endhint %}
