# Comment ça marche ?

### Modèles et hébergement

Dastra utilise des modèles d'IA générative pré-entraînés, disponibles en quatre familles au choix :

| Famille                              | Modèles configurés                                                                      | Hébergement               |
| ------------------------------------ | --------------------------------------------------------------------------------------- | ------------------------- |
| **OpenAI** _(recommandé par défaut)_ | Fast : gpt-4o-nano · Smart : gpt-5-mini · Large context : gpt-4.1-mini                  | Azure, France / EEE       |
| **Mistral**                          | Fast : mistral-small-2503 · Smart : Mistral-Large-3 · Large context : Mistral-Large-3   | Azure, France / EEE       |
| **Open source**                      | Fast : Ministral-3B · Smart : DeepSeek-V3.2 · Large context : Llama-4-Maverick-17B-128K | Azure, France / EEE       |
| **Custom AI provider**               | Votre propre fournisseur via clé API _(voir ci-dessous)_                                | Selon votre configuration |

Pour les trois premières familles, les modèles sont hébergés sur l'infrastructure Microsoft Azure en France. Ils ne sont pas opérés directement par OpenAI ou Mistral : Dastra utilise les services managés Azure, ce qui signifie que **vos données ne transitent pas vers les infrastructures propres d'OpenAI ou de Mistral**.

Pour chaque famille, trois niveaux de modèle sont utilisés selon la complexité de la tâche :

* **Fast**  (actions simples) : génération de descriptions, proposition de tags
* **Smart** (actions nécessitant plus de raisonnement) : génération d'éléments structurés dans Dastra
* **Contexte étendu** (actions traitant un volume important de données) : réponse à un questionnaire, analyse de conformité

Vous pouvez configurer la famille de modèles utilisée dans les **Paramètres de votre organisation > Assistant IA**.

***

### Custom AI provider

Dastra vous permet de connecter votre propre fournisseur d'IA via une clé API, à condition que celui-ci soit compatible avec le standard OpenAI API. Les fournisseurs supportés incluent notamment OpenAI, Google (Gemini), Mistral, Microsoft Foundry, ainsi que tout LLM auto-hébergé compatible.

Pour configurer un fournisseur personnalisé, rendez-vous dans **Paramètres > Assistant IA > Custom AI provider**, puis renseignez vos identifiants et associez-les aux trois niveaux de modèle (Fast, Smart, Contexte étendu).

{% hint style="warning" %}
Lorsque vous utilisez un Custom AI provider, les données transmises au modèle sont soumises à la politique de confidentialité de **votre fournisseur**, et non aux garanties Azure décrites sur cette page. Vérifiez les conditions de votre fournisseur avant d'activer cette option, notamment si vos prompts peuvent contenir des données à caractère personnel.
{% endhint %}

***

### Ce que Dastra envoie au modèle

Dastra transmet uniquement les informations nécessaires à la génération demandée : le texte saisi par l'utilisateur, et le cas échéant les champs structurés de l'objet concerné (traitement, système d'IA, demande d'exercice de droits, etc.).

Le détail exact des données transmises par fonctionnalité est disponible dans la section Quelles données sont transmises ?.

***

### Ce que Dastra ne fait pas

Les points suivants sont garantis contractuellement par Microsoft Azure pour tous les modèles des familles OpenAI, Mistral et Open source :

* Vos prompts et résultats **ne sont pas disponibles** pour d'autres clients Azure
* Vos données **ne sont pas transmises** à OpenAI, Mistral ou tout autre tiers
* Vos données **ne sont pas utilisées** pour entraîner ou améliorer les modèles de base
* Les modèles sont **sans état (stateless)** : aucun prompt n'est stocké dans le modèle entre deux requêtes

***

### Surveillance des abus et revue humaine

Microsoft Azure maintient un mécanisme automatisé de détection des contenus potentiellement abusifs. Dans les cas exceptionnels où un contenu est signalé, un échantillon de prompts peut être conservé temporairement dans un espace de stockage isolé par client, aux fins de revue. Pour les ressources déployées dans l'EEE (ce qui est le cas de Dastra), les réviseurs humains éventuels sont également situés dans l'EEE.

Cette conservation reste exceptionnelle et ne concerne pas les usages normaux de la plateforme. Pour plus de détails, consultez la [documentation Microsoft sur la confidentialité des données Azure Direct Models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/data-privacy).

***

### Logs d'invocation IA

Dastra conserve un historique des appels à l'assistant IA sur les **90 derniers jours**, accessible depuis **Paramètres > Assistant IA > Logs d'invocation IA**. Pour chaque appel, les informations suivantes sont enregistrées :

| Champ           | Description                                       |
| --------------- | ------------------------------------------------- |
| **Date**        | Horodatage de l'appel                             |
| **Statut**      | Succès ou échec de la génération                  |
| **Opération**   | Type de prompt utilisé                            |
| **Modèle**      | Nom du modèle sollicité                           |
| **Durée**       | Temps de traitement de la requête                 |
| **Utilisateur** | Membre du workspace ayant déclenché la génération |

### Quelles données sont transmises au modèle ?

