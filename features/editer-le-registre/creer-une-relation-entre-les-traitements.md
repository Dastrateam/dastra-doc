# Créer des relations entre les traitements

Dans Dastra vous avez la possibilité de créer des relations entre vos traitements afin de faciliter leur gestion.

Ces relations sont possibles entre des traitements situés dans un même espace de travail.

### Pourquoi faire des relations entre les traitements ?

Les relations entre les traitements peuvent être utilisées pour matérialiser les relations de responsabilité entre les différentes entités responsables de traitement.&#x20;

Par exemple, dans un groupe d'entreprise, vous pouvez mettre en place une relation entre un traitement réalisé par la maison mère avec les traitements réalisés par les filiales. C'est souvent le cas pour les traitements relatifs à l'administration générale du groupe, tel que la gestion des ressources humaines, la comptabilité, la gestion de fournisseurs etc.&#x20;

> Une société mère X met en œuvre un traitement de gestion de la paie pour le compte de ses filiales Y et Z. Dans l'entité X, un traitement (ST1) "gestion de la paie" est créé en tant que sous-traitant. A partir de ce traitement, nous pouvons créer une relation d'héritage fort avec deux autres traitements (RT1 et RT2) situés dans Y et Z qui seront créés en tant que responsable de traitement.&#x20;
>
> Ainsi, la mise à jour du traitement ST1 sera automatiquement relayée dans les traitements RT1 et RT2.&#x20;

### Ajouter une relation

Pour ce faire, il faut aller sur une fiche de traitement et sélectionner l'onglet "Relations" situé en haut de la fiche.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Bouton de création des relations intertraitement</p></figcaption></figure>



Ensuite, il faudra sélectionner un type de relations.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Création de nouvelles relations</p></figcaption></figure>

Vous pouvez créer des relations sur plusieurs traitements en une seule fois. Pour cela, il faudra créer des nouveaux traitements et sélectionner les unités organisationnelles concernées.

{% hint style="info" %}
Il est possible de créer des relations avec les traitements figurant le même espace de travail uniquement.&#x20;
{% endhint %}

### Types de relation

Il existe deux types de relations :&#x20;

1. **Relations déclaratives :** Utilisées pour établir un lien simple entre deux traitements (sans dépendance fonctionnelle).
2. **Relations fonctionnelles :** Permettent de transmettre ou d'hériter des champs d'un traitement à un autre.



### Relations déclaratives :

#### **Est l'enfant de :**&#x20;

Relation hiérarchique permettant une lecture structurée des traitements, **sans dépendance fonctionnelle** entre les champs.

> Le traitement A est hiérarchiquement rattaché au traitement B.

#### Est le parent de :&#x20;

Relation hiérarchique permettant une lecture structurée des traitements, **sans dépendance fonctionnelle** entre les champs.

> Le traitement A est hiérarchiquement au dessus du traitement B.

#### Est relatif à :&#x20;

Lien logique simple entre deux traitements, **sans asservissement ni dépendance fonctionnelle** entre les champs.

> Le traitement A est lié au traitement B.<br>

#### Est copié par :

Cette relation permet de garder une trace des éléments dupliqués à partir de ce traitement. Cette relation est créée automatiquement lors de la duplication d'un traitement.

> Le traitement A est la source (de la duplication) du traitement B.

#### Est une copie de :&#x20;

Cette relation permet de garder une trace de la source de duplication du traitement. Cette relation est créée automatiquement lors de la duplication d'un traitement.

> Le traitement A est un duplicata du traitement B.

###

### **Relations fonctionnelles** :

#### Transmet strictement (Héritage fort) :

Les champs du traitement cible **A** remplacent intégralement ceux du traitement d’origine **B.**

{% hint style="warning" %}
à l’exception des champs de l’onglet **1 « Général »** et des documents associés au traitement dans l’onglet **11 « Documentation »**.
{% endhint %}

* Asservissement strict entre A et B.
* Les champs préexistants dans B sont supprimés lors de la création du lien.
* Les champs hérités depuis A ne sont **ni modifiables, ni supprimables**, et aucun nouveau champ ne peut être ajouté dans B.
* En cas de suppression du lien, les champs initiaux de B sont restaurés (les éléments de référentiel étant conservés).

#### Hérite strictement de (Héritage fort) :&#x20;

Les champs du traitement cible **B** remplacent intégralement ceux du traitement d’origine **A**.

{% hint style="warning" %}
à l’exception des champs de l’onglet **1 « Général »** et des documents associés au traitement dans l’onglet **11 « Documentation »**.
{% endhint %}

* Asservissement strict entre B et A.
* Les champs préexistants dans A sont supprimés lors de la création du lien.
* Les champs hérités depuis B ne sont **ni modifiables, ni supprimables**, et aucun nouveau champ ne peut être ajouté dans A.
* En cas de suppression du lien, les champs initiaux de B sont restaurés.

#### Transmet (Héritage faible) :&#x20;

Le traitement d’origine **A** transmet automatiquement ses champs au traitement cible **B**.

{% hint style="warning" %}
à l’exception des champs de l’onglet **1 « Général »** et des documents associés au traitement dans l’onglet **11 « Documentation »**.
{% endhint %}

* B hérite des champs de A.
* Les champs hérités ne sont pas modifiables dans B.
* B peut ajouter, modifier ou supprimer ses propres champs.
* Toute modification des champs de A est automatiquement répercutée dans B.
* En cas de suppression du lien, les champs hérités redeviennent modifiables.
* Les champs préexistants dans B sont conservés.

#### Hérite de (Héritage faible) :  &#x20;

Le traitement cible **B** hérite automatiquement des champs du traitement d’origine **A**.

{% hint style="warning" %}
à l’exception des champs de l’onglet **1 « Général »** et des documents associés au traitement dans l’onglet **11 « Documentation »**.
{% endhint %}

* Les champs hérités ne sont pas modifiables dans B.
* B peut ajouter, modifier ou supprimer ses propres champs.
* Toute modification des champs de A est automatiquement répercutée dans B.
* En cas de suppression du lien, les champs hérités redeviennent modifiables.
* Les champs préexistants dans B sont conservés.&#x20;



### Tableau de synthèse des relations :&#x20;

| **Type de relation**                                                                       | **Onglet 1 – "Général"** | **Onglets 2 à 10 (champs métier)** | **Documentation uploadée** dans l’onglet 11 – "**Documentation"** | **Modifiabilité des champs propres au traitement cible** |
| ------------------------------------------------------------------------------------------ | ------------------------ | ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- |
| **Relations hiérarchiques / logiques**(Parent / Enfant / Relatif à / Copié par / Copie de) | Sans impact              | Sans impact                        | Sans impact                                                       | Sans impact                                              |
| **Transmet strictement (Héritage fort)**                                                   | ❌ Non transmis           | ✅ Transmis                         | ❌ Non transmise                                                   | ❌ Impossible d’ajouter / modifier / supprimer            |
| **Hérite strictement de (Héritage fort)**                                                  | ❌ Non hérité             | ✅ Hérité                           | ❌ Non héritée                                                     | ❌ Impossible d’ajouter / modifier / supprimer            |
| **Transmet (Héritage faible)**                                                             | ❌ Non transmis           | ✅ Transmis                         | ❌ Non transmise                                                   | ✅ Ajout / modification / suppression possibles           |
| **Hérite de (Héritage faible)**                                                            | ❌ Non hérité             | ✅ Hérité                           | ❌ Non héritée                                                     | ✅ Ajout / modification / suppression possibles           |
