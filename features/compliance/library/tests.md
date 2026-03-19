# Tests

Un test définit **comment** et **à quelle fréquence** un contrôle est évalué, et sur quelles preuves repose cette évaluation.

Les tests constituent le lien opérationnel entre :

* les **contrôles** (mesures mises en œuvre),
* les **preuves** collectées,
* et les **résultats de conformité** observés dans le temps.

***

### Rôle des tests dans Dastra

Un test permet de répondre à une question simple mais essentielle :

> _Le contrôle est-il effectivement appliqué et efficace ?_

Chaque test est :

* associé à un **contrôle de référence**
* exécuté selon une **fréquence définie**
* utilisé dans les **projets de conformité** pour produire des preuves et des résultats exploitables

***

### Vue bibliothèque des tests

<figure><img src="../../../.gitbook/assets/image (492).png" alt=""><figcaption></figcaption></figure>

La bibliothèque des tests offre une vision transverse de tous les tests disponibles, avec notamment :

* leur type (manuel ou automatisé),
* la date de création,
* les contrôles associés,
* des filtres avancés (framework, type, exigences, tests orphelins).

👉 Cette vue permet :

* d’identifier les tests réutilisés dans plusieurs contextes,
* de détecter les tests non rattachés,
* d’industrialiser les méthodes de vérification.

***

### Tests manuels (par défaut)

Par défaut, un test est **manuel**.

📌 Un test manuel repose sur une **action humaine**, par exemple :

* revue documentaire,
* entretien avec les équipes,
* vérification d’un registre,
* audit ponctuel d’un processus.

#### Fonctionnement dans un projet de conformité

Lorsqu’un test manuel est ajouté à un projet :

* il requiert une **mise à jour régulière des preuves**
* selon la **fréquence définie** dans le test (mensuelle, trimestrielle, annuelle, etc.)

👉 Cela permet de garantir une conformité **vivante**, mise à jour dans le temps.

***

### Configuration d’un test

{% columns %}
{% column %}


Lors de la création ou de l’édition d’un test, l’utilisateur définit :

* **le nom et la référence du test** (avec générateur de référence)
* **la fréquence du test**
* **la description détaillée**, incluant :
  * l’objectif du test
  * la procédure à suivre
  * les éléments de preuve attendus
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/image (496).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

Ces informations servent de guide opérationnel lors de l’exécution du test dans un projet.

***



### Tests automatisés avec les connecteurs Dastra

Dastra propose plusieurs types de connecteurs prêts à l’emploi (questionnaires, registres, politiques, etc.), ainsi qu’un connecteur générique. Ces connecteurs sont utilisés directement dans les **tests automatisés** du module Compliance.

<figure><img src="../../../.gitbook/assets/image (494).png" alt=""><figcaption></figcaption></figure>

En complément des tests manuels, Dastra permet de configurer des **tests automatisés** à l’aide de **connecteurs**.

Un test automatisé s’appuie sur un connecteur Dastra pour :

* interroger directement des éléments de l’espace de travail
* collecter automatiquement des preuves
* vérifier la conformité selon des critères définis

#### Exemples de connecteurs

Les connecteurs peuvent notamment permettre de :

* collecter un **registre des systèmes d’IA**
* vérifier la **présence et la mise à jour de documents** (ex. documentation des SIA)
* interroger des registres (actifs, incidents, traitements de données)
* analyser des questionnaires ou politiques

📌 Exemple :\
Un test automatisé peut vérifier que chaque système d’IA dispose d’une documentation conforme et à jour, sans intervention manuelle.



### Ajout d'un connecteur personnalisé

En complément des connecteurs standards, Dastra permet de créer des **connecteurs personnalisés** afin d’automatiser la collecte de preuves dans les tests de conformité.



<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Un connecteur personnalisé permet :

* d’exécuter une requête technique (ex. requête HTTP),
* d’interroger une source interne ou externe,
* de collecter automatiquement des éléments factuels,
* de produire des preuves exploitables dans les audits.

Le connecteur devient ainsi une **source de preuve récurrente et traçable**.

#### Requête HTTP

Le connecteur **Requête HTTP** permet d’interroger n’importe quelle API ou endpoint exposé.

Il est particulièrement adapté pour :

* interroger des outils tiers,
* vérifier l’existence ou l’état d’une ressource,
* automatiser des contrôles techniques ou documentaires.

### Configuration d’un connecteur personnalisé

Lors de la création d’un connecteur HTTP, les paramètres suivants peuvent être définis :

#### Fréquence du test

* Détermine la périodicité d’exécution du test (ex. mensuelle).
* Adaptée aux contrôles récurrents.

#### URL (obligatoire)

* Endpoint à interroger.
* Peut correspondre à une API interne ou externe.

#### Méthode HTTP (optionnelle)

* GET, POST, etc.
* À sélectionner selon le type d’interrogation.

#### En-têtes HTTP (optionnel)

* Permet notamment de gérer l’authentification (tokens, clés API, headers personnalisés).

#### Corps de requête (optionnel)

* Utile pour les requêtes POST ou les appels nécessitant un payload spécifique.

### Avantages des tests automatisés

Les tests automatisés permettent :

* une **collecte continue des preuves**
* une réduction de la charge opérationnelle
* une meilleure fiabilité des contrôles
* une détection plus rapide des écarts

Ils sont particulièrement adaptés aux contrôles récurrents ou structurés.

***

### Complémentarité des approches

Dastra permet de combiner :

* des **tests manuels** pour les contrôles nécessitant analyse ou jugement humain
* des **tests automatisés** pour les vérifications objectives et répétitives

👉 Cette complémentarité offre un équilibre entre rigueur, efficacité et pragmatisme.
