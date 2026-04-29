# Foire aux questions

### Confidentialité et données

**Mes données sont-elles utilisées pour entraîner les modèles d'IA ?**

Non. Les modèles utilisés par Dastra sont pré-entraînés et hébergés sur Microsoft Azure. Vos données ne sont jamais utilisées pour entraîner, affiner ou améliorer les modèles de base, que ce soit par Microsoft, OpenAI, Mistral ou tout autre tiers. Cette garantie est contractuelle.

***

**Les données de mon workspace sont-elles transmises au modèle à mon insu ?**

Non. Dastra ne transmet que les informations strictement nécessaires à la génération demandée : le texte que vous saisissez, et le cas échéant les champs de l'objet sur lequel vous travaillez (traitement, système d'IA, demande de droit, etc.). Les autres enregistrements de votre workspace, vos identifiants et les métadonnées de session ne sont jamais inclus. Pour le détail par fonctionnalité, consultez la page Comment ça marche ?.

***

**Où sont hébergés les modèles d'IA utilisés par Dastra ?**

Pour les familles OpenAI, Mistral et Open source, les modèles sont hébergés sur l'infrastructure Microsoft Azure en France. Vos données ne transitent pas vers les serveurs propres d'OpenAI ou de Mistral. Dastra utilise exclusivement les services managés Azure.

Si vous configurez un **Custom AI provider** avec votre propre clé API, l'hébergement dépend du fournisseur que vous choisissez.

***

**Mes prompts sont-ils conservés après la génération ?**

Les modèles Azure sont sans état (_stateless_) : les prompts et résultats ne sont pas stockés dans le modèle entre deux requêtes. Ils ne sont pas non plus journalisés à des fins de réutilisation commerciale.

**Exception :** Azure maintient un mécanisme automatisé de détection des abus. Si un contenu est signalé, un échantillon peut être conservé temporairement dans un espace isolé par client, aux fins de revue. Pour les ressources déployées dans l'EEE (ce qui est le cas de Dastra), les réviseurs humains éventuels sont également situés dans l'EEE. Cette conservation reste exceptionnelle.

***

**Qui peut voir les appels effectués à l'assistant IA dans mon organisation ?**

Les administrateurs de votre workspace ont accès aux **logs d'invocation IA** (90 jours d'historique) depuis **Paramètres > Assistant IA > Logs d'invocation IA**. Ces logs indiquent la date, le statut, le type d'opération, le modèle utilisé, la durée et l'utilisateur ayant déclenché la génération. Le contenu des prompts et des réponses n'y est pas affiché.

***

**L'assistant IA est-il couvert par le DPA (Data Processing Agreement) de Dastra ?**

Oui. L'utilisation de l'assistant IA s'inscrit dans le cadre contractuel existant entre votre organisation et Dastra. Microsoft Azure est sous-traitant de rang 2, lié par les engagements contractuels d'Azure en matière de protection des données. Pour plus de détails, référez-vous à votre DPA Dastra ou contactez notre équipe.

***

### Qualité et fiabilité

**Peut-on faire confiance aux résultats générés par l'IA ?**

Les résultats générés sont des propositions de départ, pas des réponses définitives. Ils accélèrent votre travail de documentation mais ne remplacent pas le jugement d'un expert. Tout contenu généré doit être relu et validé par une personne qualifiée avant tout usage, en particulier pour les analyses de conformité, les notices d'information et les réponses à des demandes d'exercice de droits.

***

**Qu'est-ce qu'une fonctionnalité en bêta ?**

Certaines fonctionnalités IA sont publiées en version bêta : elles sont opérationnelles mais continuent d'être affinées. Les résultats peuvent être moins constants que dans les fonctionnalités stables et doivent être traités avec une vigilance accrue.

Sont actuellement en bêta : l'analyse de conformité des traitements et l'analyse de conformité des systèmes d'IA.

***

**L'IA peut-elle se tromper sur des questions juridiques ?**

Oui. L'assistant IA n'est pas un juriste. Les contenus générés, analyses de conformité, notices, évaluations de risques, sont des aides à la réflexion basées sur les informations enregistrées dans votre workspace. Ils ne constituent pas un avis juridique et ne sauraient remplacer l'expertise d'un DPO ou d'un conseil spécialisé.

***

### Configuration et accès

**Comment choisir le modèle d'IA utilisé ?**

Rendez-vous dans **Paramètres > Assistant IA** pour sélectionner la famille de modèles : OpenAI (par défaut), Mistral, Open source ou un fournisseur personnalisé (Custom AI provider). Pour chaque famille, trois niveaux de modèle sont utilisés automatiquement selon la complexité de la tâche (Fast, Smart, Contexte étendu).

***

**Puis-je connecter mon propre fournisseur d'IA ?**

Oui, via la fonctionnalité **Custom AI provider**. Tout fournisseur compatible avec le standard OpenAI API peut être connecté : OpenAI, Google (Gemini), Mistral, Microsoft Foundry, ou un LLM auto-hébergé. Configurez vos identifiants dans **Paramètres > Assistant IA > Custom AI provider**.

{% hint style="warning" %}
Avec un Custom AI provider, les garanties Azure décrites dans cette documentation ne s'appliquent plus. Les données sont soumises à la politique de votre fournisseur.
{% endhint %}

***

**Puis-je désactiver l'assistant IA pour mon organisation ?**

Oui. Contactez notre équipe support pour désactiver la fonctionnalité au niveau de votre organisation. La désactivation est globale : il n'est pas possible de désactiver uniquement certains prompts tout en gardant les autres actifs.

***

**L'assistant IA est-il disponible sur tous les plans Dastra ?**

Oui, l'assistant IA est disponible sur tous les plans de Dastra. Certaines fonctionnalités avancées peuvent être soumises à des conditions spécifiques. Contactez notre équipe pour toute question sur votre plan.

***

### Règlement IA (AI Act)

**L'assistant IA de Dastra est-il concerné par l'AI Act ?**

Oui. L'assistant IA de Dastra entre dans la définition d'un système d'IA au sens du Règlement IA (UE 2024/1689). Selon les fonctionnalités utilisées, il relève principalement de la catégorie **risque limité**, ce qui implique des obligations de transparence (art. 50) lorsque le contenu généré est destiné à des personnes physiques.

***

**Dois-je informer les personnes concernées que j'utilise l'IA pour répondre à leurs demandes ?**

Oui, dans la plupart des cas. Lorsqu'une réponse à une demande d'exercice de droits est générée par l'assistant IA, la personne concernée doit être informée que le contenu a été produit ou assisté par un système d'IA, sauf si cela est évident au vu du contexte (art. 50 du Règlement IA). Dastra ne génère pas automatiquement cette mention. C'est à votre organisation de l'ajouter avant l'envoi.

***

**Dastra est-il fournisseur ou déployeur au sens de l'AI Act ?**

Les deux, selon le cas d'usage. Lorsque vous utilisez les modèles par défaut (OpenAI, Mistral, Open source via Azure), Dastra est **fournisseur** du système d'IA et votre organisation en est le **déployeur**. Lorsque vous connectez votre propre fournisseur via Custom AI provider, Dastra agit uniquement comme outil de conformité. Votre organisation assume alors le rôle de fournisseur et/ou déployeur vis-à-vis de son propre modèle.
