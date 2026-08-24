---
description: Vous saurez tout sur l'intégration de webhooks dans Dastra
---

# Webhooks



{% embed url="https://youtu.be/gqwGui1ua7Y" %}

## Concept 👓

Pour faire simple, les webhooks permettent de **déclencher une action** suite à un événement. Ils sont généralement utilisés pour faire communiquer des systèmes. C’est la façon la plus simple de recevoir une alerte lorsque quelque chose se produit dans Dastra. L'objectif est de notifier des applications tierces (API, CRM, Fonctions serverless...) en temps réel.



## Configuration 🛠️

Pour configurer vos webhooks, rendez-vous sur la page : [https://app.dastra.eu/general-settings/webhooks](https://app.dastra.eu/general-settings/webhooks)

![](<../../.gitbook/assets/settings-webhooks-list.png>)

* Cliquez sur créer une "url de webhook"
* Renseignez l'url de réception de votre webhook. Pour en savoir plus consultez la section [Comment réceptionner le webhook](webhooks.md#undefined).
* Renseignez l'espace de travail concerné
* Sélectionnez le ou les évènements auxquels vous souhaitez vous abonner. Le type de données renvoyés sera différent selon le type d'évènement. Par exemple, vous pouvez déclencher le webhook lors de la création d'une nouvelle demande d'exercice de droit. Dans ce cas le body de la requête contiendra un json
* Enregistrez le webhook

Vous arrivez sur l'**écran de détail du webhook.**

![](<../../.gitbook/assets/settings-webhook-detail.png>)

### Comment réceptionner le webhook 🛬

Pour réceptionner les requêtes du webhook, vous devez créer un endpoint d'API de captation de l'évènement. La requête effectuée est en **POST** et sera toujours structurée de cette façon. Le body de la requête contient un json avec le détail de l'évènement déclenché.

Voici la structure générale de la réponse envoyée :&#x20;

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

Un timeout de 10 secondes est appliqué sur la requête, au delà de ce temps la requête sera en erreur. Il est nécessaire que le code de réponse soit 200.&#x20;

Il peut y avoir un petit délai entre le moment où l'évènement a lieu dans l'application et le déclenchement du webhooks (ce délai est lié à la nature asynchrone de l'exécution du webhook dans notre infrastructure). Ce délai est plus ou moins important selon la charge de notre infrastructure et peut aller jusque 60-120 secondes maximum.

{% hint style="info" %}
Il n'existe pour l'instant aucun système permettant de rejouer les webhooks qui ont échoués et donc de compenser une éventuelle indisponibilité des serveurs de réception des webhooks. Dans ce cas, nous vous recommandons d'effectuer une synchronisation manuelle des évènements qui ont échoué.
{% endhint %}

### Tester votre url de webhooks 🧪

Vous allez pouvoir tester votre webhook en condition réelle **en cliquant sur le bouton "Tester".**



### Comment sécuriser le webhook ? 🛡️

{% hint style="info" %}
Même si ce n'est pas une obligation, il est **recommandé de valider la requête entrante** du webhook pour éviter les attaques potentielles d'un hackeur qui aurait sniffé le réseau et serait ainsi en capacité de poster n'importe quoi sur votre url de webhook et ainsi déclencher ou spammer la création d'éléments dans votre système.
{% endhint %}

Chaque fois qu'une requête de modification, suppression d'un élément de Dastra est effectuée, nous allons poster un objet sur toutes les urls que vous avez configurés sur l'évènement voulu. Dans chaque requête POST figurera une entête **Dastra-Signature**, cette entête peut être récupérée côté serveur.&#x20;

Cette entête correspond à l'intégralité du JSON posté **est hashé à l'aide de l'algorithme HMAC-Sha256** à l'aide de la clé de validation du webhook.

> DastraSignature = **HMAC256**(\<JSON sérialisé du POST>,\<clé de validation du webhook>)

Voici quelques exemples de validation de la signature de la requête :

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

### Que se passe-t-il quand l'url répond autre chose que 200

Le webhook sera automatiquement bloqué et considéré en erreur quand le seuil de 5 erreurs est dépassé.

### &#x20;Comment mettre en place des webhooks avec les API

Récupérer les webhooks liés à votre compte (dans tous les espaces de travail)

{% swagger src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls" method="get" %}
[dastra api.json](<../../.gitbook/assets/dastra-api.json>)
{% endswagger %}

Créez une nouvelle url de webhook en utilisant le endpoint POST. Renseignez les évènements auxquels vous souhaitez abonner votre webhook avec le paramètre **subscribedEvents** webhooks.

{% swagger src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls" method="post" %}
[dastra api.json](<../../.gitbook/assets/dastra-api.json>)
{% endswagger %}

Un identifiant de webhook vous sera retourné

{% swagger src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls/{id}" method="get" %}
[dastra api.json](<../../.gitbook/assets/dastra-api.json>)
{% endswagger %}

{% swagger src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls/{id}" method="delete" %}
[dastra api.json](<../../.gitbook/assets/dastra-api.json>)
{% endswagger %}
