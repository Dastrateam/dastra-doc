---
description: >-
  Quatre règles de workflow pour Brightmoor Retail Group : assigner les nouvelles
  demandes, répartir les tâches dans une équipe, alerter Microsoft Teams sur une
  violation à risque élevé et envoyer une requête HTTP.
---

# Recettes de workflow

Chaque recette est une [règle de workflow](../features/settings/workflow-rules.md) de Brightmoor Retail Group : un déclencheur, des conditions et des actions sur un type d'élément. Pour créer l'une d'elles, ouvrez **Automatisations** > **Règles de workflow**, cliquez sur **Créer une règle de workflow**, choisissez **De zéro**, puis saisissez le **Nom de la règle** et le **Type d'élément**. Activez la règle avec l'interrupteur **Statut** une fois qu'elle est enregistrée.

Gardez **Exécuter le workflow une seule fois par élément (recommandé)** activé pour les recettes qui réagissent à une création ou à une modification, afin qu'un élément ne soit jamais traité deux fois.

## Recette 1 : assigner les nouvelles demandes

Objectif : Chaque nouvelle demande d'exercice de droits a un opérateur dès la première minute, selon la filiale qui l'a reçue.

### Déclencheur

Type d'élément : **Demande**. Déclencheur : **Action**, événement **Création**.

### Conditions

Une règle compte jusqu'à cinq conditions, et chacune porte ses propres actions. Choisissez **Spécifier des conditions** pour chacune :

| Condition | Champ | Valeur |
| --- | --- | --- |
| 1 | **Unité organisationnelle** | Brightmoor Germany |
| 2 | **Unité organisationnelle** | Brightmoor UK |
| 3 | **Unité organisationnelle** | Brightmoor Retail Group |

Une demande n'a pas de champ pays. L'unité organisationnelle de la demande remplace d'ordinaire le pays d'une filiale. Pour router par langue, utilisez plutôt le champ **Langue**, et pour router par droit exercé, utilisez **Types de droits** (par exemple Effacement).

### Actions

Dans chaque condition, cliquez sur **+** et choisissez **Définir utilisateur assigné**, puis sélectionnez un utilisateur : Sophie Becker pour la condition 1, Liam O'Connor pour la condition 2 et Emma Walsh pour la condition 3. Sur une demande, cette action renseigne l'**Opérateur**.

### Résultat

Une demande reçue par la filiale allemande est assignée à Sophie Becker dès sa création. Dans la règle, **Historique** liste chaque demande traitée avec son statut, et **Exécuter** applique la règle à la main à une demande créée avant la règle.

## Recette 2 : répartir les tâches dans une équipe

Objectif : Répartir équitablement les nouvelles tâches entre les membres du service protection des données.

### Déclencheur

Type d'élément : **Tâche**. Déclencheur : **Action**, événement **Création**.

### Conditions

**S'applique à tous les éléments** : toutes les nouvelles tâches sont concernées. Pour limiter la règle, choisissez **Spécifier des conditions** et filtrez sur un champ comme un tag.

### Actions

Ajoutez **Définir utilisateur assigné**, choisissez **Sélectionnez un utilisateur dans l'équipe** et sélectionnez l'équipe dans **Sélectionnez une équipe**. Un utilisateur de l'équipe est choisi selon le modèle du tourniquet : à chaque déclenchement de la règle, le membre suivant est choisi, et le premier membre suit le dernier.

<figure><img src="../.gitbook/assets/examples-workflow-1.png" alt="Concepteur de règle de workflow avec l'action Définir le propriétaire réglée sur un utilisateur d'une équipe"><figcaption><p>L'attribution à tour de rôle</p></figcaption></figure>

### Résultat

La première tâche va au premier membre de l'équipe, la deuxième au suivant, et ainsi de suite. Le membre choisi est celui du champ **Assignée à**. Voir [Créer puis affecter des équipes](../getting-started/setup/teams.md) pour créer l'équipe. Si l'équipe n'a aucun membre, l'exécution échoue et apparaît en erreur dans l'historique.

