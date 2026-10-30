---
description: >-
  La FAQ de chaque module Dastra au même endroit, et des réponses aux questions
  générales : logos, import d'un registre existant, suppression d'un traitement,
  éléments introuvables et stockage local du navigateur.
---

# FAQ

Cette page est le point d'entrée vers les questions traitées dans la documentation. Elle liste la FAQ de chaque module, puis répond aux questions générales qui suivent la liste.

## FAQ des modules

* [FAQ Bien commencer](../getting-started/setup/faq.md) : équipes et unités organisationnelles comme acteurs, export et import des unités organisationnelles, changement de DPO et gestion des propriétaires de l'organisation.
* [FAQ Fonctionnalités générales](../features/general/faq.md) : import de jeux de données.
* [FAQ Assistant IA](../features/general/ai-assistant/faq.md) : confidentialité et données, qualité et fiabilité, configuration et accès, et AI Act.
* [FAQ Registre des traitements](../features/ropa/faq.md) : historique des modifications, suppression, jeux de données en lecture seule, modification en masse des acteurs, duplication vers un autre espace de travail, changement de type et messages d'erreur.
* [FAQ Questionnaires](../features/questionnaires/faq.md) : PIA sur plusieurs traitements, modèles d'e-mail, répondants externes, tâches suggérées, publication de modèles, messages d'erreur et limites.
* [FAQ Risques](../features/risks/faq.md) : le menu absent, passage d'un risque à l'étape suivante, risque initial, résiduel et courant, changement d'échelle de risque.
* [FAQ Tâches](../features/tasks/faq.md) : rattacher des tâches à un projet, supprimer une tâche, saisir la charge et relancer.
* [FAQ Demandes](../features/requests/faq.md) : e-mails de clôture, espace sécurisé du demandeur et vérification de son e-mail, longueur des messages et cookies de la page de collecte.
* [FAQ Zapier](../features/integrations/zapier/faq.md) : statut contractuel de Zapier, signataire du contrat et documentation sur la fiabilité.

Pour les problèmes plutôt que les questions, voir [Problèmes connus](known-problems.md) et les [problèmes connus du SSO](../features/settings/sso/known-problems.md).

## Comment modifier le logo de l'organisation dans Dastra ?

L'organisation n'a pas de logo. L'image affichée en haut à droite de l'écran, à côté de votre nom et du nom de l'organisation, est l'image de votre compte utilisateur. Pour la modifier, ouvrez le menu de votre profil en haut à droite, cliquez sur **Profil utilisateur** et envoyez une nouvelle image.

Pour personnaliser le logo utilisé dans les exports, voir la question suivante.

## Comment modifier le logo de l'espace de travail dans Dastra ?

Ouvrez les paramètres de l'espace de travail, puis la rubrique **Design & marque**. Vous pouvez y envoyer un logo carré et un logo rectangle, et choisir la **Couleur de la marque** et la **Couleur d'accentuation**. Ces éléments adaptent les exports de Dastra à votre charte graphique.

Cette rubrique est réservée aux propriétaires de l'organisation.

## Comment importer les données de mon registre des traitements au format de la CNIL ?

Vous pouvez importer dans Dastra un registre des traitements existant au format de la CNIL. L'import se fait en plusieurs étapes :

1. Importez les noms des traitements.
2. Importez les jeux de données.
3. Importez les acteurs.
4. Importez les mesures de sécurité.
5. Créez les liens entre ces objets dans les traitements.

Pour l'import des traitements, voir [Exporter / importer le registre](../features/ropa/export-import.md). Pour être accompagné dans l'import de votre registre, [contactez le support](../getting-started/support/request.md).

## Comment supprimer un traitement ?

La suppression se fait en deux étapes, pour éviter les suppressions par erreur. Placez d'abord le traitement dans la corbeille avec **Déplacer dans la corbeille**. Affichez ensuite la corbeille avec **Voir la corbeille** dans les filtres, puis choisissez **Supprimer** pour le supprimer définitivement, ou **Restaurer** pour le remettre dans le registre.

La procédure complète est décrite dans [FAQ du registre des traitements](../features/ropa/faq.md#comment-supprimer-un-traitement).

## Je ne retrouve pas des éléments, que puis-je faire ?

Si vous ne retrouvez pas un élément auquel vous devriez avoir accès, il peut être masqué pour l'une des raisons suivantes :

1. Un filtre est actif et restreint l'affichage. Le nombre de filtres actifs apparaît entre parenthèses sur le bouton, par exemple « (1) ». Cliquez sur **Effacer les filtres**.

   <figure><img src="../.gitbook/assets/other-faq-1.png" alt="Liste du registre des traitements avec un filtre actif et le bouton Effacer les filtres (1)"><figcaption><p>Un filtre actif restreint la liste</p></figcaption></figure>
2. L'élément est lié à une unité organisationnelle à laquelle vous n'avez pas accès, ou pour laquelle vous n'avez pas les droits nécessaires. Contactez le gestionnaire de votre espace de travail.
3. L'élément est dans la corbeille et n'apparaît donc plus dans la liste par défaut. Cliquez sur **Filtres** et cochez **Voir la corbeille**.

   <figure><img src="../.gitbook/assets/ropa-faq-3.png" alt="Panneau Filtres du registre avec l'option Voir la corbeille"><figcaption><p>Affichage de la corbeille</p></figcaption></figure>
4. Des paramètres incorrects sont enregistrés dans votre navigateur. Pour le vérifier, ouvrez Dastra dans une fenêtre de navigation privée. Si le problème disparaît, supprimez le stockage local de votre navigateur avec la procédure de la question suivante.

## Comment supprimer le stockage local du navigateur ?

Le stockage local (localStorage) regroupe des données que le navigateur conserve pour que Dastra fonctionne et se souvienne de vos réglages, comme vos filtres. En cas de problème d'affichage, le support peut vous demander de le supprimer.

Vous pouvez aussi utiliser le bouton **Réinitialiser les données de préférences** de votre profil utilisateur, décrit dans [Problèmes connus](known-problems.md).

### Google Chrome

1. Ouvrez le menu du navigateur, puis **Plus d'outils** > **Outils de développement** (F12).
2. Ouvrez l'onglet **Application**, puis **Stockage** > **Stockage local**.
3. Faites un clic droit sur l'adresse de Dastra et choisissez **Effacer**.
4. Actualisez la page (F5).

### Mozilla Firefox

1. Ouvrez le menu du navigateur, puis **Plus d'outils** > **Développement web** > **Outils de développement** (F12).
2. Ouvrez l'onglet **Stockage**, puis **Stockage local**.
3. Faites un clic droit sur l'adresse de Dastra et choisissez **Tout supprimer**.
4. Actualisez la page (F5).
