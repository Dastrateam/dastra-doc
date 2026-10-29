---
description: >-
  Apprenez à rendre l'authentification obligatoire, à contrôler l'accès aux
  documents et à filtrer les adresses IP de votre Trust Center.
---

# Sécurité

La section **Sécurité** de la page d'édition regroupe trois réglages : l'authentification obligatoire, l'approbation des téléchargements de documents et le filtrage par adresse IP. Les propriétaires du Trust Center se désignent dans la section **Configuration**.

<figure><img src="../../../.gitbook/assets/trust-center-security-1.png" alt="Section Sécurité d'un Trust Center avec les deux options et les règles de filtrage IP"><figcaption><p>La section Sécurité d'un Trust Center</p></figcaption></figure>

## Authentification obligatoire

Activez **Authentification nécessaire pour accéder au Trust Center** pour rendre la connexion obligatoire. Les visiteurs doivent alors se connecter à Dastra avec un compte de votre organisation avant d'ouvrir le portail. Si un SSO est attribué à tous les utilisateurs, ils sont dirigés vers ce SSO.

Nous recommandons de configurer le [SSO](../../settings/sso/README.md) avec la création automatique des utilisateurs : tous vos collaborateurs peuvent alors accéder au Trust Center sans rôle ni permission particuliers.

## Propriétaires

Le champ **Propriétaires** se trouve dans la section **Configuration**. Lisez [Page d'accueil et configuration générale](home.md).

## Contrôle d'accès aux documents

L'option **Exiger une approbation pour le téléchargement des fichiers** n'apparaît que si la fonctionnalité **Documents** est cochée. Elle est activée sur un nouveau Trust Center.

Lorsqu'elle est activée :

1. Les visiteurs voient la liste des documents, mais ne peuvent pas les télécharger directement. Ils soumettent une **demande d'accès** en indiquant leur adresse e-mail et un message.
2. Les propriétaires du Trust Center reçoivent un e-mail qui renvoie vers la demande. S'il n'y a aucun propriétaire, ce sont les propriétaires de l'organisation qui le reçoivent.
3. Le propriétaire ouvre la demande, saisit si besoin une **Justification de la décision**, puis clique sur **Approuver la demande d'accès** ou **Rejeter la demande d'accès**. Le visiteur reçoit la justification par e-mail.
4. Si la demande est approuvée, le visiteur reçoit un e-mail qui contient un lien de téléchargement valide 30 jours.

Les demandes se traitent dans l'écran **Demandes d'accès à des fichiers**, qui liste toutes les demandes avec leur statut. Le lien du e-mail de notification l'ouvre directement sur la demande concernée.

{% hint style="info" %}
Quand des propriétaires sont désignés, eux seuls peuvent approuver ou rejeter les demandes. Sans propriétaire, les demandes sont notifiées aux propriétaires de l'organisation.
{% endhint %}

## Filtrage par adresse IP

Cette section vous permet également de définir des règles pour limiter l'accès à votre Trust Center à certaines plages d'IP. Par défaut, sans ajout de filtrage IP de votre part, votre Trust Center sera accessible à toute personne disposant du lien d'accès, sous réserve que le Trust Center soit activé.

Cliquez sur **Ajouter une règle de filtrage IP**, puis renseignez le nom de la règle, le début et la fin de la plage d'IP. Une adresse IP qui n'appartient à aucune des plages est refusée.

{% hint style="info" %}
Ce filtrage est **distinct** du [filtrage IP de l'organisation](../../settings/ip-filtering.md), qui ne s'applique pas au Trust Center.
{% endhint %}
