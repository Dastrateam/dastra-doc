---
description: >-
  Dastra ist nativ in Google Tag Manager integriert. Dieser Artikel erklärt
  Ihnen, wie Sie das Blockieren oder Freigeben von Tags in Abhängigkeit von den
  Einwilligungen des Nutzers mithilfe von GTM inte
---

# Google Tag Manager

## Einführung

Google Tag Manager ist ein leistungsstarkes Tagging-Tool, das alle Code-Snippets zentralisiert, die Sie in Ihre Website integrieren möchten (Dastra kann übrigens dazugehören!).\
Diese Tagging-Lösung ist sehr effektiv für die Implementierung der effektiven Cookie-Einwilligung, da sie es nicht erfordert, die gesamte Website bei jeder Tag-Änderung neu zu deployen.

## An GTM im DataLayer gesendete Ereignisse

Die folgenden Ereignisse werden automatisch an den Google dataLayer gesendet:

| Name                              | Bedeutung                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------- |
| dastra:consent:{your-vendor-name} | Dieses Ereignis wird gesendet, wenn der Nutzer die Cookies dieses Anbieters akzeptiert hat        |
| dastra:refused:{your-vendor-name} | Dieses Ereignis wird ausgelöst, wenn der Nutzer den Cookies dieses Anbieters nicht zugestimmt hat |

Sie können daher die Tags, die den verschiedenen im Widget konfigurierten Anbietern entsprechen, mithilfe dieser beiden Ereignisse auslösen.

## Beispiel

In diesem Beispiel lösen wir das Google Optimize-Tag bei Einwilligung des Nutzers aus.

Erstellen Sie in Ihrem GTM-Container einen Trigger für ein dataLayer-Ereignis mit dem Namen „dastra:consent:google-optimize"

Das Google Optimize-Tag wird dann nur bei diesem Ereignis ausgelöst. So sieht es in der GTM-Oberfläche aus:

![](../../../../.gitbook/assets/image-169.png)

## Spezialfall der „Blocking Triggers"

In bestimmten Fällen müssen Sie bestimmte Tags deaktivieren, wenn die Einwilligung nicht erteilt wurde. Da das Ereignis „dastra:consent:\<Dienstname>" nur beim Laden einer Seite ausgeführt wird, kann dies in bestimmten Fällen unzureichend sein, wenn Sie andere Interaktions-Trigger auf der Seite verwenden, wie Klicks auf Seitenelemente, Scroll-Höhen usw.

In diesem Fall müssen bestimmte Konfigurationen vorgenommen werden, um **den Einwilligungswert direkt aus dem Einwilligungs-Cookie zu lesen**.

### 1. Eine Variable „DastraConsents" erstellen

#### Die Variable definieren

**Melden Sie sich** bei Ihrem Google Tag Manager-Konto an und gehen Sie zu „Variablen", dann erstellen Sie eine neue „Benutzerdefinierte Variable".

#### „1st party cookies" auswählen

Benennen Sie Ihr Tag z. B. „DastraConsents". Geben Sie im Feld Cookie-Name (Cookie name) den Namen des Einwilligungs-Cookies ein (Standard: **consent-eu**).\
Denken Sie daran, **die Option „URI-decode cookie" zu aktivieren**

<figure><img src="../../../../.gitbook/assets/image-7-1-1.png" alt=""><figcaption></figcaption></figure>

#### Konfigurieren Sie anschließend Ihren Trigger folgendermaßen:

In diesem Fall wird unser Tag ausgelöst, wenn die Scroll-Tiefe auf der Seite > 20% beträgt. Wir möchten, dass dieses Tag nur ausgelöst wird, wenn der Google Analytics-Dienst vom Nutzer autorisiert wurde. So konfigurieren Sie den Tag-Trigger.

<figure><img src="../../../../.gitbook/assets/image-4-1-2.png" alt=""><figcaption></figcaption></figure>

Im Bereich „Some Pages", wenn Sie das Tag nur aktivieren möchten, wenn die Nutzung eines Dienstes genehmigt wurde, geben Sie die Formel ein: **DastraConsents contains "{serviceName}":true** (Beispiel: "crisp":true) ohne Leerzeichen

Wenn Sie das Tag im Falle einer Ablehnung auslösen möchten, verwenden Sie die Formel:

**DastraConsents contains "{serviceName}":false** (Beispiel: "google-analytics":false)

