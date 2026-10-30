---
description: >-
  Apprenez comment cartographier les données personnelles de votre organisation
  dans Dastra
---

# Cartographie des données

{% embed url="https://youtu.be/Cl8aBeX68s4" %}

## Tout commence par une cartographie des données <a href="#id-0-label" id="id-0-label"></a>

Avant de constituer vos traitements, cartographiez le plus précisément possible les données de l'organisation. Dans l'application, ce module s'appelle **Référentiels**. Le schéma ci-dessous présente la structure de la cartographie que vous pouvez mettre en place.

<figure><img src="../../.gitbook/assets/assets-schema.png" alt="Schéma de la cartographie : l'éditeur fournit des actifs, auxquels sont rattachés des mesures de sécurité et des jeux de données composés de champs"><figcaption><p>Schéma de la cartographie de données</p></figcaption></figure>

Pour inventorier l'ensemble des données personnelles de votre système d'information, suivez cette procédure :

1. **Recensez les actifs** : logiciels, fichiers, plugins, serveurs, machines, etc.
2. **Identifiez l'éditeur de l'actif, le cas échéant** : saisissez les informations de la société qui produit cet actif. Elle pourra être listée parmi les sous-traitants lors de la constitution du registre.
3. **Inventoriez les données** : listez le ou les jeux de données associés (vous pouvez vous référer au DPA signé avec le sous-traitant). Pour en savoir plus, consultez [Données et conservation](../ropa/activity/datasets.md).
4. **Listez les mesures de sécurité** mises en place.

Cette cartographie facilite la constitution des traitements, puisque vous partez de la réalité de vos données.

Si vous ne souhaitez pas faire cet inventaire, ou si les logiciels que vous utilisez sont standards, créez votre référentiel d'actifs à partir de la bibliothèque de modèles prédéfinis, qui contient les actifs courants du marché (Salesforce, Jira, etc.).

## Accéder à la cartographie

1. [Accédez à votre espace de travail](../../getting-started/setup/workspace.md#accedez-a-un-espace-de-travail).
2. Dans le menu latéral, sous **Inventaire**, cliquez sur **Référentiels**.
3. La **Vue d'ensemble** s'affiche : une carte par référentiel, avec le nombre d'éléments qu'il contient.

<figure><img src="../../.gitbook/assets/referentiel-stats-overview.png" alt="Vue d'ensemble des référentiels : Actifs, Acteurs, Jeux de données, Glossaire de données, Mesures et Cat. personnes concernées, chacun avec son nombre d'éléments"><figcaption><p>La vue d'ensemble des référentiels</p></figcaption></figure>

Cliquez ensuite sur le référentiel auquel vous souhaitez accéder. Pour le détail de chaque référentiel, consultez [Référentiels](repositories/README.md).

## Établissez votre liste de mesures de sécurité

Les mesures de sécurité disposent de leur propre référentiel : saisissez-les une fois, puis rattachez-les aux actifs dans la section **Mesures de sécurité associées** de la fiche de l'actif. Ces informations figurent souvent dans le DPA signé avec l'éditeur. Préférez des libellés courts (Antivirus, Pare-feu applicatif, Contrôles d'accès) : une mesure peut ainsi être réutilisée d'un actif à l'autre.

{% embed url="https://youtu.be/5gHAl_8Tdv4" %}

## Gérez vos sous-traitants

Un sous-traitant est un acteur de votre cartographie. Renseignez-le comme **Editeur** de l'actif : il pourra ensuite être référencé comme sous-traitant lorsque cet actif est mentionné dans un traitement. Sur la fiche de l'acteur, vous pouvez aussi enregistrer ses sous-traitants ultérieurs, pour cartographier toute la chaîne de sous-traitance.

{% embed url="https://youtu.be/VATg9fGMeU0" %}
