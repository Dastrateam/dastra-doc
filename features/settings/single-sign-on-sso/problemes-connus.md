# Problèmes connus

## L'utilisateur n'est pas reconnu par le SSO

Plusieurs raisons peuvent provoquer des erreurs dans la connexion SSO d'un utilisateur.&#x20;

Si une erreur indique que l'utilisateur ne peut pas accéder à l'application, assurez vous des choses suivantes :&#x20;

* Avez vous vérifié que la configuration du SSO ne présente pas d'erreur ? Vous pouvez vous en assurer en appuyant sur le bouton Tester sur la connexion. Si cela fonctionne, c'est que la configuration est bonne. Sinon, c'est qu'une erreur s'est glissée dans la configuration.&#x20;
* Est ce que l'utilisateur est bien attaché à l'organisation ? Il est nécessaire que l'utilisateur soit présent dans la liste des utilisateurs de l'organisation. En effet, le SSO est associé à l'organisation.&#x20;
* Si l'utilisateur a déjà créé un compte utilisateur (par exemple dans une autre organisation ou dans le cadre d'un compte de test), assurez vous que l'organisation dans laquelle vous avez configuré le SSO est bien son organisation principale (pour cela, il faut aller dans la [liste des utilisateurs de l'organisation](https://app.dastra.eu/general-settings/users)). L'utilisateur doit figurer en tant qu'utilisateur interne. Si ce n'est pas le cas, cela signifie qu'une organisation gère sa connexion à Dastra (son organisation principale), il sera alors indiqué comme utilisateur externe.&#x20;
* Si l'utilisateur n'a jamais créé de compte&#x20;

## Message d'erreur

Vous rencontrez un message d'erreur de ce type  :

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

1. Assurez d'avoir un certificat valide.
2. Vérifiez que le copier/coller du certificat n'a pas inclus de saut de ligne ou de création d'espace

