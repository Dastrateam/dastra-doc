---
description: Découvrez comment le système d'invitation de Dastra fonctionne.
---

# Inviter des utilisateurs

## Invitez un utilisateur

Vous pouvez amener quelqu'un à collaborer sur vos espaces en l'invitant dans l'organisation à laquelle appartient l'espace.&#x20;

Vous pouvez inviter des utilisateurs à votre espace de travail en cliquant sur le bouton "réglages" en bas à gauche de l'écran, puis "gestion d'accès / utilisateurs" et enfin "inviter un utilisateur":

<figure><img src="../../.gitbook/assets/image (12) (2) (2).png" alt=""><figcaption></figcaption></figure>



Rentrez l'adresse email de la personne que vous souhaitez inviter dans votre espace Dastra. Si cette adresse n'est pas déjà rattachée à l'organisation, cliquez sur celle-ci pour lui envoyer un lien d'invitation.

![](<../../.gitbook/assets/image (130).png>)

Un formulaire apparait. Rentrez son nom, son prénom, son rôle, son équipe puis cliquez sur le bouton "Envoyer une invitation". La personne invitée recevra un mail contenant un lien qui, une fois cliqué, permettra à cette personne d'accéder à l'espace.\
\
Ca y est, l'utilisateur a été invité !

### Retrouvez les invitations en cours

Vous pouvez piloter les invitations en cours dans les réglages de l'espace de travail sur la section "Utilisateurs".&#x20;

<figure><img src="../../.gitbook/assets/image (12) (3).png" alt=""><figcaption></figcaption></figure>

### Renvoyer un lien d'invitation

Si l'utilisateur invité n'a pas cliqué sur le lien d'invitation et que le lien a expiré (au bout de 10 jours), vous pouvez lui renvoyer le lien d'invitation en cliquant sur le bouton "Renvoyer l'invitation".&#x20;

<figure><img src="../../.gitbook/assets/image (16) (2).png" alt=""><figcaption></figcaption></figure>

### Créer puis affectez des équipes

Dans Dastra, les utilisateurs sont regroupés par équipe, qui elles-mêmes sont affectées soit à des entités juridiques, soit à des départements. Ainsi, il est possible de gérer finement les rôles et responsabilités.

{% hint style="info" %}
Il existe plusieurs rôles proposés par défaut dans Dastra, représentant des niveaux d'autorisation:

* **Administrateur**: Ils peuvent faire tout ce que les auteurs peuvent faire, en plus de modifier les paramètres d'organisation et d'espaces.
* **Contributeur**: Ils peuvent lire et éditer des espaces. Ils peuvent voir les brouillons et les modifications qui ne sont pas encore publiés. Ils peuvent publier des modifications. Ils ne peuvent pas modifier les paramètres d'organisation ni les paramètres d'espaces.
* **Lecteur**: peuvent uniquement visiter les espaces publiés dans l'organisation. Ils ne peuvent pas éditer et ne peuvent pas voir les modifications qui ne sont pas encore publiées.
{% endhint %}

## Importer une grande liste d'utilisateurs

Vous pouvez demander l'import d'une grande liste d'utilisateurs dans la plateforme. Pour cela il faut passer par les équipes de Dastra.&#x20;

**Les étapes à suivre :**&#x20;

* rendez vous sur ce lien : [https://app.dastra.eu/general-settings/users](https://app.dastra.eu/general-settings/users)
* Cliquez sur le bouton "contacter l'équipe de Dastra"

<figure><img src="../../.gitbook/assets/image (1) (1) (4) (1).png" alt=""><figcaption></figcaption></figure>

* Créez un fichier par espace de travail au format CSV comprenant les colonnes suivantes séparées par des , (virgule) :&#x20;

De manière obligatoire : &#x20;

* Email (email de l'utilisateur)
* GivenName (prénom de l'utilisateur)
* FamilyName(nom de l'utilisateur)

De manière optionnelle :&#x20;

* Roles (séparé par des |) > cela correspond aux rôles dans Dastra
* Teams (séparé par des |) > cela correspond aux équipes dans Dastra
* SsoConfigurationId > cela correspond à l'identifiant de login SSO le cas échéant

Voici un modèle de fichier à télécharger et à remplir :&#x20;

{% file src="../../.gitbook/assets/Template_import_users (1).csv" %}
Modèle de fichier d'import
{% endfile %}

**S'agissant des identifiants de rôles :**&#x20;

Par défaut : les rôles de base ont les identifiants suivants :&#x20;

* Administrateur = 1
* Contributeur = 2
* Lecteur = 3

Pour les rôles personnalisés que vous avez créé, l'identifiant est visible depuis la console de développement de votre navigateur via l'onglet réseau.&#x20;

{% hint style="info" %}
Pour ouvrir la console sur Chrome, utilisez le raccourci clavier suivant : Cmd + Option + C (sur Mac) ou Ctrl + Maj + J (sous Windows)

Pour ouvrir la console sur Firefox, utilisez le raccourci clavier suivant : Cmd + Option + K (sur Mac) ou Ctrl + Maj + J (sous Windows)

Pour ouvrir la console, vous pouvez utiliser le raccourci clavier suivant : Cmd + Option + C

Pour ouvrir la console sur Microsoft Edge, vous pouvez utiliser le raccourci suivant : Ctrl + Maj + I
{% endhint %}

Attention, les rôles doivent être créés préalablement.



<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption><p>Ici l'identifiant du rôle est le numéro 115</p></figcaption></figure>



**S'agissant des identifiants des équipes :**&#x20;

Ceux ci sont paramétrables lors de l'ajout d'une équipe

<figure><img src="../../.gitbook/assets/image (4) (2) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Attention, les équipes doivent être crées préalablement dans l'espace de travail
{% endhint %}

Enregistrez votre fichier au format CSV UTF 8&#x20;

<figure><img src="../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

Une fois votre fichier prêt, indiquez nous dans quel espace de travail vous souhaitez importer les utilisateurs et déposez le fichier via l'interface de dépôt :&#x20;



<figure><img src="../../.gitbook/assets/image (2) (3) (1).png" alt=""><figcaption></figcaption></figure>

Nous recevrons la demande et nous reviendrons vers vous pour le suivi.
