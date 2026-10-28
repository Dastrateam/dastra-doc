---
description: Indiquez les destinataires des données du traitement.
---

# Destinataires

{% embed url="https://youtu.be/BNj0pG7ddRw" %}

[**L’article 30 1. d) du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4) impose que le registre comporte « _les catégories de destinataires auxquels les données à caractère personnel ont été ou seront communiquées, y compris les destinataires dans des pays tiers ou des organisations internationales_ ».

[**L’article 4 du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1) définit le destinataire comme « _la personne physique ou morale, l'autorité publique, le service ou tout autre organisme qui reçoit communication de données à caractère personnel, qu'il s'agisse ou non d'un tiers. Toutefois, les autorités publiques qui sont susceptibles de recevoir communication de données à caractère personnel dans le cadre d'une mission d'enquête particulière conformément au droit de l'Union ou au droit d'un État membre ne sont pas considérées comme des destinataires ; le traitement de ces données par les autorités publiques en question est conforme aux règles applicables en matière de protection des données en fonction des finalités du traitement_ ».

Autrement dit, les destinataires sont toutes les entités qui accèdent aux données, à l'exception des autorités publiques (tiers autorisés tels que la CNIL, la police judiciaire dans le cadre d’une enquête judiciaire ou l’administration fiscale, par exemple). Il s’agit des services internes du responsable de traitement (le service RH, par exemple), des sous-traitants, des responsables conjoints et des autres responsables de traitement (des partenaires commerciaux, par exemple).

## Ajouter un destinataire

1. Dans la section **Destinataires**, cliquez sur **Créer un destinataire**.
2. Dans **Catégorie**, sélectionnez le type de destinataire : **Destinataire interne**, **Sous-traitant**, **Tiers: Organisme externe**, **Tiers autorisés**, **Responsable conjoint** ou **Personne concernée par le traitement**.
3. Identifiez le destinataire :
   * **Répertoire des acteurs (recommandé)** : sélectionnez un acteur de votre répertoire des acteurs, ou créez-en un. Si le destinataire figure dans le répertoire, vous pouvez cartographier les traitements liés à cet acteur.
   * **Sélectionner une unité organisationnelle** : sélectionnez l'une de vos unités organisationnelles, par exemple un service interne.
   * **Saisie libre** : saisissez un libellé libre. Cette option n'est pas proposée pour les sous-traitants. Pour la catégorie **Personne concernée par le traitement**, c'est la seule option.
4. Si vous le souhaitez, décrivez ce que le destinataire fait des données dans **Décrire les opérations effectuées sur les données**.
5. Si le destinataire a accès aux données, activez **Le destinataire a-t-il accès aux données ?** et indiquez s'il a un **Accès à toutes les données (par défaut)** ou un **Accès à certains jeux de données**. Dans le second cas, sélectionnez les jeux de données concernés.
6. Si les données sont transférées hors de l'UE, déclarez le transfert dans le même panneau (voir [Transferts de données hors UE](transfers.md)).
7. Cliquez sur **Ajouter**.

{% hint style="info" %}
Dastra vous aide à compléter la liste :

* les responsables conjoints déclarés dans la section **Parties prenantes** apparaissent dans les **Destinataires suggérés** : cliquez sur **Ajouter** pour les ajouter ;
* lorsque vous sélectionnez un sous-traitant dont les sous-traitants ultérieurs sont renseignés dans le répertoire des acteurs, vous pouvez les ajouter en même temps avec **Ajouter les sous-traitants ultérieurs associés à l'acteur** ;
* lorsque l'acteur ou l'unité organisationnelle sélectionné se trouve dans un autre pays, Dastra propose d'ajouter un transfert.
{% endhint %}

Les destinataires sont listés avec leur **Catégorie** et leurs **Transferts**. Utilisez **Réorganiser par** pour les trier par nom ou par catégorie. Selon la catégorie du destinataire, son menu **...** permet de le **Modifier**, d'ouvrir son acteur avec **Modifier l'acteur lié**, d'**Ajouter un sous-traitant ultérieur**, d'**Envoyer un questionnaire à votre sous-traitant** ou de le **Supprimer**.

## Ajouter un sous-traitant ultérieur

Un sous-traitant peut lui-même faire appel à d'autres sous-traitants pour traiter les données. Pour les déclarer, ouvrez le menu **...** d'un destinataire de la catégorie **Sous-traitant** et cliquez sur **Ajouter un sous-traitant ultérieur**. Le sous-traitant ultérieur s'affiche sous son sous-traitant.

## Évaluer un sous-traitant

Depuis le menu **...** d'un destinataire enregistré dans le répertoire, cliquez sur **Envoyer un questionnaire à votre sous-traitant** pour évaluer cet acteur à l'aide d'un questionnaire.

## Générer un DPA

{% embed url="https://youtu.be/kUatwoQSWOM" %}

Si vous utilisez le module Contrats, vous pouvez générer un accord de sous-traitance (DPA) directement depuis le traitement. Dans la liste des destinataires, un bouton **DPA** apparaît sur les sous-traitants d'un traitement en tant que responsable de traitement lorsqu'ils sont enregistrés dans le répertoire. Il ouvre la génération de contrat avec le modèle de DPA, déjà rempli avec le traitement et le sous-traitant. La même action est disponible dans le menu **...** (**Générer DPA**).

De la même manière, lorsqu'un transfert est déclaré pour un sous-traitant, ou pour un tiers d'un traitement en tant que responsable de traitement, le bouton **CCT transfert** génère les clauses contractuelles types correspondantes.

{% content-ref url="../../../contracts/templates.md" %}
[templates.md](../../../contracts/templates.md)
{% endcontent-ref %}
