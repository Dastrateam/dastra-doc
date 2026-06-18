---
description: Cavardez les documents joints à une demande d'exercice de droits directement depuis Dastra, avec ou sans assistance IA.
---

# Caviardage des documents

Lors du traitement d'une demande d'exercice de droits, il est fréquent de devoir transmettre des documents au demandeur — copie d'identité, contrat, historique de compte, dossier client. Ces documents contiennent presque toujours des informations confidentielles qui ne doivent pas être communiquées : données relatives à des tiers, données contractuelles internes, références nominatives.

Dastra intègre un outil de caviardage directement dans le flux de traitement de la demande, sans sortir de la plateforme.

***

## Comment accéder au caviardage

L'outil de caviardage est disponible depuis l'étape **Communication / Transmission** d'une demande en cours de traitement, lorsqu'une pièce jointe est présente ou ajoutée.

1. Ouvrez une demande d'exercice de droits en cours
2. Accédez à l'étape **Communication / Transmission**
3. Sélectionnez ou ajoutez le document à transmettre
4. Cliquez sur **Caviarder le document**

<figure><img src="../../.gitbook/assets/dsr-request-processing-attachments.png" alt="Étape de traitement de la demande avec le document original à caviarder"><figcaption><p>Pièce jointe originale dans l'étape de traitement — prête à être caviardée</p></figcaption></figure>

***

## Caviardage assisté par IA

Lorsque vous lancez le caviardage, l'assistant IA analyse le document et **détecte automatiquement les zones susceptibles de contenir des identifiants personnels de tiers** : noms, adresses, coordonnées, numéros d'identification.

Ces zones sont pré-sélectionnées et affichées sur le document. Votre équipe :

* **Supprime les faux positifs** d'un clic (zones détectées à tort)
* **Ajoute manuellement** toute zone que l'IA aurait manquée

{% hint style="warning" %}
Le résultat de l'IA est une proposition de départ, pas une décision finale. Toute zone de caviardage doit être revue et validée par une personne qualifiée avant transmission.
{% endhint %}

***

## Caviardage manuel

Pour les équipes qui préfèrent conserver un contrôle total sans assistance IA, le **caviardage entièrement manuel** est disponible dans la même interface. Sélectionnez les zones à masquer directement sur le document.

***

## Génération du document caviardé

Une fois la revue terminée, cliquez sur **Générer le document caviardé**. Le document produit est :

<figure><img src="../../.gitbook/assets/dsr-request-processing-redacted.png" alt="Document caviardé généré — Invoice-redacted.pdf avec 6 zones masquées"><figcaption><p>Le document caviardé est automatiquement renommé et joint à la demande (ici : 6 zones masquées)</p></figcaption></figure>

* **Rasterisé** — le texte sous-jacent n'est pas simplement masqué visuellement mais rendu définitivement inaccessible. Il n'est pas possible d'extraire le contenu caviardé du fichier final.
* **Enregistré dans la demande** — le document caviardé est attaché à la demande et disponible pour envoi.

L'original peut être conservé ou supprimé selon la politique de votre organisation.

{% hint style="info" %}
Le caviardage par rasterisation est la méthode recommandée par les autorités de protection des données. Un simple masquage visuel (rectangle opaque sur un PDF non aplati) peut être contourné et ne constitue pas un caviardage conforme.
{% endhint %}

***

## Bonnes pratiques

* Relisez systématiquement le document caviardé avant envoi pour vérifier qu'aucune information confidentielle n'est visible.
* Conservez l'original dans Dastra pour votre dossier de conformité, sauf si votre politique interne impose sa suppression.
* Pour les documents volumineux ou complexes (contrats multi-pages, relevés de compte), combinez la détection IA avec une relecture manuelle page par page.
