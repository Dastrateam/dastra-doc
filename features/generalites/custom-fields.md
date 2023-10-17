---
description: Dastra vous donne la possibilité de personnaliser à l'infini vos formulaires
---

# Champs personnalisés

{% hint style="warning" %}
Cette fonctionnalité est encore en beta. Il se peut qu'elle comporte encore quelques instabilités.
{% endhint %}

{% embed url="https://www.youtube-nocookie.com/embed/mDyJD-mnnL0" %}
Comment utiliser les champs personnalisés dans Dastra
{% endembed %}

## Dans quel cas utiliser les champs personnalisés ?

Il se peut que certaines informations propres à votre secteur ne soient pas présentes dans les champs natifs du registre des traitements, les exercices de droits, les tâches...etc...

Dastra vous permettra de créer des champs de formulaire personnalisés que vous pouvez très facilement ajouter pour enrichir les données saisies.

Voici un exemple de configuration de champs pour l'acteur :

<figure><img src="../../.gitbook/assets/image (2) (1) (3) (1) (1).png" alt=""><figcaption><p>Configuration des champs</p></figcaption></figure>

Et voici le résultat dans le formulaire :

<figure><img src="../../.gitbook/assets/image (4) (1) (3).png" alt=""><figcaption></figcaption></figure>

## Fonctionnalités concernées

{% hint style="success" %}
Attention ! Toutes les fonctionnalités ne sont pas concernées par les champs personnalisés
{% endhint %}

Vous pouvez personnaliser les formulaires suivants :&#x20;

* [Fiches de traitement](../editer-le-registre/)
* [Exercice de droits](../gerer-les-exercices-des-droits/)
* [Tâches](../planifier/gerer-vos-taches.md)
* [Actifs](../editer-le-registre/remplir-le-questionnaire/applications.md)
* [Acteurs](../cartography/referentials.md)
* Mesures
* Jeux de données
* Champs de données
* [Violations](../../rappels-utiles/rgpd-en-bref/violations-de-donnees.md)
* [Evaluations de risques](../la-gestion-des-risques/risques.md)

{% hint style="danger" %}
### Limitations du nombre de champs

La quantité de champs personnalisés est limitée selon de plan que vous utilisez. Nous vous invitons à consulter l[a page des tarifs de l'application](https://www.dastra.eu/fr/pricing) pour plus d'informations à ce sujet
{% endhint %}

## Types de champs disponibles

Dastra vous propose plusieurs types de champs personnalisés possibles

* Texte simple
* Texte long
* Texte enrichi
* Nombre entier
* Nombre décimal
* Date
* Date et heure
* Case à cocher (réponse multiple) (**non filtrable**)
* Case à cocher (réponse unique)
* Sélecteur simple
* Sélecteur multiple
* Case à cocher (Oui/Non)

## Utilisation des champs personnalisés

Vous pouvez :

* Afficher et modifier les données des champs personnalisés dans les formulaires de chaque module
* Les champs personnalsiés peuvent s'afficher dans tous les tableaux de visualisation de l'application. Pour les afficher, cliquer sur le bouton de paramétrage des colonnes du tableau.
* Les champs personnalisés sont **présents dans tous les exports Excel** de données. Pour plus d'informations sur les exports, [consultez la page sur les exports](../editer-le-registre/exporter-importer-le-registre.md)
* Les champs personnalisés peuvent être présents dans les exports HTML, Word et PDF sur option (en cochant la case "Exportable dans les rapports" sur le champ en question)
* **A l'exception des champs à réponses multiples**, les champs personnalisés sont tous filtrables via le système de [filtres avancés](advanced-filters.md).&#x20;
* Les champs personnalisés peuvent être mis à jour en masse dans les tableaux de données
* Les champs personnalisés peuvent être importés via fichiers plats [en utilisant le système d'import](importer-vos-donnees-excel-csv.md)
* Les champs personnalisés sont **accessibles et modifiables via toutes les API**. Pour cela, il faudra utiliser le nom de variable attribué à chaque colonne. [Consultez la rubrique concernant les modifications via API des champs personnalisés](custom-fields.md#manipuler-les-champs-personnalises-dans-les-api).

## Mise en place des champs personnalisés

* Allez dans votre **Espace de travail**
* Cliquez sur le menu à gauche **Réglages de l'espace de travail**
* Cliquez sur le menu **Champs personnalisés**
* Choisissez le module dans lequel vous voulez ajouter un champ personnalisé
* Les champs doivent être créés dans des groupes. Ces groupes peuvent être positionnés d'une certaine façon dans le formulaire Cliquez sur "**Ajouter un groupe de champs**"

<figure><img src="../../.gitbook/assets/image (3) (1) (3) (1).png" alt=""><figcaption></figcaption></figure>

* **Renseignez le nom et l'emplacement** dans le formulaire que vous souhaitez

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (2) (2).png" alt=""><figcaption></figcaption></figure>

Pour certains éléments, il est possible de définir l'emplacement que vous souhaitez dans le formulaire !

* Une fois le groupe créé, vous pouvez désormais **effectuer un glisser-déposer des types de champs** que vous souhaitez mettre en place !

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (2) (3).png" alt=""><figcaption></figcaption></figure>

Renseignez toutes les informations !

* Cliquez sur enregistrer et ça y est ! Votre premier champ de donnée personnelle est en place !
* Vous pouvez effectuer des glisser déposer pour réordonner les champs comme bon vous semble.

## Manipuler les champs personnalisés dans les API

Dastra vous permet de récupérer, modifier et créer via l'[API Rest](../../api-references/configuration-api.md) toutes les valeurs des entités comprenant des champs personnalisés.

Une propriété "**customFields**" sera disponible dans toutes les entités que vous récupérez en get dans Dastra.c

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

Pour modifier cette propriété, il suffit de poster (POST) ou modifier (PUT) l'élément en mettant à jour les éléments de la collection

Pour collecter le nom des variables personnalisés, vous devez vous rendre dans la page de configuration des champs personnalisés.

{% hint style="info" %}
Attention, tous **les champs personnalisés seront validés par le serveur**. Si une colonen n'est pas présente dans la configuration, elle sera automatiquement supprimée.

Si un champ n'est pas valide (par exemple, si il n'est pas renseigné alors qu'il est marqué comme étant obligatoire), cela lèvera une exception avec le code 400
{% endhint %}

## Limitations

Vous ne pouvez **pas filtrer les champs personnalisés du type multiple (case à cocher (Multiple) et sélecteur (Multiple))**. C'est une limitation connue sur laquelle nous travaillons.&#x20;



