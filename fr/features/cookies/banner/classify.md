---
description: Apprenez à classifier les cookies par catégories de consentement.
---

# Classifiez les cookies par catégories de consentement

Dans son [projet de recommandation](https://www.cnil.fr/fr/la-cnil-lance-une-consultation-publique-sur-son-projet-de-recommandation-cookies-et-autres-traceurs) « cookies et autres traceurs », la CNIL recommande de recenser et catégoriser les cookies sur son site internet, selon qu’ils nécessitent un consentement ou non.

{% hint style="info" %}
Pour plus d'information sur les recommandations de la CNIL sur les cookies, consultez l'article « [Les recommandations de la CNIL sur les cookies expliquées à votre boss](https://www.dastra.eu/fr/article/recommendations-CNIL-cookies-expliquees-a-votre-boss/104) ».
{% endhint %}

Dans Dastra, la catégorie d'un cookie est celle du service auquel il est rattaché : vous choisissez la **finalité** de chaque service, et tous ses cookies en héritent. Les catégories proposées sont :

* **Strictement nécessaires** : cookies exemptés de consentement de par leur nature, par exemple les cookies de session ou de consentement ;
* **Préférences** ;
* **Analyse d'audience** ;
* **Marketing et expérience utilisateur** ;
* **Réseaux sociaux** ;
* **Autre**.

{% content-ref url="purposes.md" %}
[purposes.md](purposes.md)
{% endcontent-ref %}

## Choisissez la finalité d'un service

1. Ouvrez la bannière : **Consentement cookies** > **Bannières**, puis cliquez sur la bannière.
2. Dépliez la section **Services**.
3. Cliquez sur le service à classifier. Dans l'onglet **Informations de base**, choisissez la valeur du champ **Finalité de ce service**.
4. Validez, puis cliquez sur **Enregistrer**.

<figure><img src="../../../.gitbook/assets/cookies-classify-1.png" alt="La section Services de l'éditeur de bannière, avec la finalité affichée sous le nom de chaque service"><figcaption><p>La finalité de chaque service est affichée sous son nom</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/cookies-classify-2.png" alt="Le formulaire d'un service avec le champ Finalité de ce service"><figcaption><p>Le champ « Finalité de ce service » dans le formulaire d'un service</p></figcaption></figure>

Un service ne peut pas être enregistré avec la finalité « Non classés » : choisissez une des catégories ci-dessus.

{% hint style="info" %}
Vous définissez au cas par cas si le consentement doit être demandé pour un service grâce à l'option **Demander le consentement pour ces cookies ? (affichage des boutons)**. Elle est désactivée pour la catégorie **Strictement nécessaires**.
{% endhint %}

{% hint style="warning" %}
Un cookie détecté par le scan mais rattaché à aucun service (cookie non classé) n'est jamais affiché dans la bannière publique. Rattachez-le à un service existant ou créez un service à partir de celui-ci : voir [Traitez les cookies non classés](scan.md#traitez-les-cookies-non-classes).
{% endhint %}

Une fois tous vos cookies rattachés à un service classé par catégorie, vous pouvez configurer la bannière.

{% content-ref url="configure.md" %}
[configure.md](configure.md)
{% endcontent-ref %}
