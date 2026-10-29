---
description: >-
  Configurer Okta comme fournisseur d'identité dans Dastra avec le protocole
  OpenID Connect.
---

# Okta

Cette page explique comment configurer le login Okta en SSO dans Dastra avec le protocole **OpenID Connect**. Il est également possible de le faire avec SAML : voir [SAML 2](saml.md).

1. Connectez-vous à la console d'administration d'Okta.
2. Ouvrez le menu **Applications** > **Applications**, puis cliquez sur **Create App Integration**.

   ![Le menu Applications d'Okta avec le bouton Create App Integration](../../../.gitbook/assets/settings-sso-okta-home.png)
3. Sélectionnez **OIDC - OpenID Connect**.

   ![Le choix du type de connexion dans Okta](../../../.gitbook/assets/settings-sso-okta-select.png)
4. Sélectionnez le type d'application **Web application**.

   ![Le choix du type d'application dans Okta](../../../.gitbook/assets/settings-sso-okta-app-type.png)
5. Configurez l'application et cochez **Implicit (hybrid)** dans **Grant type**. Pour le logo de l'application, vous pouvez [utiliser celui-ci](https://www.dastra.eu/img/press/logodastra.png).

   ![La configuration générale de l'application dans Okta, avec Implicit (hybrid) coché](../../../.gitbook/assets/settings-sso-okta-config.png)
6. Dans Dastra, récupérez l'URL de redirection : ouvrez [la page de gestion du SSO](https://app.dastra.eu/general-settings/sso), cliquez sur **Ajouter un login SSO** et choisissez **OpenID**. Dans la section **Configuration**, vers le bas du formulaire, copiez l'URL de redirection.

   <figure><img src="../../../.gitbook/assets/settings-okta-1.png" alt="Le bas de la section Configuration du formulaire OpenID, avec l'URL de redirection à copier"><figcaption><p>L'URL de redirection affichée par Dastra</p></figcaption></figure>
7. Retournez dans Okta et collez l'URL de redirection dans **Sign-in redirect URIs**. Sélectionnez les utilisateurs d'Okta à qui vous souhaitez donner accès à Dastra (par défaut, vous pouvez cocher **Allow everyone**), puis cliquez sur **Save**.

   ![Le champ Sign-in redirect URIs d'Okta](../../../.gitbook/assets/settings-sso-okta-redirecturi-config.png)
8. Okta affiche la page des paramètres de la nouvelle application : l'identifiant du client (Client ID), la clé secrète (Client secret) et le domaine Okta, qui sert d'autorité.

   ![Les identifiants du client dans Okta](../../../.gitbook/assets/settings-sso-okta-client-settings.png)

   ![Le domaine Okta, à reprendre avec le protocole https://](../../../.gitbook/assets/settings-sso-okta-domain.png)
9. Retournez dans Dastra et renseignez les champs du formulaire :

   * **Id du client (ClientId)** : copiez le Client ID d'Okta.
   * **Authority/Domain** : saisissez le domaine d'Okta avec le protocole (`https://<votre domaine>.okta.com`).
   * **Issuer** : laissez le champ vide.
   * **Clé secrète** : copiez la clé secrète d'Okta.
   * **Scope** : `openid profile email`.
   * **Type de réponse** : `id_token`.

   <figure><img src="../../../.gitbook/assets/settings-okta-2.png" alt="Le formulaire OpenID de Dastra rempli avec les valeurs d'Okta, les valeurs secrètes étant masquées"><figcaption><p>Le formulaire OpenID de Dastra</p></figcaption></figure>
10. Cliquez sur **Enregistrer**, puis sur **Tester** sur la carte de la connexion. Si Okta vous redirige vers Dastra, la configuration est terminée.
