---
description: Diese Seite erklärt, wie Sie API-Schlüssel in Dastra erstellen
---

# Verwaltung der API-Schlüssel

### Wozu dienen API-Schlüssel?

* **Einen API-Client erstellen** für Dastra, um Daten außerhalb der Anwendung abzurufen oder zu ändern. Dieser Client kann Server-zu-Server (Client Credential) oder JavaScript (Authorization Code) sein. Weitere Informationen finden Sie in der [Dokumentation zur Authentifizierung der Dastra-API](../../api-references/authentification.md).
* **Ein Widget zur Rechteausübung konfigurieren** (nur öffentlicher Schlüssel). [Lesen Sie die Dokumentation zur Einrichtung des Rechteausübungs-Widgets](../gerer-les-exercices-des-droits/implementez-un-widget-dexercice-des-droits.md)
* **Ein Cookie-Consent-Widget konfigurieren** (nur öffentlicher Schlüssel). [Lesen Sie die Dokumentation zur Einrichtung der Cookie-Einwilligung](../gerer-le-consentement-aux-cookies/)

### Wie generiere ich einen API-Schlüssel?

1. [Greifen Sie auf den Manager](https://app.dastra.eu/general-settings/api) der Dastra-Schlüssel zu (Nur Kontoinhaber haben Zugang zu diesem Bereich)
2. Klicken Sie auf „**API-Schlüssel erstellen**"&#x20;
3. Geben Sie den Namen des Schlüssels und die Umleitungs- und CORS-URLs ein (wenn Sie die API in JavaScript mit OAuth2 verwenden möchten)
4. Klicken Sie auf „**Speichern**"
5. Sobald Ihr API-Schlüssel erstellt ist, können Sie ihn direkt aus dem Manager kopieren und einfügen (privater oder öffentlicher Schlüssel)

{% hint style="warning" %}
**Bewahren Sie Ihre API-Schlüssel sorgfältig auf! Der private Schlüssel darf unter keinen Umständen öffentlich verbreitet werden!**

**Wenn die Sicherheit Ihres API-Schlüssels kompromittiert ist**, können Sie ihn aus dem Manager löschen und einen neuen generieren
{% endhint %}