#### Fall mehrerer Trigger desselben Typs mit einer Ausnahme

Wenn Sie viele verschiedene Trigger für ein und dasselbe Tag haben, ist es auch durchaus möglich, eine Ausnahme auf diese Weise zu erstellen.\
Beispiel eines Tags mit mehreren Triggern:

<figure><img src="../../../../.gitbook/assets/image-2-1-1-1-1-1-1-1.png" alt=""><figcaption></figcaption></figure>

In diesem Fall möchten wir eine Ausnahme hinzufügen: Wenn das Google Ads-Tag (google-ads) nicht akzeptiert wurde, soll das Tag nicht ausgelöst werden.

Klicken Sie auf **„Ausnahme hinzufügen"** (Add Exception)

{% hint style="info" %}
Achtung: Ausnahmen funktionieren nur dann korrekt, wenn sie vom gleichen Typ sind. Wenn Ihre Trigger vom Typ „Page view" sind, muss die Ausnahme ebenfalls vom Typ Page view sein
{% endhint %}

Erstellen Sie einen Trigger desselben Typs mit dem Namen z. B. „Seitenaufrufe mit explizit abgelehntem Google Ads-Dienst".

{% hint style="info" %}
Wenn Sie auch das Tag standardmäßig nicht aktivieren möchten, einschließlich wenn der Nutzer nicht auf das Einwilligungs-Modal geklickt hat (und daher kein Cookie mit den Präferenzen gespeichert ist). In diesem Fall können Sie einen Trigger mit einer Negation verwenden:

**DastraConsents Does not contain "google-ads":true**
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image-3-1-1-1-1-1.png" alt=""><figcaption></figcaption></figure>

Klicken Sie auf „Speichern". Sie sollten Folgendes sehen:

<figure><img src="../../../../.gitbook/assets/image-5-1-1.png" alt=""><figcaption></figcaption></figure>

Speichern Sie Ihre Änderungen und Sie sollten feststellen, dass Ihre Tags auf den betreffenden Seiten korrekt deaktiviert sind, wenn die Einwilligung nicht erteilt wurde.

### Spezialfall: Seitenaktualisierung bei Änderung der Einwilligungskonfiguration

#### Ablehnung von Cookies nach Akzeptierung:

In bestimmten Fällen werden einige Tags nach der Ablehnung von Cookies nicht korrekt bereinigt. Dies geschieht insbesondere, wenn ein Nutzer sich entscheidet, die Cookies zu akzeptieren, dann erneut auf das Widget klickt und seine Einwilligung zurücknimmt. In den meisten Fällen stellt dies kein Problem dar, da die Marker ohnehin nicht mehrmals auf der Seite ausgeführt werden und es daher nicht mehr notwendig ist, die in die Seite eingefügten Script-Tags zu entfernen.

In bestimmten Situationen ist es möglich, dass die Tags weiterhin aktiv sind.

Um diese Art von Problemen zu verhindern, ist es möglich, eine Seitenaktualisierung zu erzwingen, die alle Marker oder JavaScript-SDKs, die von den Diensten geladen werden, vollständig zurücksetzt.

Fügen Sie einfach den folgenden Code ein (wenn möglich unterhalb des Initialisierungs-Tags des Dastra-Widgets)

```html
<script>
// If any service is refused explicitely in the modal
window.addEventListener('dastra:consents:any_refused', function(){
    // Refresh the current page
    location.reload();
})
</script>
```

#### Aktualisierung der Einwilligung:

Um die Seite neu zu laden, wenn eine Einwilligung auf irgendeine Weise geändert wird, verwenden Sie die Funktion _updated_ mit dem folgenden Code:

```markup
<script>
window.addEventListener('dastra:consents:updated', function(){
    // Refresh the current page
    location.reload();
})
</script>
```

#### Vollständige Akzeptierung der Tracker:

Um die Seite beim vollständigen Akzeptieren der Tracker neu zu laden (Schaltfläche „Alle akzeptieren"):

```markup
<script>
window.addEventListener('dastra:consents:all_accepted', function(){
    // Refresh the current page
    location.reload();
})
</script>
```

#### Akzeptierung eines bestimmten Dienstes:

Um die Seite bei der Akzeptierung eines bestimmten Dienstes neu zu laden:

```markup
<script>
window.addEventListener('dastra:consent:<slug du service>', function(){
    // Refresh the current page
    location.reload();
})
</script>
```
