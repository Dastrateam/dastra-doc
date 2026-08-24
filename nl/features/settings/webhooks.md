---
description: Leer alles over het integreren van webhooks in Dastra
---

# Webhooks

## Concept

Eenvoudig gezegd worden webhooks gebruikt om een actie** te triggeren na een gebeurtenis. Ze worden over het algemeen gebruikt om systemen met elkaar te laten communiceren. Dit is de eenvoudigste manier om een waarschuwing te ontvangen wanneer er iets gebeurt in Dastra. Het doel is om toepassingen van derden (API, CRM, serverloze functies, enz.) in realtime op de hoogte te brengen.



## Configuratie 🛠️

Om uw webhooks te configureren, gaat u naar: [https://app.dastra.eu/general-settings/webhooks](https://app.dastra.eu/general-settings/webhooks)

(<../../.gitbook/assets/image (252) (1) (1) (1).png>)

* Klik op maak een "webhook url".
* Voer je webhook ontvangst url in. Voor meer informatie, zie de sectie [Hoe de webhook ontvangen](webhooks.md#undefined).
* Voer de relevante werkruimte in
* Selecteer de gebeurtenis(sen) waarop u zich wilt abonneren. Het type gegevens dat wordt geretourneerd, verschilt afhankelijk van het type gebeurtenis. Je kunt de webhook bijvoorbeeld triggeren wanneer een nieuw verzoek om een recht uit te oefenen wordt aangemaakt. In dit geval zal de verzoektekst een json bevatten
* De webhook opslaan

Dit brengt u naar het **webhook detailscherm.**.

![](<../../.gitbook/assets/image (254) (1) (1).png>)

### Hoe de webhook te ontvangen 🛬

Om verzoeken van de webhook te ontvangen, moet je een event capture API endpoint maken. Het verzoek is in **POST** en zal altijd op deze manier gestructureerd zijn. De request body bevat een json met details van het getriggerde event.

Hier is de algemene structuur van het verzonden antwoord:&#x20;

```json
{
 "webhookId": <id van de webhook geconfigureerd in dastra>,
 "signatureUrl": "https://yourapi.com/webhooks/handle",
 "userId": <De gebruiker die het event heeft getriggerd>,
 "eventType": <De id van de gebeurtenis>,
 "eventName": <Het label van de gebeurtenis>,
 "data": <Dynamische gegevens van de gebeurtenis>,
 "date": <datum van de gebeurtenis>.
} 
```

Er wordt een time-out van 10 seconden toegepast op het verzoek, waarna het verzoek een foutmelding krijgt. De responscode moet 200.&#x20 zijn;

Er kan een kleine vertraging optreden tussen het moment dat het event optreedt in de applicatie en het moment dat de webhook wordt getriggerd (deze vertraging heeft te maken met de asynchrone aard van de uitvoering van webhooks in onze infrastructuur). Deze vertraging varieert afhankelijk van de belasting van onze infrastructuur en kan oplopen tot maximaal 60-120 seconden.

{% hint style="info" %}
Er is momenteel geen systeem om mislukte webhooks opnieuw af te spelen en zo te compenseren voor eventuele onbeschikbaarheid van de servers die de webhooks ontvangen. In dit geval raden we aan om de mislukte gebeurtenissen handmatig te synchroniseren.
{% endhint %}

### Test uw webhook url 🧪

U kunt nu uw webhook in echte omstandigheden testen **door op de knop "Testen" te klikken**.



### Hoe beveilig ik mijn webhook? 🛡️

{% hint style="info" %}
Ook al is het niet verplicht, het wordt **aanbevolen om het inkomende verzoek** van de webhook te valideren om mogelijke aanvallen te voorkomen van een hacker die het netwerk heeft afgeluisterd en zo alles op uw webhook url kan plaatsen en zo de aanmaak van elementen in uw systeem kan triggeren of spammen.
{% endhint %}

Elke keer dat er een verzoek wordt gedaan om een element in Dastra te wijzigen of te verwijderen, posten we een object naar alle url's die je hebt geconfigureerd voor de gewenste gebeurtenis. Elk POST verzoek zal een **Dastra-handtekening** header bevatten, die kan worden opgehaald aan de server kant &#x20;

Deze header komt overeen met de volledige JSON gepost **is gehashed met behulp van het HMAC-Sha256 algoritme** met behulp van de webhook validatiesleutel.

> DastraSignature = **HMAC256**(\<geserialiseerde JSON van POST>,\<webhook validatiesleutel>)

Hier zijn enkele voorbeelden van het valideren van de verzoekhandtekening:

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

### Wat gebeurt er als de url reageert met iets anders dan 200?

De webhook wordt automatisch geblokkeerd en als fout beschouwd wanneer de drempel van 5 fouten wordt overschreden.
