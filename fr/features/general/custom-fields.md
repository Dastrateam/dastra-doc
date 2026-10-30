---
description: >-
  Ajoutez à vos formulaires les champs propres à votre activité grâce aux
  champs personnalisés : types de champs, options, utilisation et API.
---

# Champs personnalisés

{% embed url="https://www.youtube-nocookie.com/embed/mDyJD-mnnL0" %}
Comment utiliser les champs personnalisés dans Dastra
{% endembed %}

## Dans quels cas utiliser les champs personnalisés

Certaines informations propres à votre secteur ne figurent pas dans les champs natifs du registre des traitements, des exercices de droits, des tâches, etc. Les champs personnalisés vous permettent de créer vos propres champs de formulaire pour enrichir les données saisies.

Voici un exemple de configuration de champs pour l'acteur :

<figure><img src="../../.gitbook/assets/general-custom-fields-1.png" alt="Page Champs personnalisés de l'acteur avec un groupe de champs et ses champs"><figcaption><p>Configuration des champs d'un acteur</p></figcaption></figure>

Et voici le résultat dans le formulaire :

<figure><img src="../../.gitbook/assets/general-custom-fields-2.png" alt="Formulaire d'un acteur avec le groupe de champs personnalisés"><figcaption><p>Les champs personnalisés dans le formulaire de l'acteur</p></figcaption></figure>

## Fonctionnalités concernées

Les champs personnalisés ne sont pas disponibles dans tous les modules. Vous pouvez personnaliser les formulaires suivants :

