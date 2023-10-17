---
description: >-
  Apprenez à renseigner les catégories de données ainsi que les règles de
  conservation associées spécifiques à un traitement.
---

# Données et conservation

{% embed url="https://www.youtube.com/watch?v=BJSynYF0aDw&list=PL-EvtNdEiDxEUikz6mrcMlKZ54r3RpBLZ&index=6" %}

[**L’article 30 du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4) exige également l’inscription des catégories de données traitées.

Il s’agit ici de définir les catégories de données traitées. Celles-ci peuvent être dites courantes ou sensibles. On distingue en effet les données qui présentent un risque plus important sur les personnes physiques tel que les données relatives à la santé des personnes, les données relatives aux opinions politiques ou à l’activité syndicale. Les données relatives à des infractions ou autres mesures d’exécution de peines constituent également des données particulièrement protégées.&#x20;

De même, le numéro d’inscription au répertoire (NIR) ou numéro de sécurité sociale peut être assimilé à une donnée sensible.&#x20;

La collecte de données sensibles est par principe interdite. Seules les exceptions prévues à l’[**article 9 du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2) permettent de les collecter.

## Jeux de données

Le jeu de données regroupe les données d'un élément précis, par exemple, une table dans une base de données ou un formulaire de collecte papier.

### Plusieurs cas d'usage des jeux de données

Les jeux de données peuvent être utilisés selon plusieurs manières :

* **Cas n°1** : en associant **un jeu de données à un actif unique**. Dans ce cas, le jeu de données correspond aux données de l'actif et n'est pas générique
* **Cas n°2** : en associant **un jeu de données au traitement de données**. Ce jeu de données peut être spécifique au traitement de données et n'est pas réutilisé dans un autre traitement de données
* **Cas n°3** : en associant des **jeux de données génériques au traitement de données**. Dans ce cas, le jeu de données peut être réutilisé dans plusieurs traitements de données.

Pour utiliser les jeux de données génériques, nous recommandons la procédure suivante :

* Ouvrir la page du traitement concernant les jeux de données
* Ouvrir un nouvel onglet sur la page des jeux de données dans la cartographie
* Sélectionner le jeu de données dans le traitement de données
* Si le jeu de données doit être modifié, il faut en créer un autre : se rendre sur l'autre onglet et dupliquer le jeu de données générique en enlevant ou en ajoutant les champs souhaités
* Pour plus de clarté, il est recommandé d'utiliser un tag pour ces jeux de données (cela vous permettra de les distinguer facilement dans le sélecteur de jeux de données). Par exemple : un tag "générique" et un tag concernant la donnée ajoutée ou enlevée

#### Utiliser des jeux de données sans champs

Par ailleurs, il est possible de rester encore plus générique en ne précisant pas les données associées au jeu de données mais en nommant le jeu de données en tant que catégorie de données (ce qui est également valable au sens du RGPD par exemple).

Selon les traitements, vous pouvez avoir des approches différentes, en fonction de la sensibilité qu'ils présentent au regard des droits et libertés des personnes concernées.

### Associer la source des données dans le jeu de données

Dans chaque jeu de données, vous pouvez inscrire l'origine des données. Celle est soit directe, soit indirecte, soit les deux.&#x20;

Un champ vous permettant de décrire l'origine de la collecte permet d'apporter la précision nécessaire.

<figure><img src="../../../.gitbook/assets/image (10) (2).png" alt=""><figcaption><p>Source des données</p></figcaption></figure>

### Associer un actif au jeu de données

Les jeux de données ont une vocation naturelle à être ajoutés à des [actifs](applications.md).&#x20;

Vous pouvez associer un actif à votre jeu de données lors de sa création.&#x20;

<figure><img src="../../../.gitbook/assets/image (2) (1) (3).png" alt=""><figcaption><p>Sélecteur d'actif</p></figcaption></figure>

Un jeu de données ne peut être associé qu'à un seul actif. En effet, en définissant les jeux de données d'un actif, ceux-ci sont uniques.&#x20;

Par exemple, en considérant un logiciel de comptabilité comme un actif, plusieurs jeux de données pourraient être associés à cet actif, tels que "données de facturation" comprenant les données relatives au module suivi des factures ou encore "données des clients" comprenant les données relatives aux comptes clients.

### Associer une catégorie de personnes concernées

Pour chaque jeu de données, vous pouvez associer une ou plusieurs catégories de personnes concernées.&#x20;

Cela vous permet de mieux comprendre quelles sont les données associées aux personnes concernées. De plus, cela simplifie le travail de cartographie.&#x20;

<figure><img src="../../../.gitbook/assets/image (3) (1) (3) (2).png" alt=""><figcaption><p>Sélecteur de catégories de personnes concernées</p></figcaption></figure>

