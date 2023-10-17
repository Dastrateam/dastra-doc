# TCF 1.1/2.0

{% hint style="danger" %}
**Pour l'instant, cette fonctionnalité est encore en phase expérimentale. Toute implémentation du TCF ne sera pas effective**&#x20;
{% endhint %}

Le [consent management platform (CMP) framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) est actuellement supporté par le widget Dastra. Pour activer l'optin des vendors de l'IAB, il vous suffit de vous rendre dans la partie "services" de la configuration du widget et d'activer la case correspondante.

Une fois la case cochée, vous pouvez observer les modifications dans l'interface du widget :

![](<../../../.gitbook/assets/image (69).png>)

Automatiquement, lors de l'optin de l'IAB, le cookie contenant les informations encodés sur le consentement de l'utilisateur aux vendeurs de l'IAB sont automatiquement créées dans le navigateur :

![](<../../../.gitbook/assets/image (71).png>)

{% hint style="info" %}
Ce cookie a une durée de vie par défaut de 180 jours et est nommé "eupubconsent"
{% endhint %}

### Capturer la chaîne du consentement de l'IAB

Lorsque l'utilisateur applique son consentement, il est possible de capter la chaîne du consentement directement en utilisant l'écouteur d’événement suivant :

```javascript
document.addEventListener('dastra:consentstring',function(consentString){
    console.log(consentString); // BOybBVKOybbNhABABBENCoAAAAAq6AAA
});
```