## Recette 3 : alerter un canal Microsoft Teams sur une violation à risque élevé

Objectif : Prévenir immédiatement le canal protection des données quand une violation de données atteint le niveau de risque élevé, car l'autorité de contrôle et les personnes concernées doivent alors être informées.

Prérequis : L'[intégration Microsoft Teams](../features/integrations/microsoft-teams.md) est installée et activée sur l'espace de travail. Sans elle, l'action n'est pas proposée.

### Déclencheur

Type d'élément : **Violation de données**. Déclencheur : **Action**, événement **Création ou modification** : le niveau de risque n'existe qu'une fois l'analyse de risque renseignée, après la création.

### Conditions

Choisissez **Spécifier des conditions** et réglez le champ **Points** sur une valeur supérieure ou égale à 6. **Points** est le score de la violation, la somme des deux scores de l'analyse de risque, et 6 est le seuil du niveau de risque élevé (voir [Calcul des risques](risk-scoring.md)). Le champ **Risque** lui-même n'est pas proposé dans les conditions.

{% hint style="info" %}
Une violation dont le niveau a été fixé à la main dans **Conclusion de l'analyse du risque : niveau de risque estimé** garde son score : la règle suit le score et non le niveau que vous avez choisi.
{% endhint %}

### Actions

Ajoutez **Envoyer une notification Teams** et renseignez :

* **Titre de la carte** : `Violation à risque élevé : {{label}}` ;
* **Message** : `Score {{score}}. Vérifiez le délai de notification à l'autorité de contrôle.` ;
* **Inclure un lien vers l'objet dans la carte** : activé, ce qui est la valeur par défaut.

Saisissez `{{` dans un champ pour lister les variables de la violation de données.

### Résultat

Une carte apparaît dans le canal Teams associé au webhook, avec un lien vers la violation. Il n'y a pas de destinataire à choisir : le canal est celui configuré dans l'intégration. Cette action ne peut pas être essayée sans canal Teams, ce qui explique l'absence de capture d'écran pour cette recette.

## Recette 4 : envoyer une requête HTTP

Objectif : Créer un ticket dans le service desk de Brightmoor à chaque arrivée d'une demande.

Prérequis : L'intégration [HTTP / Custom API](../features/integrations/custom-http.md) est activée dans **Réglages espace de travail** > **Intégrations**, avec une connexion au service desk (clé d'API, identifiants Basic ou OAuth 2.0). L'ajout de cette action demande la permission **Intégrations**.

### Déclencheur

Type d'élément : **Demande**. Déclencheur : **Action**, événement **Création**.

### Conditions

**S'applique à tous les éléments**.

### Actions

Ajoutez **Envoyer une requête HTTP** et renseignez :

* **Méthode** : POST. **URL** : `https://servicedesk.brightmoor.example/api/tickets`.
* Onglet **Authentification** : la connexion du service desk. Les identifiants restent sur la connexion, jamais dans la règle.
* Onglet **Corps** : le format **JSON**, avec ce modèle :

```
{
  "summary": "{{title}}",
  "reference": "{{refId}}",
  "origin": "Dastra"
}
```

Cliquez sur **Tester la requête**. **Aperçu** génère l'URL, les en-têtes et le corps à partir d'une vraie demande de l'espace de travail sans rien envoyer. **Envoyer la requête** effectue l'appel réel et affiche la réponse du service desk. **Générer avec l'IA** rédige la requête à partir d'une consigne et du format attendu par le service desk.

<figure><img src="../.gitbook/assets/examples-workflow-2.png" alt="Action Envoyer une requête HTTP avec la méthode POST, l'URL et le corps JSON"><figcaption><p>L'action de requête HTTP</p></figcaption></figure>

### Résultat

Le service desk reçoit un ticket pour chaque nouvelle demande. Le corps généré doit être un JSON valide : sinon rien n'est envoyé et l'exécution est consignée en erreur. Chaque appel est tracé dans les journaux de l'intégration. Désactiver l'intégration ou supprimer la connexion désactive la règle.
