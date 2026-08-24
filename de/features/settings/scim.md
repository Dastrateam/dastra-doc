---
description: >-
  Diese Seite erklärt, wie Sie die SCIM-Konfiguration von Dastra mit einem
  Unternehmensverzeichnis vom Typ Azure Active Directory (Cloud) einrichten
---

# SCIM

### Funktionsprinzip

[SCIM](http://www.simplecloud.info/), die englische Abkürzung für System for Cross-domain Identity Management (übersetzt: „System für domänenübergreifendes Identitätsmanagement"), ist ein offener Standard, der die Automatisierung der Nutzerbereitstellung unterstützt. Das SCIM-Protokoll ist ein Vermittler: Es sammelt Identitätsdaten der Nutzer bei den Identitätsanbietern (Azure AD, Google Workspace, Okta...) und übermittelt sie an die Dienstanbieter, die diese Identifikationsinformationen benötigen (wie Dastra).

{% hint style="warning" %}
Die SCIM-Funktionalität ist Kunden mit einem **Enterprise-Plan** vorbehalten.

[Konsultieren Sie unsere Preisseite](https://www.dastra.eu/pricing)
{% endhint %}

{% hint style="info" %}
Wir empfehlen Ihnen dringend, vorab [die SSO-Einrichtung](single-sign-on-sso/) **mit aktivierter Option „Für alle Nutzer erzwingen"** durchzuführen.&#x20;
{% endhint %}

### Wie konfiguriere ich SCIM mit Azure Active Directory?

Die Nutzer von Dastra können über SCIM 2.0 hinzugefügt, gelöscht und geändert werden.&#x20;

Sie definieren Gruppen in Ihrem Azure Directory und Dastra kann diese Nutzer synchronisieren. Dies ist ein idealer Weg, um Zeit zu sparen und den Aufwand der Nutzerkontenverwaltung zu vermeiden. Es handelt sich auch um eine ideale Sicherheitsimplementierung.

#### 1. Melden Sie sich bei Azure an und klicken Sie auf Azure Active Directory

<figure><img src="https://www.reftab.com/img/faq/01-azure.png" alt="01-Azure-SCIM"><figcaption></figcaption></figure>

#### 2. Gehen Sie zu „Entreprise applications"

<figure><img src="https://www.reftab.com/img/faq/02-azure.png" alt="01-Azure-SCIM"><figcaption></figcaption></figure>

#### 3. Klicken Sie auf „New application"

<figure><img src="https://www.reftab.com/img/faq/03-azure.png" alt="03-Azure-SCIM"><figcaption></figcaption></figure>

#### 4. Klicken Sie auf „Create your own application"

<figure><img src="https://www.reftab.com/img/faq/04-azure.png" alt="04-Azure-SCIM"><figcaption></figcaption></figure>

#### 5. Benennen Sie Ihre Anwendung

<figure><img src="../../.gitbook/assets/image-19-1.png" alt=""><figcaption></figcaption></figure>

#### 6. Klicken Sie in der neu erstellten Anwendung auf die Schaltfläche „Provision User Accounts"

<figure><img src="https://www.reftab.com/img/faq/06-azure.png" alt="06-Azure-SCIM"><figcaption></figcaption></figure>

#### 7. Klicken Sie auf „Get Started"

<figure><img src="https://www.reftab.com/img/faq/07-azure.png" alt="07-Azure-SCIM"><figcaption></figcaption></figure>

#### 8. Setzen Sie den Bereitstellungsmodus auf automatisch. Füllen Sie die Mandanten-URL und das Geheimnis-Token mit den Informationen aus Ihrem Dastra-Konto aus.

**Melden Sie sich bei Dastra** als Administrator an. **Gehen Sie zur Organisationskonfiguration** > **klicken Sie auf Sicherheit / SCIM**

![](<../../.gitbook/assets/image-14-1.png>)

Klicken Sie auf die Schaltfläche **Konfigurieren**

<figure><img src="../../.gitbook/assets/image-18-2.png" alt=""><figcaption></figcaption></figure>

Konfigurieren Sie Ihr SCIM. Wählen Sie den Mandanten aus, den Sie synchronisieren möchten (die Teams und Nutzer werden automatisch in diesem Mandanten bereitgestellt).

Wählen Sie dann die Standardrolle, die Sie neuen Nutzern zuweisen möchten. Beachten Sie, dass die Rollen lokal vom Dastra-Kontoadministrator verwaltet werden.

Klicken Sie auf **Speichern**

**Kopieren Sie das Authentifizierungs-Token und die SCIM-URL**

{% hint style="info" %}
Derzeit ermöglicht Dastra die SCIM-Synchronisation (Teams + Nutzer) von **nur einem Mandanten pro Organisation**.&#x20;
{% endhint %}

<figure><img src="../../.gitbook/assets/image-12-2.png" alt=""><figcaption></figcaption></figure>

Klicken Sie auf „**Verbindung testen**" und „**Speichern**". Wenn beim Verbindungstest ein Fehler auftritt, kann dies an einer nicht aktivierten Funktion in Ihrem Abonnement liegen. [Kontaktieren Sie dann den Support](../../getting-started/le-support/faire-une-demande-de-support.md)

#### 9. Aktivieren Sie die Bereitstellung der Anwendung

<figure><img src="../../.gitbook/assets/image-10-2.png" alt=""><figcaption></figcaption></figure>

#### 10. Fügen Sie Nutzer und/oder Gruppen zur erstellten Anwendung hinzu&#x20;

<figure><img src="../../.gitbook/assets/image-9-3.png" alt=""><figcaption></figcaption></figure>

### Lassen Sie Ihre Nutzer sich verbinden

Sie sollten sehen, dass sich die Nutzerkonten Ihres AD automatisch in Dastra synchronisieren. Wenn sie sich über [die Anmeldeseite](https://app.dastra.eu/login) bei Dastra anmelden, sollten sie sich mit ihrer E-Mail verbinden können. Wenn das SSO nicht konfiguriert und für alle Nutzer erzwungen ist, müssen die Nutzer ein Passwort-Reset durchführen, um sich anzumelden. Wenn das SSO aktiv ist und für alle Nutzer erzwungen wird, werden diese automatisch zum Anmeldeformular Ihres Identitätsanbieters (Azure AD, Google Workspace, Okta...) weitergeleitet.

### Verhaltensweisen und Einschränkungen der SCIM-Synchronisation

#### Verwaltung des Nutzer-Lebenszyklus

**Deaktivierung in Entra ID**

Wenn ein Nutzer in Entra ID deaktiviert wird:

* Sein Profil wird **in Dastra anonymisiert**
* Wenn er anschließend reaktiviert wird:
  * **Ein neues Nutzerkonto wird erstellt**
  * Das alte anonymisierte Konto wird nicht wiederhergestellt

***

**Vollständige Löschung in Entra ID**

Wenn ein Nutzer in Entra ID endgültig gelöscht wird:

* Sein Profil wird **vollständig in Dastra anonymisiert**
* Alle durchgeführten Aktionen werden **beibehalten**
* Der Nutzer erscheint als **„deleted user"**

**Auswirkung auf verknüpfte Daten:**

* Verknüpfte Objekte (z. B.: Verarbeitungen, Risiken, Anfragen usw.) **werden nicht gelöscht**
* Beziehungen (z. B.: Inhaber, Zuweisung) **bleiben erhalten**
* Nur die Identität des Nutzers wird anonymisiert

***

#### Verwaltung von Gruppen (Teams)

**Löschung einer Gruppe in Entra ID**

Wenn eine Gruppe in Entra ID gelöscht wird:

* Das **entsprechende Team wird in Dastra gelöscht**
* Die **Nutzer werden nicht gelöscht**
* Keine Auswirkung auf ihre individuellen Konten

***

#### Mapping und Synchronisationsumfang

**Gruppen und Workspaces**

* SCIM ermöglicht die Synchronisation **mehrerer Gruppen**
* Aktuelle Einschränkung:
  * Synchronisation möglich zu **nur einem Workspace pro Organisation**
  * Multi-Workspace wird **nicht unterstützt**

***

**Synchronisierte Attribute**

Derzeit synchronisiert Dastra:

* Den **Gruppennamen (`displayName`)**

Derzeit nicht unterstützt:

* Mapping auf **Organisationseinheiten**
* Synchronisation von Attributen wie:
  * Organisation
  * Land

> Eine Weiterentwicklung ist durch Hinzufügen eines spezifischen Attributs möglich, das eine auf Dastra-Seite verwertbare Kennung enthält.

***

#### Lokale Verwaltung nach Synchronisation

Nach der SCIM-Synchronisation:

* Administratoren können weiterhin:
  * **Rollen ändern**
  * **Berechtigungen anpassen**
* Die feingrakulare Zugriffsverwaltung bleibt **lokal in Dastra möglich**

***

#### Auswirkung auf die Lizenz

* Die SCIM-Synchronisation ist begrenzt durch:
  * die **Anzahl der in Ihrem Abonnement enthaltenen Nutzer**
* Bei Überschreitung des Kontingents:
  * gibt der SCIM-Server einen **Fehler** zurück
  * Zusätzliche Nutzer werden **nicht bereitgestellt**
