---
description: Cette page détaille la mise en place du SSO au sein de Dastra
---

# Single Sign On (SSO)

## Principe de fonctionnement

L'**authentification unique**, souvent désignée par le sigle anglais **SSO** (de single sign-on) est une méthode permettant à un utilisateur d'accéder à plusieurs applications informatiques (ou sites web sécurisés) en ne procédant qu'à une seule authentification.

L'entreprise peut utiliser **son propre système d'authentification** à la place du login local proposé par défaut par Dastra. Parmi les systèmes SSO les plus utilisés, on peut citer Microsoft Active Directory, Google Workspace (ex GSuite), Auth0, etc.

**Le fonctionnement est le suivant :**&#x20;

Un utilisateur (**User Agent**) va solliciter une connexion au fournisseur de service (**Service Provider**) qui ira solliciter un fournisseur d'identité (**Identity Provider**) qui authentifiera l'utilisateur. Cette authentification est ensuite renvoyée adressée au fournisseur du service qui acceptera la demande de connexion de l'utilisateur.&#x20;

Dans notre cas, le User Agent est le **navigateur d'un utilisateur de Dastra**. Le Service Provider est **Dastra** et l'Identity Provider est votre **fournisseur d'authentification favori** (par exemple : Active Directory).  &#x20;



![Principe de fonctionnement du SSO en utilisant le protocole SAML 2](<../../../.gitbook/assets/image (115).png>)

## Mise en place

Au sein d'un abonnement à Dastra, vous avez la possibilité, si vous avez souscrit à la fonctionnalité, de gérer un ou plusieurs login SSO. Pour accéder à la configuration du SSO, allez sur [la page de configuration des logins SSO](https://app.dastra.eu/general-settings/sso) dans l'onglet sécurité du panel de configuration du compte d'abonnement.

{% hint style="info" %}
**Attention** : vous devez être propriétaire de l'organisation pour accéder à cette page.
{% endhint %}

Dastra propose deux protocoles d'authentification unique, [**SAML 2**](saml-2.md) et [**Open ID**](openid.md). Pour accéder à l'aide de configuration, cliquez sur les liens ci-dessous.&#x20;

{% content-ref url="saml-2.md" %}
[saml-2.md](saml-2.md)
{% endcontent-ref %}

{% content-ref url="openid.md" %}
[openid.md](openid.md)
{% endcontent-ref %}

{% content-ref url="adfs.md" %}
[adfs.md](adfs.md)
{% endcontent-ref %}

## Comment activer le provisionnement automatique des utilisateurs ?

Si vous souhaitez que les utilisateurs de votre fournisseur d'identité n'ait pas besoin de se créer des comptes pour accéder à l'entité, vous pouvez cocher la case "provisionnement automatique des utilisateurs". Si vous fournissez à vos utilisateurs une url de fournisseur SSO comme celle-ci : https://account.dastra.eu/account/loginexternal?provider={id de votre provider}\&returnUrl=https://www.dastra.eu&#x20;

\=> dans le cas d'une authentification validée, ils auront automatiquement un compte créé dans Dastra.

{% hint style="warning" %}
Si le compte de l'utilisateur est supprimé ou invalidé dans le fournisseur d'authentification, son compte ne sera pas effacé dans Dastra, il ne pourra en revanche plus se connecter. Vous avez la possibilité d'épurer ses comptes[ via le gestionnaire d'utilisateur de l'abonnement](https://app.dastra.eu/general-settings/users)
{% endhint %}

Vous pouvez choisir **le rôle assigné par défaut** sur toutes les organisations associées à votre abonnement.

![](<../../../.gitbook/assets/image (124).png>)

{% hint style="info" %}
Pour l'instant, Dastra ne supporte pas le binding des rôles via les propriétés du serveur d'authentification. Si cette fonctionnalité est importante, vous pouvez nous le remonter via la [page de support](https://app.dastra.eu/general-settings/support).
{% endhint %}



### Binding des équipes

Il est possible de binder les équipes d'un espace de travail sur une propriété (Claim) renvoyé par votre serveurs d'authentification.

<figure><img src="../../../.gitbook/assets/image (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>



## Comment administrer les logins des utilisateurs ?

Vous pouvez configurer le type de login des utilisateurs en vous rendant dans [la page de gestion des utilisateurs de l'abonnement](https://app.dastra.eu/general-settings/users) . En vous rendant dans un profil utilisateur, il sera possible de choisir le login SSO privilégié. Dès lors, l'utilisateur qui se connecte à Dastra avec son adresse email, sera automatiquement redirigé vers la page de login du fournisseur d'authentification que vous avez mis en place.

![](<../../../.gitbook/assets/image (118).png>)

Vous pourrez également définir le type de login lors de l'invitation de nouveaux utilisateurs.
