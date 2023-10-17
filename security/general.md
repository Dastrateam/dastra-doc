---
description: >-
  La sécurité fait partie intégrante de la structure de nos produits Cloud, de
  notre infrastructure et de nos processus. Ainsi, vous avez la certitude que
  vos données sont protégées.
---

# Sécurité chez Dastra

## Hébergement sécurisé sur le Cloud

Nous externalisons l'hébergement des données de la plateforme auprès de Microsoft Azure.&#x20;

Les lieux de stockage des données sont situés à Paris et Marseille en France. Une redondance entre les données est effectuée entre les deux sites.&#x20;

## **Authentification à deux facteurs**

Il est possible pour tous les propriétaires d'organisation de forcer l'utilisation de l'authentification à deux facteurs. L'authentification à 2 facteurs fonctionne en utilisant TOTP.\
Chaque utilisateur peut individuellement activer la fonctionnalité d'authentification à 2 facteurs.

[En savoir plus sur l'authentification forte](mfa.md)

## Chiffrement des données en transit

Toutes les données échangées entre nos clients et applications sont chiffrées en transit à l'aide du protocole TLS (Transport Layer Security) avec PFS (Perfect Forward Secrecy). L'autorité de certification du chiffrage est CloudFlare inc.

## Chiffrement des données au repos

Les disques de données sur les serveurs hébergeant des données clients sur le cloud Azure sont toutes encodées au repos à l'aide de la technologie "Transparent data encryption".

Les fichiers physiques sont également encryptées statiquement dans le service Azure Storage avec uns système d'encryptage transparent 256-bit [AES encryption](https://en.wikipedia.org/wiki/Advanced\_Encryption\_Standard), un des algorithme les plus solide qui est FIPS 140-2 compliant.

## Test de pénétration&#x20;

Nous faisons auditer régulièrement notre application par un auditeur tiers indépendant.&#x20;

Le dernier test a été réalisé le 25 janvier 2022 et n'a révélé aucune vulnérabilité critique.

## **Journaux d'audit d'organisation**

Les administrateurs d'organisation peuvent suivre tous les changements apportés à la gestion des utilisateurs et permissions d'accès.

## Identifiants uniques

Chaque utilisateur possède un identifiant unique et l'utilisation de comptes partagés entre plusieurs utilisateurs n'est pas autorisée.

## Sauvegarde des données

L'ensemble des données (Azure SQL) et fichiers (Azure Blob Storage) de nos utilisateurs sont régulièrement sauvegardées avec un historique d'un mois.

## Règles d'archivage des données

Dans le cas d'une suppression d'un compte. Les données sont conservées 1 mois avant leur suppression définitive.

## **Règles de mot de passe**

Au moins 8 caractères comportant 3 des 4 types de caractères (majuscules, minuscules, chiffres, caractères spéciaux)&#x20;

Temporisation d’accès au compte après plusieurs échecs.

Chiffrement des mots de passe en base de données.



## Politique de renouvellement des mots de passe

Dastra permet à l'administrateur de compte via [la page de gestion de la sécurité](https://app.dastra.eu/general-settings/security) de définir une politique de renouvellement des mots de passe de l'ensemble de vos utilisateurs.

## **Contrôles de jeton d'API**

Affichez et gérez l'ensemble des clés d'API utilisés par les développeurs de votre organisation

## Contrôle des accès total

Utilisation du modèle de gestion des accès [RBAC ](https://en.wikipedia.org/wiki/Role-based\_access\_control)(Role-base-access-control). Le responsable de l'organisation est en mesure de choisir les rôles et permissions de chaque utilisa

## Authentification sécurisée basée sur OpenIdConnect pour l'ensemble de nos sites

![](<../.gitbook/assets/image (22).png>)

L'autorité d'authentification est [https://account.dastra.eu](https://account.dastra.eu) utilise la technologie [IdentityServer4 ](https://identityserver.io/)pour assurer l'authentification de tous nos utilisateurs.&#x20;

**OpenID** est un système d’[authentification](https://fr.wikipedia.org/wiki/Authentification) décentralisé qui permet l’[authentification unique](https://fr.wikipedia.org/wiki/Authentification\_unique), ainsi que le partage d’attributs. Il permet à un utilisateur de s’authentifier auprès de plusieurs sites (devant prendre en charge cette technologie) sans avoir à retenir un identifiant pour chacun d’eux mais en utilisant à chaque fois un unique identifiant OpenID.

## **Liste d'autorisation des adresses IPs**

Il est possible de filtrer les utilisateurs à la connexion en fonction de leurs adresses IP

## Liste d'autorisation des domaines des emails

Les administrateurs peuvent définit une liste blanche de domaines d'emails autorisés (ex: gmail.com). Pour effectuer ces réglages, rendez vous dans **Configuration** => **Sécurité** => **Filtres de domaines**

## Isolation stricte entre les environnements de production et de développement

Hors mis quelques personnes habilitées, les développeurs de l'application n'utilisent et n'accèdent jamais aux données de l'environnement de production. Cette isolation est stricte et ne peut être contournée.&#x20;

Dans les environnement de tests ou de pré-production, nous n'utilisons que des jeux de données de tests que nous avons produit.

## Pentests réguliers

Tous les ans, nous effectuons un test de pénétration sur tout le périmètre de l'application (API Rest, Service d'authentification, Widgets...).+

Notre méthodologie de test de sécurité suit les recommandations de l'**OWASP** et se compose de différentes phases, de la recherche d'informations de source ouverte (Reconnaissance) à l'exploitation des vulnérabilités découvertes.

