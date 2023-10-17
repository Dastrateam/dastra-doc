---
description: >-
  Dastra s'intègre avec Adfs, cette page vous explique les spécificités de la
  configuration du SSO avec AD FS
---

# ADFS

## Qu'est ce que l'ADFS ?

Les services de fédération Active Directory (généralement désignés sous l'acronyme ADFS) sont une solution d'authentification unique (SSO) conçue par Microsoft. Ces services, qui sont un composant des systèmes d'exploitation Windows Server, permettent aux utilisateurs de s'authentifier via Active Directory (AD) lorsqu'ils souhaitent accéder à une application qui ne peut pas utiliser l'authentification Windows intégrée (IWA).

## **Configuration de ADFS dans Dastra**

**Etape 1 : Créez un login SAML dans Dastra.**

* Allez sur la [page de configuration du SSO de Dastra](https://app.dastra.eu/general-settings/sso)
* Cliquez sur "Ajouter un login SSO"
* Sélectionnez **SAML** en type de "**Protocole du SSO**"
* Dans le champ "Identity Provider's Entity id (issuer)", renseignez l'url suivante : [**http**://\<adfs server url>/adfs/services/trust](http://fs.saur.fr/adfs/services/trust)&#x20;
* Dans le champ "**Fournisseur d'identité (Identity Provider) single sign on url**" "[**https**://\<adfs server url>](http://fs.saur.fr/adfs/services/trust)/adfs/ls

**Etape 2 : Récupérez le certificat ADFS**&#x20;

* Allez dans le répertoire "**Certificates**" du serveur ADFS
* Récupérez le certificat .CER de votre serveur ADFS en utilisant le certificat "**Token-Signing**".&#x20;

![](<../../../.gitbook/assets/image (259).png>)

* Cliquez sur "**View Certificates**"

![](<../../../.gitbook/assets/image (250).png>)

Copiez le code du certificat X509 Certificate en ouvrant le fichier CER avec un éditeur de texte.&#x20;

Insérez le code du certificat dans le champ du certificat qui commence par "----BEGIN CERTIFICATE-----" et termine par "--------END CERTIFICATE-----".

La configuration de votre login devrait ressembler à ceci :&#x20;

![](<../../../.gitbook/assets/image (257).png>)

**Etape 3** : Conservez les valeurs suivantes :&#x20;

* **SP redirect URI (format : https://account.dastra.eu/xxxxx-xxxx-xxxx-xxxx/Acs) :**The SP redirect URI is Application Callback URL (SAML Token will be posted here). The encoding supported are SHA-256 and higher.&#x20;
* **Identity Provider's Entity id (issuer)**

Ces deux valeurs vous serviront à configurer le serveur ADFS pour qu'il accepte les requêtes SSO de Dastra

## Configuration du client Dastra dans ADFS

Voici comment configurer le SSO Dastra avec ADFS SSO SAML2P

**Etape 1** : Sur votre serveur ADFS, ouvrez "AD FS Management"

**Etape 2 :** Cliquez à droite sur **"Relying Party Trusts**" et sélectionnez" **Add Relying Party Trust**". Ceci lancera l'assistant d'ajout de **Relying Party Trust**.



&#x20;![](<../../../.gitbook/assets/image (248).png>)

**Etape 3 :**  Dans l'écran _**Select Data Source**_ choisissez _**Enter data about the relying party manually**_.&#x20;



&#x20;![](<../../../.gitbook/assets/image (254).png>)

**Etape 4 :**  Entrez un _**Display name** , par exemple **"Dastra"**_ _puis cliquez sur **"Next"**_

**Etape 5 :** Choisissez _**AD FS profile**_ with SAML 2.0 et cliquez sur "**Next**"

**Etape 6** :  Cliquez sur _**Next**_ sur l'écran _**Configure Certificate** sans choisir de certificat_

**Etape 7 :** Sélectionnez "_**Enable support for the SAML 2.0 SSO Web SSO protocol**_."

![](<../../../.gitbook/assets/image (252).png>)&#x20;

Dans le champ "Relying party SAML 2.0 SSO service URL: mettre l'url de "**SP redirect URI "** présente dans la Dastra. Cette url est de la forme : https://account.dastra.eu/xxxx-xxxx-xxxx-xxxx/Acs

**Etape 8** : Dans la partie "**Add a Relying party trust identifier**", **Ajoutez deux valeurs** : _account.dastra.eu_ et _https://account.dastra.eu_

**Etape 9** : Cliquez sur suivant jusque la fin du processus.&#x20;

**Etape 10** : Cochez la case _**Open the Edit Claim Rules dialog**_ avant de cliquer sur "terminer". Une fenêtre "_**Edit Claim Rules"**_ va alors s'afficher.&#x20;

![](<../../../.gitbook/assets/image (251).png>)

\
**Etape 11** : Cliquez sur _**Add Rule**_ et choisissez la "Claim Rule" : "_**Send LDAP Attributes as Claims"**_.

![](<../../../.gitbook/assets/image (256).png>)

**Etape 12** : Mappez les claims de la façon suivante, les noms des claims peuvent varier selon la configuration de votre serveur. Dastra a besoin de trois attributs pour fonctionner : Email (Obligatoire), Nom et Prénom de l'utilisateur :

&#x20;![](<../../../.gitbook/assets/image (258).png>)

**Etape 13** : Cliquez sur "**Finish**" et cliquez de nouveau sur "**Add Rule**". Cette fois-ci, choisissez le type "_**Transform an Incoming Claim"** et cliquez sur suivant._

**Etape 14 :**  Configurez la règle suivante **:  Email Address => Name ID => Email**

![](<../../../.gitbook/assets/image (249).png>)

Appliquez ensuite les changements en cliquant sur "Apply"

**Etape 15** : De retour dans la fenêtre "**AD FS Management**", cliquez droit sur "**Relying Party for Dastra**" et choisissez "**properties**". Dans l'onglet _**Advanced**_ , choisissez **SHA­-256** en tant qu'algorithme sécurisé.\
&#x20;

**Etape 16** :  Vous avez réussi !

## **Fin et tests !**

Une fois que tout est configuré des deux côtés vous pouvez retourner dans Dastra et lancer un test de login SSO directement dans le gestionnaire.



