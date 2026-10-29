---
description: >-
  Hébergement, chiffrement, authentification, contrôle des accès, sauvegardes :
  les mesures de sécurité mises en oeuvre par Dastra pour protéger vos données.
---

# Sécurité chez Dastra

Cette page décrit les mesures de sécurité mises en oeuvre par Dastra pour protéger vos données : hébergement, chiffrement, authentification, contrôle des accès et sauvegardes.

{% hint style="info" %}
Les réglages de sécurité de l'organisation (authentification forte obligatoire, filtrage des adresses IP, filtrage des domaines d'e-mails, politique de renouvellement des mots de passe, déconnexion automatique, conservation des journaux de sécurité, streaming SIEM) sont réservés aux propriétaires de l'organisation et au plan Enterprise. Ils se trouvent dans **Configuration de l'organisation** > **Sécurité**.
{% endhint %}

## Hébergement sécurisé sur le Cloud

Nous externalisons l'hébergement des données de la plateforme auprès de Microsoft Azure. Nous avons choisi cette plateforme car elle est très largement déployée chez nos clients (Microsoft 365, etc.) et qu'elle offre un niveau de sécurité [parmi les plus élevés du marché](https://learn.microsoft.com/fr-fr/azure/compliance/).

Les lieux de stockage des données sont situés à Paris (données de production) et Marseille (sauvegardes), en France. Une redondance des données est réalisée dans le data center d'Amsterdam.

Pour une instance dédiée sur un cloud souverain, voir [Dastra sur Bleu](bleu.md).

## Authentification à deux facteurs

L'authentification à deux facteurs fonctionne avec le protocole TOTP.

Chaque utilisateur peut activer l'authentification à deux facteurs pour son propre compte. Les propriétaires de l'organisation peuvent aussi la rendre obligatoire pour tous les utilisateurs internes gérés par l'organisation.

Voir [Authentification forte](mfa.md).

## Single Sign On (SSO) et SCIM

Dastra propose, sur option ou en fonction du plan que vous choisissez, un [SSO en self-service](../features/settings/sso/README.md). Nous prenons en charge les protocoles SAML2P et OpenID, compatibles avec la plupart des annuaires d'entreprise. En complément, vous pouvez provisionner automatiquement les utilisateurs de votre annuaire avec le serveur [SCIM](../features/settings/scim.md).

## Chiffrement des données en transit

Toutes les données échangées entre nos clients et applications sont chiffrées en transit avec le protocole TLS (Transport Layer Security) et la confidentialité persistante (PFS, Perfect Forward Secrecy). L'autorité de certification est Cloudflare, Inc.

## Chiffrement des données au repos

Les disques de données des serveurs qui hébergent les données clients sur le cloud Azure sont chiffrés au repos avec la technologie [Transparent Data Encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16).

Les fichiers sont également chiffrés au repos dans le service Azure Storage, avec un chiffrement transparent [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) 256 bits, conforme à la norme FIPS 140-2.

L'ensemble des clés de chiffrement est stocké dans un coffre de clés managé par Dastra, avec rotation automatique.

## Tests de pénétration (pentests)

Nous faisons auditer chaque année la sécurité de l'application par un auditeur tiers indépendant.

Le dernier test n'a révélé aucune vulnérabilité critique.

Notre méthodologie de test suit les recommandations de l'**OWASP** et se compose de plusieurs phases, de la recherche d'informations de source ouverte (reconnaissance) à l'exploitation des vulnérabilités découvertes.

## Journaux d'audit de sécurité

Les administrateurs de l'organisation peuvent suivre tous les changements apportés à la gestion des utilisateurs, aux espaces de travail et aux permissions d'accès.

Les propriétaires de l'organisation règlent la durée de conservation des journaux de sécurité dans **Configuration de l'organisation** > **Sécurité**, carte **Conservation des journaux de sécurité** : de 30 jours à 3 ans (180 jours recommandés). Les journaux arrivés au terme de cette durée sont purgés chaque nuit.

Pour envoyer ces événements en continu à votre outil de supervision, voir [Streaming SIEM](../features/settings/siem.md).

## Identifiants uniques

Chaque utilisateur possède un identifiant unique. L'utilisation de comptes partagés entre plusieurs utilisateurs n'est pas autorisée.

## Sauvegarde des données

L'ensemble des données (Azure SQL) et des fichiers (Azure Blob Storage) de nos utilisateurs est sauvegardé régulièrement, avec un historique de 3 mois (rétention à long terme) et une restauration à un instant donné (PITR, point in time restore) sur 7 jours.

## Règles d'archivage des données

En cas de suppression d'un compte, les données sont conservées 1 mois avant leur suppression définitive.

## Politique de mot de passe

* Au moins **10 caractères**, comportant **4 types de caractères** : majuscules, minuscules, chiffres et caractères spéciaux.
* Temporisation d'accès au compte après plusieurs échecs de connexion.
* Chiffrement des mots de passe en base de données.

## Politique de renouvellement des mots de passe

Les propriétaires de l'organisation peuvent définir une durée de vie des mots de passe dans [Configuration de l'organisation > Sécurité](https://app.dastra.eu/general-settings/security), carte **Politique de renouvellement de mot de passe**. Elle s'applique aux utilisateurs internes de l'organisation qui n'utilisent pas le SSO. À l'expiration du délai, l'utilisateur crée un nouveau mot de passe à sa prochaine connexion.

## Déconnexion automatique

Les propriétaires de l'organisation peuvent activer la carte **Déconnexion automatique** : tous les utilisateurs internes gérés par l'organisation sont alors déconnectés après 1 heure d'inactivité.

## Contrôles de jeton d'API

Affichez et gérez l'ensemble des [clés d'API](../features/settings/api-keys.md) utilisées par les développeurs de votre organisation. Vous pouvez aussi limiter la portée d'une clé à un espace de travail et à certaines permissions.

