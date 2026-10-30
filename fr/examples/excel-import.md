---
description: >-
  Importez cinq actifs de Brightmoor Retail Group depuis un fichier CSV : colonnes,
  correspondances, mode Fusion avec un champ de correspondance et champ
  personnalisé.
---

# Importer des actifs depuis un tableur

Brightmoor Retail Group tient la liste de ses systèmes dans un tableur. Cet exemple l'importe dans le référentiel **Actifs**. Une partie de la liste est déjà dans Dastra : l'import doit donc mettre à jour les actifs existants et créer les autres. La méthode est la même pour les traitements et les autres objets : voir [Importer vos données (Excel, Csv)](../features/general/import.md) pour la référence complète.

## Le fichier d'exemple

Téléchargez le fichier : [examples-assets-import.csv](../.gitbook/assets/examples-assets-import.csv). C'est un fichier CSV avec le séparateur `;` et l'encodage UTF-8, le format attendu par l'import. Il contient cinq lignes.

| Colonne | Contenu | Valeurs possibles |
| --- | --- | --- |
| `Ref` | Référence interne, 100 caractères au maximum | Texte libre |
| `Label` | Nom de l'actif, obligatoire | Texte libre |
| `Type` | Catégorie de l'actif | `Software`, `Building`, `Network`, `Material`, `Data`, `People`, `Process`, `Algorithm` |
| `Description` | Description | Texte libre |
| `Address`, `ZipCode`, `City` | Localisation | Texte libre |
| `CountryCode` | Pays, 2 caractères | Code ISO, par exemple `DE` |
| `State` | Statut de l'actif | `Draft`, `Active` |
| `ApplicationType` | Type d'application | `Software`, `WebApp`, `Saas`, `Module`, `Other` |
| `HostingType` | Hébergement | `InHouse`, `OutSourced` |
| `ApplicationState` | Cycle de vie | `InProduction`, `InDevelopment`, `Stopped` |
| `CustomFields.criticality` | Un champ personnalisé de l'espace de travail | Texte libre |

Les valeurs possibles sont en anglais, comme dans le modèle. Une valeur qui ne correspond à aucun choix est remplacée par la valeur par défaut de la colonne : vérifiez-les avant l'import.

Dans l'application, **Voir le format des colonnes** dans l'assistant d'import liste les colonnes et les valeurs de votre version.

## 1. Créer le champ personnalisé

La dernière colonne alimente un champ personnalisé. Créez-le d'abord.

1. Dans la barre latérale, cliquez sur **Réglages espace de travail**, puis sur **Champs personnalisés**, et choisissez le module des actifs.
2. Cliquez sur **Créer un groupe de champs**, nommez-le « Brightmoor data » et enregistrez.
3. Faites glisser un champ de type texte dans le groupe. Saisissez « Criticality » dans **Libellé**.
4. Vérifiez que **Nom de la variable (slug)** est `criticality`, puis enregistrez. Le slug ne peut plus être modifié ensuite.

Un champ personnalisé s'importe par une colonne nommée `CustomFields.` suivie de son slug : `CustomFields.criticality`. Voir [Champs personnalisés](../features/general/custom-fields.md).

## 2. Lancer l'import

1. Ouvrez **Inventaire** > **Référentiels** > **Actifs**.
2. Cliquez sur la flèche à côté du bouton **Créer un actif**, puis sur **Importer**.

L'assistant propose **Télécharger le modèle de fichier** si vous préférez partir d'un fichier vierge.

## 3. Choisir le mode Fusion et le champ de correspondance

L'actif « Brightmoor customer portal » existe déjà dans l'espace de travail avec la référence `BRM-A001`. Dans le groupe **Gestion des conflits**, choisissez **Fusion : Ecraser les données des lignes qui matchent (dangereux !)**.

Choisissez ensuite le **champ à utiliser pour la correspondance des données**. Pour les actifs, les champs de correspondance sont `Ref` et `Label`. Brightmoor choisit `Ref`, qui ne change pas quand un actif est renommé. Une ligne correspond à un enregistrement quand la valeur est strictement identique, majuscules et minuscules comprises.

Avec ce choix :

* la ligne `BRM-A001` met à jour l'actif existant ;
* les quatre autres lignes créent de nouveaux actifs.

{% hint style="warning" %}
**Fusion** remplace les valeurs enregistrées par celles du fichier. Une cellule vide conserve la valeur existante, sauf dans les colonnes à choix obligatoire, comme le type ou le statut, qui prennent alors leur valeur par défaut : renseignez-les toujours. L'opération ne peut pas être annulée.
{% endhint %}

Avec **Fusion**, les champs personnalisés sont aussi mis à jour. Une ligne dont `CustomFields.criticality` est vide laisse la valeur enregistrée inchangée.

Pour laisser l'actif existant intact, choisissez plutôt **Préservation : ne pas modifier les données qui remplissent une condition** : la ligne `BRM-A001` est ignorée.

<figure><img src="../.gitbook/assets/examples-import-2.png" alt="Gestion des conflits avec Fusion sélectionné et la référence comme champ de correspondance"><figcaption><p>Le mode Fusion avec le champ de correspondance</p></figcaption></figure>

## 4. Envoyer le fichier et associer les colonnes

1. Cliquez dans la zone **Envoyer/déplacer des fichiers ici** et choisissez le fichier CSV. Dastra lit les premières lignes.
2. À l'étape **Correspondances**, Dastra associe les colonnes du fichier aux colonnes de l'import quand l'en-tête est identique au nom ou au libellé de la colonne. La colonne **Données du fichier** montre les premières valeurs de votre fichier.
3. Utilisez les onglets **Toutes les colonnes**, **Sans correspondance** et **Correspondance (fichier importé)** pour filtrer la liste. Si un en-tête ne correspond pas, choisissez la bonne colonne dans la liste de la ligne. La correspondance de `CustomFields.criticality` apparaît comme les autres.
4. Le bouton **Continuer** reste inactif tant qu'une colonne obligatoire, comme `Label`, n'a pas de correspondance.

<figure><img src="../.gitbook/assets/examples-import-1.png" alt="Étape d'association des colonnes de l'import d'actifs avec le fichier d'exemple"><figcaption><p>Les colonnes du fichier d'exemple, associées</p></figcaption></figure>

## 5. Lire le résultat

Cliquez sur **Continuer**. L'écran **Résultat** indique le nombre de lignes importées, d'objets créés, mis à jour et ignorés. Pour le fichier d'exemple en mode Fusion, attendez-vous à cinq lignes traitées, quatre actifs créés et un mis à jour. Cliquez sur **Afficher** pour ouvrir la liste.

Si une ligne est invalide, par exemple un `CountryCode` qui n'est pas un pays, tout l'import s'arrête et rien n'est enregistré. Le message donne la ligne concernée, l'en-tête comptant pour la ligne 1. Corrigez le fichier et recommencez.
