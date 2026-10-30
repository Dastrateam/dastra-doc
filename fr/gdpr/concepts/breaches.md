---
description: Découvrez comment suivre les notifications de violation de données.
---

# Violations de données

## Définition

Selon [l’article 4.12 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article4),\
une **violation de données à caractère personnel** est :

> _Une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données._

Autrement dit, il s’agit de tout **incident de sécurité**, qu’il soit **intentionnel ou accidentel**, qui compromet :

* la **confidentialité** (accès non autorisé, divulgation),
* l’**intégrité** (altération, falsification),
* la **disponibilité** (perte, effacement, indisponibilité).

***

## Exemples de violations typiques

* Suppression accidentelle de données médicales non sauvegardées.
* Perte d’une clé USB non chiffrée contenant la base clients.
* Piratage d’un serveur exposant des adresses e-mail et mots de passe.
* Envoi d’un e-mail contenant des données personnelles au mauvais destinataire.
* Divulgation d’informations RH sur un espace partagé non sécurisé.

***

## Les trois grands types de violations

| Type                | Description                                 | Exemple                            |
| ------------------- | ------------------------------------------- | ---------------------------------- |
| **Confidentialité** | Accès ou divulgation non autorisée          | Divulgation par phishing           |
| **Intégrité**       | Modification ou falsification non autorisée | Altération d’un fichier médical    |
| **Disponibilité**   | Perte ou destruction accidentelle           | Données supprimées sans sauvegarde |

***

## Les obligations légales du responsable de traitement

Lorsqu’une violation survient, le **responsable du traitement** doit réagir **sans délai**. Un sous-traitant qui constate une violation la notifie au responsable du traitement dans les meilleurs délais (article 33, paragraphe 2).

### Notification à l’autorité de contrôle

* **Délai** : si possible, 72 heures au plus tard après en avoir eu connaissance. La notification n’est pas requise lorsque la violation n’est pas susceptible d’engendrer un risque pour les droits et libertés des personnes.
* **Contenu** :
  * nature de la violation,
  * catégories et volume de données concernées,
  * conséquences probables,
  * mesures prises ou envisagées pour y remédier.

> Si la notification n’est pas transmise dans les 72h, il faut **justifier le retard**.

Référence : [Article 33 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article33)

***

### Information des personnes concernées

Si la violation **présente un risque élevé pour les droits et libertés**,\
les personnes concernées doivent être informées **dans les meilleurs délais** :

* Nature de la violation,
* Données impactées,
* Mesures prises,
* Recommandations pour limiter les effets (ex. : changement de mot de passe).

Référence : [Article 34 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article34)

***

### Documentation interne obligatoire

Même lorsqu’aucune notification n’est requise,\
**chaque violation doit être enregistrée** dans un registre interne comprenant :

* les faits relatifs à la violation,
* ses effets,
* les mesures correctives prises.

> Ce registre sert à **démontrer la conformité** (principe d’accountability).

***

## Le cycle de gestion d’une violation

1. **Détection** → Identification d’un incident ou d’un comportement anormal.
2. **Qualification** → Vérifier si les données personnelles sont concernées.
3. **Évaluation du risque** → Impact sur la vie privée des personnes.
4. **Notification (si nécessaire)** → autorité de contrôle sous 72 h si possible, personnes concernées si risque élevé.
5. **Remédiation** → Mesures correctrices et préventives.
6. **Documentation** → Enregistrement dans le registre des violations.
7. **Retour d’expérience** → Ajustements organisationnels ou techniques.

***

## Bonnes pratiques de sécurité

* Préparer un **plan de gestion des incidents** et le tester régulièrement.
* Former les équipes à la **détection et la remontée rapide** d’incidents.
* Mettre en place des **mesures préventives** (MFA, segmentation réseau, sauvegardes).
* Utiliser un **registre centralisé** pour tracer chaque violation et sa résolution.
* Évaluer la gravité via une **grille de risque** standardisée (ex. CNIL ou ISO 27005).

***

## Gestion des violations dans Dastra

Le module **Incidents** de Dastra sert à documenter et à piloter les violations de données :

| Étape        | Fonctionnalité Dastra                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------- |
| Déclaration  | Fiche de violation dans le registre des incidents                                                             |
| Évaluation   | Niveau de risque calculé à partir de la probabilité d’identification et de la gravité des conséquences        |
| Notification | Suivi de la notification à l’autorité (compte à rebours de 72 heures) et de la communication aux personnes    |
| Suivi        | Tâches associées, mesures adoptées après l’incident, post-mortem et historique                                |
| Statistiques | Page **Statistiques** avec les indicateurs sur les incidents                                                  |

***

## Ressources utiles

* [CNIL : déclarer une violation de données personnelles](https://www.cnil.fr/fr/violation-de-donnees-personnelles)
* [ENISA : agence de l’Union européenne pour la cybersécurité](https://www.enisa.europa.eu/)
* [ISO/IEC 27035 : gestion des incidents de sécurité de l’information](https://www.iso.org/standard/60803.html)

***

{% hint style="success" %}
**Bon réflexe :** Un incident signalé rapidement limite l’impact, renforce la transparence et démontre la maîtrise de la conformité.\
Dastra vous aide à structurer et documenter chaque étape du processus.
{% endhint %}

***

## Pour aller plus loin

{% content-ref url="../../features/incidents/README.md" %}
[Violations de données](../../features/incidents/README.md)
{% endcontent-ref %}

{% content-ref url="../../features/incidents/document-breach.md" %}
[Documenter une nouvelle violation de données](../../features/incidents/document-breach.md)
{% endcontent-ref %}
