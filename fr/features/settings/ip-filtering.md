---
description: >-
  Restreignez la connexion à Dastra à des plages d'adresses IP autorisées :
  périmètre, fonctionnement, blocage et points d'attention.
---

# Filtrage IP

Le filtrage IP permet de limiter l'accès à votre organisation Dastra à une liste de plages d'adresses IP autorisées (par exemple celles de vos bureaux ou de votre VPN d'entreprise). Il se configure dans **Configuration** > **Sécurité**.

{% hint style="info" %}
Cette fonctionnalité est réservée à l'offre Enterprise ou à une option payante. Rapprochez-vous de votre contact Dastra pour l'activer.
{% endhint %}

{% hint style="danger" %}
Un message d'avertissement indique « Cette action n'est pas réversible ». En pratique, une règle de filtrage ne peut pas être supprimée ni désactivée depuis l'interface : **seule une intervention de l'équipe d'administration de Dastra** permet de la retirer. Vérifiez soigneusement vos plages avant de les enregistrer, sous peine de vous verrouiller vous-même.
{% endhint %}

## Définir les règles

* Les règles s'appliquent à **toute l'organisation** (et non à un espace de travail en particulier).
* Chaque règle est exprimée sous forme de plage, avec une **adresse de début** et une **adresse de fin**. La notation CIDR (ex. `10.0.0.0/24`) n'est pas prise en charge : convertissez vos réseaux en plages de début et de fin.
* Les adresses **IPv4 et IPv6** sont acceptées.
* Il n'y a pas de limite au nombre de règles.

## Utilisateurs concernés

Le filtrage s'applique à **tous les utilisateurs de l'organisation, administrateurs compris**. Il n'existe ni exemption pour les administrateurs, ni liste d'exemptions.

Il concerne tous les modes de connexion, car le contrôle est réalisé après l'authentification :

* identifiant et mot de passe ;
* SSO (SAML 2, OpenID, ADFS, Entra, Okta) ;
* passkey ;
* lien magique ou invitation par e-mail.

Les comptes de service locaux exemptés du SSO ne sont **pas** exemptés du filtrage IP.

## Moment du contrôle

L'adresse IP est vérifiée au moment de la connexion, puis à chaque **renouvellement du jeton** d'authentification. Une session déjà ouverte n'est donc pas coupée instantanément si l'utilisateur change de réseau (par exemple du bureau au télétravail) : elle est interrompue au prochain renouvellement du jeton.

Durées de validité des jetons :

| Type de session | Durée de validité du jeton |
|---|---|
| Application web | 6 minutes (renouvelé automatiquement) |
| Session standard | 1 heure |
| Option « Se souvenir de moi » | 30 jours |

## Adresse IP prise en compte

Dastra utilise l'adresse IP publique vue par son infrastructure d'accès (celle qui reçoit votre requête avant l'application). Un utilisateur qui passe par un VPN ou un proxy d'entreprise est donc filtré sur l'**adresse de sortie** du VPN ou du proxy : c'est cette adresse qu'il faut autoriser.

## Ce que voit un utilisateur bloqué

L'utilisateur est redirigé vers une page d'erreur affichant :

> IP Address not allowed — Your IP address is not allowed by your organization. Please contact your account's administrator.

{% hint style="warning" %}
Les blocages ne sont **pas** enregistrés dans le journal d'audit et ne sont pas envoyés au [streaming SIEM](siem.md).
{% endhint %}

## Ce que le filtrage ne couvre pas

| Accès | Filtré ? |
|---|---|
| Appels API avec une [clé d'API](api-keys.md) | Non |
| [SCIM](scim.md) | Non |
| [Streaming SIEM](siem.md) et connecteurs BI | Non |
| Répondants externes de questionnaires (lien public) | Non |
| Portail des demandes de droits et Trust Center | Non, ils disposent de leur propre paramétrage (voir [Trust Center - Sécurité](../trust-center/configuration/security.md)) |

## Support Dastra

Le support Dastra est lui aussi soumis au filtrage : il ne peut plus accéder à votre compte (impersonation) depuis une adresse non autorisée. Pour supprimer ou désactiver une règle, contactez le support Dastra.
