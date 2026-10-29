# Règles de purge des demandes

{% hint style="info" %}
Vous devez disposer des **droits d’administrateur** sur l'espace de travail pour accéder à cette fonctionnalité.
{% endhint %}

Vous pouvez **automatiser la purge des demandes mises à la corbeille** pour respecter vos politiques internes de conservation, et notamment le principe de limitation de la conservation prévu par le RGPD.

Vous définissez :

* le **périmètre** des demandes concernées par la purge,
* le **mode de traitement** (suppression ou anonymisation),
* la **durée maximale de conservation** avant le déclenchement automatique.

Pour la configurer, ouvrez les paramètres de l'espace de travail, section **Processus**, puis **Demandes d'exercice de droit** et la section **Règles de purge**.

***

## Demandes concernées

La purge s’applique **uniquement aux demandes présentes dans la corbeille**. Les demandes en cours de traitement, clôturées ou archivées ne sont pas concernées.

Chaque nuit, Dastra vérifie les demandes d'après leur **date de mise à la corbeille**. Une demande qui dépasse la durée maximale définie (par exemple 180 jours) est purgée. Sont concernées :

* les demandes placées dans la corbeille depuis plus longtemps que la durée configurée ;
* tous les types de demandes (accès, suppression, opposition, etc.) ;
* toutes les demandes, quelle que soit leur origine (portail, API, import).

***

## Modes de purge

Dans **Sélectionnez un mode de purge**, choisissez l'un des deux modes.

### Suppression des demandes

Les demandes concernées sont **définitivement supprimées** de Dastra. Cette action est **irréversible**.

* Les données personnelles et le contenu des échanges sont supprimés.
* Les pièces jointes et fichiers associés sont effacés.
* Les journaux d’audit conservent uniquement des métadonnées techniques (horodatage, utilisateur, opération).

### Anonymisation des demandes

Les demandes restent visibles dans Dastra, mais leurs **données personnelles** sont remplacées par des valeurs aléatoires sans lien avec le demandeur. Ce mode conserve une trace statistique non identifiable pour vos rapports et indicateurs.

* Les champs contenant des données personnelles (nom, prénom, e-mail, adresse, ville, code postal) sont remplacés par des valeurs générées, et le texte de la demande est remplacé.
* Les messages échangés et les pièces jointes sont supprimés.
* Les métadonnées non identifiantes (type de demande, statut, dates) sont conservées pour le reporting.
* Les journaux d'activité associés sont purgés.

<figure><img src="../../../.gitbook/assets/requests-purge-1.png" alt="La section Règles de purge avec l'option d'activation, le choix du mode et la durée maximale de conservation"><figcaption><p>La configuration des règles de purge</p></figcaption></figure>

***

## Durée avant purge

Dans **Durée maximale de conservation dans la corbeille (en jours)**, indiquez l’âge maximum d’une demande dans la corbeille avant sa purge, par exemple 180 jours. Cette durée est calculée à partir de la **date de mise à la corbeille**.

Chaque nuit, vers 2 h 30 (UTC), Dastra récupère les demandes concernées et exécute la purge selon le mode sélectionné.

***

## Exemple de configuration

* **Mode de purge** : Suppression des demandes
* **Durée maximale** : 180 jours (6 mois)

Chaque nuit, toutes les demandes mises à la corbeille depuis plus de 180 jours sont automatiquement supprimées.

***

## Bonnes pratiques

* Définissez une durée cohérente avec votre politique interne de conservation des demandes (par exemple 5 ans, soit 1 825 jours).
* Choisissez la suppression pour un effacement complet.
* Choisissez l'anonymisation si vous souhaitez conserver des statistiques d’activité.
* Vérifiez que **Activer la purge automatique des demandes mises à la corbeille** est activée : sans cela, aucune purge n'a lieu.
