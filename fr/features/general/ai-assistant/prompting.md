---
description: >-
  Formulez vos demandes à Dastra AI pour obtenir des réponses complètes et sourcées : cinq réflexes, des exemples testés, la vérification d'une réponse et la création d'une compétence.
---

# Bien formuler vos demandes

Dastra AI répond à partir de votre espace de travail : la réponse est aussi précise que la demande. Nommez les fiches concernées, dites ce que vous attendez en retour et, en mode Édition, demandez-lui de regarder avant d'agir. Cette page donne cinq réflexes, des exemples de demandes et la façon de vérifier une réponse.

Les exemples ont été testés dans un espace de travail de démonstration, celui d'un distributeur fictif, Brightmoor Retail Group. Remplacez les noms de ses fiches par les vôtres.

## Cinq principes

### Nommez le périmètre avec les mots de l'application

Lorsqu'une demande désigne un groupe de fiches que Dastra ne connaît pas sous ce nom, l'assistant doit deviner lesquelles vous voulez. Listez les fiches, ou utilisez les mots de l'application : traitement, demande d'exercice de droits, unité organisationnelle.

| Au lieu de | Écrivez |
| --- | --- |
| `Comparez les durées de conservation de nos traitements marketing et signalez ceux qui semblent incohérents. Répondez sous forme de tableau.` L'assistant a retenu trois traitements et en a laissé d'autres du même type. | `Comparez les durées de conservation de ces traitements : Newsletter and promotional emails, Newsletter campaigns, Targeted advertising and retargeting, Personalised product recommendations et Brightmoor Rewards loyalty programme. Montrez pour chaque traitement sa règle et sa durée de conservation dans un tableau, et signalez ceux qui semblent incohérents.` Cinq lignes, chacune avec sa règle de conservation et un signalement. |
| `Ajoutez le tag « Reviewed 2026 » aux traitements de Brightmoor UK Ltd.` L'assistant a lu « entité » comme le nom d'une fiche et a proposé un traitement sans rapport. | `Ajoutez le tag « Reviewed 2026 » aux traitements du département Legal & Compliance de Brightmoor Retail Group.` Mode Édition. L'assistant a trouvé l'unité organisationnelle, a vu que le tag n'existait pas et s'est arrêté sur une carte d'autorisation pour le créer. |

### Demandez les preuves, pas seulement le verdict

Une question fermée reçoit une réponse tirée d'un indicateur du registre. Demandez les données qui le fondent, puis l'indicateur.

| Au lieu de | Écrivez |
| --- | --- |
| `Quels traitements portent sur des données de santé ou d'autres données sensibles et n'ont pas de PIA ?` Deux traitements justes, mais uniquement d'après l'indicateur de données sensibles, sans identifier de données de santé. | `Listez tous les traitements avec leurs catégories de données et indiquez si un PIA est enregistré. Signalez ensuite ceux qui portent sur des données de catégories particulières, comme des données de santé, et n'ont pas de PIA. Répondez sous forme de tableau.` Tous les traitements dans un tableau, les deux mêmes signalés, et la raison : un jeu de données lié contient des certificats d'arrêt maladie. |

### Donnez du contexte avec `@` ou en ouvrant la fiche

Sur une fiche, l'assistant part de ce qu'elle contient : ses compteurs, ses mesures et ses prestataires liés. Deux façons de lui donner ce contexte :

* Ouvrez la fiche et appuyez sur **Ctrl+J** (**Cmd+J** sur Mac). La fiche est jointe au-dessus de la zone de message. Le panneau rouvre la conversation précédente : cliquez d'abord sur **Nouvelle conversation**.
* Saisissez `@` et quelques lettres du nom de la fiche, puis choisissez la ligne. La mention devient une pastille dans votre message. Le menu liste des fiches et des documents, parfois aux noms proches : choisissez la ligne du bon type.

