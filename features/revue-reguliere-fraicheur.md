# Revue régulière (fraicheur)

### Qu'est ce que l'indicateur de fraîcheur ?

La fraicheur est un indicateur sur le dernier passage en revue d'un élément dans Dastra. Il peut s'agir d'un traitement, d'un objet de votre référentiel ou même d'un contrat. En activant cette fonctionnalité vous allez définir une date de revue future de l'objet, et la fraicheur se dégradera au fur et à mesure que cette date approchera. Cette fonctionnalité est un moyen simple et ludique pour garantir que vous révisez régulièrement les informations renseignées dans l'application.

<figure><img src="../.gitbook/assets/image (275).png" alt=""><figcaption><p>Schéma de fonctionnement de l'indicateur de fraicheur</p></figcaption></figure>

### Comment activer l'indicateur de fraicheur ?

Pour activer la fraicheur d'un type d'objet, rendez vous dans les réglages de votre espace de travail et sélectionnez l'onglet _Revues régulières_.

<figure><img src="../.gitbook/assets/image (344).png" alt=""><figcaption><p>Le menu de configuration de la revue régulière (fraicheur)</p></figcaption></figure>

Vous pouvez depuis ce menu activer la fraicheur pour les différents objets disposant de la fonctionnalité en cliquant sur le menu déroulant de sélection de l'objet.

<figure><img src="../.gitbook/assets/image (345).png" alt=""><figcaption><p>La liste des objets pour lesquels vous pouvez activer la fraicheur</p></figcaption></figure>

Cochez l'option activer la revue régulière de l'élément et paramétrez **l'intervalle de temps souhaité entre chaque revue**.

&#x20;La fraicheur d'un élément correspond au nombre de jours entre la dernière date à laquelle l'élément a été marqué comme frais et sa date de revue future.

La date de revue est une date dans le futur calculée à partir de la dernière date à laquelle l'élément a été marqué comme frais à laquelle nous ajoutons **l'intervalle de temps souhaité entre chaque revue**.&#x20;

Veuillez noter que cet intervalle de péremption sera le même pour tous les éléments du même type pour lesquels la revue est active.&#x20;

### Désactiver l'option fraicheur&#x20;

Pour désactiver l'option, il vous suffit de décocher la case _Activer la revue régulière de l'élément_ depuis la section Revues régulières des réglages de votre espace de travail.

### Visualisation de l'indicateur de fraicheur

Tous les objets disposant de la fonctionnalité disposent d'une colonne fraicheur que vous pouvez ajouter aux tableaux récapitulatifs. Cette colonne vous permettra de suivre l'état de fraicheur de chaque élément.&#x20;

Veuillez noter que la fraicheur ne s'affiche que pour les **éléments publiés.**

<figure><img src="../.gitbook/assets/image (349).png" alt=""><figcaption><p>La colonne fraicheur </p></figcaption></figure>

Vous retrouvez également cet indicateur dans le menu de raccourcis des éléments.

<figure><img src="../.gitbook/assets/image (350).png" alt=""><figcaption><p>l'indicateur de fraicheur dans le menu de raccourcis d'un élément</p></figcaption></figure>

### Visualisation de l'indicateur de fraicheur dans le cas spécifique du registre des traitements

L'affichage de la fraicheur dans le cadre d'un traitement de données est un peu plus poussé que sur les autres éléments disposant de la fonctionnalité.

Vous retrouverez l'indicateur de fraicheur en haut à droite de votre fiche de traitement (dans la mesure ou le traitement a été publié et marqué comme étant frais au moins une fois)

Cet indicateur est composé d'un label prenant les valeurs "Frais", "E en attente" et "Dépassé", d'une couleur (respectivement vert, jaune, rouge), d'une barre de progression diminuant à mesure que la date de péremption approche, d'un bouton pour marquer le traitement comme frais et du nombre de jours restants ou de retard par rapport à la date de péremption.&#x20;

