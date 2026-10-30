---
description: Apprenez ce que sont les durées de conservation.
---

# Durées de conservation

## Définition

Les **durées de conservation** font partie des principes fondamentaux de la protection des données.\
Elles découlent du principe de **limitation de la conservation** (article 5.1.e RGPD) et participent au **droit à l’oubli**.

Articles clés :

* **article 5 du RGPD** (limitation de la conservation) ;
* **article 30** (documentation dans le registre) ;
* **articles 13 et 14** (information des personnes).

Concrètement, vous devez déterminer pour chaque traitement :

* une **durée fixe** (ou un ensemble de durées par phase),
* et/ou un **critère objectif** permettant de la calculer (ex. « +3 ans après le dernier contact actif »).

***

## Le cycle de vie de la donnée

La conservation s’organise en **phases successives**. C’est ce cycle qui détermine vos règles.

| Phase                            | Finalité                    | Accès                     | Exemple de durée                |
| -------------------------------- | --------------------------- | ------------------------- | ------------------------------- |
| **Usage courant**                | Exploitation opérationnelle | Étendu (équipe métier)    | Durée du contrat + exécution    |
| **Archivage intermédiaire**      | Preuve / défense d’un droit | Restreint (need-to-know)  | Prescription légale (ex. 5 ans) |
| **Archivage définitif** (public) | Intérêt historique          | Très restreint            | Versement / tri par SIAF        |
| **Anonymisation**                | Statistiques / recherche    | Données non identifiantes | Illimitée si irréversible       |
| **Suppression**                  | Fin du cycle                | Sans objet                | Au terme des phases             |

{% hint style="info" %}
Le [guide de la CNIL sur les durées de conservation](https://www.cnil.fr/sites/default/files/atoms/files/guide_durees_de_conservation.pdf) détaille : registre, document de référence, procédures d’archivage/d’élimination, instructions aux sous-traitants, etc.
{% endhint %}

***

## Comment les déterminer (méthode)

1. **Clarifier la finalité**\
   → que faites-vous réellement des données ? À quoi servent-elles ?
2. **Cartographier les phases**\
   → usage courant → archivage intermédiaire → anonymisation/suppression
3. **Identifier les bases juridiques et références**\
   → lois & règlements sectoriels, délibérations CNIL, référentiels, **SIAF** (public), pratiques métier
4. **Fixer une règle claire**\
   → « **X ans après \[événement]**, puis **archivage Y ans**, puis **suppression** »\
   → ou « **tant que…**, puis **Z ans après** / **critère** »
5. **Organiser la mise en œuvre**\
   → purge **automatique** ou **pilotée**, journalisation, preuves d’exécution
6. **Informer et documenter**\
   → notice d’information (Art. 13–14), registre (Art. 30), politique interne

{% hint style="info" %}
S’il n’existe **aucune référence claire**, choisissez une durée **proportionnée à la finalité** et documentez l’analyse (accountability).
{% endhint %}

***

## Exemples de règles (à adapter)

| Contexte          | Données                           | Règle synthétique                                                 |
| ----------------- | --------------------------------- | ----------------------------------------------------------------- |
| Prospects B2B     | Identité, contact, trace d’opt-in | **3 ans** après dernier contact actif, puis **suppression**       |
| RH, candidats     | CV, lettres, entretiens           | **2 ans** après dernier contact avec le candidat, sauf opposition |
| Clients           | Contrat, facturation              | Contrat + **5 ans** (preuve), puis **archivage**/**suppression**  |
| Vidéosurveillance | Images                            | **30 jours max**, sauf incident (procédure probatoire)            |
| Cookies           | Identifiants, préférences         | Durée conforme à la bannière de cookies et à la **preuve du consentement**      |

> Ces valeurs varient selon les textes applicables, votre secteur et vos risques : **documentez vos choix**.

***

## Acteurs à impliquer

* **Métier porteur du traitement** : besoin opérationnel, événements déclencheurs
* **DPO / Juridique** : conformité, textes applicables, équilibre droits/libertés
* **Archives / SIAF (public)** : DUA, tri, versements, sort final
* **RSSI / IT** : purge, anonymisation, restriction d’accès, journaux
* **Sous-traitants** : exécution conforme aux **instructions écrites**

***

## Contrôler l’application (audits)

* Vérifier périodiquement : pertinence des durées, exécution des purges, accès en archivage, anonymisation
* Tracer les opérations : bordereaux d’élimination, rapports de purge, logs
* Revoir à chaque **évolution de finalité, base légale, prestataire**…

***

## Mettre en œuvre dans Dastra

### 1) Dans le **registre**

* Renseignez **une règle lisible** par jeu de données :\
  « _3 ans après dernier contact actif (prospect), puis suppression_ »
* Ajoutez **le critère déclencheur** (ex. « date de dernière activité CRM », « fin de contrat »)
* Liez **les références** (texte légal, référentiel interne)

### 2) **Automatiser/piloter** la purge

* Planifiez des **tâches** (revues, purges, extractions de preuves)
* Utilisez les **règles de workflow** et les **revues régulières** pour les échéances

### 3) **Preuves**

* Déposez bordereaux d’élimination, comptes rendus de purge, scripts, tickets d’exécution dans la section **Documentation** du traitement

***

## Archivage intermédiaire & sécurité

* Restreindre l’accès (RBAC, cloisonnement)
* Journaliser les consultations
* Séparer logiquement (coffre/zone d’archive)
* Chiffrer quand c’est pertinent
* Prévoir la **réversibilité** chez les sous-traitants

***

## Anonymisation vs pseudonymisation

* **Anonymisation** : irréversible → **hors RGPD** si véritablement non ré-identifiable
* **Pseudonymisation** : réversible avec clé → **toujours donnée personnelle**\
  → Documentez la méthode, testez la **ré-identifiabilité**, tenez compte des **données auxiliaires**.

***

## IA & durées de conservation

Pour les **systèmes d’IA**, définissez des durées distinctes pour :

* **Entraînement** (datasets, versions),
* **Validation / test**,
* **Logs d’inférence** (traçabilité, transparence),
* **Jeux d’évaluation** (biais, robustesse).

Liez ces durées à votre **registre des systèmes d’IA** pour assurer la cohérence **RGPD / AI Act**.

***

## Références utiles

* **CNIL** : guide sur les durées de conservation (documentation, preuves, archivage)
* **SIAF** : tableau de gestion (secteur public)
* Référentiels sectoriels, codes de conduite, conventions collectives

***

## Ressources et suites

{% embed url="https://www.youtube.com/watch?v=BK8A3L9P7T0" %}
Webinar « Durées de conservation : comment les déterminer ? »
{% endembed %}

{% content-ref url="../../features/ropa/activity/datasets.md" %}
[Données et conservation](../../features/ropa/activity/datasets.md)
{% endcontent-ref %}

{% content-ref url="../../features/tasks/README.md" %}
[Planification](../../features/tasks/README.md)
{% endcontent-ref %}

***

{% hint style="success" %}
**Bon réflexe :** écrivez des règles _actionnables_ (« X ans après \[événement], puis purge ou anonymisation »), testez-les sur un périmètre réduit, puis généralisez.\
Dastra vous aide à **documenter**, **planifier** et **prouver** l’exécution.
{% endhint %}
