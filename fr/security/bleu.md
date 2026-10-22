---
description: >-
  Dastra est disponible sur Bleu, le cloud souverain opéré en France par
  Orange et Capgemini : une instance dédiée, isolée de notre plateforme SaaS
  standard, dont les données ne quittent pas le périmètre Bleu.
---

# Dastra sur Bleu (cloud souverain)

## À qui s'adresse cette offre ?

Certaines organisations ne peuvent pas ou ne souhaitent pas héberger leurs données de conformité sur une infrastructure exposée aux lois extraterritoriales non européennes. Dastra permet de répondre à ces exigences à travers **Bleu** : une instance dédiée, distincte de notre plateforme SaaS standard, dont les données ne quittent pas le périmètre Bleu.

## Qu'est-ce que Bleu ?

Bleu est une société française détenue par **Orange et Capgemini**, qui distribue Microsoft Azure et Microsoft 365 dans un environnement isolé de l'infrastructure mondiale de Microsoft. Les services sont hébergés dans des datacenters situés en France (Île-de-France et sud de la France) et opérés exclusivement par des équipes françaises. L'offre vise l'État, les collectivités, les établissements de santé, les OIV et les OSE, et apporte une protection juridique contre les lois d'accès extraterritoriales (Cloud Act, FISA).

## Qualification SecNumCloud : où en est-on ?

La qualification **SecNumCloud 3.2** est délivrée par l'ANSSI à l'issue de quatre jalons. Pour son périmètre IaaS, PaaS et CaaS, Bleu a franchi **J0** (avril 2025, dossier accepté) et **J1** (novembre 2025, stratégie d'évaluation acceptée). Bleu figure sur la liste des prestataires SecNumCloud en cours de qualification publiée par l'ANSSI. Les étapes suivantes, l'évaluation sur site (**J2**) puis la décision de qualification (**J3**), ne sont pas encore annoncées comme franchies ; Bleu estime finaliser le processus d'ici la fin de l'année 2026.

{% hint style="warning" %}
Nous ne présentons donc pas Dastra sur Bleu comme une offre « SecNumCloud qualifiée » tant que l'ANSSI n'a pas publié sa décision.
{% endhint %}

## Ce qui change par rapport à l'offre standard

| | Offre standard | Offre Bleu |
| --- | --- | --- |
| Application | app.dastra.eu | app-bleu.dastra.eu |
| API | api.dastra.eu | api-bleu.dastra.eu |
| Authentification | account.dastra.eu | <p>account-bleu.dastra.eu<br>(annuaire d'utilisateurs, comptes et clés de signature distincts)</p> |
| Provisioning SCIM | scim.dastra.eu | scim-bleu.dastra.eu |
| Hébergement | Microsoft Azure France (Paris, Marseille) | Bleu France Central (Île-de-France) |
| Fonctionnalités d'IA | Disponibles | Disponibles, exécutées par **Mistral AI** (société française, hors périmètre Bleu) et non par Azure OpenAI |
| Recherche plein texte | Disponible | Disponible, index hébergé sur Bleu |
| Connecteurs (Jira, ServiceNow, SAP LeanIX, DocuSign, Zapier, etc.) et clés d'API | Disponibles | Disponibles |
| SSO (SAML, OpenID Connect) | Disponible | Disponible |
| Contenus éditoriaux dans l'application (actualités, webinaires) | Servis par la plateforme standard | Idem, en lecture seule, sans aucune donnée client |
| Rythme de mise à jour | Continu | Mêmes versions, déployées après la plateforme standard |

## Localisation des données et sauvegardes

Toutes les ressources de production (bases de données, fichiers, journaux d'audit, index de recherche, cache, coffre de secrets, supervision) sont hébergées dans la région **Bleu France Central**. Elles ne sont pas répliquées hors de Bleu.

Les seuls flux sortants sont les appels aux services tiers que l'offre standard utilise déjà : Mistral AI pour l'IA (données traitées à la demande) et Brevo (société française) pour l'envoi des e-mails.

## Chiffrement, authentification et secrets

Sauf mention contraire ci-dessous, les mesures décrites dans la page [Sécurité chez Dastra](general.md) s'appliquent à l'instance Bleu.

* **TLS** : le trafic public est terminé par le CDN européen bunny.net, qui gère les certificats ; TLS 1.2 minimum est imposé sur toutes les ressources (applications, bases, stockage).
* **Secrets** : coffre Azure Key Vault hébergé sur Bleu, accessible par les seules identités managées des applications ; aucun secret dans la configuration applicative.
* **Authentification** : serveur d'identité dédié. Un compte de la plateforme standard ne peut pas se connecter sur Bleu, et inversement ; aucune fédération n'existe entre les deux. La page de connexion propose un sélecteur de région pour orienter les utilisateurs.

## Isolation et environnements

L'instance Bleu est **strictement isolée** de la plateforme standard : bases de données, stockage, journaux, cache, index de recherche, coffre de secrets et identités sont distincts. Le seul flux entre les deux plateformes est la synchronisation, en lecture seule, de nos bibliothèques de référence (modèles, référentiels) vers Bleu ; aucune donnée client ne circule.
