---
description: >-
  Apprenez comment importer, créer, modifier et supprimer une demande d'exercice
  de droits via Dastra.
---

# Gestion des demandes d'exercices de droits

{% embed url="https://youtu.be/ZNY5oz9xJVo" %}

## Création d'une demande de droit

Une demande de droit peut être créée de 5 manières dans Dastra :

1. Manuellement, depuis le registre des demandes.
2. Par import d'un fichier (voir [Import et export des demandes](manage.md#import--export-des-demandes)).
3. Automatiquement, via une adresse e-mail de collecte.
4. Automatiquement, via un formulaire de collecte de demandes.
5. Automatiquement, via l'API REST.

### Création d'une demande manuellement

{% embed url="https://youtu.be/UsTkoYcqYkI" %}

Pour créer une demande manuellement depuis le registre, cliquez sur **Demandes** dans la barre latérale, puis sur **Registre des demandes** et sur le bouton **Créer une demande**.

<figure><img src="../../.gitbook/assets/requests-manage-1.png" alt="Le registre des demandes, avec le bouton Créer une demande"><figcaption><p>Le registre des demandes</p></figcaption></figure>

{% hint style="info" %}
Vous pouvez également créer des demandes automatiquement (voir ci-dessous).
{% endhint %}

### Création d'une demande via une adresse e-mail de collecte

{% embed url="https://youtu.be/Lxhzm7wjFwk" %}

Pour créer une ou plusieurs demandes à partir d'une adresse e-mail de collecte, activez d'abord l'intégration **Adresse mail de collecte** (voir [la page de l'intégration](../settings/mailboxes.md)).

Pour cela, ouvrez **Réglages espace de travail**, puis la section **Intégrations** et cliquez sur la carte **Adresse mail de collecte**.

<figure><img src="../../.gitbook/assets/requests-manage-2.png" alt="La carte de l'intégration Adresse mail de collecte"><figcaption><p>L'intégration « Adresse mail de collecte » dans Dastra</p></figcaption></figure>

{% hint style="info" %}
Si cette intégration n'est pas encore installée, installez-la. Depuis le registre des demandes, l'entrée **Transformer emails en demandes de droits** du menu du bouton **Créer une demande** y mène directement.
{% endhint %}

Dans la liste **Cas d'usage préconfigurés**, cliquez ensuite sur **Ajouter l'intégration** sur la ligne **Transforme un mail entrant en une demande avec les pièces jointes associées**. Une adresse e-mail est générée automatiquement.

<figure><img src="../../.gitbook/assets/requests-manage-3.png" alt="Le cas d'usage préconfiguré qui transforme un e-mail entrant en demande"><figcaption></figcaption></figure>

Chaque e-mail envoyé à cette adresse devient alors une demande dans Dastra, avec ses pièces jointes.

### Création d'une demande via un formulaire de collecte

Pour créer des demandes automatiquement à partir d'un formulaire de collecte (widget), voir la page « Implémenter un widget d'exercice des droits » :

{% content-ref url="widget.md" %}
[implementez-un-widget-dexercice-des-droits.md](widget.md)
{% endcontent-ref %}

### Création d'une demande via l'API

Les demandes peuvent aussi être créées depuis un autre outil grâce à l'API REST de Dastra. Voir la page « Intégration de l'API » :

{% content-ref url="api.md" %}
[api.md](api.md)
{% endcontent-ref %}

## Import / Export des demandes

{% embed url="https://youtu.be/31AMZz-DMm8" %}

Cliquez sur la flèche à côté du bouton **Créer une demande**, puis sur **Importer**.

Suivez ensuite le guide d'[import de données dans Dastra](../general/import.md).

Pour exporter, cliquez sur **Exporter** dans le même menu.