* [Fiches de traitement](../ropa/README.md)
* [Demandes d'exercice de droits](../requests/README.md)
* [Tâches](../tasks/create.md)
* [Actifs](../ropa/activity/assets.md)
* [Acteurs](../ropa/activity/stakeholders.md)
* [Mesures de sécurité](../ropa/activity/security.md)
* [Jeux de données](../ropa/activity/datasets.md)
* Champs de données
* [Violations de données](../incidents/README.md)
* [Évaluations de risques](../risks/attach-to-processing.md)
* [Systèmes d'IA](../ai-systems/README.md)
* [Contrats](../contracts/README.md)
* [Points de contrôle](../risks/process/monitor.md)

{% hint style="warning" %}
**Limite du nombre de champs.** Le nombre de champs personnalisés dépend de l'offre et de l'abonnement de votre organisation. Un indicateur de quota est affiché sur la page de configuration. Pour en savoir plus, consultez la [page des tarifs](https://www.dastra.eu/fr/pricing).
{% endhint %}

## Types de champs disponibles

Dastra propose les types de champs suivants :

| Type | Usage |
| --- | --- |
| Texte | Une ligne de texte |
| Zone de texte | Un texte sur plusieurs lignes |
| Texte formatté | Un texte avec mise en forme |
| Nombre (entier) | Un nombre sans décimale |
| Nombre (décimal) | Un nombre avec décimales |
| Date | Une date |
| Date et heure | Une date et une heure |
| Case à cocher | Plusieurs réponses possibles parmi une liste de choix |
| Radio | Une seule réponse possible parmi une liste de choix |
| Sélecteur simple | Une valeur choisie dans une liste déroulante |
| Sélecteur multiple | Plusieurs valeurs choisies dans une liste déroulante |
| Booléen | Une réponse Oui ou Non |

## Utilisation des champs personnalisés

Une fois créés, les champs personnalisés s'utilisent comme les champs natifs :

* Ils s'affichent et se modifient dans les formulaires de chaque module.
* Ils peuvent s'afficher dans tous les tableaux de l'application : cliquez sur le bouton **Personnaliser les colonnes** du tableau. Ils sont masqués par défaut.
* Ils sont **présents dans tous les exports Excel** de données. Pour plus d'informations sur les exports, [consultez la page sur les exports](../ropa/export-import.md).
* Ils sont présents dans les rapports PDF et Word lorsque le champ est coché **Inclus dans les rapports PDF ou Word ?** (coché par défaut).
* Ils sont filtrables avec les [filtres avancés](filters.md). Les champs **Case à cocher** et **Sélecteur multiple** ne peuvent en revanche pas servir au tri d'une liste.
* Ils peuvent être mis à jour en masse dans les tableaux de données.
* Ils peuvent être importés depuis des fichiers plats avec le [système d'import](import.md).
* Ils sont **accessibles et modifiables via toutes les API**, avec le nom de variable attribué au champ. Voir [Manipuler les champs personnalisés dans les API](custom-fields.md#manipuler-les-champs-personnalises-dans-les-api).

## Mise en place des champs personnalisés

1. Dans la barre latérale, cliquez sur **Réglages espace de travail**, puis sur **Champs personnalisés**.
2. Choisissez dans la liste de gauche le module dans lequel ajouter un champ personnalisé.
3. Les champs sont créés dans des groupes. Cliquez sur **Créer un groupe de champs**.
4. Renseignez le **Libellé** du groupe et son **Emplacement dans le formulaire**. Pour certains modules, comme le traitement, vous pouvez choisir l'étape du formulaire où le groupe s'affiche.

<figure><img src="../../.gitbook/assets/general-custom-fields-3.png" alt="Fenêtre Créer un groupe de champs avec le libellé et l'emplacement dans le formulaire"><figcaption><p>La création d'un groupe de champs</p></figcaption></figure>

5. Une fois le groupe créé, faites glisser un type de champ depuis la liste **Champs personnalisés** jusque dans le groupe. La fenêtre du champ s'ouvre.
6. Renseignez les options du champ (voir ci-dessous), puis enregistrez.

<figure><img src="../../.gitbook/assets/general-custom-fields-4.png" alt="Fenêtre de création d'un champ personnalisé avec ses options"><figcaption><p>Les options d'un champ personnalisé</p></figcaption></figure>

Vous pouvez réordonner les champs, ou les déplacer d'un groupe à l'autre, par glisser-déposer. Un groupe ne peut être supprimé que s'il ne contient plus de champ. Un champ supprimé va dans la corbeille : activez **Voir la corbeille** pour le restaurer.

### Options d'un champ

| Option | Description |
| --- | --- |
| **Libellé** | Le nom du champ affiché dans les formulaires. Obligatoire. |
| **Nom de la variable (slug)** | Le nom technique du champ, utilisé par les API et les imports. Il est proposé à partir du libellé, en minuscules avec des tirets bas (par exemple `business_owner` pour « Business owner »), et ne peut plus être modifié une fois le champ créé. Il s'affiche uniquement dans cette fenêtre : ouvrez le champ depuis la liste pour le lire. Pour alimenter le champ depuis un questionnaire, écrivez `custom_` suivi de ce nom (voir [Alimenter une fiche avec les réponses](../questionnaires/templates/record-mapping.md)). |
| **Texte d'infobulle** | Une aide affichée à côté du champ. |
| **Champ obligatoire** | Rend la saisie obligatoire. |
| **Inclus dans les rapports PDF ou Word ?** | Ajoute le champ aux rapports générés. Coché par défaut. |
| **Règle de validation** | Pour les champs de type Texte : vérifie que la saisie respecte une syntaxe (e-mail, URL) ou une **expression régulière personnalisée (format Javascript)**. |
| **Taille minimum** et **Taille maximum** | Longueur de la saisie pour les champs texte. |
| **Valeur minimum** et **Valeur maximum** | Bornes pour les champs numériques. |
| **Choix de réponse** | Pour les types à liste de choix : une ligne par choix, avec une couleur. **Ajouter un choix possible** ajoute une ligne ; coller un texte qui contient une option par ligne crée une réponse par ligne. |

Le nom et le nom de variable d'un champ doivent être uniques dans un même module.

## Manipuler les champs personnalisés dans les API

Dastra permet de récupérer, modifier et créer, via l'[API REST](../../api/configuration.md), toutes les valeurs des entités qui comprennent des champs personnalisés.

Une propriété `customFields` est présente dans toutes les entités que vous récupérez avec un `GET` :

```json
 {
   "id": 1234,
   "label": "Test asset",
   etc...
   "customFields": {
     "dpo_name":"jean-marc le dpo",
     "dpo_email":"dpo@github.com",
     "dpo_habilitations": ["Expert","Consulting","Data Mapping"],
     "has_large_dataset":false,
     etc...
   }
 }
```

Pour modifier cette propriété, envoyez l'élément avec `POST` ou `PUT` en mettant à jour les éléments de la collection. Les noms de variables à utiliser figurent dans la page de configuration des champs personnalisés.

{% hint style="info" %}
Tous **les champs personnalisés sont validés par le serveur**. Si une colonne n'est pas présente dans la configuration, elle est automatiquement supprimée.

Si un champ n'est pas valide (par exemple, s'il n'est pas renseigné alors qu'il est marqué comme obligatoire), l'API renvoie une erreur avec le code 400.
{% endhint %}