Les [exemples d'analyse](#exemples-de-demandes-par-objectif) ci-dessous utilisent les deux.

### Demandez le format, puis itérez dans la même conversation

Dites comment vous voulez la réponse : un tableau, les colonnes, l'ordre, un nombre de lignes. Affinez ensuite dans la même conversation. Une relance réutilise la liste précédente au lieu de chercher à nouveau, donc la nouvelle réponse reste cohérente avec elle.

1. `Listez les demandes d'exercice de droits qui ne sont pas clôturées, avec leur type, leur demandeur et leur date d'échéance, de la plus ancienne à la plus récente.`
2. `Regroupez-les maintenant par type de demande et comptez-les.`

### Cherchez d'abord, agissez ensuite

En mode Édition, une demande qui crée un élément à partir d'une description générale donne un résultat général. Demandez d'abord à l'assistant de lister ce qui manque, puis d'agir sur cette liste.

| Au lieu de | Écrivez |
| --- | --- |
| `Créez un plan d'actions de trois tâches pour compléter le traitement « Supplier and contract management ».` Les tâches étaient des tâches génériques de gestion des fournisseurs et passaient à côté des manques de la fiche. | `Listez d'abord ce qui manque dans le traitement « Supplier and contract management ». Créez ensuite un plan d'actions avec une tâche pour chacun des trois manques les plus importants.` Mode Édition. Trois tâches de priorité haute qui correspondent aux manques : durées de conservation, inventaire des données personnelles et finalités, destinataires et transferts. |

Chaque modification du mode Édition s'arrête sur une carte **Autorisation requise** : voir [Lisez la carte d'autorisation](#lisez-la-carte-dautorisation).

## Exemples de demandes par objectif

Chaque demande ci-dessous a été testée dans l'espace de démonstration, en anglais. Le mode est celui du test. Les demandes des principes ci-dessus sont aussi des exemples : la comparaison des durées de conservation et la question sur les données sensibles pour analyser et rechercher, le tag et le plan d'actions pour modifier des fiches.

| Objectif | Écrivez | Mode |
| --- | --- | --- |
| Rechercher | `Listez les demandes d'exercice de droits qui ne sont pas clôturées, avec leur type, leur demandeur et leur date d'échéance, de la plus ancienne à la plus récente.` | **Question** |
| Analyser une fiche | `Résumez ce traitement en cinq lignes, puis listez ce qui manque pour le compléter.` Depuis le panneau ouvert sur le traitement « Supplier and contract management ». | **Question** |
| Analyser une fiche | `@Online order management Quelles mesures de sécurité attendriez-vous pour ce traitement et qui ne sont pas encore liées ?` La mention est une pastille. | **Question** |
| Itérer | `Ne gardez que celles créées cette année.` Dans la conversation de la liste ci-dessus. | **Question** |
| Itérer | `Regroupez-les maintenant par type de demande et comptez-les.` Dans la même conversation. | **Question** |
| Rédiger | `Rédigez une réponse à la demande 2BEX36WB, en anglais, sur un ton formel, confirmant que nous l'avons reçue et que nous répondrons sous un mois.` Rien n'est envoyé ni enregistré : copiez le brouillon avec **Copier**. | **Question** |
| Construire un artefact | `Dessinez un schéma des flux de données du traitement Online order management.` La réponse renvoie vers un [artefact](artifacts.md). | **Question** |
| Lancer une compétence | `/dpo_opinion`, puis dans la même conversation : `Ce message est la saisine, faite aujourd'hui par Emma Walsh, DPO. Question : ce traitement peut-il rester publié alors que sa règle de conservation et ses champs de données personnelles ne sont pas renseignés ?` Sur le traitement « Supplier and contract management ». | **Question** |

## Vérifiez et orientez la réponse

### Lisez les étapes et les sources

Sous une réponse, une ligne comme **3 outil(s) utilisé(s)** indique ce que l'assistant a fait. Cliquez sur **Afficher les outils** pour voir les étapes, par exemple Parcours des enregistrements ou Lecture d'un enregistrement. Si les étapes ne correspondent pas à ce que vous vouliez, reformulez le périmètre.

Les fiches sont nommées dans la réponse, pas liées : dans un tableau, les lignes sont du texte simple. Recherchez le nom dans le registre pour ouvrir la fiche.

L'assistant dit aussi ce qu'il n'a pas pu établir. Dans les tests, il a noté qu'une mesure « non liée » ne prouve pas qu'elle n'est « pas mise en œuvre », que les échéances sont en UTC et que les flux d'un schéma au-delà des finalités enregistrées sont indicatifs. Lisez ces phrases : elles indiquent ce qu'il faut vérifier.

{% hint style="info" %}
Une réponse est une proposition à vérifier, pas une conclusion. Voir [L'IA comme point de départ, pas comme réponse définitive](README.md#lia-comme-point-de-depart-pas-comme-reponse-definitive).
{% endhint %}

### Lisez la carte d'autorisation

En mode **Édition**, l'assistant affiche une carte **Autorisation requise** avant chaque modification. Elle nomme l'outil, par exemple **Création d'un tag** ou **Création d'un plan d'action**. Cliquez sur **Voir les arguments** pour voir exactement ce qu'il s'apprête à envoyer : les fiches, les libellés, les tâches.

**Refuser** ne change rien. L'assistant le confirme (« aucune tâche n'a été créée ») et propose de réviser. Si vous envoyez un autre message pendant qu'une carte est en attente, la carte n'est plus pertinente. Les choix de la carte sont décrits dans [Modes Question et Édition](README.md#modes-question-et-edition).

### Évaluez la réponse

Cliquez sur **Bonne réponse** ou **Mauvaise réponse** sous une réponse. Une **Mauvaise réponse** ouvre une fenêtre où vous pouvez dire ce qui n'allait pas. Dastra enregistre la note et le commentaire avec le message.

## Bon à savoir

* Vérifiez le mode avant d'envoyer. Le mode est **Édition** par défaut pour les utilisateurs qui peuvent modifier. Passez en **Question** pour une demande qui ne doit rien changer.
* Démarrez une nouvelle conversation pour un nouveau sujet. Le panneau rouvre la conversation précédente : cliquez sur **Nouvelle conversation** en haut du panneau. Une relance travaille sur la réponse précédente, un nouveau sujet n'en a pas besoin.
* Vérifiez la ligne que vous choisissez dans le menu `@`. Il mélange des fiches et des documents, et un document peut avoir un nom proche de celui d'une fiche.
* Une compétence a besoin de ses informations dans le message. `/dpo_opinion` seul demande uniquement la saisine : qui l'a faite, quand, et la question.

## Transformer une demande répétée en compétence

Si vous retapez souvent la même demande, enregistrez-la comme compétence et rappelez-la avec `/`. Une compétence garde votre formulation et votre équipe peut la partager. Voir [Les compétences](agents/skills.md).
