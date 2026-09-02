---
description: Dastra s'intègre à tous vos outils
---

# Intégrations

## Intégrations

Dastra se connecte aux outils que vos équipes utilisent déjà : importez votre inventaire applicatif depuis votre ITAM ou votre CMDB, synchronisez les demandes d'exercice de droits avec votre outil de ticketing, publiez des notifications dans vos canaux collaboratifs, diffusez vos journaux d'audit de sécurité vers votre SIEM, ou joignez des fichiers depuis vos drives. Les connecteurs natifs couvrent les outils les plus courants ; Zapier couvre tout le reste.

Le magasin d'intégrations est accessible dans **Paramètres > Intégrations** de votre workspace. Il liste toutes les intégrations disponibles, filtrables par catégorie et par objet Dastra ciblé, avec un basculement **Toutes / Installées**.

#### Comment fonctionnent les intégrations natives

Chaque intégration native repose sur trois concepts :

* **Les cas d'usage** — chaque intégration expose un ou plusieurs cas d'usage (par exemple _importer les applications comme actifs_ ou _synchroniser les demandes d'exercice de droits_). Les cas d'usage s'installent, s'activent, se configurent et se désinstallent indépendamment.
* **Les connexions** — une connexion enregistre la façon dont Dastra s'authentifie auprès de l'outil externe : des identifiants stockés chiffrés par Dastra, ou une autorisation OAuth déléguée. Vous pouvez créer plusieurs connexions vers le même outil (une instance de production et une sandbox, par exemple) et choisir celle utilisée par chaque cas d'usage. Les connexions affichent leur état de santé et peuvent être testées à tout moment.
* **Le mapping des champs** — les cas d'usage d'import vous laissent choisir, pour chaque champ Dastra, le champ externe qui l'alimente, avec des valeurs par défaut, un transcodage des valeurs pour les listes fermées (statuts, étapes de cycle de vie…) et des suggestions assistées par l'IA.

Les connecteurs d'import synchronisent une fois par jour et à la demande avec **Lancer la synchronisation**. Chaque exécution est tracée dans les journaux d'intégration, avec le nombre d'éléments créés, mis à jour, marqués et en erreur.

<figure><img src="../../.gitbook/assets/integrations-catalog.png" alt=""><figcaption></figcaption></figure>

Le détail dans [Connexions, cas d'usage et mapping des champs](https://doc.dastra.eu/api-references/integrations/connexions-et-mapping-des-champs).

#### Intégrations disponibles

| Intégration                     | Ce qu'elle fait                                                                                                                           | Documentation                                                                                                    |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **ServiceNow**                  | Importe les applications métier de votre CMDB comme actifs et les garde synchronisées quotidiennement                                     | [ServiceNow](https://doc.dastra.eu/api-references/integrations/servicenow)                                       |
| **SAP LeanIX**                  | Importe vos fact sheets Application comme actifs et les garde synchronisées quotidiennement                                               | [SAP LeanIX](https://doc.dastra.eu/api-references/integrations/sap-leanix)                                       |
| **Jira**                        | Crée et suit les demandes d'exercice de droits depuis votre projet Jira, et fait évoluer les tickets liés au fil du workflow des demandes | [Jira](https://doc.dastra.eu/api-references/integrations/jira)                                                   |
| **Filerskeepers**               | Intègre vos politiques de durées de conservation Filerskeepers à Dastra                                                                   | [Filerskeepers](https://doc.dastra.eu/api-references/integrations/filerskeepers)                                 |
| **Microsoft Teams**             | Publie les notifications de vos règles de workflow sous forme de cartes dans un canal Teams                                               | [Microsoft Teams](https://doc.dastra.eu/api-references/integrations/microsoft-teams)                             |
| **Slack**                       | Délivre les notifications Dastra dans votre espace Slack                                                                                  | —                                                                                                                |
| **Docusign**                    | Envoie vos contrats à vos sous-traitants pour signature électronique                                                                      | [Intégration avec Docusign](https://doc.dastra.eu/features/contrats/integration-avec-docusign)                   |
| **OneDrive / Google Drive**     | Joint des fichiers de vos drives à vos acteurs, mesures de sécurité, traitements, tâches, incidents…                                      | [Intégrations OneDrive/Google Drive](https://doc.dastra.eu/features/settings/integrations-onedrive-google-drive) |
| **Office 365 / Gmail**          | Envoie les e-mails de Dastra depuis votre propre boîte mail                                                                               | [Configuration du SMTP](https://doc.dastra.eu/features/settings/configuration-du-smtp)                           |
| **Adresses e-mail de collecte** | Transforme les e-mails envoyés à une adresse de collecte dédiée en tâches, demandes, violations de données, contrats ou traitements       | [Adresses emails de collecte](https://doc.dastra.eu/features/settings/data-collection-mailboxes)                 |
| **SIRENE (INSEE)**              | Complète la fiche de vos parties prenantes à partir du répertoire des entreprises                                                         | —                                                                                                                |
| **Fournisseur IA**              | Connecte n'importe quel fournisseur IA compatible OpenAI à l'assistant Dastra                                                             | —                                                                                                                |
| **Single sign-on (SSO)**        | Laisse vos utilisateurs se connecter avec votre propre fournisseur d'identité                                                             | [Single Sign On (SSO)](https://doc.dastra.eu/features/settings/single-sign-on-sso)                               |
| **Streaming SIEM**              | Diffuse vos événements d'audit de sécurité vers votre SIEM en temps réel                                                                  | [Streaming SIEM](https://doc.dastra.eu/features/settings/streaming-siem)                                         |
| **Zapier**                      | Connecte Dastra à plus de 3 000 applications via des workflows automatisés                                                                | [Zapier](https://doc.dastra.eu/api-references/integrations/zapier)                                               |

Certaines intégrations s'appliquent à l'ensemble de votre organisation plutôt qu'à un workspace — le single sign-on, le streaming SIEM, Office 365 / Gmail et le fournisseur IA. Leur tuile dans le magasin vous renvoie vers les paramètres de l'organisation correspondants, où elles se configurent par un propriétaire du compte.

#### Zapier : connecter tout le reste

Zapier est un outil d'automatisation en ligne qui relie vos applications et services sans code. Un **Zap** est un workflow automatisé composé d'un **déclencheur** et d'une ou plusieurs **actions** : lorsque l'événement déclencheur se produit, les actions s'exécutent.

Côté Dastra, Zapier peut réagir à deux déclencheurs — _nouvelle demande d'exercice de droits créée_ et _nouvelle tâche créée_ — et réaliser six actions : créer une tâche, créer un acteur, créer une demande d'exercice de droits, lier un acteur à un traitement existant, rechercher un acteur, et trouver ou créer un acteur. Vous pouvez donc partir d'un événement Dastra pour agir dans une application tierce, ou partir d'un événement tiers pour agir dans Dastra.

Des modèles préconfigurés (Salesforce, Zoho, Trello, Google Sheets, Excel, Outlook, Azure DevOps…) sont disponibles depuis la [page Dastra du catalogue Zapier](https://zapier.com/apps/dastra/integrations), et l'éditeur de Zap vous permet de construire votre propre workflow de zéro. Voir la page [Zapier](https://doc.dastra.eu/api-references/integrations/zapier) et ses [questions fréquentes](https://doc.dastra.eu/api-references/integrations/zapier/questions-frequentes).

#### Sécurité et protection des données

* Les identifiants et jetons des intégrations sont stockés chiffrés, ne sont jamais renvoyés par l'API, et sont effacés lorsque vous désinstallez une intégration ou supprimez un workspace.
* Les flux OAuth valident strictement leurs callbacks, et les endpoints de webhooks entrants sont soumis à une limitation de débit.
* Les intégrations sont cloisonnées par workspace : les données d'un workspace ne sont jamais visibles depuis un autre.
* Les enregistrements créés par une intégration (actifs, demandes…) appartiennent à votre workspace et sont conservés à la désinstallation de l'intégration.

#### Un besoin non couvert ?

Si aucune intégration ne correspond à votre besoin, l'[API REST Dastra](https://doc.dastra.eu/api-references/liste-des-endpoints-dapi) vous permet de développer vos propres scripts et connecteurs, et vous pouvez soumettre une demande de connecteur à l'équipe Dastra via le support.
