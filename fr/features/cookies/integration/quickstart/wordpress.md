---
description: Apprenez à intégrer la bannière de cookies Dastra sur un site WordPress.
---

# Wordpress

## Installez le plugin Dastra

Le plugin Dastra est la méthode recommandée : il n'est pas écrasé par les mises à jour de votre thème.

1. Dans la bannière, ouvrez la section **Installation** et cliquez sur la carte **Wordpress**.
2. Cliquez sur **Visiter la page du plugin**, ou recherchez le plugin « Dastra » dans la liste des extensions de votre administration WordPress. Vous pouvez aussi télécharger le plugin depuis cette fenêtre pour l'installer manuellement.
3. Installez et activez le plugin.
4. Dans WordPress, ouvrez **Réglages** > **Dastra** et cliquez sur **Link with Dastra** pour relier le plugin à votre bannière.

<figure><img src="../../../../.gitbook/assets/cookies-wordpress-1.png" alt="La fenêtre WordPress de la section Installation avec le lien vers le plugin"><figcaption><p>La carte « Wordpress » de la section Installation</p></figcaption></figure>

## Ou collez le code dans le thème

Si vous ne pouvez pas installer de plugin, collez le code de la bannière dans le thème. Une mise à jour du thème écrase cette modification : reportez-la alors dans un thème enfant.

1. Dans la section **Installation** de la bannière, cliquez sur la carte **Javascript** et copiez le code.
2. Dans l'administration de votre site WordPress, cliquez sur **Apparence**, puis sur **Éditeur de thème**.
3. Sélectionnez le fichier `footer.php`, puis insérez le code juste avant la balise `</body>`.

![L'éditeur de thème WordPress avec le fichier footer.php ouvert](../../../../.gitbook/assets/cookies-wordpress-theme-editor.png)

4. Cliquez sur **Mettre à jour le fichier**, puis rafraîchissez la page de votre site. La bannière apparaît.

Ajoutez aussi un bouton qui rouvre la bannière, comme décrit dans [Démarrage rapide](README.md#rouvrir-la-banniere-depuis-un-bouton).
