---
description: Découvrez comment suivre les notifications de violation de données.
---

# Violations de données

### 📖 Définition

Selon [l’article 4.12 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article4),\
une **violation de données à caractère personnel** est :

> _Une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel transmises, conservées ou traitées d'une autre manière, ou l'accès non autorisé à de telles données._

Autrement dit, il s’agit de tout **incident de sécurité**, qu’il soit **intentionnel ou accidentel**, qui compromet :

* la **confidentialité** (accès non autorisé, divulgation),
* l’**intégrité** (altération, falsification),
* la **disponibilité** (perte, effacement, indisponibilité).

***

### ⚠️ Exemples de violations typiques

* Suppression accidentelle de données médicales non sauvegardées.
* Perte d’une clé USB non chiffrée contenant la base clients.
* Piratage d’un serveur exposant des adresses e-mail et mots de passe.
* Envoi d’un e-mail contenant des données personnelles au mauvais destinataire.
* Fuite d’informations RH sur un espace partagé non sécurisé.

***

### 🧩 Les trois grands types de violations

| Type                | Description                                 | Exemple                            |
| ------------------- | ------------------------------------------- | ---------------------------------- |
| **Confidentialité** | Accès ou divulgation non autorisée          | Fuite de données par phishing      |
| **Intégrité**       | Modification ou falsification non autorisée | Altération d’un fichier médical    |
| **Disponibilité**   | Perte ou destruction accidentelle           | Données supprimées sans sauvegarde |

***

### 🕓 Les obligations légales du responsable de traitement

Lorsqu’une violation survient, le **responsable du traitement** doit réagir **sans délai**.

#### 1️⃣ Notification à l’autorité de protection (CNIL)

* **Délai** : 72 heures après en avoir eu connaissance.
* **Contenu** :
  * nature de la violation,
  * catégories et volume de données concernées,
  * conséquences probables,
  * mesures prises ou envisagées pour y remédier.

> Si la notification n’est pas transmise dans les 72h, il faut **justifier le retard**.

📚 Référence : [Article 33 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article33)

***

#### 2️⃣ Information des personnes concernées

Si la violation **présente un risque élevé pour les droits et libertés**,\
les personnes concernées doivent être informées **dans les meilleurs délais** :

* Nature de la violation,
* Données impactées,
* Mesures prises,
* Recommandations pour limiter les effets (ex. : changement de mot de passe).

📚 Référence : [Article 34 du RGPD](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article34)

***

#### 3️⃣ Documentation interne obligatoire

Même lorsqu’aucune notification n’est requise,\
**chaque violation doit être enregistrée** dans un registre interne comprenant :

* les faits relatifs à la violation,
* ses effets,
* les mesures correctives prises.

> Ce registre permet de **démontrer la conformité** (principe d’accountability).

***

### 🔁 Le cycle de gestion d’une violation

1. **Détection** → Identification d’un incident ou d’un comportement anormal.
2. **Qualification** → Vérifier si les données personnelles sont concernées.
3. **Évaluation du risque** → Impact sur la vie privée des personnes.
4. **Notification (si nécessaire)** → CNIL sous 72h, personnes concernées si risque élevé.
5. **Remédiation** → Mesures correctrices et préventives.
6. **Documentation** → Enregistrement dans le registre des violations.
7. **Retour d’expérience** → Ajustements organisationnels ou techniques.

***

### 🧠 Bonnes pratiques de sécurité

* Préparer un **plan de gestion des incidents** et le tester régulièrement.
* Former les équipes à la **détection et la remontée rapide** d’incidents.
* Mettre en place des **mesures préventives** (MFA, segmentation réseau, sauvegardes).
* Utiliser un **registre centralisé** pour tracer chaque violation et sa résolution.
* Évaluer la gravité via une **grille de risque** standardisée (ex. CNIL ou ISO 27005).

***

### 🧾 Gestion des violations dans Dastra

Dastra permet de **documenter et piloter les violations de données** de manière centralisée :

| Étape        | Fonctionnalité Dastra                                              |
| ------------ | ------------------------------------------------------------------ |
| Déclaration  | Formulaire de signalement personnalisable                          |
| Évaluation   | Calcul automatique du risque sur les droits des personnes          |
| Notification | Génération de rapports pour la CNIL et communication aux personnes |
| Suivi        | Journal d’actions et plan de remédiation                           |
| Reporting    | Tableaux de bord et indicateurs de conformité                      |

***

### 📚 Ressources utiles

* [CNIL – Déclarer une violation de données personnelles](https://www.cnil.fr/fr/violation-de-donnees-personnelles)
* [ENISA – Data Breach Notification Guidelines](https://www.enisa.europa.eu/)
* [ISO/IEC 27035 – Gestion des incidents de sécurité de l’information](https://www.iso.org/standard/60803.html)

***

{% hint style="success" %}
💡 **Bon réflexe :** Un incident signalé rapidement limite l’impact, renforce la transparence et démontre la maîtrise de la conformité.\
Dastra vous aide à structurer et documenter chaque étape du processus.
{% endhint %}