{% hint style="info" %}
Indiquer les personnes concernées est utile dans la gestion des [demandes d'exercice des droits](../../gerer-les-exercices-des-droits/). En effet, vous pourrez retrouver facilement les données qui l'objet de la demande en identifiant rapidement les jeux de données concernés.
{% endhint %}

### Associer des champs de données

Chaque jeu de données a vocation à être complété par des champs de données. Ces champs sont les données en tant que tel.&#x20;

Les champs qui s'affichent dans le sélecteur sont les champs disponibles dans le glossaire de données.&#x20;

<figure><img src="../../../.gitbook/assets/image (8) (1) (3).png" alt=""><figcaption><p>Sélecteur de champs de données</p></figcaption></figure>

Si une donnée n'est pas présente, vous pouvez la créer directement depuis ce sélecteur pour l'ajouter au jeu de données.&#x20;

Les champs peuvent être catégorisés selon des catégories prédéterminées. Il s'agit notamment des catégories préconisées par la CNIL.

<figure><img src="../../../.gitbook/assets/image (9) (2).png" alt=""><figcaption><p>Sélecteur de catégorie de données personnelles</p></figcaption></figure>

C'est également au niveau du champ que vous pouvez indiquer la présence d'une donnée sensible. Par exemple, une donnée de santé ou un autre type de donnée sensible.&#x20;

Dans ce cas, vous êtes invité à justifier de la collecte de cette donnée et en particulier du fondement juridique la permettant.

&#x20;

<figure><img src="../../../.gitbook/assets/image (4) (3) (2).png" alt=""><figcaption><p>Donnée sensible</p></figcaption></figure>

{% hint style="info" %}
Cette information sera analysée par l'application pour déclencher un critère intelligent [d'AIPD](analyse-dimpact.md).&#x20;
{% endhint %}

### Associer une règle de conservation des données

Dans chaque jeu de données, vous pouvez associer une règle de conservation des données.&#x20;

<figure><img src="../../../.gitbook/assets/image (6) (2).png" alt=""><figcaption><p>Durées de conservation</p></figcaption></figure>

Les durées de conservation sont considérées par défaut car elles peuvent être personnalisées au niveau du traitement (voir infra).

Vous pouvez ajouter une durée en base active, en archive intermédiaire ou une règle de purge.

La base active est la base courante du traitement. L'archivage intermédiaire est une forme de conservation plus restreinte. Le champ « purge » vous permet de décrire les conditions de suppression des données ou leur transmission pour archivage définitif.

## Conservation des données

La conservation limitée des données fait partie des principes généraux du droit des données à caractère personnel et est rappelée à l’[**article 5 1. e) du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2). Celui-ci prévoit en effet que « _conservées sous une forme permettant l'identification des personnes concernées pendant une durée n'excédant pas celle nécessaire au regard des finalités pour lesquelles elles sont traitées_ ».

Concrètement, cela signifie que lors de la mise en œuvre d’un traitement de données, il faut penser à son devenir lorsque la finalité aura été accomplie. La donnée devra être soit détruite de manière définitive, soit anonymisée, soit traitée pour une nouvelle finalité compatible.&#x20;

La durée de conservation dépend de la finalité du traitement et de la nature des données. Les durées de conservation peuvent être définies en fonction des types de données. Par exemple, pour la gestion de la paie, les données relatives au bulletin de salaire sont conservées 1 mois en base active et 5 ans en archivage intermédiaire tandis que les données relatives à l’ordre de virement pour paiement sont conservées le temps nécessaire à l’émission du bulletin de paie en base active et 10 ans à compter de la clôture en archive intermédiaire.&#x20;

La durée peut être exprimée en valeur ou, si ce n’est pas possible, les critères utilisés pour définir la période de conservation (jusqu’à la désinscription par exemple). Il est recommandé, en particulier par la CNIL dans sa [**recommandation du 11 octobre 2005 sur l’archivage électronique dans le secteur privé**](https://www.legifrance.gouv.fr/affichCnil.do?id=CNILTEXT000017651957), de mettre en place des procédures permettant de gérer les durées de conservation au niveau de la catégorie de données et en particulier, de gérer les purges ou destructions de données.

#### Personnaliser les règles de conservation d'un jeu de données

Les champs de données d'un jeu de données générique ne peuvent pas varier d'un traitement à l'autre. Cependant, la durée de conservation peut être différente. En effet, il est possible de personnaliser la durée de conservation d'un jeu de données en fonction du traitement. Ainsi, la durée de conservation du jeu de données ne sera plus prise en compte.&#x20;

Pour cela, il est nécessaire d'ajouter le jeu de données au traitement. Sur la liste des jeux de données, il faut cliquer sur les boutons "base active/...".

<figure><img src="../../../.gitbook/assets/image (4) (1) (5).png" alt=""><figcaption><p>Bouton "base active"</p></figcaption></figure>

Vous pourrez voir apparaitre la fenêtre de personnalisation.&#x20;

<figure><img src="../../../.gitbook/assets/image (11).png" alt=""><figcaption><p>Fenêtre de personnalisation des durées de conservation</p></figcaption></figure>

Lorsque la durée de conservation est personnalisée au niveau du traitement, un petit logo de stylo apparait sur le bouton concerné :&#x20;

L'objectif à terme peut être de limiter l'utilisation de jeux de données génériques et de s'orienter vers une cartographie plus précise soit via les traitements de données (cas n°2) soit via les actifs (cas n°1).

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (2) (4).png" alt=""><figcaption><p>Durée personnalisée au niveau du traitement</p></figcaption></figure>



####

##

\
