---
description: Learn how to integrate the Dastra cookie banner on a WordPress website.
---

# Wordpress

## Install the Dastra plugin

The Dastra plugin is the recommended method: theme updates do not overwrite it.

1. In the banner, open the **Installation** section and click the **Wordpress** card.
2. Click **Visit the plugin page**, or search for the "Dastra" plugin in the plugins list of your WordPress administration. You can also download the plugin from this window and install it manually.
3. Install and activate the plugin.
4. In WordPress, open **Settings** > **Dastra** and click **Link with Dastra** to link the plugin to your banner.

<figure><img src="../../../../.gitbook/assets/cookies-wordpress-1.png" alt="The WordPress window of the Installation section with the link to the plugin"><figcaption><p>The "Wordpress" card of the Installation section</p></figcaption></figure>

## Or paste the code in the theme

If you cannot install a plugin, paste the banner code in the theme. A theme update overwrites this change: apply it in a child theme instead.

1. In the **Installation** section of the banner, click the **JavaScript** card and copy the code.
2. In the administration of your WordPress site, click **Appearance**, then **Theme Editor**.
3. Select the `footer.php` file, then insert the code just before the `</body>` tag.

![The WordPress theme editor with the footer.php file open](../../../../.gitbook/assets/cookies-wordpress-theme-editor.png)

4. Click **Update File**, then refresh the page of your website. The banner appears.

Also add a button that reopens the banner, as described in [Quick start](README.md#reopen-the-banner-from-a-button).
