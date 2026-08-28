---
description: >-
  Melden Sie sich ohne Passwort bei Dastra an – mit Passkeys auf Basis der
  Standards WebAuthn / FIDO2
---

# Passkeys

## Einführung

Ein **Passkey** ersetzt Ihr Passwort durch die Biometrie oder die PIN Ihres Geräts: Fingerabdruck, Gesichtserkennung oder Entsperrcode.

Dastra setzt auf die offenen Standards [WebAuthn](https://de.wikipedia.org/wiki/WebAuthn) und [FIDO2](https://de.wikipedia.org/wiki/FIDO-Allianz). Konkret bedeutet das:

* Der **private Schlüssel verlässt Ihr Gerät nie** (bzw. Ihren Passkey-Manager: iCloud Keychain, Google Password Manager, Windows Hello, 1Password, YubiKey…). Dastra speichert ausschließlich den öffentlichen Schlüssel.
* Es gibt **kein gemeinsames Geheimnis**, das gestohlen werden könnte: Mit einem Datenleck kann sich niemand in Ihr Konto einloggen.
* Ein Passkey ist **an die Domain von Dastra gebunden** und damit von Natur aus phishingresistent. Eine betrügerische Website kann Sie nicht dazu verleiten, ihn zu verwenden.

{% hint style="success" %}
Eine Anmeldung mit Passkey und Nutzerverifizierung (Biometrie oder PIN) gilt als **zwei Authentifizierungsfaktoren**. Sie müssen also keinen 6-stelligen Code eingeben, selbst wenn Ihre Organisation die [Zwei-Faktor-Authentifizierung](mfa.md) erzwingt.
{% endhint %}

## Wie erstelle ich einen Passkey?

Es gibt zwei Wege.

### Über Ihre Sicherheitseinstellungen

* Rufen Sie [https://app.dastra.eu/general-settings/account-security](https://app.dastra.eu/general-settings/account-security) auf
* Klicken Sie im Bereich **Passkeys** auf **Verwalten**
* Geben Sie Ihrem Passkey einen Namen (zum Beispiel „Mein Telefon“ oder „MacBook pro“) und klicken Sie auf **Passkey hinzufügen**
* Folgen Sie der Aufforderung Ihres Browsers oder Betriebssystems (Fingerabdruck, Gesicht, PIN, physischer Sicherheitsschlüssel…)

### Über die Einladung nach der Anmeldung

Nach einer Anmeldung mit Passwort schlägt Dastra Ihnen vor, einen Passkey zu erstellen, sofern Sie noch keinen haben. Sie können:

* sofort **einen Passkey erstellen**;
* **Später** wählen: Die Einladung wird in diesem Browser 90 Tage lang nicht mehr angezeigt;
* **Nicht mehr fragen** wählen: Die Einladung wird für Ihr Konto dauerhaft deaktiviert (Sie können weiterhin über Ihre Sicherheitseinstellungen einen Passkey erstellen).

## Wie melde ich mich mit einem Passkey an?

* Geben Sie Ihre E-Mail-Adresse auf der Anmeldeseite ein
* Klicken Sie im nächsten Schritt auf **Mit einem Passkey anmelden**

<figure><img src="../.gitbook/assets/security-passkey-login-button.png" alt="Schaltfläche Mit einem Passkey anmelden auf der Anmeldeseite"><figcaption><p>Die Schaltfläche „Mit einem Passkey anmelden“ erscheint, sobald für Ihr Konto ein Passkey registriert ist</p></figcaption></figure>

* Bestätigen Sie mit Fingerabdruck, Gesicht, PIN oder Sicherheitsschlüssel

{% hint style="info" %}
Die Schaltfläche erscheint nur, wenn Ihr Browser WebAuthn unterstützt **und** mindestens ein Passkey für Ihr Konto registriert ist. Ihr Passwort und die Anmeldung per E-Mail-Link bleiben verfügbar.
{% endhint %}

## Passkeys verwalten

Im Bereich **Verwalten** (Sicherheitseinstellungen Ihres Kontos) können Sie:

* **mehrere Passkeys registrieren** – das ist empfehlenswert: einer pro Gerät (Telefon, Laptop, physischer Sicherheitsschlüssel) verhindert, dass Sie den Zugang verlieren, wenn Sie ein Gerät verlieren;
* einen Passkey **umbenennen**;
* einen nicht mehr genutzten Passkey **löschen** (Gerät verkauft, verloren oder gestohlen).

Der Bereich **Passkeys** in Ihren Sicherheitseinstellungen zeigt zudem, wann jeder Passkey zuletzt verwendet wurde – so erkennen Sie veraltete Schlüssel schnell.

{% hint style="info" %}
Wenn Sie keinen Namen eingeben, wird der Passkey automatisch nach seinem Erstellungsdatum benannt. Das Hinzufügen und Löschen eines Passkeys wird in den Audit-Logs Ihrer Organisation protokolliert.
{% endhint %}

{% hint style="warning" %}
Wenn Sie Ihren letzten Passkey löschen und Ihr Konto kein Passwort besitzt, können Sie sich nur noch mit einem per E-Mail zugesandten Einmalcode anmelden. In diesem Fall wird eine Bestätigung verlangt.
{% endhint %}

## Einschränkungen

* Passkeys stehen **Nutzern nicht zur Verfügung, deren Organisation Single Sign-on (SSO) erzwingt**: Diese Nutzer authentifizieren sich bei ihrem Identitätsanbieter, der selbst Passkeys anbieten kann.
* Ein zu alter Browser oder ein zu altes Betriebssystem unterstützt WebAuthn möglicherweise nicht. In diesem Fall werden Sie durch eine Meldung informiert.
