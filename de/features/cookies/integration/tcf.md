# TCF 1.1/2.0

{% hint style="danger" %}
**Derzeit befindet sich diese Funktion noch in der Experimentierphase. Jede Implementierung des TCF wird nicht wirksam sein**&#x20;
{% endhint %}

Das [Consent Management Platform (CMP) Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) wird derzeit vom Dastra-Widget unterstützt. Um das Opt-in der IAB-Anbieter zu aktivieren, gehen Sie einfach in den Bereich „Dienste" der Widget-Konfiguration und aktivieren Sie das entsprechende Kontrollkästchen.

Sobald das Kontrollkästchen aktiviert ist, können Sie die Änderungen in der Widget-Oberfläche sehen:

![](<../../../.gitbook/assets/image-69.png>)

Beim IAB-Opt-in wird automatisch das Cookie, das die kodierten Informationen über die Einwilligung des Nutzers zu den IAB-Anbietern enthält, im Browser erstellt:

![](<../../../.gitbook/assets/image-71.png>)

{% hint style="info" %}
Dieses Cookie hat standardmäßig eine Lebensdauer von 180 Tagen und heißt „eupubconsent"
{% endhint %}

### Die IAB-Einwilligungszeichenkette erfassen

Wenn der Nutzer seine Einwilligung erteilt, ist es möglich, die Einwilligungszeichenkette direkt mit dem folgenden Event-Listener zu erfassen:

```javascript
document.addEventListener('dastra:consentstring',function(consentString){
    console.log(consentString); // BOybBVKOybbNhABABBENCoAAAAAq6AAA
});
```
