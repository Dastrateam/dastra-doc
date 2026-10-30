---
description: >-
  Richten Sie die einmalige Anmeldung (SSO) für Ihre Organisation in Dastra
  ein: Protokolle, Verbindungsoptionen, automatische Nutzererstellung und
  Verwaltung der Anmeldungen.
---

# Single Sign On (SSO)

## Funktionsprinzip

Die **einmalige Anmeldung**, oft mit dem englischen Kürzel **SSO** (Single Sign-On) bezeichnet, ist eine Methode, mit der ein Nutzer nach einer einzigen Authentifizierung auf mehrere Anwendungen (oder gesicherte Websites) zugreifen kann.

Ein Unternehmen kann **sein eigenes Authentifizierungssystem** anstelle der lokalen Anmeldung verwenden, die Dastra standardmäßig anbietet. Zu den am häufigsten verwendeten SSO-Systemen gehören Microsoft Active Directory, Google Workspace (früher GSuite) und Auth0.

**Die Funktionsweise ist wie folgt:**

Ein Nutzer (**User Agent**) fordert eine Verbindung beim Dienstanbieter (**Service Provider**) an, der einen Identitätsanbieter (**Identity Provider**) bittet, den Nutzer zu authentifizieren. Das Ergebnis der Authentifizierung wird dann an den Dienstanbieter zurückgesendet, der die Verbindungsanfrage des Nutzers akzeptiert.

Bei Dastra ist der User Agent **der Browser eines Dastra-Nutzers**, der Service Provider ist **Dastra** und der Identity Provider ist **Ihr Authentifizierungsanbieter** (zum Beispiel Active Directory).

<figure><img src="../../../.gitbook/assets/sso.png" alt="Funktionsweise des SSO mit dem Protokoll SAML 2: die Austauschvorgänge zwischen Dienstanbieter, User Agent und Identitätsanbieter"><figcaption></figcaption></figure>

## Einrichtung

