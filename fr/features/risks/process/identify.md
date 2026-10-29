---
description: Apprenez comment identifier les risques dans Dastra.
---

# 1. Identifier

Pour créer un risque, ouvrez **Gestion des risques** > **Risques**, choisissez l'onglet du type d'objet concerné et cliquez sur **Créer un risque**. Vous pouvez aussi le créer depuis la page d'un traitement (voir [Associer un risque à un traitement](../attach-to-processing.md)). La section **Identification** s'ouvre.

<figure><img src="../../../.gitbook/assets/risks-identify-1.png" alt="Section Identification d'un nouveau risque : unité organisationnelle, objet lié, propriétaire, date d'identification et type de risque"><figcaption><p>La section Identification d'un risque</p></figcaption></figure>

Renseignez les éléments d'identification :

* l'unité organisationnelle : par défaut, celle du traitement si le risque est rattaché à un traitement ;
* l'objet concerné, par exemple le traitement ;
* le propriétaire du risque, qui a la responsabilité de le suivre et de le piloter ;
* la date d'identification ;
* le type de risque, choisi dans le référentiel ;
* une description du risque, propre à cet objet.

{% hint style="info" %}
Dastra propose un référentiel de types de risque. Il fait gagner du temps et se réutilise sur d'autres objets.
{% endhint %}

Si votre type de risque n'est pas dans le référentiel, ajoutez-le directement depuis cette page avec **Créer un type de risque**.

## Ajouter un type de risque <a href="#ajouter-un-type-de-risque" id="ajouter-un-type-de-risque"></a>

Vous pouvez aussi gérer les types de risque dans **Gestion des risques** > **Types de risque**, avec le bouton **Créer un type de risque**.

Un type de risque se réutilise pour générer le même risque sur autant d'objets que vous le souhaitez. Par exemple, vous souhaitez identifier le même risque chez plusieurs de vos sous-traitants : renseignez ce type de risque une seule fois et réutilisez-le pour chaque sous-traitant ou prestataire.

Dans la section **Identification** du type de risque, donnez-lui un nom et une référence interne. Les tags sont facultatifs.

<figure><img src="../../../.gitbook/assets/risks-identify-2.png" alt="Formulaire d'un type de risque : nom, référence, évènement redouté et sa description"><figcaption><p>Un type de risque : nom, référence et évènement redouté</p></figcaption></figure>

Un risque est la combinaison d'un évènement redouté et d'une ou plusieurs menaces de réalisation de cet évènement. Il se mesure en termes de vraisemblance (probabilité d'occurrence) et de gravité (impact).

### Évènement redouté

Pour ajouter un type de risque, identifiez l'évènement redouté et ses impacts. L'évènement redouté est la conséquence de l'occurrence d'un risque.

Classiquement, on évoque trois types d'évènements redoutés en matière de sécurité des systèmes d'information et de vie privée. Le RGPD invite d'ailleurs à [garantir la sécurité](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32016R0679#d1e3428-1-1) des données personnelles selon ces trois axes (article 32) :

* l'atteinte à la **confidentialité**
* l'atteinte à la **disponibilité**
* l'atteinte à l'**intégrité**

Vous pouvez créer vos propres catégories d'évènements redoutés avec **Créer un évènement redouté** : un accident industriel ou un acte de corruption, par exemple. Les évènements redoutés ne sont pas limités en nombre. Le module se concentre d'abord sur les risques liés aux systèmes d'information.

Pour chaque évènement redouté, précisez les impacts qu'il engendre dans le champ **Description de l'évènement redouté**.

Les impacts varient selon le contexte et l'objet dont on traite le risque. Pour les risques liés aux données personnelles, ils consistent en des préjudices pour les personnes : usurpation d'identité, accusation à tort, perte de l'état civil, etc.

### Menaces

Pour chaque évènement redouté, identifiez la ou les menaces qui permettent sa réalisation. Imaginez un scénario : appuyez-vous sur des évènements passés ou sur votre imagination pour anticiper ce qui pourrait arriver.

Dans la section **Menaces**, sélectionnez une menace existante avec **Ajouter une menace** ou créez-en une. Le champ **Description de la menace** précise le scénario.

<figure><img src="../../../.gitbook/assets/risk-threats-section.png" alt="Section Menaces d'un type de risque, avec le bouton Ajouter une menace"><figcaption><p>La section Menaces d'un type de risque</p></figcaption></figure>

Dastra propose des modèles de menaces génériques. Pour les importer, ouvrez **Gestion des risques** > **Menaces**, ouvrez le menu du bouton **Créer une menace** et cliquez sur **Créer à partir de modèles**.

### Sources

Les sources de risque sont les éléments qui permettent la réalisation de l'évènement redouté : qui ou quoi pourrait en être à l'origine ?

Prenez en compte les sources humaines, par exemple un administrateur informatique, un cyberattaquant ou un État étranger, et les sources non humaines, par exemple l'eau, un séisme ou un virus informatique non ciblé.

Dans la section **Sources**, sélectionnez ou créez les sources, puis précisez-les dans **Description de la source**.

<figure><img src="../../../.gitbook/assets/risks-identify-3.png" alt="Section Sources d'un type de risque avec deux sources sélectionnées"><figcaption><p>La section Sources d'un type de risque</p></figcaption></figure>

### Points de contrôle

Pour chaque type de risque, déterminez les mesures existantes ou prévues qui traitent le risque. Ces points de contrôle sont de plusieurs natures : mesures de sécurité, techniques, organisationnelles, juridiques ou fonctionnelles.

Dans la section **Points de contrôle**, sélectionnez des points existants avec **Sélectionnez les points de contrôle** ou créez-en avec **Créer un point de contrôle**. Chaque point de contrôle indique :

* son objectif : réduire l'impact (mitigation) ou la probabilité (prévention) du risque ;
* ses réponses possibles et leur score, de 0 à 100 points. Par défaut, un nouveau point de contrôle propose les réponses **Oui** (1 point), **Non** (0 point) et **Non applicable** ;
* son responsable, sa priorité (1 est la plus haute, 10 la plus basse) et, si besoin, une évaluation récurrente avec le nombre de jours entre deux contrôles.

<figure><img src="../../../.gitbook/assets/risks-identify-4.png" alt="Section Points de contrôle d'un type de risque avec trois points de contrôle sélectionnés"><figcaption><p>La section Points de contrôle d'un type de risque</p></figcaption></figure>

Dans les risques liés à la sécurité des systèmes d'information, la norme ISO 27001 identifie des points de contrôle standards. Le guide sécurité des données personnelles de la CNIL en propose aussi plusieurs.

### Pré-évaluation

Dans un type de risque, vous pouvez inclure une évaluation. Elle est reprise dans chaque risque créé à partir de ce type, ce qui fait gagner du temps. Elle est facultative.

L'évaluation se fait en vraisemblance et en gravité, selon l'échelle que vous avez paramétrée (voir [Évaluer](assess.md)).

Vous pouvez définir le risque initial : le risque théorique lié à l'activité, avant toute mesure de maîtrise (contrôle interne).

Vous pouvez aussi définir le risque résiduel : le risque subsistant après la mise en œuvre des dispositifs de maîtrise, les points de contrôle notamment. Il ne peut pas dépasser le risque initial.

<figure><img src="../../../.gitbook/assets/risks-identify-5.png" alt="Section Pré-évaluation d'un type de risque avec les niveaux initial et résiduel"><figcaption><p>La pré-évaluation des risques initial et résiduel</p></figcaption></figure>
