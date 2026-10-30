---
description: Apprenez ce qu'est une donnée personnelle.
---

# Donnée personnelle

## Définition d’une donnée personnelle

Selon l’[article 4 du RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj), une **donnée personnelle** est _toute information se rapportant à une personne physique identifiée ou identifiable_.\
Autrement dit, il s’agit de **toute information qui permet d’identifier directement ou indirectement un individu.**

Une personne physique peut être identifiée :

* **Directement** : par un nom, un prénom, une photo, un numéro d’identification, etc.
* **Indirectement** : par le croisement d’informations telles qu’un numéro de téléphone, une adresse e-mail, une plaque d’immatriculation, une voix ou une image.

L’identification peut donc se faire :

* à partir **d’une seule donnée** (ex. : numéro de sécurité sociale) ;
* ou par **le croisement de plusieurs éléments** (ex. : une femme née à telle date, habitant telle ville, employée dans telle entreprise).

{% hint style="info" %}
Les coordonnées d’une entreprise ne sont pas, en principe, des données personnelles (exemple : **contact@entreprise.fr**).\
En revanche, une adresse e-mail nominative du type **prenom.nom@entreprise.fr** en est bien une.
{% endhint %}

***

## Catégories de données personnelles

Les **catégories de données personnelles** regroupent les informations selon leur nature ou leur usage.

Quelques exemples courants :

* **Identité** : nom, prénom, date de naissance, photo, signature
* **Vie personnelle** : adresse, situation familiale, loisirs
* **Vie professionnelle** : CV, fonction, évaluations, salaire
* **Situation économique ou financière** : revenus, comptes bancaires, transactions
* **Connexion et usage** : adresse IP, identifiant de connexion, logs, cookies
* **Localisation** : coordonnées GPS, trajets, historiques de déplacement

> Ces catégories sont essentielles pour **structurer votre registre de traitements** et identifier les risques associés à chaque type de donnée.

***

## Les données dites « sensibles »

Certaines données personnelles bénéficient d’une protection renforcée : ce sont les **données sensibles**, car leur utilisation peut avoir un impact fort sur les droits et libertés des personnes.

Elles révèlent notamment :

* L’**origine raciale ou ethnique** supposée,
* Les **opinions politiques**,
* Les **convictions religieuses ou philosophiques**,
* L’**appartenance syndicale**,
* Les **données génétiques** et les **données biométriques** traitées pour identifier une personne de manière unique,
* Les **données de santé**,
* L’**orientation sexuelle** ou la **vie sexuelle** d’une personne.

{% hint style="info" %}
Exemples : empreintes digitales utilisées pour identifier une personne (biométrie), dossier médical, ADN, appartenance religieuse.
{% endhint %}

***

## Le principe d’interdiction et les exceptions

Le **traitement des données sensibles est interdit**, sauf exceptions prévues par le RGPD (article 9).\
Ces exceptions incluent notamment :

* Le **consentement explicite** de la personne concernée,
* Les données **manifestement rendues publiques** par la personne,
* Les traitements **nécessaires à la sauvegarde de la vie humaine**,
* Les traitements **nécessaires pour des motifs d’intérêt public important**, sur la base du droit de l’Union ou d’un État membre,
* Les traitements effectués par des **associations** à but politique, religieux, philosophique ou syndical pour leurs membres.

> Ces cas doivent toujours être **documentés dans le registre** et assortis de **mesures de sécurité adaptées.**

***

## Données personnelles et intelligence artificielle

Les **systèmes d’intelligence artificielle** utilisent souvent des données personnelles pour l’entraînement, le test ou l’exploitation des modèles.\
L’**AI Act** complète donc le RGPD en imposant une **traçabilité et une documentation** des données utilisées par les systèmes d’IA.

Exemples :

* Données d’entraînement contenant des images de visages (biométrie) ;
* Données textuelles issues de communications privées ;
* Données comportementales issues de capteurs ou de navigation.

Dans Dastra, chaque système d’IA est relié aux **traitements de données** qu’il utilise, au sein du **registre des systèmes d’IA**, pour assurer la conformité croisée RGPD / AI Act.

{% content-ref url="../../features/ai-systems/README.md" %}
[systemes-dia](../../features/ai-systems/README.md)
{% endcontent-ref %}

***

## Pour aller plus loin

Explorez dans Dastra les fonctionnalités associées à la gestion des données personnelles :

{% content-ref url="../../features/ropa/activity/datasets.md" %}
[Jeux de données et durées de conservation](../../features/ropa/activity/datasets.md)
{% endcontent-ref %}

***

{% hint style="success" %}
**Bon réflexe :**\
Identifiez, classez et documentez vos catégories de données dès la phase de conception de vos traitements ou de vos systèmes d’IA.\
Cela facilitera la tenue de votre registre et le respect du principe de _privacy by design_.
{% endhint %}
