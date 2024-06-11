# Créer des relation entre les traitements

Dans Dastra vous avez la possibilité de créer des relations entre vos traitements afin de faciliter leur gestion.

Ces relations sont possibles entre des traitements situés dans un même espace de travail mais également au sein d'espaces de travail différents.

### Pourquoi faire des relations entre les traitements ?

Les relations entre les traitements peuvent être utilisées pour matérialiser les relations de responsabilité entre les différentes entités responsables de traitement.&#x20;

Par exemple, dans un groupe d'entreprise, vous pouvez mettre en place une relation entre un traitement réalisé par la maison mère avec les traitements réalisés par les filiales. C'est souvent le cas pour les traitements relatifs à l'administration générale du groupe, tel que la gestion des ressources humaines, la comptabilité, la gestion de fournisseurs etc.&#x20;

> Une société mère X met en œuvre un traitement de gestion de la paie pour le compte de ses filiales Y et Z. Dans l'entité X, un traitement (ST1) "gestion de la paie" est créé en tant que sous-traitant. A partir de ce traitement, nous pouvons créer une relation d'héritage fort avec deux autres traitements (RT1 et RT2) situés dans Y et Z qui seront créés en tant que responsable de traitement.&#x20;
>
> Ainsi, la mise à jour du traitement ST1 sera automatiquement relayée dans les traitements RT1 et RT2.&#x20;

### Ajouter une relation

Pour ce faire, il faut aller sur une fiche de traitement et sélectionner l'onglet "Relations" situé en haut de la fiche.

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption><p>Bouton de création des relations intertraitement</p></figcaption></figure>



Ensuite, il faudra sélectionner un type de relations.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption><p>Création de nouvelles relations</p></figcaption></figure>

Vous pouvez créer des relations sur plusieurs traitements en seule fois. Pour cela, il faudra créer des nouveaux traitements et sélectionner les unités organisationnelles concernées.

{% hint style="info" %}
Il est possible de créer des relations avec les traitements figurant le même espace de travail uniquement.&#x20;
{% endhint %}

### Détail des relations

#### Est l'enfant de :&#x20;

Relation hiérarchique permettant la visualisation graphique. Pas d’asservissement entre les champs.

Le traitement A est hiérarchiquement sous le traitement B.

#### Est le parent de :&#x20;

Relation hiérarchique permettant la visualisation graphique. Pas d’asservissement entre les champs.

Le traitement A est hiérarchiquement au dessus du traitement B.

#### Est relatif à :&#x20;

Simple lien logique entre 2 traitements, aucun asservissement entre les deux ni de règle de contrôle.&#x20;

#### Est copié par :

Cette relation permet de garder une trace des éléments dupliqués à partir de ce traitement. Un lien relationnel est créé automatiquement lorsqu’un traitement est dupliqué.&#x20;

#### Est une copie de :&#x20;

Cette relation permet de garder une trace de la source de duplication du traitement. Un lien relationnel est créé automatiquement lorsqu’un traitement est dupliqué.&#x20;

#### Transmet strictement (Héritage fort) :

Les champs du traitement d'origine (A) remplacent les champs du traitement cible (B).&#x20;

Asservissement strict entre le traitement A et le traitement B. Les champs du traitement B préexistants sont supprimés au moment où le lien est mis en place. Les champs du traitement B asservis au traitement A ne sont pas modifiables dans le traitement B, et aucun nouveau champ ne peut être ajouté, supprimé ou modifié. Dans la mesure où les éléments de référentiels sont conservés, les champs préexistants au traitement B sont rétablis lorsque le lien est révoqué.

#### Hérite strictement de (Héritage fort) :&#x20;

Les champs du traitement cible (B) remplacent les champs du traitement d'origine (A).&#x20;

Asservissement strict entre le traitement B et le traitement A. Les champs de A préexistants sont supprimés au moment où le lien est mis en place. Les champs de A asservis à B ne sont pas modifiables dans A, et aucun nouveau champ ne peut être ajouté, supprimé ou modifié. Dans la mesure où les éléments de référentiels sont conservés, les champs préexistants au traitement B sont rétablis lorsque le lien est révoqué.

#### Hérite de (Héritage faible) :&#x20;

Le traitement cible (B) hérite automatiquement des champs du traitement d'origine (A).&#x20;

Il est possible d'ajouter, de supprimer ou modifier des nouveaux champs dans le traitement B, mais ne peut pas modifier les champs hérités du traitement A. Toute modification dans les champs du traitement A est automatiquement répercutée dans les champs hérités du traitement B . Lorsque le lien est révoqué, les champs hérités du traitement A redeviennent modifiables dans le traitement B. Les champs préexistant dans le traitement B avant la mise en place du lien sont conservés une fois le lien créé.

#### Transmet (Héritage faible) :&#x20;

Le traitement d'origine (A) transmet automatiquement ses champs au traitement cible (B).&#x20;

Le traitement cible B hérite automatiquement des champs du traitement d'origine A. Le traitement cible B peut ajouter, supprimer ou modifier des nouveaux champs, mais ne peut pas modifier les champs hérités du traitement A. Toute modification dans les champs du traitement A est automatiquement répercutée dans les champs hérités du traitement B. Lorsque le lien est révoqué, les champs hérités redeviennent modifiables dans le traitement B. Les champs préexistant à B avant la mise en place du lien sont conservés une fois le lien créé.

