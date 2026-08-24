---
description: >-
  Sicherheit ist ein integraler Bestandteil der Struktur unserer Cloud-Produkte,
  unserer Infrastruktur und unserer Prozesse. So haben Sie die Gewissheit, dass
  Ihre Daten geschützt sind.
---

# Sicherheit bei Dastra

Bei Dastra nehmen wir die Sicherheit sehr ernst. Hier einige Informationen, die wir zur Umsetzung von Sicherheitsmaßnahmen teilen:

## Sicheres Cloud-Hosting

Wir lagern das Hosting der Plattformdaten an Microsoft Azure aus. Wir haben diese Plattform gewählt, weil sie bei unseren Kunden weit verbreitet ist (MS 365...) und sie ein Sicherheitsniveau bietet, das [zu den höchsten auf dem Markt](https://learn.microsoft.com/de-de/azure/compliance/) gehört.

Die Datenspeicherorte befinden sich in Paris (Produktionsdaten) und Marseille (Backups) in Frankreich. Eine Datenredundanz wird im Rechenzentrum Amsterdam durchgeführt.

## **Zwei-Faktor-Authentifizierung**

Die Zwei-Faktor-Authentifizierung funktioniert unter Verwendung des TOTP-Protokolls.\
Jeder Nutzer kann die Zwei-Faktor-Authentifizierung individuell aktivieren. Es ist für alle Organisationseigentümer möglich, die Verwendung der Zwei-Faktor-Authentifizierung zu erzwingen.

[Mehr erfahren über die Zwei-Faktor-Authentifizierung](mfa.md)

## Single Sign On (SSO) und SCIM

Dastra bietet optional oder je nach gewähltem Plan ein [Self-Service-SSO](../features/settings/single-sign-on-sso/) an, das einfach und gut dokumentiert ist. Wir unterstützen die Protokolle SAML2P oder OpenID, die mit jedem Unternehmensverzeichnis kompatibel sind. Ergänzend ist es möglich, die Nutzer Ihres Verzeichnisses automatisch über unseren [SCIM](../features/settings/scim.md)-Server zu provisionieren.

## Verschlüsselung der Daten während der Übertragung

Alle Daten, die zwischen unseren Clients und Anwendungen ausgetauscht werden, sind während der Übertragung mit dem TLS-Protokoll (Transport Layer Security) mit PFS (Perfect Forward Secrecy) verschlüsselt. Die Zertifizierungsstelle für die Verschlüsselung ist CloudFlare Inc.

## Verschlüsselung der Daten im Ruhezustand

Die Datenfestplatten auf den Servern, die Kundendaten in der Azure-Cloud hosten, sind alle im Ruhezustand mit der Technologie "[Transparent Data Encryption](https://learn.microsoft.com/de-de/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16)" verschlüsselt.

Die physischen Dateien sind ebenfalls statisch im Azure Storage-Dienst mit einer transparenten 256-Bit-[AES-Verschlüsselung](https://de.wikipedia.org/wiki/Advanced_Encryption_Standard) verschlüsselt, einem der stärksten Algorithmen, der FIPS 140-2-konform ist.

Die gesamten Verschlüsselungsschlüssel werden **in einem von Dastra verwalteten Schlüsseltresor** gespeichert (einschließlich automatischer Schlüsselrotation).

## Penetrationstests (Pentests)

Wir lassen die Sicherheit der Anwendung jährlich von einem unabhängigen externen Auditor prüfen.

Der letzte Test wurde im September 2024 durchgeführt und hat keine kritischen Schwachstellen ergeben.

Unsere Sicherheitstestmethodik folgt den Empfehlungen des **OWASP** und besteht aus verschiedenen Phasen, von der Open-Source-Informationsrecherche (Reconnaissance) bis zur Ausnutzung entdeckter Schwachstellen.

## **Sicherheits-Audit-Protokolle**

Die Organisationsadministratoren können alle Änderungen an der Nutzerverwaltung, den Mandanten und den Zugriffsberechtigungen nachverfolgen.

## Eindeutige Kennungen

Jeder Nutzer besitzt eine eindeutige Kennung, und die Nutzung gemeinsamer Konten zwischen mehreren Nutzern ist nicht gestattet.

## Datensicherung

Alle Daten (Azure SQL) und Dateien (Azure Blob Storage) unserer Nutzer werden regelmäßig gesichert, mit einer Historie von 3 Monaten (Long Time Retention) und PITR (Point in Time Restore) über 7 Tage.

## Regeln zur Datenarchivierung

Bei Löschung eines Kontos werden die Daten 1 Monat vor ihrer endgültigen Löschung aufbewahrt.

## **Passwortrichtlinie**

Mindestens **10 Zeichen** mit **4 Zeichentypen** (Großbuchstaben, Kleinbuchstaben, Ziffern, Sonderzeichen)

Temporäre Kontosperre nach mehreren Fehlversuchen.

Verschlüsselung der Passwörter in der Datenbank.

## Richtlinie zur Passworterneuerung

Dastra ermöglicht es dem Kontoadministrator über [die Seite zur Sicherheitsverwaltung](https://app.dastra.eu/general-settings/security), eine Richtlinie zur Passworterneuerung für alle Ihre Nutzer festzulegen.

## **API-Token-Kontrollen**

Zeigen Sie alle [API-Schlüssel](../features/settings/gestion-des-cles-dapi.md) an und verwalten Sie diese, die von den Entwicklern Ihrer Organisation verwendet werden. Sie können deren Geltungsbereich auch auf bestimmte Mandanten oder bestimmte Berechtigungen beschränken.

## Vollständige Zugriffskontrolle

Verwendung des Zugriffsverwaltungsmodells [RBAC](https://de.wikipedia.org/wiki/Role_Based_Access_Control) (Role-Based-Access-Control). Der Organisationsverantwortliche kann die [Rollen und Berechtigungen](../features/settings/roles-et-permissions.md) jedes Nutzers äußerst flexibel festlegen.

## Sichere Authentifizierung basierend auf OpenIdConnect für alle unsere Websites

Die Authentifizierungsinstanz ist [https://account.dastra.eu](https://account.dastra.eu) und verwendet OpenID, um die Authentifizierung aller unserer Nutzer zu gewährleisten.

**OpenID** ist ein dezentrales [Authentifizierungs](https://de.wikipedia.org/wiki/Authentifizierung)-System, das [Single Sign-On](https://de.wikipedia.org/wiki/Single_Sign-on) sowie die gemeinsame Nutzung von Attributen ermöglicht. Es erlaubt einem Nutzer, sich bei mehreren Websites zu authentifizieren (die diese Technologie unterstützen müssen), ohne für jede einzelne eine Kennung merken zu müssen, sondern jedes Mal eine einzige OpenID-Kennung zu verwenden.

## **IP-Adressen-Zulassungsliste**

Es ist möglich, Nutzer bei der Anmeldung anhand ihrer IP-Adressen zu filtern

## E-Mail-Domain-Zulassungsliste

Administratoren können eine Whitelist erlaubter E-Mail-Domains definieren (z. B.: gmail.com). Für diese Einstellungen navigieren Sie zu **Konfiguration der Organisation** => **Sicherheit** => **Filtern Sie die IP-Adressen der Nutzer**

## Strikte Trennung zwischen Produktions- und Entwicklungsumgebungen

Abgesehen von einigen autorisierten Personen nutzen und greifen die Anwendungsentwickler niemals auf die Daten der Produktionsumgebung zu. Diese Trennung ist strikt und kann nicht umgangen werden.

In Test- oder Vorproduktionsumgebungen verwenden wir ausschließlich von uns erstellte Testdatensätze.

##
