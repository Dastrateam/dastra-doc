---
description: Zeigen Sie je nach geografischem Standort des Nutzers ein anderes Cookie-Banner an.
---

# Geo-Targeting-Varianten

## Überblick

Mit dem Dastra-Einwilligungsmodul können Sie **geografisch ausgerichtete Varianten** Ihres Cookie-Banners erstellen. Jede Variante ist eine angepasste Version des Banners (Erscheinungsbild, Texte, angezeigte Dienste), die automatisch anhand des **geografischen Standorts des Nutzers** angezeigt wird, der aus seiner IP-Adresse ermittelt wird.

Diese Funktion ist nützlich für Organisationen, die in mehreren Ländern oder Rechtsräumen tätig sind, da die Pflichten zur Cookie-Einwilligung je nach Rechtsordnung unterschiedlich sind (DSGVO und ePrivacy in Europa, CCPA in Kalifornien, LGPD in Brasilien usw.).

{% hint style="info" %}
**Warum das rechtlich wichtig ist**

Ein in Frankreich konformes Banner ist nicht zwangsläufig konform für einen kalifornischen Nutzer (Opt-out statt Opt-in) oder einen britischen Nutzer (nach dem Brexit hat das ICO eigene Leitlinien). Mit geografisch ausgerichteten Varianten passen Sie Ihr Banner an jeden rechtlichen Kontext an, ohne die Zahl der Banner zu vervielfachen.
{% endhint %}

Varianten hängen von Ihrem Tarif ab: Die Auswahlliste der Varianten ist deaktiviert, wenn die Funktion nicht in Ihrem Abonnement enthalten ist.

***

## Eine geografisch ausgerichtete Variante erstellen

### 1. Die Konfiguration öffnen

1. Klicken Sie im Menü auf **Cookie-Banner** > **Banner** und dann auf Ihr Banner.
2. Öffnen Sie oben rechts im Editor die Auswahlliste, die **Standardkonfiguration** anzeigt. Sie listet die vorhandenen Varianten auf.
3. Klicken Sie auf **Erstellen Sie eine geografisch ausgerichtete Variante**.

<figure><img src="../../../.gitbook/assets/cookies-geo-targeting-1.png" alt="Die Auswahlliste der Varianten im Banner-Editor"><figcaption><p>Die Auswahlliste der Varianten</p></figcaption></figure>

### 2. Die Variante benennen

Geben Sie im Feld **Name der Variante** einen aussagekräftigen Namen ein (höchstens 80 Zeichen), zum Beispiel `Banner - Kalifornien (CCPA)` oder `Banner - EWR-Zone`.

### 3. Die anvisierten geografischen Zonen auswählen

Wählen Sie unter **Länder oder geografische Regionen, auf die sich das Banner bezieht** die **Länder oder Regionen**, für die die Variante gilt. In der Liste steht eine Suche zur Verfügung.

Dastra bietet unter **Vorauswahl** zwei Abkürzungen:

* **EU/EWR**: wählt alle Länder des Europäischen Wirtschaftsraums aus.
* **Geeignete Länder**: wählt die Länder aus, die von der Europäischen Kommission nach Artikel 45 DSGVO als angemessen anerkannt sind.

Die Liste ist nach Ländern gegliedert und ermöglicht es, **Regionen unterhalb der Landesebene** anzusprechen (zum Beispiel französische Regionen oder US-Bundesstaaten). Sie können zum Beispiel innerhalb eines allgemeineren Banners für die Vereinigten Staaten eine Variante speziell für Kalifornien erstellen.

{% hint style="warning" %}
**Vorrang der Varianten**

Können mehrere Varianten auf denselben Nutzer zutreffen (zum Beispiel ein Nutzer in der Île-de-France mit einer Variante „Frankreich“ und einer Variante „Île-de-France“), hat die **spezifischste** Variante (die Region) Vorrang vor der allgemeineren (dem Land).
{% endhint %}

### 4. Die Variante anpassen

Sobald die Variante erstellt ist, öffnet sie sich im Editor. Sie können Folgendes anpassen:

* **Erscheinungsbild und Design**: Farben, Layout, Schaltflächen;
* **Texte und Übersetzungen**: an den lokalen rechtlichen Kontext angepasste Texte;
* **Dienstleistungen**: Sie können die Liste der angezeigten Tracker einschränken oder erweitern;
* **Auslöser**: für die Variante spezifische Anzeigebedingungen.

{% hint style="info" %}
Eine Variante übernimmt die folgenden Einstellungen aus dem Standard-Banner: die zulässigen URLs, die Generierung der Cookie-Richtlinie, den Namen, die Domäne und die Lebensdauer des Einwilligungs-Cookies, den Speichermodus, den Vorschau-Modus und den Versionsschlüssel. Um sie zu ändern, öffnen Sie die **Standardkonfiguration**.
{% endhint %}

### 5. Die Anzeige des Banners deaktivieren (optional)

Im Abschnitt der Variante können Sie über die Option zur Deaktivierung der Banner-Anzeige (alle Cookies mit Standardeinwilligung werden ausgelöst) festlegen, **kein Banner** für Nutzer in der anvisierten Zone anzuzeigen.

Wenn sie aktiviert ist, wird den betreffenden Besuchern kein Einwilligungsfenster angezeigt. Alle Cookies werden dann mit ihrer **Standardeinwilligung** ausgelöst, wie sie für jeden Dienst konfiguriert ist.

{% hint style="warning" %}
**Nur für Zonen ohne vorherige Einwilligungspflicht**

Diese Option ist relevant für Länder, in denen die lokalen Vorschriften vor dem Setzen von Cookies keine aktive Einwilligung verlangen (zum Beispiel bestimmte Länder außerhalb des EWR ohne gleichwertige ePrivacy-Gesetzgebung). Verwenden Sie sie niemals für Nutzer in der EU oder im EWR, im Vereinigten Königreich oder in jedem anderen Rechtsraum, der ein Opt-in verlangt.
{% endhint %}

{% hint style="info" %}
Die Standardeinwilligung jedes Dienstes legen Sie im Abschnitt **Dienstleistungen** des Banners fest. Prüfen Sie diese Werte, bevor Sie die Option aktivieren.
{% endhint %}

***

## Typische Anwendungsfälle

| Situation                                           | Empfohlene Konfiguration                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------------ |
| Europäische Website mit US-Traffic                  | EWR-Variante (striktes Opt-in) + US-/Kalifornien-Variante (CCPA-Opt-out) |
| Französische Website mit einer deutschen Tochtergesellschaft | Variante Frankreich + Variante Deutschland mit an die Anforderungen des BfDI angepassten Texten |
| Globale Website mit minimaler Compliance außerhalb des EWR | Globales Standard-Banner + DSGVO-konforme EWR-Variante            |

***

## Wie es technisch funktioniert

Dastra ermittelt den Standort anhand der **IP-Adresse** des Besuchers, ohne dass Sie etwas konfigurieren müssen. Der Standort bestimmt, welche Variante angezeigt wird. Das Einwilligungs-Cookie des Besuchers enthält seinen Standort nicht, aber das erkannte Land und die IP-Adresse werden mit dem [Einwilligungsnachweis](consent-proof.md) gespeichert.

{% hint style="info" %}
Um die Anzeige einer Variante aus Ihrem Browser zu testen, verwenden Sie ein VPN mit Standort in der anvisierten Zone.
{% endhint %}
