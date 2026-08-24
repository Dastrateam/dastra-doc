# Questions fréquentes

### Les demandeurs reçoivent-ils une notification par e-mail lors de la clôture d'une demande ? <a href="#comment-afficher-lhistorique-des-modifications-sur-un-traitement" id="comment-afficher-lhistorique-des-modifications-sur-un-traitement"></a>

Par défaut, aucun e-mail n'est envoyé automatiquement. La notification de clôture est envoyée au demandeur **uniquement si la case "Envoyer une notification de clôture de la demande à"** est explicitement cochée au moment de la clôture.

{% hint style="info" %}
Pensez à cocher cette option systématiquement lorsque vous souhaitez informer la personne concernée de la résolution de sa demande — c'est une bonne pratique pour démontrer le respect du délai de réponse imposé par le RGPD.
{% endhint %}

***

### Pendant combien de temps le demandeur a-t-il accès à l'espace sécurisé après la clôture ?

Une fois la demande clôturée, le demandeur conserve un accès à son espace sécurisé (historique des échanges, documents transmis) pendant **60 jours**.

Cet accès lui permet également de délivrer un message au gestionnaire de la demande via l'interface de conversation.&#x20;

Au-delà de cette période, l'accès est révoqué automatiquement.<br>

***

### La page de collecte des demandes pose-t-elle des cookies ? Faut-il un bandeau de consentement ?

Non. La page widget Dastra (URL de type `https://api.dastra.eu/v1/client/data-subject-request/page?id=…`) ne pose **qu'un seul cookie** : `acaAffinity`.

Il s'agit d'un cookie de **load balancing** (Azure Application Gateway), dont la seule fonction est de maintenir la stabilité de la session serveur en routant les requêtes vers le même nœud backend. Il est de durée **session**, sécurisé (`Secure`, `HttpOnly`) et entre dans l'**exemption de consentement** prévue à l'article 5§3 de la directive ePrivacy, confirmée par les lignes directrices de la CNIL (cookies strictement nécessaires au fonctionnement du service).

**Aucun bandeau de consentement n'est requis sur cette page.**

{% hint style="success" %}
Audit réalisé le 27 avril 2026 : 0 cookie analytique, 0 cookie publicitaire, 0 tracker tiers détecté. Les ressources tierces chargées (Bootstrap via cdnjs.cloudflare.com, police Poppins via fonts.bunny.net, SDK via cdn.dastra.eu) ne posent aucun cookie.
{% endhint %}

***

### Le cookie `acaAffinity` doit-il figurer dans notre registre des cookies ?

Oui, par souci d'exhaustivité documentaire, même s'il est exempté de consentement. Voici l'entrée recommandée :

| Champ               | Valeur                                          |
| ------------------- | ----------------------------------------------- |
| Nom                 | `acaAffinity`                                   |
| Domaine             | `api.dastra.eu`                                 |
| Catégorie           | Technique / Strictement nécessaire              |
| Finalité            | Load balancing — stabilité de session serveur   |
| Durée               | Session (supprimé à la fermeture du navigateur) |
| Émetteur            | Dastra (sous-traitant)                          |
| Base légale         | Exemption ePrivacy — strictement nécessaire     |
| Consentement requis | Non                                             |

