---
description: >-
  La sécurité fait partie intégrante de la structure de nos produits Cloud, de
  notre infrastructure et de nos processus. Ainsi, vous avez la certitude que
  vos données sont protégées.
---

# Sécurité chez Dastra

## Hébergement sécurisé sur le Cloud

Nous externalisons l'hébergement des données de la plateforme auprès de Microsoft Azure. Nous avons choisi cette plateforme car elle est très largement déployée chez nos clients (MS 365...) et celle-ci offre le niveau de sécurité [parmi les plus élevés du marché](https://learn.microsoft.com/fr-fr/azure/compliance/).

Les lieux de stockage des données sont situés à Paris (données de production) et Marseille (les sauvegardes) en France. Une redondance des données est réalisée dans le data center d'Amsterdam.&#x20;

## **Authentification à deux facteurs**

L'authentification à 2 facteurs fonctionne en utilisant le protocole TOTP. \
Chaque utilisateur peut individuellement activer la fonctionnalité d'authentification à 2 facteurs. Il est possible pour tous les propriétaires d'organisation de forcer l'utilisation de l'authentification à deux facteurs.&#x20;

[En savoir plus sur l'authentification forte](mfa.md)

## Single Sign On (SSO) et SCIM

Dastra propose sur option ou en fonction du plan que vous choisissez un [SSO en self service](../features/settings/single-sign-on-sso/) simple et bien documenté. Nous supportons les protocoles SAML2P ou OpenID compatibles avec n'importe quel annuaire d'entreprise. En complément, il est possible de provisionner automatiquement les utilisateurs de votre annuaire à l'aide de notre serveur [SCIM](../features/settings/scim.md).

## Chiffrement des données en transit

Toutes les données échangées entre nos clients et applications sont chiffrées en transit à l'aide du protocole TLS (Transport Layer Security) avec PFS (Perfect Forward Secrecy). L'autorité de certification du chiffrage est CloudFlare inc.

## Chiffrement des données au repos

Les disques de données sur les serveurs hébergeant des données clients sur le cloud Azure sont toutes encodées au repos à l'aide de la technologie "[Transparent data encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16)".

Les fichiers physiques sont également encryptées statiquement dans le service Azure Storage avec uns système d'encryptage transparent 256-bit [AES encryption](https://en.wikipedia.org/wiki/Advanced\_Encryption\_Standard), un des algorithme les plus solide qui est FIPS 140-2 compliant.

L'ensemble des clés de chiffrement est stocké **dans un coffre de clés managé par Dastra** (incluant de la rotation automatique).

## Tests de pénétration (Pentests)&#x20;

Nous faisons auditer tous les ans la sécurité de l'application par un auditeur tiers indépendant.&#x20;

Le dernier test a été réalisé en septembre 2023 et n'a révélé aucune vulnérabilité critique.

Notre méthodologie de test de sécurité suit les recommandations de l'**OWASP** et se compose de différentes phases, de la recherche d'informations de source ouverte (Reconnaissance) à l'exploitation des vulnérabilités découvertes.

## **Journaux d'audit de sécurité**

Les administrateurs d'organisation peuvent suivre tous les changements apportés à la gestion des utilisateurs, espaces de travail et permissions d'accès.

## Identifiants uniques

Chaque utilisateur possède un identifiant unique et l'utilisation de comptes partagés entre plusieurs utilisateurs n'est pas autorisée.

## Sauvegarde des données

L'ensemble des données (Azure SQL) et fichiers (Azure Blob Storage) de nos utilisateurs sont régulièrement sauvegardées avec un historique 3 mois (long time retention) et en PITR (point in time restore) sur 7 jours.

## Règles d'archivage des données

Dans le cas d'une suppression d'un compte. Les données sont conservées 1 mois avant leur suppression définitive.

## **Politique de mot de passe**

Au moins **10 caractères** comportant **4 types de caractères** (majuscules, minuscules, chiffres, caractères spéciaux)&#x20;

Temporisation d’accès au compte après plusieurs échecs.

Chiffrement des mots de passe en base de données.

## Politique de renouvellement des mots de passe

Dastra permet à l'administrateur de compte via [la page de gestion de la sécurité](https://app.dastra.eu/general-settings/security) de définir une politique de renouvellement des mots de passe de l'ensemble de vos utilisateurs.

## **Contrôles de jeton d'API**

Affichez et gérez l'ensemble des [clés d'API](../features/settings/gestion-des-cles-dapi.md) utilisés par les développeurs de votre organisation. Vous pouvez également limiter le scope de celles-ci à certains espaces de travails ou certaines permissions.

## Contrôle des accès total

Utilisation du modèle de gestion des accès [RBAC ](https://en.wikipedia.org/wiki/Role-based\_access\_control)(Role-base-access-control). Le responsable de l'organisation est en mesure de choisir les [rôles et permissions](../features/settings/roles-et-permissions.md) de chaque utilisateur de manière extrêmement souple.

## Authentification sécurisée basée sur OpenIdConnect pour l'ensemble de nos sites

L'autorité d'authentification est [https://account.dastra.eu](https://account.dastra.eu) utilise OpenId afin d'assurer l'authentification de tous nos utilisateurs.&#x20;

**OpenID** est un système d’[authentification](https://fr.wikipedia.org/wiki/Authentification) décentralisé qui permet l’[authentification unique](https://fr.wikipedia.org/wiki/Authentification\_unique), ainsi que le partage d’attributs. Il permet à un utilisateur de s’authentifier auprès de plusieurs sites (devant prendre en charge cette technologie) sans avoir à retenir un identifiant pour chacun d’eux mais en utilisant à chaque fois un unique identifiant OpenID.

## **Liste d'autorisation des adresses IPs**

Il est possible de filtrer les utilisateurs à la connexion en fonction de leurs adresses IP

## Liste d'autorisation des domaines des emails

Les administrateurs peuvent définit une liste blanche de domaines d'emails autorisés (ex: gmail.com). Pour effectuer ces réglages, rendez vous dans **Configuration** => **Sécurité** => **Filtres de domaines**

## Isolation stricte entre les environnements de production et de développement

Hors mis quelques personnes habilitées, les développeurs de l'application n'utilisent et n'accèdent jamais aux données de l'environnement de production. Cette isolation est stricte et ne peut être contournée.&#x20;

Dans les environnement de tests ou de pré-production, nous n'utilisons que des jeux de données de tests que nous avons produit.

##

