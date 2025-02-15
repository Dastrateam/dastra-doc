---
description: >-
  Cette page de documentation explique comment Dastra s'intègre nativement à
  votre fournisseur de fichiers cloud préféré pour le stockage des fichiers de
  la GED
---

# Intégrations OneDrive/Google Drive

### Intérêt du stockage cloud personnalisé

Par défaut, la [GED de Dastra](../gestion-de-documents-ged/) s'appuie sur un système de stockage standard sécurisé basé sur Azure Blob Storage. Les fichiers sont chiffrés et analysés par un antivirus. Les fichiers sont redondés sur un autre serveur. Pour en savoir plus, consultez [notre documentation sur la sécurité de Dastra](../../security/general.md)

Bien que très sécurisé et pratique dans la plupart des scénarios, le stockage des fichiers dans l'application Dastra peut faire doublon avec d'autres GED ou gestionnaire de fichiers cloud. Pour remédier à ce problème, Dastra s'intègre nativement aux principaux fournisseur de fichiers sur le cloud.

<figure><img src="../../.gitbook/assets/image (252) (1).png" alt=""><figcaption><p>Les fichiers de la GED de Dastra peuvent être stockés dans plusieurs sites de stockage différents</p></figcaption></figure>

### Configurer un stockage cloud personnalisé

Pour configurer votre gestionnaire de fichiers cloud, c'est très simple :

* Rendez-vous dans le [gestionnaire de fichier](https://app.dastra.eu/workspace/0/referentials/folders)
* Cliquez sur le **sélecteur en haut à gauche des fichiers** :&#x20;

![image.png](https://static.dastra.eu/richtextbackoffice/511cd52b-858d-482b-805f-e0ed97f018a7/image.png)

* Cliquez sur **Gérez le stockage cloud**
* Choisissez votre fournisseur (Google Drive ou OneDrive)

![](<../../.gitbook/assets/image (257) (1).png>)

* **Cliquez sur le bouton "Ajouter"**, vous allez être redirigé vers la page de login du fournisseur qui vous demandera les autorisations nécessaires à l'établissement de la connexion avec Dastra.&#x20;
* A la fin du processus, vous allez choisir le disque du drive que vous souhaitez utiliser (Un drive google ou un disque sharepoint pour OneDrive)

### Attacher des fichiers de votre cloud à Dastra

* **Editez n'importe quelle entité** : tâche, traitement, acteur...&#x20;
* **Choisissez la source de donnée** en haut à gauche de la boîte permettant de charger les fichiers.

![](<../../.gitbook/assets/image (254) (1).png>)

* Envoyez des fichiers directement sur votre Drive (Modifiez les, déplacez les)
* Cliquez sur **sélectionnez dans le gestionnaire**. et choisissez le fichier à attacher

![](<../../.gitbook/assets/image (255).png>)



### Limitations

**Google Drive** : attention, uniquement les fichiers créés depuis votre espace Dastra pourront être ajoutés ou modifiés à votre Google Drive. Dastra n'a pas les droits d'accès pour accéder à des fichiers créés de votre côté dans le Drive. C'est une limitation de ce connecteur. Vous pouvez partager les fichiers créés dans Dastra avec d'autres collaborateurs sans problème.

**One Drive :** le système n'a été testé que sur la version personnelle de OneDrive.  Si vous rencontrez des problèmes avec les versions entreprise, n'hésitez pas à [contacter le support](https://www.dastra.eu/fr/contact?type=support)

Par défaut Dastra va créer des fichiers dans le répertoire "**Applications\DastraOneDrive**" qu'il considèrera comme sa racine

{% hint style="warning" %}
Attention ! La mise en place de la connexion OneDrive **donne un accès à l'ensemble des fichiers de votre Drive personnel**. Il faut donc être très prudent, car le connecteur sera mis à disposition à l'ensemble des utilisateurs disposant du droit de lecture "Fichiers".

Il est recommandé de créer un lecteur OneDrive dédié, vous pouvez suivre ce [guide de création de site dédié dans sharepoint](https://learn.microsoft.com/en-us/sharepoint/create-site-collection).
{% endhint %}
