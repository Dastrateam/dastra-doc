---
description: Stuur de beveiligingsauditgebeurtenissen van uw account in realtime door naar uw SIEM
---

# SIEM-streaming

### Wat is het?

SIEM-streaming stuurt **de beveiligingsauditgebeurtenissen van uw Dastra-account in realtime door naar uw SIEM**: aanmeldingen, wijzigingen van machtigingen, API-sleutels, MFA- en SSO-wijzigingen, verwijderingen van gebruikers en workspaces, enz. Alle auditgebeurtenissen van het account worden doorgestuurd, zodat uw beveiligingsteam het volledige spoor heeft in de tool die het al bewaakt (Splunk, Sentinel, Sumo Logic, QRadar …).

Los van streaming kunnen de auditlogs ook **handmatig worden geëxporteerd** in SIEM-formaten – zie [Handmatige export](#handmatige-export-vanuit-de-auditlogs) hieronder.

### Vereisten

* Het **Enterprise-abonnement** (functie Geavanceerde beveiliging).
* **Eigenaar** van het account zijn: de configuratie staat in het **Beveiligingscentrum**, onderaan de pagina **Beveiliging** (sectie **SIEM-gebeurtenissenstreaming**).
* Aan de SIEM-kant: een HTTP-event-collector-endpoint dat via HTTPS bereikbaar is (bv. een Splunk-HEC-endpoint) en het bijbehorende token of de API-sleutel.

<figure><img src="../../.gitbook/assets/siem-menu.png" alt=""><figcaption><p>De sectie SIEM-gebeurtenissenstreaming in Beveiligingscentrum > Beveiliging</p></figcaption></figure>

### Configuratie

Vul het formulier in en klik op **Opslaan**:

* **Collector-endpoint** (verplicht) – de HTTP(S)-URL van uw SIEM-collector, bv. `https://collector.example.com/services/collector/event` voor Splunk HEC.
* **Authenticatie** – hoe het token met elke gebeurtenis wordt verstuurd:
  * **Bearer** – `Authorization: Bearer <token>` (standaard),
  * **API Key** – `Authorization: ApiKey <token>`,
  * **Authorization met aangepast schema** – `Authorization: <schema> <token>`, waarbij u het woord van het **Autorisatieschema** invult (bv. `Splunk` voor een Splunk-HEC-input, `Api-Token` voor Dynatrace),
  * **Custom header** – het token wordt verstuurd in de header die u opgeeft bij **Headernaam** (bv. `X-API-Key`),
  * **None** – geen authenticatieheader (bv. wanneer het token deel uitmaakt van de URL).
* **Token / API-sleutel** – het token van de collector. Het wordt versleuteld opgeslagen en nooit meer getoond; laat het veld later leeg om het huidige te behouden.
* **Aangepaste headers (optioneel)** – extra HTTP-headers die met elke gebeurtenis worden verstuurd, als sleutel/waarde-paren.
* **Gebeurtenisformaat**:
  * **Splunk HEC (JSON)** – het eigen formaat van de Splunk HTTP Event Collector. Er verschijnen twee extra optionele velden: **Source type** (standaard `dastra:audit`) en **Index**.
  * **Dynatrace (Log Monitoring v2)** – het eigen formaat van de Dynatrace-logingest-API.
  * **CEF (Common Event Format)** – voor ArcSight, Sumo Logic en de meeste SIEM's die CEF verwerken.
  * **Syslog (RFC 5424)** – gestructureerde syslogregels.
* **Minimale ernst** – het laagste niveau dat nog wordt doorgestuurd: **Alle gebeurtenissen**, **Notice en hoger**, **Warning en hoger (beveiligingsgebeurtenissen)** of **Error en hoger**. Het standaardniveau – en aanbevolen – is **Warning en hoger**: u behoudt de voor de beveiliging relevante signalen (mislukte aanmeldingen, wijzigingen van machtigingen, SSO/MFA, API-sleutels, verwijderingen …) zonder uw SIEM te overspoelen met dagelijkse activiteit. Kies *Alle gebeurtenissen* alleen als uw SIEM het volledige auditspoor moet verwerken.
* **TLS-certificaat controleren** – laat dit ingeschakeld; schakel het alleen uit voor een zelfondertekende ontwikkelcollector.

Schakel vervolgens **Realtime streaming activeren** in.

{% hint style="info" %}
**Veelvoorkomende voorbeelden** – Splunk HEC: endpoint `https://<host>:8088/services/collector/event`, formaat *Splunk HEC (JSON)*, authenticatie *Bearer* (of *Authorization met aangepast schema* + `Splunk` voor klassieke HEC-inputs). Dynatrace: endpoint `https://<omgeving>.live.dynatrace.com/api/v2/logs/ingest`, formaat *Dynatrace (Log Monitoring v2)*, authenticatie *Authorization met aangepast schema* + `Api-Token`.
{% endhint %}

<figure><img src="../../.gitbook/assets/siem-form.png" alt=""><figcaption><p>Configuratie van SIEM-streaming</p></figcaption></figure>

### De verbinding testen

**Verbinding testen** stuurt een synthetische testgebeurtenis met de waarden van het formulier naar uw collector en toont het resultaat ("Testgebeurtenis succesvol afgeleverd", of de HTTP-fout die de collector teruggeeft). Gebruik het na elke wijziging – de test vereist niet dat streaming is ingeschakeld.

{% hint style="info" %}
Streaming geldt voor het hele account (alle workspaces). Er is één SIEM-configuratie per account.
{% endhint %}

### Wat wordt naar het SIEM gestuurd?

Elke auditgebeurtenis wordt afzonderlijk en doorlopend afgeleverd, met de volgende inhoud:

| Veld | Inhoud |
| --- | --- |
| `id` | Unieke identificatie van de auditgebeurtenis |
| `time` / `timestamp` | Tijdstip van de gebeurtenis (UTC) |
| `action` | Type gebeurtenis, bv. `UserLogin`, `PermissionChange`, `ApiKeyAdded` |
| `message` | Leesbare beschrijving |
| `objectType` / `objectId` | Betrokken record, indien van toepassing |
| `severity` | Ernst van het type syslog (zie hieronder) |
| `outcome` | `success` of `failure` |
| `actorId` / `actorName` / `actorEmail` | Wie de actie heeft uitgevoerd |
| `tenantId` / `workspaceId` / `workspaceName` / `areaId` | Waar het is gebeurd |
| `url` | Directe link naar het record in Dastra |

Voor de beveiliging gevoelige gebeurtenissen krijgen een hogere ernst, los van hun weergaveprioriteit in Dastra: herhaalde mislukte aanmeldingen worden als **Error** verstuurd (met `outcome: failure`); wijzigingen van machtigingen, het aanmaken/verwijderen van API-sleutels, MFA- en SSO-wijzigingen, intrekkingen en verwijderingen van gebruikers en verwijderingen van workspaces worden als **Warning** verstuurd. Op deze ernst is ook de instelling **Minimale ernst** gebaseerd – *Warning en hoger* (de aanbevolen instelling) beperkt de stroom tot deze beveiligingsgebeurtenissen.

{% hint style="info" %}
De gebeurtenissen bevatten de naam en het e-mailadres van de uitvoerder van de actie – de gegevens die al in het Dastra-auditlogboek worden getoond. Er wordt geen inhoud van records (persoonsgegevens van betrokkenen, documentinhoud …) doorgestuurd.
{% endhint %}

### Handmatige export vanuit de auditlogs

U kunt het beveiligingsauditspoor op verzoek exporteren, in dezelfde formaten, zonder streaming te configureren:

1. Open **Beveiligingscentrum > Beveiligingslogs**.
2. Stel de filters (periode, workspace …) naar wens in.
3. Open het menu **Exporteren (SIEM)** naast de gebruikelijke exportknop en kies **CEF (Common Event Format)**, **Syslog (RFC 5424)** of **Splunk HEC (JSON)**.

Het bestand (`dastra-security-logs-<datum>`) bevat de overeenkomende auditgebeurtenissen, tot 100.000, klaar om door uw SIEM te worden ingelezen.

Hetzelfde menu biedt ook **Realtime streaming configureren**, een snelkoppeling naar de hierboven beschreven streamingconfiguratie.

<figure><img src="../../.gitbook/assets/audit-logs-export-siem.png" alt=""><figcaption><p>Eenmalige SIEM-export vanuit de beveiligingslogs</p></figcaption></figure>

### Probleemoplossing

* **Test mislukt: HTTP 401/403** – controleer het token en het authenticatieschema dat uw collector verwacht (Splunk HEC verwacht het token zoals geconfigureerd op de HEC-input; sommige collectors verwachten een aangepaste header).
* **Test mislukt: certificaatfout** – uw collector gebruikt een certificaat dat Dastra niet kan controleren. Herstel de certificaatketen; schakel **TLS-certificaat controleren** alleen uit voor een ontwikkelcollector.
* **Er komen geen gebeurtenissen aan** – controleer of **Realtime streaming activeren** is ingeschakeld en raadpleeg de ingestlogs van uw collector. Gebruik **Verbinding testen** om connectiviteit en configuratie van elkaar te scheiden.