{% hint style="info" %}
Dastra ne transmet **aucune donnée de votre workspace** au modèle IA sans que vous en soyez à l'origine. Seules les informations listées ci-dessous, selon la fonctionnalité utilisée, sont incluses dans la requête envoyée au modèle.
{% endhint %}

| Fonctionnalité                                             | Données transmises au modèle                                                                                                                                         | Données personnelles potentielles                                       |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Générer un traitement**                                  | Texte libre saisi par l'utilisateur                                                                                                                                  | Non — sauf si l'utilisateur mentionne des personnes dans sa description |
| **Générer un actif**                                       | Texte libre + URL de la politique de confidentialité fournie                                                                                                         | Non                                                                     |
| **Générer un acteur**                                      | Texte libre + URL ou pièce jointe fournie                                                                                                                            | Non                                                                     |
| **Générer un jeu de données**                              | Texte libre saisi par l'utilisateur                                                                                                                                  | Non                                                                     |
| **Générer une mesure de sécurité**                         | Texte libre saisi par l'utilisateur                                                                                                                                  | Non                                                                     |
| **Générer une notice d'information**                       | Champs structurés du traitement (finalités, base légale, durées, destinataires, droits)                                                                              | Potentiellement — si les champs contiennent des références nominatives  |
| **Générer une description**                                | Texte libre saisi par l'utilisateur                                                                                                                                  | Non                                                                     |
| **Proposer des tags**                                      | Contenu textuel de l'objet (nom, description)                                                                                                                        | Non                                                                     |
| **Générer un modèle de questionnaire**                     | Texte libre saisi par l'utilisateur                                                                                                                                  | Non                                                                     |
| **Répondre à un questionnaire (PIA, analyse de risque…)**  | Champs structurés du traitement lié + instructions personnalisées éventuelles                                                                                        | Potentiellement — selon le contenu du traitement                        |
| **Générer une réponse à une demande d'exercice de droits** | Nom et prénom du demandeur, message de la demande, langue, nom du workspace, finalités, nom de l'opérateur, date et délai restant, état et identifiant de la demande | **Oui** — nom, prénom et contenu de la demande                          |
| **Générer un post-mortem de violation**                    | Champs structurés de la violation (description, données affectées, mesures prises)                                                                                   | Potentiellement — selon le contenu de la fiche violation                |
| **Extraire les métadonnées d'un contrat**                  | Contenu textuel du document transmis (pièce jointe ou URL)                                                                                                           | Potentiellement — selon le contenu du contrat                           |
| **Générer un document personnalisé**                       | Instructions saisies par l'utilisateur + contenu source éventuel                                                                                                     | Potentiellement — selon les instructions fournies                       |
| **Générer un rapport personnalisé**                        | Instructions saisies par l'utilisateur                                                                                                                               | Non — sauf si l'utilisateur inclut des données dans ses instructions    |
| **Analyse de risque (système d'IA)**                       | Champs structurés du système d'IA (description, finalités, données traitées, parties prenantes)                                                                      | Potentiellement — selon le contenu du système d'IA                      |
| **Générer une description de système d'IA**                | Texte libre + URL ou pièce jointe fournie                                                                                                                            | Non                                                                     |
| **Générer une notice système d'IA**                        | Champs structurés du système d'IA concerné                                                                                                                           | Potentiellement                                                         |
| **Suggestions de contrôles / exigences / tests**           | Contexte de l'objet concerné (nom, description, référentiel)                                                                                                         | Non                                                                     |

{% hint style="warning" %}
**Bonne pratique** : évitez d'inclure des données à caractère personnel directement dans les champs de texte libre (descriptions, instructions personnalisées). Utilisez des identifiants ou des termes génériques lorsque c'est possible.
{% endhint %}

#### Données qui ne sont jamais transmises

Les éléments suivants ne font **jamais** partie des requêtes envoyées au modèle IA :

* Les identifiants et mots de passe des utilisateurs Dastra
* Les données des autres enregistrements de votre workspace (seul l'objet sur lequel vous travaillez est concerné)
* Les métadonnées de session (nom de l'utilisateur connecté, adresse IP, etc.)
* Les pièces jointes non explicitement fournies dans la fonctionnalité concernée

#### Durée de conservation des requêtes

Les modèles Azure utilisés par Dastra sont **sans état (stateless)** : les prompts et les résultats ne sont pas stockés dans le modèle et ne sont pas utilisés pour réentraîner ou améliorer les modèles de base.

{% hint style="info" %}
**Exception — détection des abus** : Microsoft Azure maintient un mécanisme automatisé de surveillance des contenus potentiellement abusifs. Si un prompt est signalé, un échantillon peut être conservé temporairement dans un espace de stockage isolé par client, aux fins de revue. Pour les ressources déployées dans l'EEE (ce qui est le cas de Dastra), les éventuels réviseurs humains sont également situés dans l'EEE. Cette conservation reste exceptionnelle et ne concerne pas les usages normaux de la plateforme.
{% endhint %}

Pour plus d'informations, consultez la [documentation Microsoft sur la confidentialité des données Azure Direct Models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/data-privacy).
