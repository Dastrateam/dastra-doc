---
description: Dans cette page, retrouvez la résolution des principaux problèmes connus.
---

# Problèmes connus

## L'utilisateur invité ne reçoit pas les e-mails d'invitations

**Vérifiez que l'adresse email de l'utilisateur (domaine, nom...)** est correct. Si celle-ci est incorrecte, l'interface ne remontera pas d'erreur

Vérifiez que la boîte mail de la personne n'est pas pleine

Dans de très rares cas, Dastra peut être bloqué par le filtre anti-spam du serveur. Dans ce cas, vous pouvez générer un lien d'invitation en créant de nouveau une invitation en **cliquant sur "Inviter un utilisateur**" > **Suivre les étapes > Sélectionnez "Générer un lien".**&#x20;

<figure><img src="../.gitbook/assets/image (9) (4).png" alt=""><figcaption></figcaption></figure>

**Cliquez sur "Générer lien" > Copiez le lien présent dans la page**

<figure><img src="../.gitbook/assets/image (2) (2) (2).png" alt=""><figcaption></figcaption></figure>

Vous pouvez ainsi transmettre le lien d'invitation à l'utilisateur via un chat d'entreprise, un envoi depuis votre boîte mail...

{% hint style="info" %}
Attention, une validation de l'adresse mail sera nécessaire pour que l'utilisateur puisse accéder à votre espace
{% endhint %}

## Résoudre les problèmes liés au cache de votre navigateur

Lorsque vous utilisez un navigateur, celui-ci utilise le cache et les cookies pour enregistrer des informations provenant des sites Web. Les supprimer corrige certains problèmes, comme ceux liés au chargement des applications comme Dastra.\


Pour résoudre ces problèmes, nous vous mettons à disposition plusieurs solutions : &#x20;

1. **Faire une mise à jour du navigateur**, en utilisant CTRL + F5 (ou MAC + F5)&#x20;
2. Si la première solution ne fonctionne pas, faire une **réinitialisation des données de préférences**". Cette action vous permettra de supprimer facilement les cookies déposés par Dastra, effacer les éléments enregistrés dans votre stockage local et réinitialiser vos préférences d'affichage dans Dastra, et peut ainsi aider à résoudre certains problèmes d'affichages et bugs.

Pour l'actionner, rendez-vous dans l'onglet "profil" au sein de vos paramètres personnels :&#x20;

![](<../.gitbook/assets/image (3) (1) (4).png>)

{% hint style="info" %}
En sélectionnant cette option, vous perdrez vos réglages de colonnes dans tous les tableaux de Dastra et vous redéclencherez l'affichage des tutoriels dans tous les modules.&#x20;
{% endhint %}

Ces deux actions n'ont pas permis de résoudre votre problème ? Contactez le support directement depuis l'application, via chat ou onglet "porte-voix".



## Erreur 401 lors de la connexion

**Scénario** : vous vous connecter à Dastra via l'url https://app.dastra.eu, vous saisissez vos identifiants et vous arrivez sur une page d'erreur "**Accès refusé (401)**" .

Aperçu de la page :\
![](<../.gitbook/assets/image (1) (1) (1) (2) (4) (1).png>)

**Solutions** :&#x20;

1. **Vérifier les paramètres d'horloge de votre ordinateur**. Il est fortement recommandé d'activer la synchronisation du temps avec internet. En effet, les délais d'expiration de vos jetons d'identification sont comparés au temps de votre machine. Si la date n'est pas bien synchronisée avec le temps du serveur, vous allez rencontrer cette erreur. Pour configurer votre horloge, rendez-vous sur les liens suivants :&#x20;
   * [Mac](https://support.apple.com/fr-fr/guide/mac-help/mchlp2996/mac)
   * [PC](https://support.microsoft.com/fr-fr/windows/comment-d%C3%A9finir-l-heure-et-le-fuseau-horaire-dfaa7122-479f-5b98-2a7b-fa0b6e01b261)
2. **Utilisez cette adresse pour accéder à Dastra: https://app.dastra.eu** . Vous pouvez l'enregistrer dans vos favoris. Ce problème peut se produire lorsque vous tentez d'accéder à Dastra par les urls avec le domaine account.dastra.eu (souvent enregistrées automatiquement dans les suggestions d'url de votre navigateur)
3. **Nettoyez les données du site et les cookies de votre navigateur**

## Erreur 403 : Accès Refusé

Le message d'erreur "Erreur 403 accès refusé" indique que vous tentez d'accéder à une partie du système Dastra sans avoir l'autorisation nécessaire. Cela se produit lorsque l'accès à certains éléments ou modules a été restreint par un administrateur dans votre espace de travail, en fonction des autorisations de votre rôle ou de votre équipe.

**Comment Résoudre**

* **Vérifiez les Permissions** : Assurez-vous d'avoir les autorisations nécessaires pour le module ou l'élément souhaité.
* **Contactez l'un des administrateurs de votre espace de travail** : En cas de doute, contactez l'un des administrateurs de votre espace de travail pour vérifier ou mettre à jour vos droits d'accès.

## Erreur 404 : Élément introuvable

Le message d'erreur "Erreur 404 élément introuvable" indique que vous tentez d'accéder à un élément introuvable sur Dastra. Cela peut se produire lorsque l'élément en question a été modifier, déplacé ou supprimé (par un autre utilisateur ou par vous-même).

**Comment Résoudre**

* **Vérifiez l'URL**
* **Cherchez l'élément à partir d'un moteur de recherche**

## Erreur 500

Cette erreur peut survenir de façon ponctuelle, elle est souvent causée par :\
-Des problèmes de connexion\
-Des problèmes liés à votre environnement (navigateur, extension, etc)\
-Le fait que plusieurs personne travaille en simultané sur le même élément\
-L'exécution d'une action nécessitant beaucoup de ressource de la part du serveur.

Dans la plupart des cas, il s’agit d’un incident temporaire et nous vous recommandons d’attendre quelques minutes avant de réessayer.\
\
Si le problème se reproduit, n'hésitez pas à remonter un rapport de bug depuis le porte-voix dans Dastra afin que nos équipes puissent étudier le problème.\


## Message d'erreur : "Le champ Label est requis."

Ce message apparait généralement quand un élément a été laissé vide lors de la réponse à un questionnaire.\


## Message d'erreur : "Attention, du contenu HTML interdit est présent dans un champ !"

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2025-03-04 163623.png" alt=""><figcaption><p>Attention, du contenu HTML interdit est présent dans un champ !</p></figcaption></figure>

\
Ce message signifie que du code HTML (généralement contenu entre les balises <>) est présent dans un champ ou le HTML est interdit (pour raison de sécurité).\


\
Le message suivant permet d'identifier facilement le champ concerné :

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2025-03-04 164132.png" alt=""><figcaption><p>Attention, du contenu HTML interdit est présent dans un champ </p></figcaption></figure>



## Message d'erreur : "L'identifiant de l'utilisateur n'existe pas dans votre organisation." à l'enregistrement d'un traitement

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2025-05-15 102250.png" alt=""><figcaption><p>L'identifiant de l'utilisateur n'existe pas dans votre organisation.</p></figcaption></figure>

Ce message signifie qu'un utilisateur ayant été supprimé de votre espace de travail est toujours défini comme approbateur dans les parties prenantes du traitement :

<figure><img src="../.gitbook/assets/Capture d&#x27;écran 2025-05-15 102626.png" alt=""><figcaption><p>Utilisateur supprimé définit en tant que partie prenante du traitement</p></figcaption></figure>

Il faut retirer l'utilisateur supprimé des parties prenantes du traitement pour résoudre le problème.
