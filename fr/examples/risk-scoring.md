---
description: >-
  Calculez un risque pas à pas sur l'échelle 5×5 par défaut et sur l'échelle 4×4
  de la CNIL, puis voyez comment le score d'une violation de données est
  calculé.
---

# Calcul des risques

Cet exemple évalue un risque de Brightmoor Retail Group sur deux échelles, puis évalue une violation de données. Les deux calculs diffèrent : le score d'un risque est un produit, celui d'une violation de données est une somme.

## Le risque

Brightmoor identifie le risque « Loss of customer payment data » sur le traitement « Online order management ». Dans la section **Evaluation du risque**, Emma Walsh, la déléguée à la protection des données, choisit une **Gravité** et une **Vraisemblance** pour le risque initial, puis pour le risque résiduel une fois les contrôles en place. Voir [Évaluer un risque](../features/risks/process/assess.md) pour l'écran.

Le score d'un risque est **gravité × vraisemblance**. Le score maximal d'une échelle est le produit de ses deux niveaux les plus élevés. Dastra affiche le score sous la forme « score / maximum » et, dans certaines vues, en pourcentage du maximum.

## Sur l'échelle 5×5 par défaut

L'échelle par défaut, **Echelle de risque par défaut**, compte cinq niveaux sur chaque axe.

| Niveau | Gravité | Vraisemblance |
| --- | --- | --- |
| 1 | Négligable | Improbable |
| 2 | Faible | Peu probable |
| 3 | Moyen | Possible |
| 4 | Elevé | Probable |
| 5 | Critique | Très probable |

Brightmoor évalue le risque initial à une gravité **Elevé** (4) et une vraisemblance **Possible** (3). Les paiements par carte sont traités par un prestataire externe, mais la base des commandes conserve les derniers chiffres et l'adresse de facturation. Après les contrôles (chiffrement, revues d'accès), la vraisemblance résiduelle passe à **Improbable** (1).

| Risque | Gravité | Vraisemblance | Calcul | Score | Pourcentage | Case de la matrice |
| --- | --- | --- | --- | --- | --- | --- |
| Initial | 4 | 3 | 4 × 3 | 12 / 25 | 48 % | rouge |
| Résiduel | 4 | 1 | 4 × 1 | 4 / 25 | 16 % | verte |

<figure><img src="../.gitbook/assets/examples-risk-1.png" alt="Section Évaluation du risque avec les risques initial et résiduel placés sur la matrice 5 × 5"><figcaption><p>Le risque sur l'échelle par défaut</p></figcaption></figure>

Le pourcentage est le score divisé par le maximum (25), arrondi. La couleur de la case vient de la matrice de l'échelle : avec cinq niveaux, la ligne est la gravité comptée depuis le haut et la colonne est la vraisemblance.

