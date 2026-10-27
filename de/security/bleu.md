---
description: >-
  Dastra ist auch auf Bleu verfügbar: eine dedizierte, von unserer
  Standard-SaaS-Plattform isolierte Instanz, deren Daten den Bleu-Perimeter
  nicht verlassen.
---

# Dastra auf Bleu (souveräne Cloud)

Manche Organisationen dürfen ihre Compliance-Daten nicht auf einer Infrastruktur hosten, die nicht-europäischen extraterritorialen Gesetzen unterliegt. Deshalb ist Dastra auch auf **Bleu** verfügbar: eine dedizierte Instanz, getrennt von unserer Standard-SaaS-Plattform, deren Daten den Bleu-Perimeter nicht verlassen.

## Was ist Bleu?

Bleu ist ein französisches Unternehmen im Besitz von **Capgemini und Orange**, das Microsoft Azure und Microsoft 365 in einer von der weltweiten Microsoft-Infrastruktur isolierten Umgebung bereitstellt. Die Dienste werden in Rechenzentren in Frankreich (Île-de-France und Südfrankreich) gehostet und ausschließlich von französischen Teams betrieben. Das Angebot richtet sich an den Staat, Gebietskörperschaften, Gesundheitseinrichtungen, Betreiber kritischer Infrastrukturen (OIV) und Betreiber wesentlicher Dienste (OSE) und bietet rechtlichen Schutz vor extraterritorialen Zugriffsgesetzen (Cloud Act, FISA).

## SecNumCloud-Qualifizierung: aktueller Stand

Die Qualifizierung **SecNumCloud 3.2** wird von der ANSSI nach vier Meilensteinen erteilt. Für den Bereich IaaS, PaaS und CaaS hat Bleu **J0** (April 2025, Antrag angenommen) und **J1** (September 2025, Bewertungsstrategie angenommen) erreicht. Die Vor-Ort-Bewertung (**J2**) läuft; die Qualifizierungsentscheidung (**J3**) steht noch aus.

{% hint style="warning" %}
Wir stellen Dastra auf Bleu daher nicht als „SecNumCloud-qualifiziertes“ Angebot dar, solange die ANSSI ihre Entscheidung nicht veröffentlicht hat.
{% endhint %}

## Was sich gegenüber dem Standardangebot ändert

| | Standardangebot | Bleu-Angebot |
| --- | --- | --- |
| Anwendung | `app.dastra.eu` | `app-bleu.dastra.eu` |
| API | `api.dastra.eu` | `api-bleu.dastra.eu` |
| Authentifizierung | `account.dastra.eu` | `account-bleu.dastra.eu` — eigenes Nutzerverzeichnis, eigene Konten und Signaturschlüssel |
| SCIM-Provisionierung | `scim.dastra.eu` | `scim-bleu.dastra.eu` |
| Hosting | Microsoft Azure France (Paris, Marseille) | Bleu France Central (Île-de-France) |
| KI-Funktionen | Verfügbar | Verfügbar, ausgeführt von **Mistral AI** (französisches Unternehmen, außerhalb des Bleu-Perimeters) statt von Azure OpenAI |
| Volltextsuche | Verfügbar | Verfügbar, Index auf Bleu gehostet |
| Konnektoren (Jira, ServiceNow, LeanIX, DocuSign, Zapier…) und API-Schlüssel | Verfügbar | Verfügbar |
| SSO (SAML, OpenID Connect) | Verfügbar | Verfügbar |
| Redaktionelle Inhalte in der Anwendung (News, Webinare) | Von der Standardplattform ausgeliefert | Ebenso, schreibgeschützt, ohne jegliche Kundendaten |
| Update-Rhythmus | Kontinuierlich | Dieselben Versionen, nach der Standardplattform ausgerollt |

## Datenspeicherort und Sicherungen

Alle Produktionsressourcen (Datenbanken, Dateien, Audit-Protokolle, Suchindex, Cache, Secret-Tresor, Monitoring) werden in der Region **Bleu France Central** gehostet. Sie werden nicht außerhalb von Bleu repliziert.

Die einzigen ausgehenden Datenflüsse sind Aufrufe der Drittanbieterdienste, die das Standardangebot bereits nutzt: Mistral AI für die KI-Funktionen (Daten werden bedarfsweise verarbeitet) und Brevo (französisches Unternehmen) für den E-Mail-Versand.

## Verschlüsselung, Authentifizierung und Secrets

Sofern unten nicht anders angegeben, gelten für die Bleu-Instanz die auf der Seite [Sicherheit bei Dastra](general.md) beschriebenen Maßnahmen.

* **TLS**: Der öffentliche Datenverkehr wird vom europäischen CDN bunny.net terminiert, das die Zertifikate verwaltet; auf allen Ressourcen (Anwendungen, Datenbanken, Speicher) wird mindestens TLS 1.2 erzwungen.
* **Secrets**: Azure Key Vault auf Bleu gehostet, zugänglich ausschließlich für die verwalteten Identitäten der Anwendungen; keine Secrets in der Anwendungskonfiguration.
* **Authentifizierung**: dedizierter Identity-Server. Ein Konto der Standardplattform kann sich nicht auf Bleu anmelden und umgekehrt; zwischen beiden besteht keine Föderation. Die Anmeldeseite bietet eine Regionsauswahl, um Nutzer zu leiten.

## Isolierung und Umgebungen

Die Bleu-Instanz ist **strikt isoliert** von der Standardplattform: Datenbanken, Speicher, Protokolle, Cache, Suchindex, Secret-Tresor und Identitäten sind getrennt. Der einzige Datenfluss zwischen beiden Plattformen ist die schreibgeschützte Synchronisierung unserer Referenzbibliotheken (Vorlagen, Referenzrahmen) nach Bleu; Kundendaten werden dabei nicht übertragen.
