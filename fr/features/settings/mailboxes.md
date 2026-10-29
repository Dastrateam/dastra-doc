---
description: >-
  Créez automatiquement des objets dans Dastra à partir d'e-mails reçus sur des
  adresses de collecte dédiées.
---

# Adresses emails de collecte

Cette intégration crée automatiquement des objets dans Dastra à partir des e-mails reçus sur des adresses de collecte dédiées. Dastra met ces adresses à votre disposition et transforme chaque e-mail entrant en objet.

Cinq types d'objets peuvent être associés à une adresse de collecte :

* les tâches ;
* les traitements de données ;
* les demandes d'exercice de droits ;
* les contrats ;
* les violations de données.

## Mettre en place une adresse de collecte

L'installation demande la permission de gérer les intégrations dans l'espace de travail. Vous ne pouvez avoir qu'une seule adresse de collecte par type d'objet et par espace de travail.

1. Ouvrez **Réglages espace de travail** > **Intégrations**, puis cliquez sur la carte **Adresse mail de collecte**.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-1.png" alt="Le catalogue des intégrations avec la carte Adresse mail de collecte"><figcaption><p>La carte Adresse mail de collecte dans les intégrations</p></figcaption></figure>
2. Dans la liste des **Cas d'usage préconfigurés**, repérez le type d'objet que vous voulez alimenter et cliquez sur **Ajouter l'intégration**.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-2.png" alt="La liste des cinq cas d'usage de l'adresse de collecte, chacun avec le bouton Ajouter l'intégration"><figcaption><p>Un cas d'usage par type d'objet</p></figcaption></figure>
3. Dans le panneau qui s'ouvre, choisissez si besoin l'**Unité organisationnelle de destination** des objets créés. Si vous laissez ce champ vide, les objets sont créés dans l'unité organisationnelle par défaut.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-3.png" alt="Le panneau de configuration avec le champ Unité organisationnelle de destination et le bouton Enregistrer"><figcaption><p>Le choix de l'unité organisationnelle de destination</p></figcaption></figure>
4. Cliquez sur **Enregistrer**. Dastra finalise l'installation et affiche l'adresse e-mail à utiliser.

   <figure><img src="../../.gitbook/assets/settings-mailboxes-4.png" alt="Le panneau affichant l'adresse de collecte générée, avec le bouton de copie"><figcaption><p>L'adresse de collecte générée</p></figcaption></figure>

Pour supprimer une adresse de collecte, ouvrez de nouveau le panneau du cas d'usage et cliquez sur **Supprimer**. L'adresse est alors libérée et ne reçoit plus d'e-mails.

## Fonctionnement

* Chaque e-mail reçu sur une adresse de collecte crée un objet du type associé dans Dastra.
* L'objet est créé dans l'unité organisationnelle choisie à l'installation.
* Le sujet de l'e-mail devient le nom de l'objet.
* Le corps de l'e-mail devient la description de l'objet.
* Les pièces jointes de l'e-mail deviennent des pièces jointes de l'objet, sous les conditions décrites ci-dessous.

## Pièces jointes

Une pièce jointe est conservée lorsque :

* son extension est valide. Les extensions autorisées sont `7z`, `csv`, `doc`, `docx`, `eml`, `epub`, `gif`, `htm`, `html`, `jpeg`, `jpg`, `json`, `md`, `msg`, `ods`, `odg`, `odp`, `odt`, `pdf`, `png`, `ppt`, `pptx`, `rar`, `rtf`, `svg`, `txt`, `xls`, `xlsm`, `xlsx` et `zip` ;
* s'il s'agit d'une image (jpg, png, gif, etc.), elle pèse au moins 5 Ko. Cette limite évite d'ajouter des images sans intérêt, comme les logos des signatures d'e-mail.

## Retrouver les objets créés par une adresse de collecte

Les objets concernés ont un champ **source**, ou **origine de collecte**. Pour l'afficher dans un tableau, ajoutez la colonne correspondante.

Tous les objets créés depuis une adresse de collecte portent aussi le tag **Email entrant**, qui permet de les repérer.

## Notification de succès

Quand un objet est créé à la suite d'un e-mail reçu, Dastra envoie automatiquement une notification par e-mail à l'adresse qui a déclenché l'intégration. Cet e-mail confirme que l'objet a bien été créé dans Dastra.

L'e-mail de confirmation est rédigé dans la langue par défaut de l'espace de travail où l'intégration est installée (réglages de l'espace de travail, langue par défaut).

## Rediriger automatiquement vos e-mails existants vers Dastra

Si vous disposez déjà d'une adresse dédiée aux demandes d'exercice de droits (par exemple `privacy@votreentreprise.com`), vous n'avez pas besoin de la remplacer. Configurez une règle de redirection dans votre serveur de messagerie pour transférer les e-mails entrants vers l'adresse de collecte Dastra.

Les e-mails arrivent alors directement dans Dastra, sans intervention manuelle, et vos contacts continuent d'utiliser votre adresse habituelle.

### Avec Microsoft Exchange / Office 365

Ouvrez le **Centre d'administration Exchange** > **Flux de messagerie** > **Règles**, puis cliquez sur **+ Ajouter une règle**. Configurez la règle ainsi :

1. Condition : **L'expéditeur est situé** > **En dehors de l'organisation**. Vous pouvez ajouter un filtre sur des mots-clés de l'objet pour ne rediriger que les demandes pertinentes (par exemple, l'objet contient « demande » ou « droits »).
2. Action : **Rediriger le message vers**, puis saisissez l'adresse de collecte Dastra générée à l'étape précédente.
3. Mode : **Appliquer** (Enforce).

{% hint style="info" %}
Avec des filtres sur l'objet, vous redirigez seulement certains types de demandes (effacement, accès, portabilité, etc.) vers l'adresse de collecte correspondante, et vous gardez les autres messages dans votre boîte habituelle.
{% endhint %}

{% hint style="warning" %}
Vérifiez que votre règle ne crée pas de boucle de redirection si l'adresse Dastra redirige elle-même des e-mails. Utilisez la condition « Reçu de l'extérieur de l'organisation » pour éviter les boucles.
{% endhint %}

### Avec Google Workspace (Gmail)

Dans la **Console d'administration Google** > **Applications** > **Google Workspace** > **Gmail** > **Routage**, ajoutez une règle de routage entrant avec l'action **Modifier les destinataires**, puis saisissez l'adresse de collecte Dastra.
