---
description: >-
  La bibliothèque des risques permet d’identifier, qualifier et suivre les
  risques liés aux exigences et aux contrôles définis dans les frameworks de
  conformité.
---

# Risques

Dans Dastra, un risque représente un **événement redouté** susceptible d’avoir un impact négatif sur l’organisation, en lien avec l’utilisation, le développement ou l’exploitation de systèmes (ex. systèmes d’IA).

Les risques sont un **élément clé de pilotage** : ils permettent de mesurer l’exposition de l’organisation et d’évaluer l’efficacité réelle des contrôles mis en place.

***

### Risques et contrôles : une relation centrale

Un point essentiel à comprendre est que **les risques ne sont jamais isolés**.

👉 Dans Dastra :

* un **risque est couvert par un ou plusieurs contrôles**
* un **contrôle contribue à réduire un ou plusieurs risques**

Les contrôles constituent donc les **mesures de maîtrise du risque**.\
Ils permettent de réduire :

* la **probabilité** de survenance du risque,
* et/ou son **impact** sur l’organisation.

Cette relation permet de passer d’une approche déclarative à une **gestion opérationnelle du risque**, basée sur des actions concrètes et vérifiables.

***

### Vue bibliothèque des risques

<figure><img src="../../../.gitbook/assets/image (497).png" alt=""><figcaption></figcaption></figure>

La bibliothèque des risques offre une vision globale des risques identifiés, avec notamment :

* leur référence et leur description,
* les tags associés (confidentialité, performance, robustesse, etc.),
* les niveaux d’impact et de probabilité initiaux,
* des filtres pour faciliter l’analyse transverse.

👉 Cette vue permet :

* d’identifier les risques majeurs,
* de vérifier leur couverture par des contrôles,
* de prioriser les efforts de conformité.

***

### Création et description d’un risque

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image (498).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}


Lors de la création ou de l’édition d’un risque, l’utilisateur renseigne :

* **le nom et la référence du risque**
* une **description** permettant de qualifier le scénario de risque
* des **tags** pour faciliter la catégorisation
{% endcolumn %}
{% endcolumns %}

***

### Évaluation du risque

Chaque risque fait l’objet de deux évaluations distinctes :

#### Risque initial

Le **risque initial** correspond au niveau de risque **avant la mise en place des contrôles**.

Il est évalué selon :

* une **probabilité**
* un **impact**

Ces deux dimensions sont positionnées sur une **grille de risques** standardisée.

***

#### Risque résiduel

Le **risque résiduel** correspond au niveau de risque **après application des contrôles associés**.

👉 La comparaison entre risque initial et risque résiduel permet :

* de mesurer l’efficacité des contrôles,
* de visualiser la réduction du risque,
* de justifier les choix de remédiation.

📌 À ce stade, la **grille de risques est fixe** et commune à l’ensemble des risques, afin de garantir une évaluation homogène et comparable.

***

### Association des contrôles

{% columns %}
{% column %}


Un risque doit être associé à un ou plusieurs **contrôles**, qui représentent les mesures mises en œuvre pour le maîtriser.

L’association permet :

* d’identifier clairement les leviers de réduction du risque,
* de suivre l’impact des contrôles sur le risque résiduel,
* d’assurer la traçabilité entre conformité et gestion des risques.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image (500).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}



***

### Association des menaces

Les risques peuvent également être reliés à des **menaces**, qui représentent les **événements ou causes** susceptibles de déclencher le risque.

👉 Exemple :

* **Menace** : absence de supervision des logs IA
* **Risque** : fuite d’informations via requêtes IA

Cette distinction permet une analyse plus fine et plus structurée des scénarios de risque.

***

### Pourquoi intégrer les risques dans la bibliothèque

La centralisation des risques dans la bibliothèque permet :

* une vision transverse des risques sur l’ensemble des frameworks
* une meilleure cohérence dans leur évaluation
* un lien direct entre risques, contrôles et exigences
* un pilotage plus efficace de la conformité et de la sécurité
