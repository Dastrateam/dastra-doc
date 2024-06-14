# Intégration avec Docusign

Nous avons mis en place une intégration native entre Dastra et DocuSign, leader mondial de la signature électronique vous permettant d'envoyer, de signer et de suivre le statut d'une signature directement depuis le module contrat de Dastra.&#x20;

Rendez vous dans [les réglages de votre espace de travail, onglet intégrations](https://app.dastra.eu/workspace/2/settings/integrations), pour mettre en place l'intégration et y avoir accès dans la partie signature d'un contrat.

<figure><img src="../../.gitbook/assets/image (360).png" alt=""><figcaption><p>Sélectionnez Docusign dans les intégrations</p></figcaption></figure>

Une fois l'intégration Docusign ouverte, veuillez cliquer sur "Ajouter l'intégration", vous serez alors redirigé vers l'authentification Docusign pour associer votre compte Docusign à Dastra.

Une fois la connexion établie, il vous faudra renseigner dans Dastra votre Docusign  AccountId et votre Docusign Account Base URI que vous[ retrouvez ici](https://apps.docusign.com/admin/apps-and-keys).&#x20;

<figure><img src="../../.gitbook/assets/image (361).png" alt=""><figcaption><p>Les clés à renseigner dans Dastra provenant de votre compte Docusign</p></figcaption></figure>

Une fois ces champs renseignés, vous avez terminé le paramétrage de l'intégration. Vous pouvez désormais vous rendre dans le module contrat et gérer les signature de vos contrat de manière électronique.&#x20;

### Interface de signature Docusign

Vous retrouvez ci-dessous l'interface de signature d'un contrat via Docusign (accessible depuis le bouton 'ajouter signature' d'un signataire).

Pour pouvoir valider cette page, il vous faut impérativement un acteur (signataire) avec une adresse email valide, une pièce jointe à signer de type .pdf, .doc, .docx et un intitulé pour l'email d'invitation à signer.&#x20;

Vous pouvez ajouter des instructions détaillées pour la signature du document, ces dernières seront incluses au mail d'invitation à signer et seront également visibles par le signataire dans l'interface Docusign lorsqu'il accèdera au document à signer.&#x20;

<figure><img src="../../.gitbook/assets/image (362).png" alt=""><figcaption><p>Interface d'envoi de signature par Docusign via Dastra</p></figcaption></figure>

Une fois la signature envoyée, son statut est automatiquement synchronisé sur votre contrat et sera mis à jour à chaque changement de statut de la signature côté Docusign.

<figure><img src="../../.gitbook/assets/image (363).png" alt=""><figcaption><p>Une signature en attente</p></figcaption></figure>
