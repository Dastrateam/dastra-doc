---
description: >-
  Questions fréquentes sur l'assistant IA de Dastra : confidentialité,
  fiabilité, configuration et AI Act.
---

# Foire aux questions

## Confidentialité et données

**Mes données sont-elles utilisées pour entraîner les modèles d'IA ?**

Non. Les modèles utilisés par Dastra sont pré-entraînés et hébergés sur Microsoft Azure. Vos données ne sont jamais utilisées pour entraîner, affiner ou améliorer les modèles de base, que ce soit par Microsoft, OpenAI, Mistral ou tout autre tiers. Cette garantie est contractuelle.

***

**Les données de mon espace de travail sont-elles transmises au modèle à mon insu ?**

Non. Dastra ne transmet que les informations strictement nécessaires à la génération demandée : le texte que vous saisissez, et le cas échéant les champs de l'objet sur lequel vous travaillez (traitement, système d'IA, demande de droit, etc.). Les autres enregistrements de votre espace de travail, vos identifiants et les métadonnées de session ne sont jamais inclus. Seule exception : lorsque vous activez l'option **Utiliser des éléments existants** à la génération d'un traitement, les libellés des mesures de sécurité, actifs et champs de données existants sont transmis afin que l'assistant les réutilise. Pour le détail par fonctionnalité, consultez la page [Comment ça marche ?](how-it-works.md).

***

**Où sont hébergés les modèles d'IA utilisés par Dastra ?**

Pour les familles OpenAI, Mistral et Open source, les modèles sont hébergés sur l'infrastructure Microsoft Azure en France. Vos données ne transitent pas vers les serveurs propres d'OpenAI ou de Mistral. Dastra utilise exclusivement les services managés Azure.

Si vous configurez un **fournisseur d'IA personnalisé** avec votre propre clé d'API, l'hébergement dépend du fournisseur que vous choisissez.

***

**Mes prompts sont-ils conservés après la génération ?**

Les modèles Azure sont sans état (_stateless_) : les prompts et résultats ne sont pas stockés dans le modèle entre deux requêtes. Ils ne sont pas non plus journalisés à des fins de réutilisation commerciale.

**Exception :** Azure maintient un mécanisme automatisé de détection des abus. Si un contenu est signalé, un échantillon peut être conservé temporairement dans un espace isolé par client, aux fins de revue. Pour les ressources déployées dans l'EEE (ce qui est le cas de Dastra), les réviseurs humains éventuels sont également situés dans l'EEE. Cette conservation reste exceptionnelle.

***

**Qui peut voir les appels effectués à l'assistant IA dans mon organisation ?**

Les propriétaires de l'organisation ont accès aux journaux d'utilisation de l'IA (90 jours d'historique) dans **Paramètres de l'organisation** > **Assistant IA**, carte **Utilisation de l'IA**, onglet **Logs (90 jours)**. Ils indiquent la date, le statut, le type d'opération, le nom du modèle, les crédits consommés, la durée et l'utilisateur ayant déclenché la génération. Le contenu des prompts et des réponses n'y est pas affiché.

***

**L'assistant IA est-il couvert par le DPA (Data Processing Agreement) de Dastra ?**

Oui. L'utilisation de l'assistant IA s'inscrit dans le cadre contractuel existant entre votre organisation et Dastra. Microsoft Azure est sous-traitant de rang 2, lié par les engagements contractuels d'Azure en matière de protection des données. Pour plus de détails, référez-vous à votre DPA Dastra ou contactez notre équipe.

***

## Qualité et fiabilité

**Peut-on faire confiance aux résultats générés par l'IA ?**

Les résultats générés sont des propositions de départ, pas des réponses définitives. Ils accélèrent votre travail de documentation mais ne remplacent pas le jugement d'un expert. Tout contenu généré doit être relu et validé par une personne qualifiée avant tout usage, en particulier pour les analyses de conformité, les notices d'information et les réponses à des demandes d'exercice de droits.

***

**Qu'est-ce qu'une fonctionnalité en bêta ?**

Certaines fonctionnalités IA sont publiées en version bêta : elles sont opérationnelles mais continuent d'être affinées. Les résultats peuvent être moins constants que dans les fonctionnalités stables et doivent être traités avec une vigilance accrue.

Sont actuellement en bêta : l'analyse de conformité des traitements et l'analyse de conformité des systèmes d'IA.

***

**L'IA peut-elle se tromper sur des questions juridiques ?**

Oui. L'assistant IA n'est pas un juriste. Les contenus générés, analyses de conformité, notices, évaluations de risques, sont des aides à la réflexion basées sur les informations enregistrées dans votre espace de travail. Ils ne constituent pas un avis juridique et ne sauraient remplacer l'expertise d'un DPO ou d'un conseil spécialisé.

***

## Configuration et accès

**Comment choisir le modèle d'IA utilisé ?**

Le propriétaire de l'organisation ouvre **Paramètres de l'organisation** > **Assistant IA** et sélectionne la **Famille de modèles d'IA** : OpenAI (par défaut), Mistral, Open source ou **Modèles AI personnalisés**. Pour chaque famille, trois niveaux de modèle sont utilisés automatiquement selon la complexité de la tâche (Rapide, Avancé, Contexte étendu).

***

**Puis-je connecter mon propre fournisseur d'IA ?**

