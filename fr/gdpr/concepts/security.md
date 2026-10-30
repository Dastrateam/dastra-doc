---
description: Découvrez les nouveautés en termes de sécurité avec le RGPD.
---

# Mesures de sécurité

Le RGPD (article 32) impose aux responsables de traitement et sous-traitants de **garantir la sécurité des données personnelles** par des **mesures techniques et organisationnelles appropriées**.\
Ces mesures doivent être **proportionnées aux risques** présentés par le traitement, à la **nature des données** et aux **finalités poursuivies**.

> Objectif : assurer la **confidentialité**, l’**intégrité**, la **disponibilité** et la **résilience** des systèmes et des données.

***

## Une approche fondée sur le risque

Avant de choisir des mesures, il faut :

1. Identifier les **éléments à protéger** (données, systèmes, flux).
2. Évaluer les **menaces et vulnérabilités** (erreur humaine, attaque, panne, etc.).
3. Déterminer les **impacts potentiels** (perte, divulgation, altération…).
4. Choisir des **mesures adaptées** pour réduire ces risques à un niveau acceptable.

> Le RGPD ne fixe pas de liste figée de mesures : il impose des mesures **appropriées au risque** (article 32), compte tenu de l’état des connaissances, des coûts de mise en œuvre et du contexte du traitement.\
> Chaque organisation doit **adapter** son dispositif à son contexte et pouvoir **le démontrer**.

***

## Catégories de mesures de sécurité

### Mesures techniques

Agissent directement sur les systèmes d’information.

| Domaine                              | Exemples                                                                    |
| ------------------------------------ | --------------------------------------------------------------------------- |
| **Contrôle d’accès**                 | Authentification forte (MFA), gestion des habilitations, journalisation     |
| **Chiffrement**                      | Données au repos et en transit, certificats TLS, clés gérées et renouvelées |
| **Pseudonymisation / anonymisation** | Séparation logique, hachage, tokens                                         |
| **Sauvegardes et résilience**        | Backups réguliers, tests de restauration, redondance                        |
| **Sécurisation applicative**         | Tests de pénétration, correctifs, durcissement des serveurs                 |
| **Surveillance**                     | SIEM, alertes en cas d’accès anormal, détection d’incidents                 |

***

### Mesures organisationnelles

Structurent la gouvernance et les comportements internes.

| Domaine                          | Exemples                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------- |
| **Politique de sécurité**        | Charte informatique, gouvernance SSI, plan de gestion des incidents              |
| **Formation et sensibilisation** | Campagnes internes, modules e-learning, simulations phishing                     |
| **Gestion des tiers**            | Clauses contractuelles, audits de sous-traitants, évaluations régulières         |
| **Procédures internes**          | Processus d’habilitation, plan de reprise d’activité (PRA/PCA), revue périodique |

***

### Mesures physiques

Protègent les locaux, équipements et supports matériels.

| Domaine                   | Exemples                                                        |
| ------------------------- | --------------------------------------------------------------- |
| **Accès physique**        | Contrôle badge, caméras, zones à accès restreint                |
| **Protection matérielle** | Coffres, racks sécurisés, alimentation de secours               |
| **Destruction sécurisée** | Broyage, effacement certifié, gestion des déchets informatiques |

***

## Cycle de gestion de la sécurité

1. **Identifier** : données, systèmes, vulnérabilités, menaces.
2. **Évaluer** : risques et impacts potentiels (analyse de risque).
3. **Protéger** : définir et appliquer les mesures de sécurité.
4. **Surveiller** : détecter les incidents, auditer les contrôles.
5. **Améliorer** : corriger, renforcer, documenter les actions.

***

## Les mesures dans Dastra

Dans Dastra, vous pouvez documenter, évaluer et suivre les mesures de sécurité dans le cadre de la gouvernance RGPD et de l’AI Act :

* Décrivez vos mesures dans le référentiel **Mesures** et rattachez-les aux traitements, aux actifs et aux violations de données.
* Évaluez les risques avec le module de gestion des risques.
* Planifiez des actions correctives avec les tâches et suivez leur avancement.
* Conservez les preuves de conformité (politiques, audits, preuves d’exécution).
* Suivez le niveau de conformité de votre organisation à des référentiels comme ISO 27001, dans le module **Conformité**.

***

## Ressources utiles

* [CNIL : guide de la sécurité des données personnelles](https://www.cnil.fr/fr/principes-cles/guide-de-la-securite-des-donnees-personnelles)
* [ISO/IEC 27001 : systèmes de management de la sécurité de l’information](https://www.iso.org/fr/isoiec-27001-information-security.html)
* [ANSSI : recommandations de sécurité informatique](https://www.ssi.gouv.fr/)

***

{% hint style="success" %}
**Bon réflexe :** Adoptez une logique de **sécurité intégrée et vivante** : chaque nouveau projet, sous-traitant ou outil doit faire l’objet d’une évaluation de risque et d’une mise à jour des mesures.
{% endhint %}
