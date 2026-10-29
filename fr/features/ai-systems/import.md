---
description: >-
  Importez dans Dastra votre registre existant de systèmes d'IA depuis un
  fichier CSV ou Excel, avec le format attendu pour chaque colonne.
---

# Importer vos systèmes d'IA

Si vous disposez déjà d'un registre de systèmes d'IA, importez-le dans Dastra plutôt que de tout saisir à la main.

1. Cliquez sur **Systèmes d'IA** dans la barre latérale, puis sur **Registre des systèmes d'IA**.
2. En haut à droite, ouvrez le menu du bouton **Créer un nouveau système d'IA** et cliquez sur **Importer**.
3. Sur la page qui s'ouvre, ajoutez votre fichier en bas de page.

<figure><img src="../../.gitbook/assets/ai-systems-import-1.png" alt="Menu du bouton Créer un nouveau système d'IA avec les actions Créer à partir de modèles, Importer et Exporter"><figcaption><p>L'action Importer dans le menu du registre des systèmes d'IA</p></figcaption></figure>

Pour le détail de la procédure, voir [Importer vos données (Excel, Csv, JSON)](../general/import.md).

## Format du fichier

Le fichier contient une ligne d'en-têtes qui reprend les noms des colonnes décrites ci-dessous. Toutes les colonnes sont facultatives, sauf `Label`.

Les colonnes de type énumération attendent exactement les valeurs de la colonne « Valeurs autorisées ». La casse n'a pas d'importance. Une valeur qui ne correspond à aucune valeur autorisée est ignorée.

| Colonne | Description | Type | Contraintes | Valeurs autorisées |
| --- | --- | --- | --- | --- |
| `Label` | Nom du système | Texte | Obligatoire, 1 à 120 caractères | Texte libre |
| `Ref` | Référence interne | Texte | 50 caractères au maximum | Texte libre |
| `Description` | Description du système | Texte | 4 000 caractères au maximum | Texte libre |
| `State` | État du système | `AiSystemState` | | `Draft`, `Cancelled`, `Pending`, `Active` |
| `RiskLevel` | Niveau de risque | `AiSystemRiskLevel` | | `Low`, `Medium`, `High`, `Unacceptable` |
| `RiskLevelJustification` | Justification du niveau de risque | Texte | | Texte libre |
| `BenefitLevel` | Niveau de valeur ajoutée | `AiSystemBenefitLevel` | | `Low`, `Medium`, `High` |
| `BenefitLevelJustification` | Justification de la valeur ajoutée | Texte | | Texte libre |
| `DateArchived` | Date de mise à la corbeille | Date | Formats `DD-MM-YYYY` ou `DD/MM/YYYY` | Date |
| `DateCreation` | Date de création | Date | Même format | Date |
| `DateUpdate` | Date de mise à jour | Date | Même format | Date |
| `DateDeployment` | Date de déploiement | Date | Même format | Date |
| `DateRetirement` | Date de retrait | Date | Même format | Date |
| `TransparencyNoticeDone` | Notice de transparence fournie | Booléen | | `true` ou `false` |
| `TransparencyNoticeHtml` | Contenu HTML de la notice | Texte | | HTML |

### Correspondance avec les libellés de l'application

Les valeurs du fichier sont les noms techniques, pas les libellés affichés dans l'application. N'écrivez pas le libellé à l'écran dans le fichier.

| Colonne | Valeur du fichier | Libellé affiché |
| --- | --- | --- |
| `State` | `Draft` | Projet |
| `State` | `Pending` | En attente |
| `State` | `Active` | En cours |
| `State` | `Cancelled` | Annulé |
| `RiskLevel` | `Low` | Minimal |
| `RiskLevel` | `Medium` | Risque limité |
| `RiskLevel` | `High` | Haut risque |
| `RiskLevel` | `Unacceptable` | Inacceptable |
| `BenefitLevel` | `Low` | Bas |
| `BenefitLevel` | `Medium` | Moyen |
| `BenefitLevel` | `High` | Élevé |

## Exemple de ligne

```
"ChatGPT interne","SYS-001","Modèle interne d’assistance documentaire","Active","Medium","Usage responsable mais risques modérés","High","Très forte valeur ajoutée pour les équipes","01/02/2024","15/01/2024","01/03/2024","20/03/2024","","false","<p>Cette IA est utilisée pour assister les employés dans la rédaction de documents internes.</p>"
```

## Modèle d'en-têtes prêt à l'emploi

Copiez cette ligne dans un fichier `.csv` vierge :

```
Label,Ref,Description,State,RiskLevel,RiskLevelJustification,BenefitLevel,BenefitLevelJustification,DateArchived,DateCreation,DateUpdate,DateDeployment,DateRetirement,TransparencyNoticeDone,TransparencyNoticeHtml
```
