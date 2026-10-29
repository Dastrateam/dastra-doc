---
description: >-
  Classez un système d'IA selon les quatre niveaux de risque de l'AI Act et
  évaluez sa valeur ajoutée, avec ou sans l'aide de l'assistant IA.
---

# Analyse de risque et valeur ajoutée

Deux étapes de la fiche d'un système d'IA évaluent le système : **Classification** pour son niveau de risque, **Valeur ajoutée** pour son intérêt pour votre organisation. Cette page décrit les deux étapes et l'aide que l'assistant IA apporte pour les remplir.

## Classification du niveau de risque

À l'étape **Classification**, vous attribuez l'un des quatre niveaux de risque à chaque système : **Minimal**, **Risque limité**, **Haut risque** ou **Inacceptable**. Ces niveaux sont ceux de l'AI Act, du risque minimal au risque inacceptable. Sous chaque niveau, Dastra affiche des exemples de systèmes concernés.

Ajoutez une justification du niveau choisi dans le champ **Justification du niveau de risque**. Elle devient disponible une fois le niveau sélectionné.

<figure><img src="../../.gitbook/assets/ai-systems-risk-analysis-1.png" alt="Étape Classification avec le sélecteur de niveau de risque, le bouton Générer classification et le champ de justification"><figcaption><p>L'étape Classification d'un système d'IA</p></figcaption></figure>

### Niveaux de risque selon l'AI Act

L'AI Act classe les systèmes d'IA en quatre catégories. Chacune entraîne des obligations différentes.

#### Risque minimal

Systèmes d'IA dont le risque pour les droits fondamentaux ou la sécurité des personnes est négligeable ou nul.

Exemples : filtres anti-spam, moteurs de recommandation de contenus sans impact significatif, IA utilisées dans les jeux vidéo.

Obligations : l'AI Act n'en prévoit pas de particulière, mais les règles générales restent applicables, comme le RGPD et l'obligation de maîtrise de l'IA du personnel (article 4).

#### Risque limité

Systèmes d'IA soumis à des obligations de transparence envers les utilisateurs, sans impact significatif sur leurs droits.

Exemples : chatbots conversationnels, contenus hypertruqués (deepfakes) générés à des fins de divertissement.

Obligations :

* informer l'utilisateur qu'il interagit avec un système d'IA ;
* signaler qu'un contenu a été généré ou modifié par une IA.

#### Risque élevé

Systèmes d'IA qui présentent un risque significatif pour la santé, la sécurité ou les droits fondamentaux. Ils relèvent d'un cadre strict de conformité et d'évaluation.

Exemples :

* scoring de crédit ;
* recrutement automatisé, par exemple le tri de candidatures ;
* identification biométrique, hors pratiques interdites ;
* IA utilisées dans les dispositifs médicaux ou les infrastructures critiques.

Obligations :

* évaluation de la conformité avant la mise sur le marché ;
* gestion des risques ;
* gouvernance des données utilisées ;
* transparence et documentation technique détaillée ;
* surveillance humaine et traçabilité.

{% hint style="info" %}
L'article 27 de l'AI Act impose une analyse d'impact sur les droits fondamentaux à certains déployeurs de systèmes à haut risque : déployeurs de droit public, entités privées qui fournissent des services publics et déployeurs de certains systèmes du secteur financier. Voir [Analyse d'impact sur les droits fondamentaux (FRIA)](fria.md).
{% endhint %}

#### Risque inacceptable

Systèmes d'IA interdits parce qu'ils vont à l'encontre des valeurs de l'Union européenne ou portent atteinte aux droits fondamentaux.

Exemples :

* scoring social des personnes ;
* identification biométrique à distance en temps réel dans l'espace public à des fins répressives, hors exceptions strictes ;
* manipulation subliminale des personnes.

Obligations : la mise sur le marché et l'utilisation dans l'Union européenne sont interdites.

Attribuer le bon niveau de risque vous aide à déterminer les obligations applicables, à prioriser les actions de mise en conformité et à communiquer clairement avec vos équipes métiers et juridiques.

