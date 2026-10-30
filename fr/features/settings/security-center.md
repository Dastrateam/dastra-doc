---
description: >-
  Définissez les règles de sécurité de votre organisation (renouvellement des
  mots de passe, déconnexion automatique, authentification forte, filtres d'IP
  et de domaines e-mail) et consultez les journaux de sécurité et l'historique
  d'activités.
---

# Sécurité de l'organisation et journaux de sécurité

Cette page s'adresse aux propriétaires de l'organisation. Elle décrit la page **Sécurité** des paramètres de l'organisation, où vous définissez les règles de sécurité qui s'appliquent à tous les utilisateurs de votre organisation, et les deux pages de journaux qui permettent de suivre ce qui s'y passe.

## Ouvrir la page Sécurité

Cliquez sur l'icône d'engrenage de la barre supérieure (**Paramètres de l'organisation**), puis sur **Sécurité** dans le menu de gauche. La page n'est visible que des propriétaires de l'organisation. Elle nécessite le plan **Entreprise** : avec un autre plan, la page affiche le message **Cette fonctionnalité est réservée au plan : Entreprise**.

<figure><img src="../../.gitbook/assets/settings-security-center-1.png" alt="La page Sécurité des paramètres de l'organisation avec ses cartes"><figcaption><p>La page Sécurité, avec une carte par règle</p></figcaption></figure>

Chaque carte s'applique dès que vous la modifiez : il n'y a pas de bouton d'enregistrement.

## Politique de renouvellement de mot de passe

La carte **Politique de renouvellement de mot de passe** définit une durée de vie des mots de passe : **90 jours**, **180 jours** ou **365 jours**. Choisissez **Indéfini** pour désactiver la politique.

La politique concerne les utilisateurs internes de votre organisation qui ne se connectent pas avec le SSO. Les utilisateurs externes ne sont pas concernés. Lorsque la durée est dépassée, l'utilisateur est invité à créer un nouveau mot de passe fort à sa prochaine connexion.

## Conservation des journaux de sécurité

La carte **Conservation des journaux de sécurité** définit la durée pendant laquelle Dastra conserve les [journaux de sécurité](#journaux-de-securite). Choisissez une durée dans **Choisissez une durée de conservation** : 30 jours, 90 jours, 180 jours (**Recommandé**), 365 jours, 730 jours ou 1 095 jours.

Dastra supprime chaque nuit à 01h00 les journaux plus anciens que cette durée. Alignez la durée sur vos propres règles de conservation des traces d'audit.

## Déconnexion automatique

La carte **Déconnexion automatique** comporte un interrupteur, **Actif** ou **Désactivé**. Lorsqu'il est actif, tous les utilisateurs internes de votre organisation sont déconnectés après 1 heure d'inactivité.

## Forcer l'authentification forte

La carte **Forcer les utilisateurs à utiliser l'authentification forte (A deux facteurs)** comporte un interrupteur. Lorsqu'il est actif, tous les utilisateurs internes de votre organisation doivent configurer l'authentification à deux facteurs à leur prochaine connexion. Dastra utilise le protocole TOTP, avec une application d'authentification, pour la seconde étape après le mot de passe. Pour la configurer en tant qu'utilisateur, consultez [Se connecter et gérer l'authentification](../../getting-started/setup/login.md#activer-lauthentification-forte).

## Filtrer les adresses IP et les domaines e-mail

Deux cartes restreignent les connexions :

* **Filtrer les adresse IP des utilisateurs** limite l'accès à des plages d'adresses IP. Lisez [Filtrage IP](ip-filtering.md) avant d'enregistrer une règle : vous ne pouvez pas la supprimer depuis l'interface.
* **Filtrer les domaines des e-mails de vos utilisateurs** n'autorise la connexion qu'aux utilisateurs dont l'adresse e-mail appartient aux domaines listés. Saisissez un domaine comme `dastra.eu`, puis appuyez sur Entrée. La configuration peut prendre quelques minutes à se mettre en place.

Ce filtre est distinct du bloc **Domaines email autorisés** de la page **Single sign on**, qui affecte les nouveaux collègues à un espace de travail : consultez [Domaines emails](email-domains.md).

## Streaming SIEM

La dernière carte diffuse vos événements de sécurité en temps réel vers votre SIEM. Consultez [Streaming SIEM](siem.md).

## Journaux de sécurité

Les journaux de sécurité listent les événements de sécurité de votre organisation. Cliquez sur l'icône d'engrenage de la barre supérieure, puis sur **Journaux de sécurité** dans le menu de gauche. Seuls les propriétaires de l'organisation peuvent ouvrir cette page.

<figure><img src="../../.gitbook/assets/settings-security-logs-1.png" alt="La page Journaux de sécurité avec ses filtres et la liste des événements"><figcaption><p>La page Journaux de sécurité</p></figcaption></figure>

1. Choisissez une période avec le sélecteur de dates.
2. Cliquez sur **Evènements** pour sélectionner un ou plusieurs types d'événements : la liste se met à jour.
3. Lisez la liste : **Date**, **Importance**, le libellé de l'événement et l'**Utilisateur** qui l'a déclenché.
4. Cliquez sur un événement ou sur **Détails** pour ouvrir sa page. Elle affiche les types, la **Description**, l'utilisateur, la date et l'**Identifiant de l'évènement**, en **Affichage structuré** ou **Affichage brut**, avec un bouton **Copier** pour les données brutes.

**Exporter** télécharge les journaux de la période sélectionnée. **Exporter (SIEM)** les télécharge dans un format que votre SIEM sait lire : **CEF (Common Event Format)**, **Syslog (RFC 5424)** ou **Splunk HEC (JSON)**. Le même menu ouvre **Configurer le streaming temps réel** pour les organisations au plan Entreprise. Consultez [Streaming SIEM](siem.md#export-manuel-depuis-les-journaux-daudit).

Dastra conserve les événements pendant la durée définie dans [Conservation des journaux de sécurité](#conservation-des-journaux-de-securite).

## Historique d'activités

La page **Historique d'activités**, également dans les paramètres de l'organisation, liste les événements de toute l'organisation : créations, modifications, suppressions et autres actions sur les fiches, en plus des événements de sécurité. Elle est visible de tous les utilisateurs qui ouvrent les paramètres de l'organisation.

1. Choisissez une période.
2. Affinez la liste avec les filtres **Espace de travail**, **Type**, **Evènements** et **Utilisateur**. Cliquez sur **Effacer les filtres** pour les retirer.
3. Les événements sont regroupés par jour. Cliquez sur **Afficher plus** pour voir les plus anciens.
4. Cliquez sur un événement pour ouvrir son détail, avec les mêmes affichages structuré et brut que les journaux de sécurité.

Seuls les propriétaires de l'organisation voient le bouton **Exporter** de cette page.
