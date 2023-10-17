---
description: >-
  L'assistant IA de Dastra utilise la puissance de l'IA OpenAI GPT-4 pour
  générer automatiquement des fiches de traitement
---

# 😇 Assistant IA (beta)

## Quels cas d'usage avec Dastra ?&#x20;

Avec Dastra, vous pouvez utiliser l'IA pour deux cas d'usages principaux :&#x20;

### **Générer des traitements de données**

Générez rapidement des traitements de données au format attendu par Dastra à partir d'une description rapide de votre traitement.&#x20;

A partir de l'usage décrit des données, Dastra vous proposera un modèle de traitement incluant un nom, un ou des jeux de données incluant des champs, une durée de conservation, des mesures de sécurité, des destinataires et une description du traitement. \
En un rien de temps, vous pourrez créer votre traitement.&#x20;

Vous avez une modification à apporter sur ce qui est proposé ? Editez le traitement une fois créé directement.

### **Générer des actifs**

Générez rapidement des actifs (de type logiciel par exemple) au format attendu par Dastra. L'IA vous proposera un nom, des liens vers la politique de confidentialité de l'acteur, créera un acteur en tant qu'éditeur.&#x20;

Gagnez en rapidité et laissez l'IA préremplir ces informations pour vous.&#x20;

## Comment utiliser l'IA générative de Dastra ?

Vous pouvez utiliser l'assistant IA pour générer des traitements de données ou des actifs. Pour cela cliquez sur le bouton "Créer un traitement" et sur "générer avec IA". L'assistant IA vous fera une proposition de modèle de données que vous pourrez ensuite adapter à vos besoins.

{% embed url="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LvBxs22wUMicv9uWp6C-2584506019%2Fuploads%2F3LnwYaR0wxVm1itxA4XH%2Fia-gpt-dastra.mp4?alt=media&token=ba3d66f4-e290-4215-83ec-7a2f91641d39" %}

{% hint style="warning" %}
**Que faire si je ne souhaite pas avoir cette fonctionnalité sur mon compte ?**

Si jamais vous ne souhaitez pas que cette option soit disponible dans votre espace de travail, vous pouvez [nous contacter ](../../commencer/le-support/faire-une-demande-de-support.md)afin que nous désactivions la fonctionnalité au niveau de votre organisation.
{% endhint %}

## Comment ça marche ?

Dastra utilise le modèle d'**IA OpenAI GPT 3.5 boost** (Modèle de [ChatGPT](https://chat.openai.com/)) fourni par [le service OpenAI hébergé sur Azure](https://azure.microsoft.com/fr-fr/products/cognitive-services/openai-service). Le modèle utilisé est pré-entrainé. **Nous ne transférons absolument aucune donnée de votre organisation** dans le but d'entraîner cette intelligence artificielle.&#x20;

Dastra utilise simplement la puissance de l'IA générative de GPT pour générer du contenu à partir de simple requête textuelle. Dastra a simplement fourni le modèle de document attendu (JSON) et un exemple de traitement de données (issu de notre bibliothèque) que nous souhaitons avoir et le modèle d'IA s'occupe du reste.

Nous transférons uniquement le texte du prompt que vous allez envoyer à l'IA

{% hint style="warning" %}
**Avertissement sur la qualité du contenu suggéré !**&#x20;

Les données générées par l'assistant **sont uniquement des propositions**. Il est nécessaires de bien relire et mettre à jour les informations générées automatiquement par l'assistant. Dastra ne s'engage pas sur la qualité des informations proposées.
{% endhint %}

Dastra **ne réalise aucun transfert de données** présentes dans votre espace de travail vers le service d'IA.

Les requêtes textuelles et les résultats du service :

* **ne sont PAS disponibles pour d'autres clients**. ne sont PAS à la disposition de l'OpenAI.
* **ne sont PAS utilisés pour améliorer les modèles de l'OpenAI**&#x20;
* **ne sont PAS utilisées pour améliorer automatiquement les modèles Azure OpenAI** pour votre utilisation dans votre ressource (les modèles sont sans état, sauf si vous affinez explicitement les modèles avec vos données d'entraînement).&#x20;

Si vous souhaitez avoir plus d'informations sur le fonctionnement de ce modèle, [rendez-vous sur cette page ](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy)
