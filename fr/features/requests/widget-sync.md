# Synchronisation des widgets

Lorsque plusieurs widgets de demande d'exercice de droits partagent une configuration similaire (mêmes champs, mêmes textes), vous pouvez les synchroniser. Désignez un widget comme source, synchronisez-y des widgets enfants, puis propagez toute modification en un seul clic vers l'ensemble des widgets liés.

Cette fonctionnalité est particulièrement utile pour les organisations qui gèrent plusieurs variantes d'un même widget (par exemple, un widget de suppression de compte décliné par application ou par marché géographique).

Dans l'application, un widget est un formulaire de collecte : ouvrez-le depuis **Demandes** > **Formulaires de collecte**. Les boutons de synchronisation se trouvent en haut de la page du formulaire, à côté de **Aperçu**.

## Synchroniser depuis un autre widget

Pour récupérer la configuration d'un widget existant vers le widget courant :

1. Cliquez sur le bouton déroulant **Synchroniser**, à côté de **Aperçu**.
2. Cliquez sur **Synchroniser depuis un autre formulaire**.
3. Dans **Formulaire source**, choisissez le widget source.
4. Sous **Que voulez-vous synchroniser ?**, cochez les éléments à récupérer : **Textes et traductions**, **Champs du formulaire** et **Design et apparence**.
5. Cliquez sur **Synchroniser**.

<figure><img src="../../.gitbook/assets/requests-widget-sync-1.png" alt="Page d’un formulaire de collecte avec le bouton déroulant de synchronisation à côté du bouton Aperçu"><figcaption><p>Le bouton de synchronisation, à côté de Aperçu, importe la configuration d'un widget source</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/consent-widget-sync-form-dialog.png" alt="Fenêtre de synchronisation depuis un autre formulaire"><figcaption><p>Choix du widget source et des éléments à récupérer</p></figcaption></figure>

Une fois la synchronisation faite, le widget devient un widget enfant de la source. Le bouton affiche alors **Synchronisé** et propose **Effacer** pour supprimer le lien avec la source.

## Propager les modifications vers les widgets enfants

Une fois vos modifications effectuées sur le widget source, propagez-les en un clic à tous les widgets liés :

1. Cliquez sur **Propager les modifications aux formulaires liés**, suivi du nombre de widgets enfants entre parenthèses.
2. Vérifiez la liste des widgets enfants, puis cochez les éléments à propager.
3. Cliquez sur **Propager**.

<figure><img src="../../.gitbook/assets/consent-widget-propagate-dialog.png" alt="Fenêtre de propagation vers les formulaires liés"><figcaption><p>Propagation des modifications du widget source vers tous ses enfants (textes, champs, design)</p></figcaption></figure>

{% hint style="info" %}
Le bouton **Propager les modifications aux formulaires liés** n'apparaît que sur un widget qui a au moins un widget enfant. Dans ce cas, le bouton de synchronisation est masqué : un widget source ne peut pas lui-même être synchronisé depuis un autre widget.
{% endhint %}
