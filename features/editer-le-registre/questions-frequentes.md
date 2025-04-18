---
description: >-
  Cette page présente les principales interrogations et les réponses que nous
  vous proposons.
---

# Questions fréquentes

## Comment afficher l'historique des modifications sur un traitement ?

Pour tous les traitements, vous pouvez afficher l'historique des modifications ainsi que le détail des changements.&#x20;

Il suffit de cliquer sur l'icone en haut de la page représentant une horloge.

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-12-18 103715.png" alt=""><figcaption><p>Bouton d'accès à l'historique</p></figcaption></figure>

Attention, les modifications d'unités organisationnelles ne sont pas tracées.&#x20;

## Est-il possible d'ajouter automatiquement des éléments dans le champ "parties prenantes" dans un nouveau traitement ?

Non, on ne peut pas mettre à jour de parties prenantes de manière automatisée via les workflow automatisés.&#x20;

Par contre, il est possible de créer un champ personnalisé au niveau des parties prenantes qu'il est possible de modifier via le workflow automatisé.

## Comment supprimer un traitement ?

Pour supprimer un traitement, il y a nécessairement un passage par la corbeille via le bouton "Déplacer dans la corbeille" et ensuite en affichant la corbeille depuis les filtres, il est possible de supprimer définitivement le traitement. Cela constitue un garde fou contre les suppressions hâtives.

Pour déplacer un traitement dans la corbeille, il faut aller sur les trois petits points sur le traitement pour afficher le menu.

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-12-18 103935.png" alt=""><figcaption></figcaption></figure>

Et enfin, afficher les archives

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

et supprimer&#x20;

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Comment utiliser les jeux de données sans pouvoir modifier les données ?

Vous vous posez la question de savoir comment restreindre l'accès aux données (champs) des jeux de données pour éviter tout problème de liaison avec d'autres fiches de traitement.

En effet, il est possible que vos relais DPO doivent utiliser les jeux de données que vous leur proposez sans devoir en créer de nouveaux.&#x20;

Dans ce cas, il convient de faire un rôle personnalisé.&#x20;

Pour cela, il faut se rendre dans les rôles : [https://app.dastra.eu/general-settings/roles](https://app.dastra.eu/general-settings/roles)

Ensuite, créer un rôle personnalisé avec les permissions :&#x20;

* Registre : lecture, écriture
* Cartographie des données : lecture

<figure><img src="../../.gitbook/assets/image (2) (2) (3).png" alt=""><figcaption><p>Rôle permettant l'accès aux jeux de données sans pouvoir les modifier</p></figcaption></figure>

Ensuite, il faut attribuer ce rôle aux utilisateurs concernés.&#x20;

Ils ne pourront pas modifier les éléments de la cartographie.

{% hint style="info" %}
Si vous ne trouvez la réponse dans ce guide, vous pouvez nous [contacter via le support](../../commencer/le-support/faire-une-demande-de-support.md)


{% endhint %}

## Ajouter des parties prenantes ou des destinataires sur plusieurs traitements ?

Vous pouvez ajouter des parties prenantes sur plusieurs traitements en masse en utilisant les modifications groupées.&#x20;

Pour cela, il faut se mettre sur la vue tableau du registre et sélectionner les traitements avec les cases à cocher.&#x20;

Ensuite, vous verrez le bouton "Choisir des actions groupées" apparaitre.&#x20;

Sélectionner l'option "Lier des acteurs" et ajoutez vos acteurs en tant que partie prenante.&#x20;

<figure><img src="../../.gitbook/assets/image (17) (2).png" alt=""><figcaption></figcaption></figure>

## Obtenir la liste des actifs par unité organisationnelle (UO) ?

Vous pouvez obtenir la liste des actifs répartis par unité organisationnelle via les liens qu'ils ont avec les traitements.&#x20;

Vous pouvez utiliser l'export des traitements au format excel pour cela. En filtrant les traitements par UO et en exportant les traitements sélectionnés, vous pouvez choisir d'exporter uniquement le champ Actifs dans l'export. Ainsi vous avez l'export des actifs par UO. Vous pouvez aussi choisir d'exporter les UO et les actifs uniquement pour avoir tous les actifs de toutes les UO. En utilisant la vue cartographie du registre, vous trouvez également cette information en visualisation graphique.

## Comment dupliquer un registre dans un autre espace de travail ?

Vous pouvez dupliquer un registre et les traitements associés de plusieurs façons :&#x20;

* soit en[ exportant et réimportant](exporter-importer-le-registre.md) les traitements au format JSON
* soit en allant dans l'espace de travail cible et créer les traitements à partir de la bibliothèque. Vous pourrez alors changer la source de la bibliothèque et choisir l'espace de travail d'origine du registre.

## Comment changer de type de traitement (passer d'un traitement créer en tant que responsable de traitement a un traitement créé en tant que sous-traitant et vise versa) ?

Vous pouvez changer de type de traitement en cliquant sur "Basculer en sous-traitant" ou "Basculer en responsable de traitement" :&#x20;

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-10-16 122037.png" alt=""><figcaption></figcaption></figure>
