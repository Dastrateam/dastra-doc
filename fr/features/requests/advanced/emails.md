# Personnalisation des emails envoyés aux demandeurs

Si vous ne souhaitez pas utiliser les formulations par défaut, vous pouvez modifier tous les e-mails de notification envoyés aux demandeurs.

Vous pouvez :

* Adapter les **sujets et corps des messages**.
* Gérer les **traductions** pour envoyer les e-mails dans la langue du demandeur.
* Ajouter des langues. Si la langue d'une demande n'est pas paramétrée, le demandeur reçoit les e-mails en anglais.

## Ajouter une langue et modifier les textes

1. Dans les paramètres de l'espace de travail, section **Processus**, ouvrez **Demandes d'exercice de droit**.
2. Ouvrez la section **Textes et traductions des emails de notification**.
3. Choisissez une langue dans la liste **Ajouter la langue**.
4. Cliquez sur **Modifier** à côté de la langue, puis adaptez les sujets et les textes.
5. Ouvrez l'e-mail à personnaliser (en-tête et pied de page, confirmation d'identité, confirmation, code d'accès à l'espace demandeur, nouveau message ou clôture de la demande), remplacez les valeurs par défaut affichées sous le libellé de chaque champ, puis cliquez sur **Enregistrer**.

<figure><img src="../../../.gitbook/assets/requests-emails-1.png" alt="La section Textes et traductions des emails de notification avec la liste des langues"><figcaption><p>Les langues personnalisées</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/requests-emails-2.png" alt="L'édition des textes d'un e-mail de notification dans une langue"><figcaption><p>La personnalisation d'un message</p></figcaption></figure>

{% hint style="info" %}
Conservez les balises telles que `{{data.Code}}` : elles sont remplacées par des données lors de l'envoi et le message en a besoin pour fonctionner. Vous pouvez ajouter d'autres variables dans le texte : tapez `{{` pour ouvrir la liste des variables disponibles.
{% endhint %}
