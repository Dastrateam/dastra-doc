---
description: >-
  L'assistant IA de Dastra génère et enrichit des éléments de votre espace de
  travail à partir de simples descriptions, avec des agents et un serveur MCP.
---

# Assistant IA

L'assistant IA de Dastra vous permet de générer et d'enrichir des éléments de votre espace de travail à partir de simples descriptions textuelles. Il s'appuie sur des modèles d'IA générative hébergés sur Azure, en France et dans l'Espace Économique Européen, sans qu'aucune donnée de votre organisation ne soit utilisée pour entraîner ces modèles.

La disponibilité de l'assistant IA dépend de l'offre de votre organisation, module par module. Dans un module que votre offre n'inclut pas, les boutons IA sont grisés. Pour modifier le périmètre de votre offre, contactez notre équipe.

## L'IA comme point de départ, pas comme réponse définitive

L'assistant IA est conçu pour **accélérer votre travail de conformité**, non pour remplacer l'expertise humaine. Tout contenu généré par l'assistant, qu'il s'agisse d'une description de traitement, d'une notice d'information ou d'une analyse de conformité, est **une proposition qui nécessite une relecture et une validation** par une personne qualifiée avant tout usage.

En particulier :

{% hint style="warning" %}
**Le contenu généré par l'IA ne constitue pas un avis juridique.** Il ne peut pas se substituer au jugement d'un professionnel de la protection des données ou d'un conseil juridique.

**Les évaluations de conformité sont des aides à l'analyse.** Les scores et recommandations produits par l'IA reposent uniquement sur les informations enregistrées dans votre espace de travail. Ils reflètent la qualité de cette documentation, et non un avis juridique indépendant.

**Vous gardez le contrôle.** Aucun résultat généré par l'IA n'est appliqué ou communiqué automatiquement. Chaque résultat nécessite une action humaine délibérée pour être utilisé.
{% endhint %}

## Protection des données et confidentialité

