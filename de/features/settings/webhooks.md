---
description: >-
  Benachrichtigen Sie Ihre Anwendungen in Echtzeit, wenn in Dastra ein Ereignis
  eintritt: Webhooks konfigurieren, empfangen, absichern und über die API
  verwalten.
---

# Webhooks

## Konzept

Ein Webhook löst als Reaktion auf ein Ereignis eine Aktion aus. Webhooks lassen Systeme miteinander kommunizieren: Sie melden Ihnen sofort, wenn in Dastra etwas passiert. Ziel ist es, Drittanwendungen (APIs, CRM, Serverless-Funktionen usw.) in Echtzeit zu benachrichtigen.

## Konfiguration

Webhooks werden auf Organisationsebene konfiguriert und sind den Inhabern vorbehalten. Klicken Sie in der oberen Leiste auf das Zahnradsymbol (**Organisationseinstellungen**) und dann im linken Menü auf **Webhooks**. Die direkte Adresse lautet [https://app.dastra.eu/general-settings/webhooks](https://app.dastra.eu/general-settings/webhooks).

<figure><img src="../../.gitbook/assets/settings-webhooks-1.png" alt="Die Liste der konfigurierten Webhooks mit ihrem Status"><figcaption><p>Die Liste der Webhooks</p></figcaption></figure>

1. Klicken Sie auf **Erstellen Sie eine Webhook-URL**.
2. Geben Sie die **URL des Webhooks** ein. Was sie empfängt, erfahren Sie unter [Wie Sie den Webhook empfangen](webhooks.md#comment-receptionner-le-webhook).
3. Wählen Sie den Mandanten unter **Auswahl eines bestimmten Mandanten**. Wenn Sie keinen auswählen, gilt der Webhook für **Alle Mandanten**.
4. Optional: Geben Sie die **E-Mail-Adresse, die für den Versand von Benachrichtigungen bei wiederholten Fehlern verwendet wird**, ein. Dastra sendet eine E-Mail an diese Adresse, wenn der Webhook in den Fehlerzustand gerät.
5. Wählen Sie unter **Welche Veranstaltungen möchten Sie erhalten?** das Ereignis oder die Ereignisse aus, die Sie abonnieren möchten. Mindestens ein Ereignis ist erforderlich. Die Art der zurückgegebenen Daten hängt vom Ereignis ab: Wenn Sie zum Beispiel die Erstellung einer Betroffenenanfrage wählen, enthält der Request-Body ein JSON, das diese Anfrage beschreibt.
6. Klicken Sie auf **Speichern**.

<figure><img src="../../.gitbook/assets/settings-webhooks-3.png" alt="Das Formular zum Erstellen eines Webhooks mit URL, Mandant, E-Mail-Adresse und Ereignissen"><figcaption><p>Das Webhook-Formular</p></figcaption></figure>

Die verfügbaren Ereignisse sind die des Benachrichtigungscenters, gruppiert nach Objekttyp (Verarbeitungstätigkeiten, Betroffenenanfragen, Datenschutzvorfälle usw.).

{% hint style="info" %}
Eine Organisation kann bis zu 30 Webhooks anlegen.
{% endhint %}

Damit gelangen Sie zur Detailansicht des Webhooks. Sie zeigt die URL, den Mandanten, den Status des Webhooks (aktiviert oder **Deaktiviert**), gegebenenfalls die **Letzte Fehlermeldung**, die abonnierten Ereignisse und den **Validierungsschlüssel für den Webhook**, den Sie kopieren können. Dort finden Sie auch die Schaltflächen **Bearbeiten**, **Test-Webhook senden** und **Löschen**.

<figure><img src="../../.gitbook/assets/settings-webhooks-2.png" alt="Die Detailansicht eines Webhooks mit maskiertem Validierungsschlüssel"><figcaption><p>Die Details eines Webhooks</p></figcaption></figure>

## Wie Sie den Webhook empfangen <a href="#comment-receptionner-le-webhook" id="comment-receptionner-le-webhook"></a>

Um Webhook-Anfragen zu empfangen, müssen Sie einen API-Endpunkt zur Erfassung von Ereignissen erstellen. Die Anfrage erfolgt als POST und ist immer gleich aufgebaut. Der Request-Body enthält ein JSON mit den Details des ausgelösten Ereignisses.

Hier ist die allgemeine Struktur der gesendeten Anfrage:

```json
{
 "webhookId": <id of the webhook configured in dastra>,
 "signatureUrl": "https://yourapi.com/webhooks/handle",
 "userId": <The user who triggered the event>,
 "eventType": <The id of the event>,
 "eventName": <The label of the event>,
 "data": <Event dynamic data>,
 "date": <date of the event>
}
```

Für die Anfrage gilt ein Timeout von 10 Sekunden, danach gilt sie als fehlgeschlagen. Die Antwort muss ein Erfolgscode (2xx) sein, zum Beispiel 200.

Zwischen dem Eintreten des Ereignisses in der Anwendung und dem Senden des Webhooks kann eine kleine Verzögerung liegen. Sie hängt mit der asynchronen Ausführung von Webhooks in unserer Infrastruktur zusammen, richtet sich nach der Auslastung der Infrastruktur und kann bis zu 60 bis 120 Sekunden betragen.

{% hint style="info" %}
Derzeit gibt es kein System, um fehlgeschlagene Webhooks erneut abzuspielen und so eine Nichtverfügbarkeit des empfangenden Servers auszugleichen. In diesem Fall empfehlen wir, die fehlgeschlagenen Ereignisse manuell zu synchronisieren.
{% endhint %}

## Ihre Webhook-URL testen

Um Ihren Webhook unter realen Bedingungen zu testen, öffnen Sie seine Detailansicht und klicken Sie auf **Test-Webhook senden**. Gehen Sie im Fenster **Webhook-Testtool** so vor:

1. Wählen Sie unter **Bitte wählen Sie das Ereignis aus, das Sie testen möchten.** das zu testende Ereignis aus. Die Liste zeigt die Ereignisse, die der Webhook abonniert hat.
2. Ändern Sie bei Bedarf die gesendeten Daten unter **Übermitteln Sie die Daten (falls erforderlich)**. Dastra füllt sie mit einem Beispiel für das gewählte Ereignis aus.
3. Klicken Sie auf **Test-Webhook senden**.

Eine Bestätigungsmeldung zeigt an, dass Ihre URL mit dem Code 200 geantwortet hat. Wurde der Webhook nach Fehlern blockiert, aktiviert ihn ein erfolgreicher Test wieder.

<figure><img src="../../.gitbook/assets/settings-webhooks-4.png" alt="Das Fenster Webhook-Testtool mit dem Ereignis und den zu sendenden Daten"><figcaption><p>Das Testtool für Webhooks</p></figcaption></figure>

## Den Webhook absichern

{% hint style="info" %}
Die Validierung der eingehenden Anfrage ist nicht zwingend, wird aber empfohlen. Sie verhindert, dass jemand, der das Netzwerk beobachtet hat, beliebige Inhalte an Ihre Webhook-URL sendet und so die Erstellung von Elementen in Ihrem System auslöst oder vervielfacht.
{% endhint %}

Jedes Mal, wenn ein von Ihnen abonniertes Ereignis eintritt, sendet Dastra eine POST-Anfrage an die Webhook-URL. Jede Anfrage enthält den Header `Dastra-Signature`, den Ihr Server auslesen kann.

Sein Wert ist der HMAC-SHA256 des exakten JSON-Bodys der Anfrage, berechnet mit dem Signaturschlüssel des Webhooks und anschließend in Base64 kodiert.

> Dastra-Signature = **Base64**(**HMAC-SHA256**(\<JSON-Body der Anfrage>, \<Signaturschlüssel des Webhooks>))

Verwenden Sie den Signaturschlüssel genau so, wie er in der Detailansicht des Webhooks angezeigt wird. Hier sind Beispiele für die Validierung der Signatur:

{% tabs %}
{% tab title="PHP" %}
```php
<?php
$secret = 'YOUR_WEBHOOK_KEY'; // signature key shown on the webhook details screen

$payload = file_get_contents('php://input'); // raw request body
$signature = $_SERVER['HTTP_DASTRA_SIGNATURE'] ?? ''; // value of the Dastra-Signature header

$computed = base64_encode(hash_hmac('sha256', $payload, $secret, true));

if (!hash_equals($computed, $signature)) {
    http_response_code(401);
    exit;
}

// the signature is valid: process the event
http_response_code(200);
```
{% endtab %}

{% tab title="C#" %}
```csharp
[HttpPost("webhooks/handle")]
public async Task<IActionResult> Handle()
{
    string signature = Request.Headers["Dastra-Signature"];
    string key = "YOUR_WEBHOOK_KEY";

    using var reader = new StreamReader(Request.Body, Encoding.UTF8);
    string payload = await reader.ReadToEndAsync();

    if (!ValidateSignature(signature, payload, key))
    {
        return Unauthorized();
    }

    // the signature is valid: process the event
    return Ok();
}

private static bool ValidateSignature(string signature, string payload, string secret)
{
    using var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(secret));
    byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(payload));
    string computed = Convert.ToBase64String(hash);

    return CryptographicOperations.FixedTimeEquals(
        Encoding.UTF8.GetBytes(computed),
        Encoding.UTF8.GetBytes(signature ?? string.Empty));
}
```
{% endtab %}
{% endtabs %}

## Verhalten bei Fehlern

Der Webhook gilt als fehlerhaft, wenn mehr als 5 Fehler aufgezeichnet wurden. Dastra sendet dann keine Ereignisse mehr an seine URL, solange der letzte Fehler weniger als 24 Stunden zurückliegt. Ist in der Konfiguration eine E-Mail-Adresse angegeben, erhält sie eine Nachricht. Ein erfolgreicher Test setzt den Fehlerzähler zurück.

## Webhooks über die API einrichten

Rufen Sie die mit Ihrem Konto verknüpften Webhooks ab (in allen Mandanten). Der optionale Parameter `workspaceId` beschränkt die Liste auf einen Mandanten.

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls" method="get" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}

Erstellen Sie über den POST-Endpunkt eine neue Webhook-URL. Geben Sie mit dem Parameter `subscribedEvents` die Ereignisse an, die Ihr Webhook abonnieren soll.

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls" method="post" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}

Sie erhalten eine Webhook-ID zurück. Damit können Sie den Webhook lesen, aktualisieren oder löschen.

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls/{id}" method="get" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls/{id}" method="put" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/dastra-api.json" path="/v1/WebHookUrls/{id}" method="delete" %}
[dastra-api.json](../../.gitbook/assets/dastra-api.json)
{% endopenapi %}