### Générer la classification avec l'IA

Si votre plan inclut les fonctions d'IA correspondantes, le bouton **Générer classification** apparaît au-dessus du sélecteur de niveau. Il propose un niveau de risque à partir des informations déjà saisies dans la fiche.

1. Cliquez sur **Générer classification**. La fenêtre rappelle les données transmises au modèle d'IA : nom du système, description, modèles, rôle au regard de l'AI Act, actifs, traitements liés, jeux de données et catégories de personnes concernées.
2. Cliquez sur **Générer**.
3. Lisez la proposition : le niveau de risque, une justification qui cite les dispositions applicables de l'AI Act, le score de confiance de l'analyse et les informations manquantes qui pourraient modifier ou consolider la classification.
4. Cliquez sur **Appliquer au formulaire** pour reporter le niveau et la justification dans l'étape, ou sur **Retour** pour relancer la génération.
5. Relisez le résultat, corrigez-le si besoin, puis enregistrez la fiche.

<figure><img src="../../.gitbook/assets/ai-systems-risk-analysis-2.png" alt="Fenêtre Générer classification avec le niveau proposé, le score de confiance, la justification et le bouton Appliquer au formulaire"><figcaption><p>Une classification proposée par l'assistant IA</p></figcaption></figure>

{% hint style="warning" %}
La proposition de l'assistant IA aide à classer le système, elle ne remplace pas votre analyse juridique. Relisez-la avant de l'appliquer.
{% endhint %}

### Questionnaire de classification

Tant qu'aucun niveau de risque n'est défini, un encadré **Besoin d'aide pour déterminer le niveau de risque ?** propose de lancer un questionnaire d'évaluation des risques de l'IA. Il vous aide à déterminer la classification du système au regard de l'AI Act : pratiques interdites, domaines à haut risque et obligations de transparence.

Cliquez sur **Lancer questionnaire de classification** et choisissez un modèle de type **Analyse de risque d'un système d'IA**. Le questionnaire se planifie comme les autres : voir [Planifier un questionnaire](../questionnaires/schedule.md). Si la fenêtre n'affiche aucun modèle, installez-en un depuis la bibliothèque, comme pour [l'analyse d'impact](fria.md). L'encadré apparaît si votre plan inclut le module **Questionnaires** et si vous pouvez y créer des questionnaires.

## Valeur ajoutée d'un système d'IA

L'étape **Valeur ajoutée** évalue l'intérêt du système pour votre organisation. Sélectionnez l'un des trois niveaux, **Bas**, **Moyen** ou **Élevé**, puis expliquez dans le champ **Justification du bénéfice** ce que le système apporte concrètement, par exemple :

* un gain de performance opérationnelle ;
* une amélioration de la qualité des services ;
* une réduction des risques ou des coûts.

<figure><img src="../../.gitbook/assets/ai-systems-risk-analysis-3.png" alt="Étape Valeur ajoutée avec le sélecteur de niveau, le bouton Générer l'évaluation et le champ de justification"><figcaption><p>L'étape Valeur ajoutée d'un système d'IA</p></figcaption></figure>

### Générer l'évaluation avec l'IA

Le bouton **Générer l'évaluation** fonctionne comme **Générer classification**. L'assistant IA analyse le contexte de la fiche (finalité, modèles, actifs, traitements liés) et propose un niveau de valeur ajoutée avec une justification. Cliquez sur **Générer**, relisez la proposition, puis cliquez sur **Appliquer au formulaire**. Corrigez ensuite le texte si besoin et enregistrez la fiche.

## Pourquoi remplir ces deux étapes

Renseigner le niveau de risque et la valeur ajoutée vous montre si un système d'IA constitue plutôt une opportunité stratégique pour votre organisation ou un risque disproportionné au regard de sa faible utilité. Un système à haut risque et à faible valeur ajoutée peut ne pas justifier son maintien en production.

Cette analyse combinée facilite vos arbitrages et l'alignement de votre portefeuille d'IA sur vos priorités stratégiques et réglementaires.
