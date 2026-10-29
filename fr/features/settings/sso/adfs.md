---
description: >-
  Dastra s'intègre avec Adfs, cette page vous explique les spécificités de la
  configuration du SSO avec AD FS
---

# ADFS

## Présentation d'ADFS

Les services de fédération Active Directory (généralement désignés sous l'acronyme ADFS) sont une solution d'authentification unique (SSO) conçue par Microsoft. Ces services, qui sont un composant des systèmes d'exploitation Windows Server, permettent aux utilisateurs de s'authentifier via Active Directory (AD) lorsqu'ils souhaitent accéder à une application qui ne peut pas utiliser l'authentification Windows intégrée (IWA).

## Configuration d'ADFS dans Dastra

**Étape 1 : créez un login SAML dans Dastra.**

* Allez sur la [page de configuration du SSO de Dastra](https://app.dastra.eu/general-settings/sso) (**Configuration de l'organisation** > **Single sign on**)
* Cliquez sur **Ajouter un login SSO**
* Sélectionnez **SAML2** dans **Choisir le protocole SSO**, puis **Configuration manuelle**
* Dans le champ **Identity Provider's Entity id (issuer)**, renseignez l'URL suivante : `http://<adfs server url>/adfs/services/trust`
* Dans le champ **Fournisseur d'identité (Identity Provider) single sign on url**, renseignez : `https://<adfs server url>/adfs/ls`

**Étape 2 : récupérez le certificat ADFS**

* Allez dans le répertoire **Certificates** du serveur ADFS
* Récupérez le certificat .CER de votre serveur ADFS en utilisant le certificat **Token-Signing**.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-certificates-view.png" alt="Le répertoire Certificates du serveur ADFS, avec le certificat Token-Signing"><figcaption></figcaption></figure>

* Cliquez sur **View Certificates**

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-certificate-export-wizard.png" alt="L'assistant d'exportation du certificat"><figcaption></figcaption></figure>

Ouvrez le fichier CER avec un éditeur de texte et copiez le code du certificat X509. Collez-le dans le champ du certificat, entre `-----BEGIN CERTIFICATE-----` et `-----END CERTIFICATE-----`.

La configuration de votre login devrait ressembler à ceci :

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-dastra-idp-configuration.png" alt="Le formulaire du login SAML dans Dastra, rempli avec les valeurs d'ADFS"><figcaption></figcaption></figure>

**Étape 3 : conservez les valeurs suivantes.**

* **SP redirect URI** (format : `https://account.dastra.eu/xxxxx-xxxx-xxxx-xxxx/Acs`) : l'URL de retour de l'application, à laquelle le jeton SAML est envoyé. Les algorithmes SHA-256 et supérieurs sont pris en charge. Copiez-la en haut du formulaire SAML.
* **Identity Provider's Entity id (issuer)**, affiché en haut du même formulaire.

Ces deux valeurs servent à configurer le serveur ADFS pour qu'il accepte les requêtes SSO de Dastra.

## Configuration du client Dastra dans ADFS

Voici comment configurer le SSO Dastra avec ADFS SSO SAML2P.

**Étape 1 :** sur votre serveur ADFS, ouvrez **AD FS Management**.

**Étape 2 :** faites un clic droit sur **Relying Party Trusts** et sélectionnez **Add Relying Party Trust**. L'assistant d'ajout de relying party trust se lance.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-relying-party-trust-menu.png" alt="Le menu Relying Party Trusts dans AD FS Management"><figcaption></figcaption></figure>

**Étape 3 :** sur l'écran **Select Data Source**, choisissez **Enter data about the relying party manually**.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-select-data-source.png" alt="L'écran Select Data Source de l'assistant"><figcaption></figcaption></figure>

**Étape 4 :** saisissez un **Display name**, par exemple « Dastra », puis cliquez sur **Next**.

**Étape 5 :** choisissez **AD FS profile** (SAML 2.0) et cliquez sur **Next**.

**Étape 6 :** sur l'écran **Configure Certificate**, cliquez sur **Next** sans choisir de certificat.

**Étape 7 :** sélectionnez **Enable support for the SAML 2.0 WebSSO protocol**.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-configure-url-saml.png" alt="L'écran Configure URL de l'assistant"><figcaption></figcaption></figure>

Dans le champ **Relying party SAML 2.0 SSO service URL**, saisissez l'URL **SP redirect URI** affichée dans Dastra. Elle a la forme `https://account.dastra.eu/xxxx-xxxx-xxxx-xxxx/Acs`.

**Étape 8 :** dans la partie **Relying party trust identifier**, ajoutez deux valeurs : `account.dastra.eu` et `https://account.dastra.eu`.

**Étape 9 :** cliquez sur **Next** jusqu'à la fin de l'assistant.

**Étape 10 :** cochez la case **Open the Edit Claim Rules dialog** avant de cliquer sur **Close**. La fenêtre **Edit Claim Rules** s'affiche.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-relying-party-trust-finish.png" alt="La dernière étape de l'assistant avec l'option Edit Claim Rules"><figcaption></figcaption></figure>

**Étape 11 :** cliquez sur **Add Rule** et choisissez le modèle de règle **Send LDAP Attributes as Claims**.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-claim-rule-template-ldap.png" alt="La liste des modèles de règles de claims"><figcaption></figcaption></figure>

**Étape 12 :** mappez les claims comme ci-dessous. Les noms des claims peuvent varier selon la configuration de votre serveur. Dastra a besoin de trois attributs : l'e-mail (obligatoire), le nom et le prénom de l'utilisateur.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-claim-rule-configure-ldap.png" alt="Le mappage des attributs LDAP vers les claims sortants"><figcaption></figcaption></figure>

**Étape 13 :** cliquez sur **Finish**, puis de nouveau sur **Add Rule**. Cette fois, choisissez le modèle **Transform an Incoming Claim** et cliquez sur **Next**.

**Étape 14 :** configurez la règle suivante : **Email Address** => **Name ID** => **Email**.

<figure><img src="../../../.gitbook/assets/settings-sso-adfs-claim-rule-configure-nameid.png" alt="La règle Transform an Incoming Claim configurée pour le Name ID"><figcaption></figcaption></figure>

Appliquez ensuite les changements en cliquant sur **Apply**.

**Étape 15 :** de retour dans la fenêtre **AD FS Management**, faites un clic droit sur le relying party de Dastra et choisissez **Properties**. Dans l'onglet **Advanced**, choisissez SHA-256 comme algorithme sécurisé.

**Étape 16 :** la configuration est terminée.

## Fin et tests

Une fois que tout est configuré des deux côtés, retournez dans Dastra et cliquez sur **Tester**, à droite de la connexion dans la liste des logins SSO.
