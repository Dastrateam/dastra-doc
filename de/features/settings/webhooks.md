---
description: Erfahren Sie alles über die Integration von Webhooks in Dastra
---

# Webhooks

## Konzept 👓

Einfach ausgedrückt ermöglichen Webhooks das **Auslösen einer Aktion** nach einem Ereignis. Sie werden in der Regel verwendet, um Systeme miteinander kommunizieren zu lassen. Es ist die einfachste Art, eine Warnung zu erhalten, wenn etwas in Dastra passiert. Das Ziel ist die Benachrichtigung von Drittanwendungen (API, CRM, Serverless-Funktionen...) in Echtzeit.

## Konfiguration 🛠️

Um Ihre Webhooks zu konfigurieren, gehen Sie auf die Seite: [https://app.dastra.eu/general-settings/webhooks](https://app.dastra.eu/general-settings/webhooks)

![](<../../.gitbook/assets/Erweiterte Konfiguration27.png>)

* Klicken Sie auf „**Erstellen Sie eine Webhook-URL**"
* Geben Sie die Empfangs-URL Ihres Webhooks ein. Weitere Informationen finden Sie im Abschnitt [Webhook empfangen](webhooks.md#undefined).
* Geben Sie den betroffenen Mandanten an
* Wählen Sie das oder die Ereignisse, die Sie abonnieren möchten. Der Typ der zurückgegebenen Daten unterscheidet sich je nach Ereignistyp. Zum Beispiel können Sie den Webhook bei der Erstellung einer neuen Rechteausübungsanfrage auslösen. In diesem Fall enthält der Body der Anfrage ein JSON
* Speichern Sie den Webhook

Sie gelangen zum **Detailbildschirm des Webhooks.**

![](../../.gitbook/assets/image-254-1-1.png)

### Webhook empfangen 🛬

Um die Webhook-Anfragen zu empfangen, müssen Sie einen API-Endpoint zur Erfassung des Ereignisses erstellen. Die durchgeführte Anfrage ist ein **POST** und ist immer wie folgt strukturiert. Der Body der Anfrage enthält ein JSON mit den Details des ausgelösten Ereignisses.

Hier ist die allgemeine Struktur der gesendeten Antwort:

```json
{
 "webhookId": <id of the webhook configured in dastra>,
 "signatureUrl": "https://yourapi.com/webhooks/handle",
 "userId": <The user whot triggered the event>,
 "eventType": <The id of the event>,
 "eventName": <The label of the event>,
 "data": <Event dynamic data>,
 "date": <date of the event>
} 
```

Ein Timeout von 10 Sekunden wird auf die Anfrage angewendet, nach Ablauf dieser Zeit wird die Anfrage als Fehler gewertet. Der Antwortcode muss 200 sein.

Es kann eine kleine Verzögerung zwischen dem Zeitpunkt des Ereignisses in der Anwendung und dem Auslösen des Webhooks geben (diese Verzögerung ist auf die asynchrone Natur der Webhook-Ausführung in unserer Infrastruktur zurückzuführen). Diese Verzögerung variiert je nach Auslastung unserer Infrastruktur und kann maximal 60-120 Sekunden betragen.

{% hint style="info" %}
Es gibt derzeit kein System zum erneuten Abspielen fehlgeschlagener Webhooks und damit zur Kompensation einer eventuellen Nichtverfügbarkeit der Webhook-Empfangsserver. In diesem Fall empfehlen wir eine manuelle Synchronisation der fehlgeschlagenen Ereignisse.
{% endhint %}

### Ihre Webhook-URL testen 🧪

Sie können Ihren Webhook unter realen Bedingungen testen, **indem Sie auf die Schaltfläche „Testen" klicken.**

### Webhook absichern 🛡️

{% hint style="info" %}
Obwohl nicht verpflichtend, wird **empfohlen, die eingehende Webhook-Anfrage zu validieren**, um potenzielle Angriffe eines Hackers zu vermeiden, der das Netzwerk ausspioniert hat und somit in der Lage wäre, beliebige Daten auf Ihre Webhook-URL zu posten und damit die Erstellung von Elementen in Ihrem System auszulösen oder zu spammen.
{% endhint %}

Jedes Mal, wenn eine Anfrage zur Änderung oder Löschung eines Dastra-Elements durchgeführt wird, posten wir ein Objekt auf alle URLs, die Sie für das gewünschte Ereignis konfiguriert haben. In jeder POST-Anfrage befindet sich ein Header **Dastra-Signature**, der serverseitig abgerufen werden kann.

Dieser Header entspricht dem gesamten geposteten JSON, **gehasht mit dem Algorithmus HMAC-Sha256** unter Verwendung des Webhook-Validierungsschlüssels.

> DastraSignature = **HMAC256**(\<serialisiertes JSON des POST>,\<Webhook-Validierungsschlüssel>)

Hier einige Beispiele zur Validierung der Anfrage-Signatur:

{% tabs %}
{% tab title="PHP" %}
```php
error_reporting(E_ALL);
ini_set('display_errors', 1); 
c
$secret = "your dastra validation key";// your secret key
$payload = "";// equest body
$headers = "";// request message headers array

$signature = "";// the HMAC hash key in the HTTP header 'Dastra-Signature'
$result = false;// verification result

if (isset($_POST)) {
    try {
        $payload = file_get_contents('php://input');
        $headers = get_ds_headers();
        if (array_key_exists("Dastra-Signature", $headers)) {
            $signature = $headers["Dastra-Signature"];
            $result = hash_is_valid($secret, $payload, $signature);
            log_result($signature, $payload, $result);
        }
     } catch (Exception $e) {
        logger("\nException: " . $e->getMessage() . "\n");
    }
    header("HTTP/1.1 200 OK");
}

function get_ds_headers()
{
    $headers = array();
    foreach ($_SERVER as $key => $value) {
        if (strpos($key, 'HTTP_') === 0) {
            $headers[str_replace(' ', '', ucwords(str_replace('_', ' ', strtolower(substr($key, 5)))))] = $value;
        }
    }
    return $headers;
}
 
function compute_hash($secret, $payload)
{
    $hexHash = hash_hmac('sha256', $payload, utf8_encode($secret));
    $base64Hash = base64_encode(hex2bin($hexHash));
    return $base64Hash;
}
 
function hash_is_valid($secret, $payload, $verify)
{
    $computed_hash = compute_hash($secret, $payload);
     return hash_equals($verify,$computed_hash);
 }
```
{% endtab %}

{% tab title="C#" %}
```csharp

[HttpPost]
public IActionResult Handle(){
    string dastraSignature = Request.Headers["Dastra-Signature"];
    string key = "Your validation key";
    string payload = GetRequestBody();
}

private static bool ValidateSignature(string signature, string payload, string secret)
{
    using (var hmacsha256 = new HMACSHA256(Encoding.UTF8.GetBytes(secret)))
    {
        var hash = hmacsha256.ComputeHash(Encoding.UTF8.GetBytes(payload));
        var result = Convert.ToBase64String(hash);
    }
    
    return result.Equals(signature)
}

private static string GetRequestBody()
{
    var bodyStream = new StreamReader(Request.InputStream);
    bodyStream.BaseStream.Seek(0, SeekOrigin.Begin);
    var bodyText = bodyStream.ReadToEnd();
    return bodyText;
}
```
{% endtab %}
{% endtabs %}

### Was passiert, wenn die URL etwas anderes als 200 antwortet

Der Webhook wird automatisch blockiert und als fehlerhaft betrachtet, wenn die Schwelle von 5 Fehlern überschritten wird.

### Webhooks mit den APIs einrichten

Die mit Ihrem Konto verknüpften Webhooks abrufen (in allen Mandanten)

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls" method="get" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}

Erstellen Sie eine neue Webhook-URL mit dem POST-Endpoint. Geben Sie die Ereignisse an, die Sie mit dem Parameter **subscribedEvents** abonnieren möchten.

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls" method="post" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}

Eine Webhook-ID wird Ihnen zurückgegeben

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls/{id}" method="get" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls/{id}" method="delete" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}