<figure><img src="../.gitbook/assets/image (270).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/image (269).png" alt=""><figcaption><p>En vue mobile, vous retrouvez également cet indicateur dans la barre de navigation en haut de votre fiche de traitement</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (271).png" alt=""><figcaption><p>Exemple de traitement périmé</p></figcaption></figure>

### Règles d'affichage des statuts de revue&#x20;

Il y a 3 statuts possibles s'agissant de la fraîcheur d'un traitement : frais, en attente ou dépassé. Par défaut, les règles d'affichage suivantes s'appliquent :&#x20;

<table><thead><tr><th width="167">Statut de revue</th><th>Règle d'affichage</th></tr></thead><tbody><tr><td>Frais (couleur verte)</td><td>S'affiche lorsque la différence (en jours) entre la date de revue future et la date du jour est supérieure à 10% de l'intervalle de revue (en jours) entre la date de revue future et la précédente date de revue</td></tr><tr><td>En attente (couleur orange)</td><td>S'affiche lorsque la différence (en jours) entre la date de revue future et la date du jour est inférieure ou égale à 10% de l'intervalle de revue (en jours) entre la date de revue future et la précédente date de revue</td></tr><tr><td>Dépassé (couleur rouge)</td><td>S'affiche lorsque la date de future revue est dépassée par rapport à la date d'aujourd'hui</td></tr></tbody></table>



{% hint style="info" %}
**Exemple  :**&#x20;

Sur la base des hypothèses suivantes :

* date de revue précédente : 24 Juin 2024
* date de revue future : 24 Juin 2025&#x20;
* Intervalle de revue = 1 an (365 jours)

Alors la date de passage du statut "Frais" à "En attente" sera le **19 mai 2025**, soit 36,5 jours avant le 24 Juin 2025.
{% endhint %}





### Rafraichir un élément

Vous pouvez à tout moment, et sans forcément attendre la date de prochaine revue, décider de passer en revue l'élément. Pour ce faire, cliquez sur la cellule de la colonne fraicheur d'un élément lorsque vous êtes dans une vue tableau. Il faut bien sur que la fonctionnalité soit active pour cet élément et que vous affichiez la colonne en question.

<figure><img src="../.gitbook/assets/image (346).png" alt=""><figcaption><p>Accéder à la fenêtre de revue régulière de l'élément</p></figcaption></figure>

Vous pouvez également y accéder directement depuis la vue d'édition de l'élément que vous souhaitez passer en revue en cliquant sur l'icône fraicheur située dans le menu de raccourcis.

<figure><img src="../.gitbook/assets/image (347).png" alt=""><figcaption><p>L'icône fraicheur à cliquer pour accéder à la revue d'un élément.</p></figcaption></figure>

Vous accéderez alors à la fenêtre de passage en revue de l'élément. A noter qu'il est possible de consulter les anciennes revues depuis cette fenêtre.

<figure><img src="../.gitbook/assets/image (348).png" alt=""><figcaption><p>La fenêtre de passage en revue d'un élément</p></figcaption></figure>

En passant un élément en revue, vous relancerez un cycle de fraicheur à partir de la date du jour et ce jusqu'à la prochaine date de revue. La date de revue est calculée par défaut en fonction du réglage de l'intervalle de revue de l'élément (voir plus haut). Vous pouvez décider d'ignorer cette date par défaut et appliquer une date de péremption spécifique à cet élément en cochant l'option "Changer la date de prochaine revue" et en sélectionnant une nouvelle date (la date de prochaine revue doit au minimum être fixé à J+1)

### Notifications

Le créateur de l'élément, ainsi que les utilisateurs associés à l'élément (les propriétaires par exemple dans le cas des traitements), lors du passage à l'état périmé d'un élément, seront notifiés par email pour leur rappeler que l'élément n'a pas été révisé depuis longtemps et qu'il est temps de le rafraichir.
