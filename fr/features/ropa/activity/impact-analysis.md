---
description: Évaluez l'impact du traitement sur la vie privée.
---

# Analyse d'impact

{% embed url="https://youtu.be/We7jZ2DpmLk" %}

La section **Analyse d'impact** vous aide à évaluer si votre traitement doit faire l’objet d’une analyse d’impact relative à la protection des données (AIPD, appelée PIA dans Dastra), prévue par l’[**article 35 du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article35).

Cette section n'est disponible que pour les traitements en tant que **Responsable de traitement**.

Qu'est-ce qu'un PIA ? Un processus qui permet d'évaluer la nécessité et la proportionnalité du traitement et d'en gérer les risques.

Dans quels cas dois-je mener un PIA ? Lorsque le traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes concernées. Le Comité européen de la protection des données (CEPD) a précisé le champ d’application de cette exigence. Concrètement, si le traitement remplit au moins deux des critères suivants, un PIA est obligatoire :

* Évaluation ou notation
* Décision automatisée avec effet juridique ou effet similaire significatif
* Surveillance systématique
* Données sensibles ou données à caractère hautement personnel
* Données traitées à grande échelle
* Croisement ou combinaison d'ensembles de données
* Données concernant des personnes vulnérables
* Usage innovant ou application de nouvelles solutions technologiques ou organisationnelles
* Traitement qui empêche les personnes concernées d'exercer un droit ou de bénéficier d'un service ou d'un contrat

Pour un traitement particulièrement sensible pour les personnes concernées, un seul critère peut parfois suffire.

## Remplir la section Analyse d'impact

1. Si le traitement relève d'un type de traitement pour lequel une autorité de contrôle n'exige pas de PIA, répondez **Oui** à **Ce traitement est-il exempté de PIA ?** et expliquez pourquoi dans **Justification de l'exemption de PIA**. Les critères sont alors masqués.
2. Sinon, répondez **Non**. Si un PIA a déjà été réalisé, saisissez sa date dans **Date du dernier PIA**.
3. Sous **Évaluation des 9 critères de l'AIPD (CEPD)**, répondez **Non applicable**, **Non** ou **Oui** pour chaque critère. Survolez l'icône d'information à côté d'un critère pour afficher des exemples.

Les critères s'affichent ainsi dans l'application :

* **Evaluation ou notation incluant les activités de profilage et de prédiction**
* **Prise de décision automatique avec effet juridique ou similaire**
* **Surveillance systématique des personnes**
* **Collecte de données sensibles ou données à caractère hautement personnel**
* **Collecte de données à large échelle**
* **Croisement ou combinaison de données**
* **Collecte de données concernant des personnes vulnérables**
* **Ce traitement utilise-t-il une technologie ou un usage innovant (IA...) ?**
* **Exclusion du bénéfice d’un droit/contrat**

Dès que vous répondez **Oui** à au moins deux critères, Dastra considère qu'un PIA est nécessaire. Si vous utilisez les [questionnaires](../../questionnaires/README.md), un message en haut de la section vous rappelle alors que **Vous devez réaliser une analyse d'impact (PIA)**, avec un bouton **Créer un PIA** pour lancer un [questionnaire PIA](../../questionnaires/types/dpia.md). Une fois la date du PIA saisie, le message devient **Un PIA a été effectué** et vous rappelle de le renouveler régulièrement. Lorsque les critères sont renseignés et que moins de deux sont remplis, ou lorsque le traitement est exempté, Dastra affiche **Le PIA n'est pas obligatoire**.

{% hint style="info" %}
La liste des traitements concernés dépend des recommandations de votre autorité de contrôle nationale. Consultez notre [guide du PIA pays par pays](../../../other/dpia-by-country.md) pour identifier vos obligations.
{% endhint %}

## Générer l'évaluation avec l'assistant IA

L'assistant IA peut proposer une réponse pour chacun des 9 critères à partir des informations déjà renseignées dans la fiche du traitement : nom, description, finalités, catégories de personnes concernées, catégories de données personnelles, actifs et destinataires.

<figure><img src="../../../.gitbook/assets/ropa-impact-analysis-1.png" alt="Bouton Générer l&#x27;évaluation à côté du titre Évaluation des 9 critères de l&#x27;AIPD (CEPD) dans la section Analyse d&#x27;impact"><figcaption><p>Le bouton Générer l'évaluation lance l'analyse des 9 critères par l'assistant IA</p></figcaption></figure>

1. Dans la section **Analyse d'impact** du traitement, cliquez sur **Générer l'évaluation**, à côté du titre **Évaluation des 9 critères de l'AIPD (CEPD)**.
2. Vérifiez la rubrique **Données partagées avec le modèle d'IA**. Elle liste les informations du traitement transmises à l'assistant.
3. Cliquez sur **Générer**.
4. Examinez la proposition. Pour chaque critère, l'assistant donne une réponse (Oui, Non ou Non applicable) avec une justification, ainsi qu'un score de confiance de l'analyse. Le cas échéant, la rubrique **Informations manquantes qui pourraient changer l'évaluation** liste les éléments à compléter dans la fiche pour fiabiliser le résultat.
5. Cliquez sur **Appliquer au formulaire** pour reporter les réponses dans la section, ou sur **Retour** pour revenir à l'écran précédent.

Vous gardez la main sur chaque réponse. Après application, chaque critère reste modifiable individuellement. La proposition de l'assistant est une aide à l'analyse et ne remplace pas votre propre évaluation.

## Listes publiées par les autorités de contrôle

Par ailleurs, les autorités de contrôle publient une liste des types de traitement pour lesquels un PIA est obligatoire, et peuvent publier une liste des types de traitement pour lesquels un PIA n'est pas requis.

La CNIL a publié ces deux listes, accessibles ici :

[Liste des types de traitement pour lesquels un PIA n'est pas requis](https://www.cnil.fr/sites/default/files/atoms/files/liste-traitements-aipd-non-requise.pdf)

[Liste des types de traitement pour lesquels un PIA est obligatoire](https://www.cnil.fr/sites/default/files/atoms/files/liste-traitements-aipd-requise.pdf)

L’[**article 30 du RGPD**](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4#Article30) n’exige pas de préciser si un PIA a été réalisé sur le traitement.
