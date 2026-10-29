---
description: "Definitionen der Begriffe, die Dastra strukturieren: Organisation, Mandant, Organisationseinheit, Entität, Abteilung und Inhaber."
---

# Wichtige Begriffe

Bevor Sie Dastra nutzen, sollten Sie sich die Zeit nehmen, die Begriffe zu verstehen, die die Plattform strukturieren. Sie helfen Ihnen, Ihre Verarbeitungstätigkeiten, Ihre Teams und Ihre Verantwortlichkeiten zu organisieren.

***

## Inhaltsverzeichnis

* [Organisation](key-concepts.md#organisation)
* [Mandant](key-concepts.md#mandant)
* [Organisationseinheit](key-concepts.md#organisationseinheit)
* [Entität](key-concepts.md#entitat)
* [Abteilung](key-concepts.md#abteilung)
* [Inhaber der Organisation](key-concepts.md#inhaber-der-organisation)

***

## Organisation

Eine **Organisation** fasst die Konten und Nutzer zusammen, die mit Ihrem Dastra-Abonnement verknüpft sind. Sie ist die Wurzelstruktur: Sie enthält alle Ihre Mandanten.

Den Namen Ihrer Organisation sehen Sie oben rechts in der Benutzeroberfläche, unter dem Namen Ihres Nutzerkontos.

{% hint style="info" %}
Eine Organisation kann mehrere Mandanten enthalten, die jeweils einem anderen Projekt, einer anderen Entität oder einem anderen Team gewidmet sind. Ein Nutzer kann mehreren Organisationen angehören.
{% endhint %}

***

## Mandant

Ein **Mandant** ist die Umgebung, in der Sie mit Ihrem Team zusammenarbeiten. Er bündelt die Module und Daten Ihrer Entitäten: Verarbeitungstätigkeiten, Audits, Risiken, Datenschutzvorfälle, Betroffenenanfragen usw. Die Daten eines Mandanten sind aus einem anderen Mandanten nie zugänglich.

Sie wählen Ihren Mandanten bei der Anmeldung, indem Sie in der Liste Ihrer Mandanten auf seine Kachel klicken.

Geben Sie Ihren Mandanten aussagekräftige Namen (zum Beispiel "Compliance Konzern" oder "Entitäten Deutschland"). Das erleichtert die Navigation, wenn die Organisation mehrere Mandanten hat.

***

## Organisationseinheit

**Organisationseinheiten** strukturieren einen Mandanten entsprechend Ihrer internen Organisation. Es gibt zwei Arten: Entitäten und Abteilungen.

Sie ordnen Verarbeitungstätigkeiten, Aufgaben, Betroffenenanfragen, Datenschutzvorfälle und Risiken einer Organisationseinheit zu. Außerdem können Sie ihr Zugriffsrechte für Nutzer oder Teams zuordnen.

{% hint style="info" %}
Organisationseinheiten sind die Referenz für Berichte und für Zugriffsberechtigungen. Siehe [Organisationseinheiten erstellen und konfigurieren](organizational-units.md).
{% endhint %}

***

## Entität

Eine **Entität** entspricht einer juristischen Person, also einem **Verantwortlichen**: einem Unternehmen, einer Tochtergesellschaft, einem Verein. Auf dieser Ebene ordnen Sie Verarbeitungstätigkeiten und die wichtigsten rechtlichen Informationen zu.

Eine Entität enthält:

* die Kontaktdaten des Verantwortlichen,
* den **DSB** (Datenschutzbeauftragten),
* die **federführende Aufsichtsbehörde**,
* die ihr zugeordneten Abteilungen und untergeordneten Entitäten.

Beispiel:

> Entität: _Dastra Deutschland GmbH_\
> Abteilung: _Marketing_\
> DSB: _Max Mustermann_

***

## Abteilung

Eine **Abteilung** repräsentiert einen Bereich einer Entität (zum Beispiel Personal, IT, Marketing, Recht). Sie verfeinert die Verteilung der Tätigkeiten innerhalb einer Entität.

Abteilungen dienen dazu:

* Verarbeitungstätigkeiten oder Audits nach Bereich zu filtern,
* Aufgaben oder Anfragen einer gezielten Gruppe zuzuweisen,
* einem Team Zugriffsrechte auf einen genau abgegrenzten Bereich zu geben.

Eine Abteilung kann untergeordnete Abteilungen haben. Eine Entität kann ebenfalls untergeordnete Entitäten haben, zum Beispiel um die Tochtergesellschaften eines Konzerns abzubilden.

{% hint style="info" %}
Abteilungen sind optional. Sie sind nützlich, sobald die Organisation mehrere Bereiche hat, deren Verarbeitungstätigkeiten Sie getrennt verfolgen möchten.
{% endhint %}

***

## Inhaber der Organisation

Der **Inhaber** ist der Hauptadministrator der Organisation. Nur Inhaber können Mandanten erstellen, die Einstellungen der Organisation ändern, angepasste Rollen erstellen und andere Inhaber hinzufügen oder entfernen.

Beschränken Sie die Anzahl der Inhaber, damit die Governance klar bleibt. Andere Nutzer erhalten Rollen, die zu ihren Anforderungen passen: siehe [Rollen und Berechtigungen verwalten](roles.md).
