---
description: >-
  Sicherheit ist ein integraler Bestandteil der Struktur unserer Cloud-Produkte,
  unserer Infrastruktur und unserer Prozesse. So haben Sie die Gewissheit, dass
  Ihre Daten geschützt sind.
---

# Sicherheit bei Dastra

Bei Dastra nehmen wir die Sicherheit sehr ernst. Hier einige Informationen, die wir zur Umsetzung von Sicherheitsmaßnahmen teilen:

{% hint style="info" %}
Die Sicherheitseinstellungen der Organisation (verpflichtende starke Authentifizierung, IP-Adressfilterung, Filterung der E-Mail-Domains, Richtlinie zur Passwortaktualisierung, automatische Abmeldung, Aufbewahrung von Sicherheitsprotokollen, SIEM-Streaming) sind den Organisationseigentümern und dem Enterprise-Plan vorbehalten. Sie befinden sich unter **Konfiguration der Organisation** > **Sicherheit**.
{% endhint %}

## Sicheres Cloud-Hosting

Wir lagern das Hosting der Plattformdaten an Microsoft Azure aus. Wir haben diese Plattform gewählt, weil sie bei unseren Kunden weit verbreitet ist (MS 365...) und sie ein Sicherheitsniveau bietet, das [zu den höchsten auf dem Markt](https://learn.microsoft.com/de-de/azure/compliance/) gehört.

Die Datenspeicherorte befinden sich in Paris (Produktionsdaten) und Marseille (Backups) in Frankreich. Eine Datenredundanz wird im Rechenzentrum Amsterdam durchgeführt.

Für eine dedizierte Instanz in einer souveränen Cloud siehe [Dastra auf Bleu (souveräne Cloud)](bleu.md).

## **Zwei-Faktor-Authentifizierung**

Die Zwei-Faktor-Authentifizierung funktioniert unter Verwendung des TOTP-Protokolls.\
Jeder Nutzer kann die Zwei-Faktor-Authentifizierung individuell aktivieren. Organisationseigentümer können sie außerdem für alle internen Nutzer, die von der Organisation verwaltet werden, verpflichtend machen.

Siehe [Zwei-Faktor-Authentifizierung](mfa.md).

## Single Sign On (SSO) und SCIM

Dastra bietet optional oder je nach gewähltem Plan ein [Self-Service-SSO](../features/settings/sso/README.md) an, das einfach und gut dokumentiert ist. Wir unterstützen die Protokolle SAML2P oder OpenID, die mit jedem Unternehmensverzeichnis kompatibel sind. Ergänzend ist es möglich, die Nutzer Ihres Verzeichnisses automatisch über unseren [SCIM](../features/settings/scim.md)-Server zu provisionieren.

## Verschlüsselung der Daten während der Übertragung

Alle Daten, die zwischen unseren Clients und Anwendungen ausgetauscht werden, sind während der Übertragung mit dem TLS-Protokoll (Transport Layer Security) mit PFS (Perfect Forward Secrecy) verschlüsselt. Die Zertifizierungsstelle für die Verschlüsselung ist CloudFlare Inc.

## Verschlüsselung der Daten im Ruhezustand

Die Datenfestplatten auf den Servern, die Kundendaten in der Azure-Cloud hosten, sind alle im Ruhezustand mit der Technologie "[Transparent Data Encryption](https://learn.microsoft.com/de-de/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16)" verschlüsselt.

Die physischen Dateien sind ebenfalls statisch im Azure Storage-Dienst mit einer transparenten 256-Bit-[AES-Verschlüsselung](https://de.wikipedia.org/wiki/Advanced_Encryption_Standard) verschlüsselt, einem der stärksten Algorithmen, der FIPS 140-2-konform ist.

Die gesamten Verschlüsselungsschlüssel werden **in einem von Dastra verwalteten Schlüsseltresor** gespeichert (einschließlich automatischer Schlüsselrotation).

## Penetrationstests (Pentests)

Wir lassen die Sicherheit der Anwendung jährlich von einem unabhängigen externen Auditor prüfen.

Der letzte Test hat keine kritischen Schwachstellen ergeben.

Unsere Sicherheitstestmethodik folgt den Empfehlungen des **OWASP** und besteht aus verschiedenen Phasen, von der Open-Source-Informationsrecherche (Reconnaissance) bis zur Ausnutzung entdeckter Schwachstellen.

## **Sicherheits-Audit-Protokolle**

Die Organisationsadministratoren können alle Änderungen an der Nutzerverwaltung, den Mandanten und den Zugriffsberechtigungen nachverfolgen.

Organisationseigentümer legen unter **Konfiguration der Organisation** > **Sicherheit** in der Karte **Aufbewahrung von Sicherheitsprotokollen** fest, wie lange die Sicherheitsprotokolle aufbewahrt werden: von 30 Tagen bis zu 3 Jahren (empfohlen: 180 Tage). Ältere Protokolle werden jede Nacht bereinigt.

Um diese Ereignisse fortlaufend an Ihr Überwachungstool zu übertragen, siehe [SIEM-Streaming](../features/settings/siem.md).

## Eindeutige Kennungen

Jeder Nutzer besitzt eine eindeutige Kennung, und die Nutzung gemeinsamer Konten zwischen mehreren Nutzern ist nicht gestattet.

## Datensicherung

Alle Daten (Azure SQL) und Dateien (Azure Blob Storage) unserer Nutzer werden regelmäßig gesichert, mit einer Historie von 3 Monaten (Long Time Retention) und PITR (Point in Time Restore) über 7 Tage.

## Regeln zur Datenarchivierung

Bei Löschung eines Kontos werden die Daten 1 Monat vor ihrer endgültigen Löschung aufbewahrt.

## **Passwortrichtlinie**

Mindestens **10 Zeichen** mit **4 Zeichentypen** (Großbuchstaben, Kleinbuchstaben, Ziffern, Sonderzeichen)

Verzögerung beim Zugriff auf das Konto nach mehreren fehlgeschlagenen Anmeldeversuchen.

Verschlüsselung der Passwörter in der Datenbank.

## Richtlinie zur Passworterneuerung

Organisationseigentümer können unter [Konfiguration der Organisation > Sicherheit](https://app.dastra.eu/general-settings/security) in der Karte **Richtlinie zur Passwortaktualisierung** eine Gültigkeitsdauer für Passwörter festlegen. Sie gilt für die internen Nutzer der Organisation, die kein SSO verwenden. Nach Ablauf der Frist erstellt der Nutzer bei der nächsten Anmeldung ein neues Passwort.

## Automatische Abmeldung

Organisationseigentümer können die Karte **Automatische Abmeldung** aktivieren: Alle internen Nutzer, die von der Organisation verwaltet werden, werden dann nach 1 Stunde Inaktivität abgemeldet.

## **API-Token-Kontrollen**

Zeigen Sie alle [API-Schlüssel](../features/settings/api-keys.md) an und verwalten Sie diese, die von den Entwicklern Ihrer Organisation verwendet werden. Sie können deren Geltungsbereich auch auf bestimmte Mandanten oder bestimmte Berechtigungen beschränken.

## Vollständige Zugriffskontrolle

Verwendung des Zugriffsverwaltungsmodells [RBAC](https://de.wikipedia.org/wiki/Role_Based_Access_Control) (Role-Based-Access-Control). Der Organisationsverantwortliche kann die [Rollen und Berechtigungen](../features/settings/roles.md) jedes Nutzers äußerst flexibel festlegen.

## Sichere Authentifizierung basierend auf OpenIdConnect für alle unsere Websites

Die Authentifizierungsinstanz ist [https://account.dastra.eu](https://account.dastra.eu) und verwendet OpenID, um die Authentifizierung aller unserer Nutzer zu gewährleisten.

**OpenID** ist ein dezentrales [Authentifizierungs](https://de.wikipedia.org/wiki/Authentifizierung)-System, das [Single Sign-On](https://de.wikipedia.org/wiki/Single_Sign-on) sowie die gemeinsame Nutzung von Attributen ermöglicht. Es erlaubt einem Nutzer, sich bei mehreren Websites zu authentifizieren (die diese Technologie unterstützen müssen), ohne für jede einzelne eine Kennung merken zu müssen, sondern jedes Mal eine einzige OpenID-Kennung zu verwenden.

## **IP-Adressen-Zulassungsliste**

Der Zugriff auf die Organisation kann auf zugelassene IP-Adressbereiche beschränkt werden. Die Filterung gilt für alle Nutzer (einschließlich Administratoren) und alle Anmeldemethoden (Passwort, SSO, Passkey, Magic Link), bei der Anmeldung und bei jeder Token-Erneuerung. Sie gilt nicht für APIs, SCIM oder SIEM-Streaming. Details finden Sie auf der Seite [IP-Filterung](../features/settings/ip-filtering.md).

## E-Mail-Domain-Zulassungsliste

Organisationseigentümer können die Liste der erlaubten E-Mail-Domains festlegen (z. B. `example.com`): Nur Nutzer, deren E-Mail-Adresse zu einer dieser Domains gehört, können sich anmelden. Navigieren Sie dazu zu **Konfiguration der Organisation** > **Sicherheit**, Karte **Filtern Sie die E-Mail-Domains Ihrer Nutzer**. Die Einrichtung kann einige Minuten in Anspruch nehmen.

## Strikte Trennung zwischen Produktions- und Entwicklungsumgebungen

Abgesehen von einigen autorisierten Personen nutzen und greifen die Anwendungsentwickler niemals auf die Daten der Produktionsumgebung zu. Diese Trennung ist strikt und kann nicht umgangen werden.

In Test- oder Vorproduktionsumgebungen verwenden wir ausschließlich von uns erstellte Testdatensätze.