Ein Dastra-Abonnement kann eine oder mehrere SSO-Anmeldungen enthalten, wenn die Funktion in Ihrem Abonnement enthalten ist. Um sie zu verwalten, öffnen Sie die **Organisationseinstellungen** (unten im Menü **Mandanteneinstellungen**) und dann **Einmalige Anmeldung**. Sie gelangen auf die [Konfigurationsseite der SSO-Anmeldungen](https://app.dastra.eu/general-settings/sso).

{% hint style="info" %}
Nur ein Inhaber der Organisation kann auf diese Seite zugreifen.
{% endhint %}

<figure><img src="../../../.gitbook/assets/settings-sso-overview-1.png" alt="Die Seite Einmalige Anmeldung mit dem Block der zugelassenen E-Mail-Domains, der Liste der SSO-Verbindungen und der SCIM-Karte"><figcaption><p>Die Seite <strong>Einmalige Anmeldung</strong></p></figcaption></figure>

Die Seite besteht aus drei Blöcken:

* **Zugelassene E-Mail-Domains** oben: siehe [E-Mail-Domains](../email-domains.md).
* Die Liste Ihrer SSO-Verbindungen, die Sie mit **SSO-Login hinzufügen** erweitern.
* **SCIM** unten: siehe [SCIM](../scim.md).

Um eine Verbindung zu erstellen, klicken Sie auf **SSO-Login hinzufügen** und wählen Sie dann das Protokoll. Dastra bietet zwei Single-Sign-On-Protokolle an, [**SAML 2**](saml.md) und [**OpenID**](openid.md). Über die folgenden Links gelangen Sie zu den Konfigurationsanleitungen.

{% content-ref url="saml.md" %}
[saml.md](saml.md)
{% endcontent-ref %}

{% content-ref url="openid.md" %}
[openid.md](openid.md)
{% endcontent-ref %}

{% content-ref url="adfs.md" %}
[adfs.md](adfs.md)
{% endcontent-ref %}

{% content-ref url="entra-id.md" %}
[entra-id.md](entra-id.md)
{% endcontent-ref %}

{% content-ref url="okta.md" %}
[okta.md](okta.md)
{% endcontent-ref %}

{% content-ref url="known-problems.md" %}
[known-problems.md](known-problems.md)
{% endcontent-ref %}

## Formularfelder

Das Formular einer SSO-Verbindung öffnet sich in einem Seitenfenster mit drei Abschnitten.

**1. Allgemeines**

* **Bezeichnung der SSO-Anmeldung**: der Name der Verbindung in der Liste, höchstens 80 Zeichen.
* **Für alle Nutzer erzwingen**: Alle Nutzer müssen sich mit dieser SSO-Anmeldung anmelden. Siehe [SSO für alle Nutzer aktivieren](#sso-fur-alle-nutzer-aktivieren).
* **Aktivieren**: Ist die Verbindung deaktiviert, bleibt die Standardanmeldung mit Passwort in Kraft.
* **Standardmäßig neuen eingeladenen Benutzern zugewiesen**: Dastra wählt diese Verbindung standardmäßig aus, wenn Sie einen neuen Nutzer einladen.

**2. Konfiguration**

* Die protokollspezifischen Felder: siehe [SAML 2](saml.md) und [OpenID](openid.md).
* **Der Name des Anspruchs, der die E-Mail-Adresse enthält**: der Name des Claims, in dem Ihr Identitätsanbieter die E-Mail-Adresse des Nutzers zurückgibt. Wenn Dastra Ihre Nutzer nicht erkennt, siehe [Bekannte Probleme](known-problems.md).

**3. Automatische Erstellung von Nutzern**

* **Nutzer wird erstellt, wenn der Nutzer noch nie zu Dastra eingeladen wurde**: aktiviert die automatische Kontoerstellung. Siehe [Automatische Nutzerbereitstellung aktivieren](#automatische-nutzerbereitstellung-aktivieren).
* **Die standardmäßig allen Mandanten des Abonnements zugewiesene Rolle, wenn der Nutzer erstellt wird**: optional.
* **Auswahl eines bestimmten Mandanten**: optional. Wenn Sie einen Mandanten auswählen, erscheint ein Feld für den Namen des Gruppenanspruchs: siehe [Team-Binding](#team-binding).

## SSO für alle Nutzer aktivieren

1. Klicken Sie in der Liste der SSO-Verbindungen auf die Verbindung.
2. Aktivieren Sie im Abschnitt **Allgemeines** die Option **Für alle Nutzer erzwingen**.

<figure><img src="../../../.gitbook/assets/settings-sso-overview-3.png" alt="Der Abschnitt Allgemeines des SSO-Formulars mit aktivierter Option Für alle Nutzer erzwingen und dem Feld für ausgenommene Nutzer"><figcaption><p>Der Abschnitt <strong>Allgemeines</strong> der Verbindung</p></figcaption></figure>

### Von der SSO-Anmeldung befreite Nutzer

In manchen Fällen möchten Sie **das SSO für bestimmte Nutzer ausschalten**, zum Beispiel für einen Sicherheitsadministrator, ein Dienstkonto oder einen Nutzer, der nicht in Ihrem Active Directory enthalten ist. Sie können bestimmte Nutzer benennen, die nicht auf die SSO-Anmeldung Ihrer Organisation weitergeleitet werden. Wir empfehlen, mindestens einen Nutzer mit einem lokalen Dienstkonto zu benennen: So können Sie sich bei einer SSO-Störung, etwa einem Ausfall des Identitätsanbieters oder einem Konfigurationsfehler, wieder Zugang verschaffen.

Diese Nutzer melden sich **mit ihrem Passwort** an der Anwendung an.

Um sie zu benennen, wählen Sie Nutzer Ihrer Organisation im Feld **Bestimmte Nutzer, die von der SSO ausgenommen sind (z. B. Sicherheitsadministratoren)** aus. Dieses Feld erscheint, wenn **Für alle Nutzer erzwingen** aktiviert ist.

## Automatische Nutzerbereitstellung aktivieren

Wenn die Nutzer Ihres Identitätsanbieters kein Konto benötigen sollen, bevor sie auf die Organisation zugreifen, aktivieren Sie im Abschnitt **Automatische Erstellung von Nutzern** die Option **Nutzer wird erstellt, wenn der Nutzer noch nie zu Dastra eingeladen wurde**.

Die automatische Bereitstellung funktioniert nur, wenn sich die Nutzer über den Link Ihrer SSO-Verbindung anmelden. Von der Standard-Anmeldeseite aus funktioniert sie nicht. Der Link sieht so aus:

```
https://account.dastra.eu/Account/ExternalLogin?returnUrl=https://app.dastra.eu&provider={your provider id}
```

Die Adressen im Link sind die Ihrer Region. Um ihn zu erhalten, klicken Sie auf der Karte der Verbindung rechts neben **Testen** auf die Schaltfläche **Link kopieren** und senden Sie ihn dann an Ihre Nutzer.

<figure><img src="../../../.gitbook/assets/settings-sso-overview-2.png" alt="Die Karte einer SSO-Verbindung mit den Schaltflächen Testen und Link kopieren"><figcaption><p>Die Schaltfläche <strong>Link kopieren</strong> auf der Karte</p></figcaption></figure>

Nach einer erfolgreichen Authentifizierung wird das Konto automatisch in Dastra erstellt. Die Inhaber der Organisation erhalten dann eine Benachrichtigung mit dem Namen und der E-Mail-Adresse des erstellten Kontos, dem Datum und der Uhrzeit, der SSO-Verbindung, die es erstellt hat, der zugewiesenen Standardrolle und gegebenenfalls dem betroffenen Mandanten. Sie verweist auf die Seite **Nutzer**, damit Sie die erwarteten Rechte ohne Verzögerung vergeben können.

{% hint style="warning" %}
Wird das Konto eines Nutzers beim Authentifizierungsanbieter gelöscht oder deaktiviert, wird es in Dastra nicht gelöscht, aber der Nutzer kann sich nicht mehr anmelden. Sie können diese Konten in der [Nutzerverwaltung des Abonnements](https://app.dastra.eu/general-settings/users) bereinigen.
{% endhint %}

Sie können **Die standardmäßig allen Mandanten des Abonnements zugewiesene Rolle, wenn der Nutzer erstellt wird** auswählen.

<figure><img src="../../../.gitbook/assets/settings-sso-overview-4.png" alt="Der Abschnitt Automatische Erstellung von Nutzern mit der Standardrolle, dem Mandanten und dem Namen des Gruppenanspruchs"><figcaption><p>Der Abschnitt <strong>Automatische Erstellung von Nutzern</strong></p></figcaption></figure>

{% hint style="info" %}
Dastra unterstützt derzeit nicht die Zuordnung von Rollen anhand der Eigenschaften des Authentifizierungsservers. Wenn Ihnen diese Funktion wichtig ist, melden Sie dies über die [Supportseite](https://app.dastra.eu/general-settings/support).
{% endhint %}

### Team-Binding

Sie können die Teams eines Mandanten an eine Eigenschaft (Claim) binden, die Ihr Authentifizierungsserver zurückgibt. Wählen Sie den Mandanten unter **Auswahl eines bestimmten Mandanten** aus und geben Sie dann im darunter erscheinenden Feld den Namen des Gruppenanspruchs ein: Dastra stellt die Teams anhand dieses Claims bereit.

## Nutzeranmeldungen verwalten

Sie legen die Anmeldeart jedes Nutzers in der [Nutzerverwaltung des Abonnements](https://app.dastra.eu/general-settings/users) fest (**Organisationseinstellungen** > **Nutzer**). Öffnen Sie das Profil des Nutzers und wählen Sie unter **Standardmäßige Verbindungsmethode** die bevorzugte SSO-Anmeldung. Ein Nutzer, der sich anschließend mit seiner E-Mail-Adresse bei Dastra anmeldet, wird auf die Anmeldeseite des von Ihnen eingerichteten Authentifizierungsanbieters weitergeleitet.

Wenn das SSO für alle Nutzer erzwungen wird, zeigt das Profil stattdessen eine entsprechende Meldung an.

Um die Anmeldeart mehrerer Nutzer auf einmal zu ändern, aktivieren Sie sie in der Liste **Nutzer** und öffnen Sie dann **Bitte wählen Sie eine Sammelaktion aus** über der Liste und wählen Sie **Anmeldemodus ändern**. Wählen Sie die Methode unter **Standardmäßige Verbindungsmethode** und speichern Sie dann. Externe Nutzer und Nutzer, die in ein global zugewiesenes SSO gezwungen sind, bleiben unberührt. Die Aktion erscheint, wenn SSO Teil Ihres Tarifs ist.

<figure><img src="../../../.gitbook/assets/settings-sso-overview-5.png" alt="Ein Nutzerprofil mit der Liste Standardmäßige Verbindungsmethode"><figcaption><p>Das Feld <strong>Standardmäßige Verbindungsmethode</strong></p></figcaption></figure>

Die Anmeldeart können Sie auch beim Einladen neuer Nutzer festlegen.

## Wenn Sie sich nicht per SSO anmelden können

Prüfen Sie zuerst die [bekannten Probleme](known-problems.md). Wenn Sie weiterhin blockiert sind, wenden Sie sich umgehend an den [Support](../../../getting-started/support/request.md).
