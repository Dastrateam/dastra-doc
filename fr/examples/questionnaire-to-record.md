---
description: >-
  Construisez un questionnaire AI Act dont les réponses renseignent le niveau de
  risque, les rôles et un champ personnalisé d'un système d'IA chez Brightmoor
  Retail Group.
---

# Des réponses de questionnaire dans une fiche

Brightmoor Retail Group a déjà inscrit son système d'IA « CV screening assistant » dans le registre, mais la fiche est incomplète. Emma Walsh, la déléguée à la protection des données, veut que la personne responsable de l'outil réponde à un questionnaire AI Act, et que les réponses complètent le système d'IA. Cet exemple construit ce questionnaire. La référence est [Alimenter une fiche avec les réponses](../features/questionnaires/templates/record-mapping.md).

Le questionnaire renseigne quatre champs : le nom, le niveau de risque, les rôles de Brightmoor au sens de l'AI Act et un champ personnalisé contenant le responsable métier.

## 1. Créer le champ personnalisé

Dans **Réglages espace de travail** > **Champs personnalisés**, choisissez le module des systèmes d'IA et créez un champ texte nommé « Business owner ». Ouvrez le champ et lisez son **Nom de la variable (slug)** : `business_owner`. Il n'est plus modifiable après la création. Voir [Champs personnalisés](../features/general/custom-fields.md).

## 2. Créer le modèle

1. Dans **Questionnaires**, créez un modèle personnalisé nommé « AI Act intake ».
2. Réglez **Type de questionnaire** sur **Création d'un système d'IA**. Ce type porte le modèle de données d'un système d'IA.
3. Réglez **Objet associé** sur les systèmes d'IA, pour que chaque réponse puisse être liée à un système d'IA.

## 3. Ajouter les questions

Pour chaque question ci-dessous, ouvrez les propriétés de la question, cochez **Souhaitez-vous personnaliser le nom de la variable (pour les utilisateurs avancés uniquement) ?** et définissez le nom de la variable.

| Question | Type de question | Nom de la variable | Comment le définir |
| --- | --- | --- | --- |
| Nom du système d'IA | Texte court | `label` | **Sélectionnez une variable à mapper**, puis la ligne `label` |
| Quel est le niveau de risque de ce système d'IA ? | Liste de cases à cocher (une seule réponse possible) | `riskLevel` | **Sélectionnez une variable à mapper**, puis la ligne `riskLevel` |
| Quel est le rôle de Brightmoor ? | Liste personnalisée | `responsibilities` | **Sélectionnez une variable à mapper**, puis la ligne `responsibilities` |
| Rôle (sous-question de la liste) | Liste de cases à cocher (une seule réponse possible) | `responsibilityType` | Saisi à la main |
| Qui est responsable métier de ce système d'IA ? | Texte court | `custom_business_owner` | Saisi à la main : `custom_` et le nom technique |

Trois points à connaître :

* Pour `riskLevel`, choisir le champ crée une réponse par valeur : Low, Medium, High et Unacceptable, avec ces noms de variable exacts. Renommez les libellés comme vous le souhaitez, par exemple Minimal, Limité, Élevé et Inacceptable, et conservez les noms de variable.
* Pour les rôles, les six valeurs de l'AI Act sont Provider, Deployer, Distributor, Importer, AuthorizedRepresentative et Manufacturer. Ajoutez une réponse par rôle à la sous-question, avec la valeur comme nom de variable de la réponse.
* Le champ personnalisé ne figure pas dans la liste des variables, c'est pourquoi son nom est saisi en entier.

Enregistrez le modèle.

<figure><img src="../.gitbook/assets/examples-questionnaire-1.png" alt="Fenêtre de sélection d'une variable listant les champs d'un système d'IA"><figcaption><p>Les variables proposées pour un système d'IA</p></figcaption></figure>

## 4. Lier la réponse au système d'IA et recueillir les réponses

1. Planifiez le questionnaire. Dans **Objet lié à la réponse**, sélectionnez le système d'IA « CV screening assistant ». Voir [Planifier un questionnaire](../features/questionnaires/schedule.md).
2. Liam O'Connor répond : nom « CV screening assistant », niveau de risque **High** (un outil de recrutement est un usage à haut risque selon l'annexe III de l'AI Act), rôle **Deployer**, responsable métier « Sophie Becker, RH ».
3. La réponse est validée et publiée.

## 5. Fusionner les réponses dans le système d'IA

Comme la réponse est liée à un système d'IA existant, son propriétaire voit le bouton **Fusionner les données (Système d'IA)**.

1. Cliquez sur **Fusionner les données**. L'aperçu montre le système d'IA construit à partir des réponses. Choisissez l'**Unité organisationnelle** et cliquez sur **Créer et fusionner l'existant**.
2. Dans la fenêtre de fusion, comparez le système d'IA existant avec le système temporaire, nommé « CV screening assistant (From Questionnaire) ». Conservez les valeurs du questionnaire pour `riskLevel`, les rôles et le champ personnalisé, et conservez les valeurs existantes pour le reste.
3. Confirmez la fusion.

| Champ | Avant | Après |
| --- | --- | --- |
| Niveau de risque | Vide | High |
| Rôles | Aucun | Deployer |
| Business owner (champ personnalisé) | Vide | Sophie Becker, RH |

Le système d'IA porte maintenant les réponses. Rien n'a été modifié avant l'étape 3 : les réponses ne mettent jamais une fiche à jour d'elles-mêmes.

Si le système d'IA n'existait pas, la réponse n'aurait aucune fiche liée. Le bouton se lirait **Création d'objet** et **Créer** ajouterait le système d'IA au registre.

<figure><img src="../.gitbook/assets/examples-questionnaire-2.png" alt="Page de demande de fusion avec l'aperçu du système d'IA et le bouton de création et fusion"><figcaption><p>La demande de fusion d'une réponse</p></figcaption></figure>
