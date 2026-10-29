---
description: Erfahren Sie, wie Sie Cookies nach Einwilligungskategorien klassifizieren.
---

# Cookies nach Einwilligungskategorien klassifizieren

In ihrem [Empfehlungsentwurf](https://www.cnil.fr/fr/la-cnil-lance-une-consultation-publique-sur-son-projet-de-recommandation-cookies-et-autres-traceurs) zu Cookies und anderen Trackern (auf Französisch) empfiehlt die CNIL, die Cookies Ihrer Website aufzulisten und danach zu kategorisieren, ob sie eine Einwilligung erfordern oder nicht.

{% hint style="info" %}
Weitere Informationen zu den CNIL-Empfehlungen zu Cookies finden Sie im Artikel „[Die Cookie-Empfehlungen der CNIL, erklärt für Ihren Chef](https://www.dastra.eu/fr/article/recommendations-CNIL-cookies-expliquees-a-votre-boss/104)“ (auf Französisch).
{% endhint %}

In Dastra ist die Kategorie eines Cookies die Kategorie des Dienstes, zu dem es gehört: Sie wählen den **Zweck** jedes Dienstes, und alle seine Cookies übernehmen ihn. Folgende Kategorien stehen zur Verfügung:

* **Unbedingt erforderlich**: Cookies, die ihrer Natur nach von der Einwilligung ausgenommen sind, zum Beispiel Sitzungs- oder Einwilligungs-Cookies;
* **Einstellungen**;
* **Analyse der Besucherzahlen**;
* **Marketing und Nutzererfahrung**;
* **Soziale Netzwerke**;
* **Sonstiges**.

{% content-ref url="purposes.md" %}
[Cookie-Zwecke](purposes.md)
{% endcontent-ref %}

## Den Zweck eines Dienstes festlegen

1. Öffnen Sie das Banner: **Cookie-Banner** > **Banner**, dann klicken Sie auf das Banner.
2. Klappen Sie den Abschnitt **Dienstleistungen** auf.
3. Klicken Sie auf den Dienst, den Sie klassifizieren möchten. Wählen Sie im Tab **Grundlegende Informationen** im Feld **Zweck dieses Dienstes** einen Wert aus.
4. Bestätigen Sie und klicken Sie dann auf **Speichern**.

<figure><img src="../../../.gitbook/assets/cookies-classify-1.png" alt="Der Abschnitt Dienstleistungen des Banner-Editors, mit dem Zweck unter dem Namen jedes Dienstes"><figcaption><p>Der Zweck jedes Dienstes steht unter seinem Namen</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/cookies-classify-2.png" alt="Das Formular eines Dienstes mit dem Feld Zweck dieses Dienstes"><figcaption><p>Das Feld „Zweck dieses Dienstes“ im Formular des Dienstes</p></figcaption></figure>

Ein Dienst kann nicht mit dem Zweck **Unkategorisiert** gespeichert werden: Wählen Sie eine der oben genannten Kategorien.

{% hint style="info" %}
Ob für einen Dienst eine Einwilligung eingeholt werden muss, entscheiden Sie im Einzelfall mit der Option **Möchten Sie die Einwilligung für diese Cookies einholen? (Anzeige der Schaltflächen)**. Sie ist für die Kategorie **Unbedingt erforderlich** deaktiviert.
{% endhint %}

{% hint style="warning" %}
Ein vom Scan erkanntes Cookie, das mit keinem Dienst verknüpft ist (nicht klassifiziertes Cookie), wird im öffentlichen Banner nie angezeigt. Fügen Sie es einem bestehenden Dienst hinzu oder legen Sie daraus einen Dienst an: siehe [Nicht klassifizierte Cookies behandeln](scan.md#nicht-klassifizierte-cookies-behandeln).
{% endhint %}

Sobald alle Ihre Cookies zu einem nach Kategorie klassifizierten Dienst gehören, können Sie das Banner konfigurieren.

{% content-ref url="configure.md" %}
[Das Cookie-Einwilligungsbanner einrichten](configure.md)
{% endcontent-ref %}