Le risque courant se situe entre les deux. Après chaque réponse à un point de contrôle, Dastra le recalcule avec cette formule : risque courant = risque initial − (risque initial − risque résiduel) × taux de remédiation. Avec un taux de remédiation de 50 %, le risque courant est de 12 − (12 − 4) × 0,5 = 8. Voir [Effet sur le risque courant](../features/risks/process/monitor.md#effet-sur-le-risque-courant).

## Sur l'échelle 4×4 de la CNIL

Brightmoor décide d'utiliser l'échelle à quatre niveaux de la méthode de la CNIL pour les analyses d'impact. Dans **Réglages espace de travail** > **Gestion des risques**, une échelle est créée avec le **Modèle d'échelle de risque** **4 niveaux - PIA de la CNIL**, puis activée avec **Enregistrer et activer cette grille** (voir [Configurer l'échelle de risques](../features/risks/process/assess.md)).

| Niveau | Gravité | Valeur | Vraisemblance | Valeur |
| --- | --- | --- | --- | --- |
| 1 | Négligable | 10 000 € | Improbable | 25 % |
| 2 | Faible | 50 000 € | Peu probable | 50 % |
| 3 | Moyen | 100 000 € | Possible | 75 % |
| 4 | Elevé | 1 000 000 € | Probable | 100 % |

<figure><img src="../.gitbook/assets/examples-risk-2.png" alt="Éditeur d'échelle de risque avec la matrice à quatre niveaux du modèle CNIL"><figcaption><p>L'échelle 4 levels - Classic DPIA</p></figcaption></figure>

Les valeurs sont celles par défaut du modèle. Elles sont modifiables, comme les libellés.

La même évaluation, gravité **Elevé** (4) et vraisemblance **Possible** (3), donne maintenant :

| Risque | Gravité | Vraisemblance | Calcul | Score | Pourcentage | Case de la matrice |
| --- | --- | --- | --- | --- | --- | --- |
| Initial | 4 | 3 | 4 × 3 | 12 / 16 | 75 % | rouge |
| Résiduel | 4 | 1 | 4 × 1 | 4 / 16 | 25 % | orange |

Le score est identique, mais le maximum est plus bas, donc le même risque pèse davantage : 75 % au lieu de 48 %, et le risque résiduel est orange au lieu de vert. C'est pourquoi Dastra demande une confirmation avant d'activer une autre échelle quand des risques existent, et pourquoi il vaut mieux choisir l'échelle avant de saisir vos premiers risques (voir la [FAQ](../features/risks/faq.md)).

## Une violation de données

Le module Incidents n'utilise pas les échelles de risque. À l'étape **Analyse de risque** d'une violation de données, répondez **Non** à **Une analyse du risque a-t-elle déjà été effectuée ?**, puis choisissez deux scores de 1 à 4 :

* **Identification des personnes concernées** : la facilité à identifier les personnes à partir des données ;
* **Impacts sur les personnes concernées** : la gravité des conséquences pour elles.

Les libellés des quatre valeurs sont **1 - Négligeable**, **2 - Limité**, **3 - Important** et **4 - Maximal**. Le score de la violation est leur **somme**, de 2 à 8, et il détermine le **Niveau de risque** :

| Total des deux scores | Niveau de risque | Conséquence affichée par Dastra |
| --- | --- | --- |
| 2 et 3 | Risque négligeable | La notification à l'autorité de contrôle et la communication aux personnes ne sont pas nécessaires |
| 4 et 5 | Risque réel | Notification à l'autorité de contrôle obligatoire |
| 6 à 8 | Risque élevé | Notification à l'autorité de contrôle et communication aux personnes concernées obligatoires |

Brightmoor découvre qu'un export clients était lisible pendant quelques heures dans un espace de stockage mal configuré. Il contient des noms, des adresses e-mail et des historiques de commandes.

| Cas | Identification | Impact | Calcul | Score | Niveau de risque |
| --- | --- | --- | --- | --- | --- |
| Export des seuls numéros de commande | 2 | 1 | 2 + 1 | 3 | Risque négligeable |
| Export des noms sans coordonnées | 3 | 1 | 3 + 1 | 4 | Risque réel |
| Export du fichier clients | 4 | 2 | 4 + 2 | 6 | Risque élevé |

Pour le troisième cas, un produit donnerait 4 × 2 = 8, mais Dastra additionne les scores : 4 + 2 = 6. C'est déjà un **Risque élevé** : la notification à l'autorité de contrôle et la communication aux personnes concernées sont obligatoires. Voir [Documenter une nouvelle violation de données](../features/incidents/document-breach.md) pour l'étape et le compteur de 72 heures.

{% hint style="info" %}
Avec **Oui** à **Une analyse du risque a-t-elle déjà été effectuée ?**, vous saisissez votre propre analyse et choisissez vous-même le niveau dans **Conclusion de l'analyse du risque : niveau de risque estimé**. Le niveau choisi remplace le niveau calculé.
{% endhint %}
