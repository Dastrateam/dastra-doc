# Actions supplémentaires dans les workflows automatiques

Les règles de workflow automatisent des opérations dans Dastra. Pour les demandes d'exercice de droits, elles proposent des actions spécifiques que vous configurez selon vos règles de gestion. Ouvrez **Règles de workflow** dans les paramètres de l'espace de travail, puis ajoutez une action à une règle portant sur les demandes.

<figure><img src="../../../.gitbook/assets/requests-workflow-actions-1.png" alt="La liste des actions proposées pour une règle de workflow portant sur les demandes"><figcaption><p>Actions spécifiques aux demandes d'exercice de droits</p></figcaption></figure>

## Actions propres aux demandes

* **Envoyer un message de demande** : envoie un message au demandeur depuis la demande, avec un texte libre ou un modèle.
* **Clôturer la demande** : ferme la demande avec un motif de clôture, et peut envoyer la notification de clôture au demandeur.
* **Anonymiser la demande** : efface les données identifiantes de la demande. L'action est irréversible.
* **Déplacer dans la corbeille** : place la demande dans la corbeille, où les [règles de purge](purge.md) s'appliquent ensuite.

## Autres actions utiles pour les demandes

* **Modifier un champ** : met à jour un champ de la demande.
* **Ajouter une tâche** : crée une tâche, par exemple pour faire valider la réponse par le DPO.
* Envoyer une notification : prévient des personnes au sujet de la demande.
* Définir un responsable : désigne le responsable de la demande.
* Ajouter des tags : ajoute des tags à la demande.
* Planifier une réponse à un questionnaire.
* Envoyer une requête HTTP : appelle un service externe.
* **Exécuter un agent IA** : lance un agent IA, selon votre offre et vos droits.

{% hint style="info" %}
Pour en savoir plus sur les workflows, consultez la page [Règles de workflow](../../settings/workflow-rules.md).
{% endhint %}
