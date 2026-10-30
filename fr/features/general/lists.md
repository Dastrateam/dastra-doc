---
description: >-
  Sélectionnez plusieurs éléments, agissez dessus en une fois, choisissez les
  colonnes d'une liste et utilisez la corbeille, dans tous les modules Dastra.
---

# Listes, actions groupées et corbeille

Les listes de Dastra (traitements, actifs, demandes, tâches, contrats, etc.) se comportent toutes de la même façon. Cette page décrit comment sélectionner plusieurs éléments, agir dessus en une fois, choisir les colonnes et utiliser la corbeille. Pour trier et filtrer une liste, consultez [Filtres avancés](filters.md).

## Sélectionner des éléments

Cochez la case au début de chaque ligne, ou la case de l'en-tête pour **Sélectionner tous les éléments de la page**. Une barre affiche alors le nombre d'éléments sélectionnés.

Lorsque la liste contient plus de résultats que la page, le bouton **Sélectionner tout**, suivi du total entre parenthèses, sélectionne tous les résultats de la recherche et des filtres en cours, y compris les lignes qui ne sont pas affichées. Cliquez sur **Déselectionner** pour vider la sélection.

## Agir sur plusieurs éléments

Une fois des éléments sélectionnés, ouvrez **Choisir une action groupée** au-dessus de la liste, ou faites un clic droit sur une ligne sélectionnée. Les actions dépendent du module, de vos permissions et des fonctionnalités de votre offre. Les plus courantes sont :

<figure><img src="../../.gitbook/assets/general-lists-1.png" alt="La liste des traitements avec trois lignes sélectionnées et le menu des actions groupées ouvert"><figcaption><p>Trois lignes sélectionnées et le menu Choisir une action groupée</p></figcaption></figure>

* **Modifier les champs** : changer la valeur d'un ou plusieurs champs sur tous les éléments sélectionnés. Une fenêtre **Modifier** suivie du nombre d'enregistrements s'ouvre. Seuls les champs modifiables en masse sont proposés.
* **Basculer l'étape de processus** : passer tous les éléments sélectionnés à une autre étape de workflow, dans les modules qui utilisent des étapes de workflow.
* **Exporter** : exporter les éléments sélectionnés.
* **Déplacer dans la corbeille** : consultez [Corbeille](#corbeille).

Pour la liste complète des actions d'un module, consultez sa propre page, par exemple [Agir sur plusieurs traitements à la fois](../ropa/README.md#agir-sur-plusieurs-traitements-a-la-fois). Lorsque la sélection est importante, Dastra la traite en arrière-plan et affiche **Le traitement en masse a démarré** : les listes sont mises à jour une fois le traitement terminé.

## Choisir les colonnes

Cliquez sur **Personnaliser les colonnes** dans l'en-tête de la liste pour afficher, masquer et réordonner les colonnes, puis conservez le résultat dans une vue personnalisée. Consultez [Personnaliser les colonnes](filters.md#personnaliser-les-colonnes) dans la page des filtres avancés.

## Corbeille

Dans tous les modules, supprimer un élément le déplace d'abord dans la corbeille.

1. Sélectionnez l'élément ou les éléments, puis choisissez **Déplacer dans la corbeille**.
2. Confirmez. Les éléments de la corbeille n'apparaissent plus dans les listes, mais ils ne sont pas supprimés définitivement.
3. Pour les retrouver, activez **Voir la corbeille** ou **Inclure la corbeille**, selon la liste.
4. Ouvrez le menu d'un élément de la corbeille : **Restaurer** le remet dans les listes, **Supprimer définitivement** le supprime.

{% hint style="warning" %}
**Supprimer définitivement** est irréversible.
{% endhint %}

Les règles de purge, lorsqu'un module en propose, suppriment automatiquement les éléments de la corbeille : consultez [Règles de purge des demandes](../requests/advanced/purge.md) pour les demandes d'exercice des droits.
