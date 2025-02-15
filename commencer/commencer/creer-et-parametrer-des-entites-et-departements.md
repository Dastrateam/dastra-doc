---
description: Apprenez à créer et paramétrer des entités et des départements dans Dastra.
---

# Créer et paramétrer les unités organisationnelles

{% embed url="https://youtu.be/WPSzbYtu3j4" %}

### Introduction

Les unités organisationnelles permettent de structurer votre espace de travail. Deux types d'unités organisationnelles peuvent être créés :&#x20;

* les **entités** qui correspondent à des entités juridiques et représentent un responsable de traitement,
* les **départements** qui permettent d'organiser les entités.

Dans Dastra, la notion d'espace de travail est décorrélée de celle d'entité juridique. Ainsi, **un espace de travail peut faire référence à plusieurs entités juridiques** distinctes (comme dans un groupe par exemple). En revanche, il ne peut y avoir qu'un seul représentant légal par entité juridique.

{% hint style="info" %}
Chaque entité dans Dastra est considérée comme un responsable de traitement.&#x20;
{% endhint %}

### Accéder au module "Unités organisationnelles" dans Dastra.

Rendez-vous dans "Réglages" à gauche de l'écran, puis cliquez sur "Unités organisationnelles".



![Bouton d'accès aux réglages de l'espace de travail](<../../.gitbook/assets/Capture d'écran 2024-10-17 123108.png>)



![Accès aux paramètres des unités organisationnelles](<../../.gitbook/assets/Capture d'écran 2024-10-17 123327.png>)

Vous accéderez ainsi à l'écran de **création et de paramétrage** des unités organisationnelles :

![Interface de gestion des unités organisationnelles](<../../.gitbook/assets/image (250) (1).png>)

## Créer ou modifier une entité

Pour créer une entité juridique, il vous suffit de cliquer sur le bouton "Créer une entité (responsable de traitement)" depuis le module "Entités et départements".

![Bouton "Créer une entité"](<../../.gitbook/assets/image (207).png>)

Renseignez les champs demandés : le nom et le pays sont obligatoires. Vous pouvez renseigner le le nom du ou de la responsable (le représentant légal), ainsi que le ou la délégué(e) à la protection des données (le cas échéant) et le représentant au sein de l'UE (le cas échéant).

{% hint style="info" %}
Contrairement aux départements, le nombre d'entités (responsables de traitements) pouvant être entré dans Dastra est limité par un quota qui dépend de votre abonnement. Si vous souhaitez augmenter ce quota, [contactez le service commercial](https://www.dastra.eu/fr/contacts).
{% endhint %}

Pour modifier une entité, cliquez sur les 3 points à droite de l'entité concernée, puis sur "Modifier"

![Menu déroulant lié à une entité.](<../../.gitbook/assets/image (208).png>)

Réalisez les modifications souhaitées et cliquez sur "enregistrer".

## Créer ou modifier un département

Pour créer un département, il vous suffit de cliquer sur le bouton "Créer un département" depuis le module "Unités organisationnelles" et remplir les champs demandés.

![Bouton "Créer un département"](<../../.gitbook/assets/image (209).png>)

Pour modifier un département, il suffit de cliquer sur les 3 points à droite du département que vous souhaitez modifier, cliquer sur "Modifier" et remplir les champs demandés, avant de cliquer sur "enregistrer".

![Menu déroulant lié à un département](<../../.gitbook/assets/image (210).png>)

## Importer des unités organisationnelles

Vous pouvez importer une liste d'unités organisationnelles via un fichier d'import. Ce fichier est à télécharger en cliquant sur le bouton "Importer" dans l'interface de gestion des unités organisationnelles.&#x20;

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-10-17 123622.png" alt=""><figcaption></figcaption></figure>

Cliquez ensuite "Télécharger le modèle de fichier"

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-10-17 123723.png" alt=""><figcaption></figcaption></figure>

Vous pouvez aussi le télécharger directement ici&#x20;

{% file src="../../.gitbook/assets/sample-Area.csv" %}
&#x20;Fichier d'import des unités organisationnelles
{% endfile %}





Le fichier doit être renseigné avec les champs suivants de manière obligatoire :&#x20;

* **Id** : L'identifiant unique de l'unité organisationnelle (nombre à 5 chiffres)
* **Label** : Le nom de l'unité organisationnelle (chaine de caractère)
* **CountryCode** : Le pays de l'unité organisationnelle (codes de pays sur 2 caractères [ISO 3166](https://documentation.abes.fr/sudoc/formats/CodesPays.htm) )
* **Type** : Type d'unité organisationnelle ("Entity" pour entité et "Area" pour Départment)\
  &#x20;

Le champ **ParentId** n'est pas obligatoire, mais il permet d'identifier l'unité organisationnelle parente (si existante) via son ID (nombre à 5 chiffres).

{% hint style="warning" %}
il est essentiel de limiter le nombre d'étages hiérarchiques à 7 niveaux (relations parent-enfant) pour assurer un traitement correct des données.
{% endhint %}



Exemple :

<table><thead><tr><th>Id</th><th>ParentId</th><th width="492">Label</th><th>CountryCode</th><th>Type</th></tr></thead><tbody><tr><td>20996</td><td></td><td>HOLDING</td><td>FR</td><td>Entity</td></tr><tr><td>21009</td><td>20996</td><td>Informatique</td><td>BE</td><td>Area</td></tr></tbody></table>

Après avoir renseigné le fichier, déposez-le dans le champ de dépôt et suivez les instructions.



## Visualiser et paramétrer les entités et départements depuis l'organigramme

Dans Dastra, vous pouvez également visualiser de manière graphique  les entités et départements ainsi que les paramétrer directement depuis l'organigramme.

Pour cela, cliquez sur la vue "Organigramme" depuis le module "Entités et départements".

![Vue "Organigramme"](<../../.gitbook/assets/image (205).png>)

Ainsi, vous pourrez visualiser le schéma organisationnel de votre groupement de manière graphique :

![Exemple d'organigramme dans Dastra](<../../.gitbook/assets/image (206).png>)

{% hint style="info" %}
Vous pouvez réaliser dans la vue "Organigramme" la plupart des opérations disponibles dans la vue "Entités / départements"
{% endhint %}

## Limiter les accès au contenu d'une unité organisationnelle

Vous pouvez grâce au système d'équipes d'utilisateurs limiter l'accès au contenu attaché à une unité organisationnelle.&#x20;

Pour cela, il faut attacher des équipes à des unités organisationnelles.&#x20;

Le système est arborescent. Cela signifie que, pour qu'une équipe accède à une UO enfant, elle doit accéder à l'UO parent.&#x20;



Voici une vidéo explicative :



{% embed url="https://youtu.be/RCLIWokRmAA" %}

## Aller plus loin

{% content-ref url="creer-puis-affectez-des-equipes.md" %}
[creer-puis-affectez-des-equipes.md](creer-puis-affectez-des-equipes.md)
{% endcontent-ref %}