Les données de votre organisation ne sont jamais utilisées pour entraîner des modèles d'IA. Les modèles utilisés par Dastra sont hébergés sur l'infrastructure Microsoft Azure en France, sous des garanties contractuelles qui excluent vos données de tout entraînement ou partage avec des tiers. Pour tous les détails, consultez la page [Comment ça marche ?](how-it-works.md#comment-ca-marche).

## Ce que l'assistant IA peut vous aider à faire

L'assistant est disponible dans plusieurs modules de la plateforme :

* **Traitements de données** : générer des descriptions, des jeux de données, des mesures de sécurité, des notices d'information et des analyses de conformité
* **Systèmes d'IA** : générer des descriptions, des notices et des analyses de risque
* **Questionnaires** : générer des réponses assistées par IA à des PIA et analyses de risque
* **Demandes d'exercice de droits** : rédiger des réponses dans plusieurs langues et registres
* **Actifs et acteurs** : générer des entrées structurées à partir d'une URL ou d'une description libre
* **Contrats** : extraire des métadonnées depuis un document importé
* **Documents et rapports personnalisés** : générer du contenu à partir de vos propres instructions

Pour un guide pas à pas de chaque fonctionnalité, consultez la page [Cas d'usage](use-cases.md).

## Dastra AI, agents et serveur MCP

Au-delà de la génération de contenu, Dastra propose un assistant conversationnel, **Dastra AI**, que vous interrogez depuis le tableau de bord ou depuis le bouton **Ouvrir Dastra AI** en bas à droite de l'écran. Vous pouvez aussi créer vos propres [agents](agents/README.md), conversationnels ou autonomes, et connecter vos outils d'IA à Dastra avec le [serveur MCP](mcp.md). Ces fonctionnalités dépendent de l'offre de votre organisation et des permissions de chaque utilisateur.

Toutes les fonctionnalités IA partagent le quota mensuel de crédits IA décrit dans [Comment ça marche ?](how-it-works.md#credits-et-quotas-ia).

## Discuter avec Dastra AI

**Dastra AI** répond à vos questions sur votre espace de travail dans une conversation. Il consulte vos fiches avec des outils en lecture seule : vous pouvez demander un résumé, la liste des demandes en retard ou les traitements qui n'ont pas d'AIPD.

1. Cliquez sur **Ouvrir Dastra AI**, en bas à droite de l'écran, ou appuyez sur **Ctrl+J** (**Cmd+J** sur Mac).
2. Saisissez votre question, ou choisissez l'une des **Suggestions**. Elles changent selon la page où vous êtes : la fiche consultée, le registre, les demandes, les systèmes d'IA.
3. Lisez la réponse. Lorsque l'assistant s'appuie sur vos fiches, il affiche ses étapes et les cite. Utilisez les **Suggestions de questions** pour poursuivre.

<figure><img src="../../../.gitbook/assets/general-ai-chat-1.png" alt="Le panneau Dastra AI sur un traitement, avec les suggestions et la zone de message"><figcaption><p>Le panneau Dastra AI, avec le menu + ouvert</p></figcaption></figure>

Le panneau propose plusieurs outils :

* **Basculer en plein écran** étend le panneau à tout l'écran. Un lien vers la page de l'agent IA d'un espace de travail ouvre l'assistant en plein écran, puis revient au tableau de bord de cet espace.
* **Nouvelle conversation** démarre une conversation vierge. La liste des conversations conserve les précédentes : renommez-les ou supprimez-les depuis cette liste. Supprimer une conversation supprime tous ses messages.
* **Choisir un agent** passe de l'assistant standard aux [agents](agents/README.md) activés dans votre espace de travail.
* **Ajouter du contexte** et **Joindre un fichier** donnent à l'assistant une fiche ou un document sur lequel travailler. Saisissez `@` pour mentionner une fiche ou un utilisateur.
* Saisissez `/` ou cliquez sur **Compétences** pour lancer une [compétence](agents/skills.md), un prompt réutilisable.
* **Dicter un message** enregistre votre voix et la transcrit dans la zone de message. Votre navigateur demande l'accès au micro la première fois.
* Évaluez une réponse avec **Bonne réponse** ou **Mauvaise réponse**, et ajoutez un commentaire, pour envoyer un retour à Dastra.

### Modes Question et Édition

En mode **Question**, l'assistant lit seulement : rien ne change dans votre espace de travail. En mode **Édition**, il peut aussi créer et modifier des fiches, et demande votre confirmation avant d'appliquer une modification. Le sélecteur de mode apparaît pour les utilisateurs qui ont la permission d'écriture de l'assistant. Le mode **Édition** nécessite l'option correspondante dans l'offre de votre organisation. Sans elle, l'option est verrouillée.

{% hint style="info" %}
Dastra AI est disponible lorsque votre offre l'inclut et que votre rôle a la permission de l'assistant IA. Les messages consomment le quota mensuel de crédits IA, et une bannière vous prévient lorsque le quota est presque épuisé.
{% endhint %}

## Fonctionnalités en bêta

Certaines fonctionnalités IA sont publiées en version bêta : elles sont opérationnelles mais continuent d'être affinées sur la base des retours utilisateurs. Les fonctionnalités bêta sont clairement identifiées dans l'interface.

Lors de l'utilisation d'une fonctionnalité bêta :

* Les résultats peuvent être moins constants que dans les fonctionnalités stables et doivent être traités avec une vigilance accrue.
* Les prompts et critères sous-jacents sont activement améliorés. Les résultats peuvent évoluer entre les versions.
* Les retours sont les bienvenus et aident Dastra à améliorer la fonctionnalité. Utilisez l'option de feedback disponible dans l'interface.

{% hint style="warning" %}
Les fonctionnalités bêta ne doivent jamais constituer l'unique fondement d'une décision de conformité. Elles sont conçues pour accompagner une revue humaine approfondie, non pour la remplacer.
{% endhint %}

**Actuellement en bêta** : l'analyse de conformité par l'IA, disponible sur les traitements, les systèmes d'IA, les contrats, les acteurs, les applications et les réponses de questionnaire. Ouvrez-la avec le bouton **Analyse IA** de la fiche, ou demandez à Dastra AI d'analyser une fiche. Le résultat donne une note de A à F, les critères analysés et des tâches suggérées. Vous pouvez l'imprimer, le relancer ou le poursuivre dans la conversation.

***

{% content-ref url="how-it-works.md" %}
[comment-ca-marche.md](how-it-works.md)
{% endcontent-ref %}

{% content-ref url="use-cases.md" %}
[cas-dusage.md](use-cases.md)
{% endcontent-ref %}

{% content-ref url="faq.md" %}
[foire-aux-questions.md](faq.md)
{% endcontent-ref %}

{% content-ref url="agents/README.md" %}
[README.md](agents/README.md)
{% endcontent-ref %}

{% content-ref url="mcp.md" %}
[serveur-mcp.md](mcp.md)
{% endcontent-ref %}
