---
description: >-
  Les discussions internes vous permettent d'échanger avec les utilisateurs de
  la plateforme, avec mentions, citations et notifications.
---

# Discussions internes

Les discussions internes fonctionnent comme un chat attaché à un élément de Dastra : traitement, demande d'exercice de droits, tâche, violation, acteur, actif, jeu de données, champ de données, point de contrôle, évaluation de risque, contrat, système d'IA, projet ou audit de conformité, réponse à un questionnaire. Chaque élément a une seule conversation.

## Fonctionnement

1. Ouvrez la fiche de l'élément concerné.
2. Cliquez sur le bouton **Discussions internes**, une bulle accompagnée du nombre de messages. Le fil s'ouvre dans un panneau à droite.

<figure><img src="../../.gitbook/assets/general-discussions-1.png" alt="Fiche d'un traitement avec le bouton Discussions internes et le panneau de discussion ouvert"><figcaption><p>Le bouton Discussions internes et le fil de discussion d'une fiche</p></figcaption></figure>

3. Cliquez dans la zone **Rédiger un message** et saisissez votre message. Le bouton **Ajouter un document** joint un fichier, par clic ou par glisser-déposer.
4. Cliquez sur **Envoyer**, ou appuyez sur **Ctrl+Entrée**.

Un brouillon non envoyé est conservé dans votre navigateur et retrouvé à la réouverture du panneau. Vous pouvez modifier ou supprimer vos propres messages depuis leur menu. Un message modifié affiche **Modifié le** suivi de la date.

## Mentions

Mentionnez les utilisateurs concernés avec le caractère **@**. Une liste d'utilisateurs de votre espace de travail s'affiche et se filtre à mesure que vous tapez.

<figure><img src="../../.gitbook/assets/general-discussions-2.png" alt="Liste des utilisateurs proposée après la saisie du caractère @ dans la zone de message"><figcaption><p>La liste des utilisateurs proposée après @</p></figcaption></figure>

La mention déclenche une notification immédiate à l'utilisateur concerné.

## Citations

Vous pouvez répondre directement à un message précis, pour garder le contexte lisible dans un long fil.

1. Survolez le message auquel vous souhaitez répondre et cliquez sur **Répondre**. Ce bouton est disponible sur les messages des autres utilisateurs.
2. Un encart **Réponse à** suivi du nom de l'auteur s'affiche au-dessus de la zone de texte, avec un aperçu du message cité. Son auteur est mentionné automatiquement dans votre réponse, ce qui déclenche sa notification.
3. Saisissez votre message, ajoutez d'éventuelles pièces jointes, puis cliquez sur **Envoyer**.

Pour retirer la citation tout en gardant votre message en cours de rédaction, cliquez sur l'icône corbeille de l'encart. Vous pouvez aussi retirer la mention si vous ne souhaitez pas notifier l'auteur.

{% hint style="info" %}
Un message ne peut citer qu'un seul message à la fois. La citation est conservée si vous modifiez ensuite votre message.
{% endhint %}

Une fois publié, le message cité s'affiche dans un encart au-dessus de votre réponse. Si le message cité est supprimé par la suite, l'encart affiche **Ce message a été supprimé** : votre réponse reste visible.

## Notifications

À chaque nouveau message, Dastra notifie :

* les utilisateurs mentionnés dans le message, immédiatement ;
* les personnes responsables de l'élément (par exemple son propriétaire, son opérateur ou la personne à qui il est assigné, selon le type d'élément), sauf l'auteur du message.

La ligne **Utilisateurs notifiés** sous la zone de saisie indique combien de personnes recevront votre message et en donne la liste. La façon dont chaque utilisateur reçoit ses notifications dépend de ses préférences : consultez la page [Notifications](../settings/notifications.md).

{% hint style="info" %}
Si vous utilisez Slack, les utilisateurs mentionnés peuvent aussi être prévenus par le bot Dastra dans Slack, à condition que leur adresse e-mail Dastra soit la même que dans Slack. Voir [Intégrations](../integrations/README.md).
{% endhint %}

## Ouverture et fermeture de la conversation

Dès qu'un message est envoyé sur un élément sans conversation en cours, ou après une fermeture, la conversation est ouverte. Le bouton **Discussions internes** affiche alors un petit rond rouge.

<figure><img src="../../.gitbook/assets/general-discussions-3.png" alt="Bouton Discussions internes avec un rond rouge pour une conversation ouverte et un rond vert pour une conversation fermée"><figcaption><p>Le rond rouge signale une conversation ouverte, le rond vert une conversation fermée</p></figcaption></figure>

Quand l'échange est terminé, cliquez sur **Fermer la conversation** en bas du fil. Ce bouton est réservé aux utilisateurs qui disposent de la permission **Discussions** dans leur rôle. Le rond devient vert, et le fil indique **La conversation a été clôturée par** suivi du nom de la personne. Un utilisateur qui a la même permission peut cliquer sur **Annuler** pour rouvrir la conversation.

## Hub des conversations

Le hub regroupe toutes les conversations de votre espace de travail. Vous y répondez aux questions de vos utilisateurs tout en accédant aux fiches concernées.

Pour l'ouvrir, cliquez sur l'icône de bulle (**Toutes les discussions**) dans la barre supérieure. Un badge rouge indique le nombre de conversations ouvertes.

<figure><img src="../../.gitbook/assets/general-discussions-4.png" alt="Barre supérieure avec l'icône Toutes les discussions et son badge, et page du hub des conversations"><figcaption><p>L'icône Toutes les discussions et le hub des conversations</p></figcaption></figure>

Sur la page du hub :

* la colonne de gauche liste les types d'objets qui ont des conversations ; sélectionnez-en un pour filtrer ;
* activez **Afficher les conversations fermées** pour inclure les conversations clôturées ;
* chaque conversation s'affiche sous forme de carte avec le nom de l'élément, un lien vers sa fiche, ses derniers messages et une zone de réponse.