Oui, avec la famille **Modèles AI personnalisés** (Custom AI provider). Tout fournisseur compatible avec le standard OpenAI API peut être connecté : OpenAI, Anthropic (Claude), Google (Gemini), Mistral, Azure AI Foundry, ou un LLM auto-hébergé. Configurez vos identifiants dans **Paramètres de l'organisation** > **Assistant IA**, bloc **Identifiants de fournisseur d'IA**.

{% hint style="warning" %}
Avec un fournisseur d'IA personnalisé, les garanties Azure décrites dans cette documentation ne s'appliquent plus. Les données sont soumises à la politique de votre fournisseur.
{% endhint %}

***

**Puis-je désactiver l'assistant IA pour mon organisation ?**

L'application ne propose pas d'interrupteur pour désactiver l'assistant IA : sa disponibilité dépend de l'offre de votre organisation. Les fonctionnalités IA sont activées module par module (traitements et référentiels, conformité, risques, violations, questionnaires, contrats, exercices de droits, analyses). Dans un module que votre offre n'inclut pas, les boutons IA sont grisés. Pour modifier ce périmètre, contactez notre équipe.

Un seul réglage est à la main des administrateurs : l'**Analyse IA automatique des preuves**, activée par défaut, que vous désactivez par espace de travail dans **Réglages espace de travail** > **Conformité**.

***

**L'assistant IA est-il disponible sur tous les plans Dastra ?**

Non. L'assistant IA, chacune de ses fonctionnalités par module, les agents IA et le serveur MCP font l'objet d'options de l'offre. Contactez notre équipe pour connaître le périmètre de votre offre.

***

**Qu'est-ce que les crédits IA ?**

Les crédits IA sont l'unité de mesure de la consommation de l'assistant IA au sein de votre organisation. Chaque appel à une fonctionnalité IA consomme un certain nombre de crédits, variable selon le modèle sollicité (Rapide, Avancé ou Contexte étendu) et la quantité de données traitées.

Les propriétaires de l'organisation peuvent consulter la consommation en cours et le solde restant dans **Paramètres de l'organisation** > **Assistant IA**, carte **Utilisation** ([accès direct](https://app.dastra.eu/general-settings/ai)).

***

**Que se passe-t-il si mon organisation atteint son quota de crédits ?**

Lorsque le quota est atteint, les fonctionnalités IA sont temporairement suspendues jusqu'au prochain renouvellement. Votre espace de travail et vos données restent entièrement accessibles ; seule la génération IA est désactivée.

Pour augmenter votre quota ou anticiper un renouvellement, contactez notre équipe.

***

**Le décompte de crédits s'applique-t-il avec un fournisseur d'IA personnalisé ?**

Non. Lorsque votre organisation configure un **fournisseur d'IA personnalisé**, le système de crédits Dastra est désactivé : aucun crédit n'est décompté. La consommation est gérée directement par votre fournisseur selon ses propres conditions de facturation.

***

## Règlement IA (AI Act)

**L'assistant IA de Dastra est-il concerné par l'AI Act ?**

Oui. L'assistant IA de Dastra entre dans la définition d'un système d'IA au sens du Règlement IA (UE 2024/1689). Selon les fonctionnalités utilisées, il relève principalement de la catégorie **risque limité**, ce qui implique des obligations de transparence (art. 50) lorsque le contenu généré est destiné à des personnes physiques.

***

**Dois-je informer les personnes concernées que j'utilise l'IA pour répondre à leurs demandes ?**

Pas au titre d'une obligation stricte, mais c'est fortement recommandé à titre de bonne pratique.

L'article 50(1) du Règlement IA vise les systèmes d'IA **qui interagissent directement** avec des personnes physiques. Dans Dastra, ce n'est pas le cas : c'est un utilisateur humain (DPO, juriste) qui génère le texte, le relit, le valide et l'envoie lui-même à la personne concernée. Il n'y a pas d'interaction directe entre le système d'IA et le destinataire final, donc l'obligation stricte de l'art. 50(1) ne s'applique pas.

{% hint style="info" %}
Les guidelines draft de l'AI Office (publiées en consultation en 2025) confirment explicitement cette interprétation : _"l'interaction directe exclut les interactions humaines indirectes ou médiées \[...] **par exemple si des agents du service client utilisent des outils d'assistance IA pour communiquer avec des personnes physiques** ou si le résultat de l'IA n'est pas mis à la disposition de la personne par le système d'IA lui-même, mais par une autre personne qui diffuse le contenu."_ (Section 3.1.1). Le cas d'usage Dastra correspond exactement à ce schéma.

À noter : les obligations de l'article 50 s'appliquent depuis le **2 août 2026**. La Commission européenne a adopté des lignes directrices définitives en juillet 2026, qui peuvent compléter cette analyse.
{% endhint %}

En revanche, informer la personne concernée qu'une réponse a été assistée par IA reste une **bonne pratique** au titre du principe de loyauté et de transparence du RGPD (art. 5(1)(a)). Dastra ne génère pas automatiquement cette mention : si votre organisation souhaite l'inclure, c'est à vous de l'ajouter avant l'envoi.

***

**Dastra est-il fournisseur ou déployeur au sens de l'AI Act ?**

Les deux, selon le cas d'usage. Lorsque vous utilisez les modèles par défaut (OpenAI, Mistral, Open source via Azure), Dastra est **fournisseur** du système d'IA et votre organisation en est le **déployeur**. Lorsque vous connectez votre propre fournisseur d'IA personnalisé, Dastra agit uniquement comme outil de conformité. Votre organisation assume alors le rôle de fournisseur et/ou déployeur vis-à-vis de son propre modèle.