## Contrôle des accès

Dastra utilise le modèle de gestion des accès [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) (Role-Based Access Control). Le propriétaire de l'organisation choisit les [rôles et permissions](../features/settings/roles.md) de chaque utilisateur de manière fine.

## Authentification sécurisée basée sur OpenID Connect pour l'ensemble de nos sites

L'autorité d'authentification est [https://account.dastra.eu](https://account.dastra.eu). Elle utilise OpenID pour authentifier tous nos utilisateurs.

**OpenID** est un système d'[authentification](https://fr.wikipedia.org/wiki/Authentification) décentralisé qui permet l'[authentification unique](https://fr.wikipedia.org/wiki/Authentification_unique) ainsi que le partage d'attributs. Il permet à un utilisateur de s'authentifier auprès de plusieurs sites qui prennent en charge cette technologie, avec un seul identifiant OpenID, sans avoir à retenir un identifiant pour chacun d'eux.

## Liste d'autorisation des adresses IP

Vous pouvez restreindre l'accès à l'organisation à des plages d'adresses IP autorisées. Le filtrage s'applique à tous les utilisateurs (administrateurs compris) et à tous les modes de connexion (mot de passe, SSO, passkey, lien magique), à la connexion puis à chaque renouvellement du jeton. Il ne s'applique pas aux API, au SCIM ni au streaming SIEM.

Dastra vérifie que votre propre adresse IP fait partie des plages autorisées. Vérifiez soigneusement vos plages avant de les enregistrer : une règle ne peut pas être retirée depuis l'interface. Pour le détail, consultez la page [Filtrage IP](../features/settings/ip-filtering.md).

## Liste d'autorisation des domaines d'e-mails

Les propriétaires de l'organisation peuvent définir la liste des domaines d'e-mails autorisés (par exemple `example.com`) : seuls les utilisateurs dont l'adresse e-mail appartient à l'un de ces domaines peuvent se connecter. Rendez-vous dans **Configuration de l'organisation** > **Sécurité**, carte **Filtrer les domaines des e-mails de vos utilisateurs**. La configuration peut prendre quelques minutes pour s'appliquer.

## Isolation stricte entre les environnements de production et de développement

À l'exception de quelques personnes habilitées, les développeurs de l'application n'utilisent et n'accèdent jamais aux données de l'environnement de production. Cette isolation est stricte et ne peut pas être contournée.

Dans les environnements de test et de préproduction, nous n'utilisons que des jeux de données de test que nous avons produits.
