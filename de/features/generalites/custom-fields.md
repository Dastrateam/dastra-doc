---
description: Dastra bietet Ihnen die Möglichkeit, Ihre Formulare unbegrenzt anzupassen
---

# Benutzerdefinierte Felder

So verwenden Sie benutzerdefinierte Felder in Dastra

## Wann sollten benutzerdefinierte Felder verwendet werden?

Es kann vorkommen, dass bestimmte branchenspezifische Informationen nicht in den nativen Feldern des Verarbeitungsverzeichnisses, der Betroffenenanfragen, der Aufgaben usw. vorhanden sind.

Dastra ermöglicht es Ihnen, benutzerdefinierte Formularfelder zu erstellen, die Sie ganz einfach hinzufügen können, um die erfassten Daten zu erweitern.

Hier ein Beispiel für die Konfiguration von Feldern für den Stakeholder:

<figure><img src="../../.gitbook/assets/image-2-1-3-1-1.png" alt=""><figcaption><p>Feldkonfiguration</p></figcaption></figure>

Und hier das Ergebnis im Formular:

<figure><img src="../../.gitbook/assets/image-4-1-3.png" alt=""><figcaption></figcaption></figure>

## Betroffene Funktionen

{% hint style="success" %}
Achtung! Nicht alle Funktionen unterstützen benutzerdefinierte Felder.
{% endhint %}

Sie können die folgenden Formulare anpassen:

* [Verarbeitungsblätter](../editer-le-registre/)
* [Betroffenenanfragen](../gerer-les-exercices-des-droits/)
* [Aufgaben](../planifier/gerer-vos-taches.md)
* [Assets](../editer-le-registre/remplir-le-questionnaire/applications.md)
* [Stakeholder](../cartography/referentials/)
* [Maßnahmen](../editer-le-registre/remplir-le-questionnaire/mesures-de-securite.md)
* [Datensätze](../editer-le-registre/remplir-le-questionnaire/categorie-de-donnees.md)
* Datenfelder
* [Datenschutzvorfälle](../../rappels-utiles/rgpd-en-bref/violations-de-donnees.md)
* [Risikobewertungen](../la-gestion-des-risques/risques.md)
* [KI-Systeme](../systemes-dia/)
* [Verträge](../contrats/)
* [Kontrollpunkte](../compliance/library/risks.md#association-des-controles)

{% hint style="danger" %}
#### Begrenzung der Feldanzahl

Die Anzahl der benutzerdefinierten Felder ist je nach verwendetem Plan begrenzt. Bitte konsultieren Sie [die Preisseite der Anwendung](https://www.dastra.eu/de/pricing) für weitere Informationen zu diesem Thema.
{% endhint %}

## Verfügbare Feldtypen

Dastra bietet Ihnen verschiedene Arten von benutzerdefinierten Feldern:

* Einfacher Text
* Langer Text
* Formatierter Text
* Ganzzahl
* Dezimalzahl
* Datum
* Datum und Uhrzeit
* Kontrollkästchen (Mehrfachauswahl) (**nicht filterbar**)
* Kontrollkästchen (Einfachauswahl)
* Einfacher Selektor
* Mehrfach-Selektor (**nicht filterbar**)
* Kontrollkästchen (Ja/Nein)

## Verwendung benutzerdefinierter Felder

Sie können:

* Daten benutzerdefinierter Felder in den Formularen jedes Moduls anzeigen und bearbeiten
* Benutzerdefinierte Felder können in allen Anzeigetabellen der Anwendung dargestellt werden. Um sie anzuzeigen, klicken Sie auf die Schaltfläche zur Spalteneinstellung der Tabelle.
* Benutzerdefinierte Felder sind **in allen Excel-Datenexporten enthalten**. Weitere Informationen zu Exporten finden Sie auf der [Seite zu Exporten](../editer-le-registre/exporter-importer-le-registre.md).
* Benutzerdefinierte Felder können optional in HTML-, Word- und PDF-Exporten enthalten sein (indem Sie das Kontrollkästchen "In Berichten exportierbar" beim betreffenden Feld aktivieren)
* **Mit Ausnahme der Mehrfachantwort-Felder** sind alle benutzerdefinierten Felder über das System der [erweiterten Filter](advanced-filters.md) filterbar.
* Benutzerdefinierte Felder können in den Datentabellen massenhaft aktualisiert werden
* Benutzerdefinierte Felder können über Flat-Files [mit dem Importsystem](importer-vos-donnees-excel-csv.md) importiert werden
* Benutzerdefinierte Felder sind **über alle APIs zugänglich und bearbeitbar**. Dazu müssen Sie den Variablennamen verwenden, der jeder Spalte zugewiesen ist. [Konsultieren Sie den Abschnitt zur Bearbeitung benutzerdefinierter Felder über die API](custom-fields.md#manipuler-les-champs-personnalises-dans-les-api).

## Einrichtung benutzerdefinierter Felder

* Gehen Sie zu Ihrem **Mandanten**
* Klicken Sie im linken Menü auf **Einstellungen des Mandanten**
* Klicken Sie auf das Menü **Benutzerdefinierte Felder**
* Wählen Sie das Modul, in dem Sie ein benutzerdefiniertes Feld hinzufügen möchten
* Die Felder müssen in Gruppen erstellt werden. Diese Gruppen können an einer bestimmten Position im Formular platziert werden. Klicken Sie auf "**Feldgruppe hinzufügen**"

<figure><img src="../../.gitbook/assets/image-3-1-3-1.png" alt=""><figcaption></figcaption></figure>

* **Geben Sie den Namen und die Position** im Formular ein, die Sie wünschen

<figure><img src="../../.gitbook/assets/image-1-1-1-2-2.png" alt=""><figcaption></figcaption></figure>

Für bestimmte Elemente ist es möglich, die gewünschte Position im Formular festzulegen!

* Sobald die Gruppe erstellt ist, können Sie nun **die gewünschten Feldtypen per Drag-and-Drop** einrichten!

<figure><img src="../../.gitbook/assets/image-1-1-1-2-3.png" alt=""><figcaption></figcaption></figure>

Füllen Sie alle Informationen aus!

* Klicken Sie auf Speichern und fertig! Ihr erstes benutzerdefiniertes Datenfeld ist eingerichtet!
* Sie können die Felder per Drag-and-Drop nach Belieben neu anordnen.

## Benutzerdefinierte Felder in den APIs verwenden

Dastra ermöglicht es Ihnen, über die [REST-API](../../api-references/configuration-api.md) alle Werte der Entitäten mit benutzerdefinierten Feldern abzurufen, zu ändern und zu erstellen.

Eine Eigenschaft "**customFields**" ist in allen Entitäten verfügbar, die Sie per GET in Dastra abrufen.

```json
 {
   "id": 1234,
   "label": "Test asset",
   etc...
   "customFields": {
     "dpo_name":"jean-marc le dpo",
     "dpo_email":"dpo@github.com",
     "dpo_habilitations": ["Expert","Consulting","Data Mapping"],
     "has_large_dataset":false,
     etc...
   }
 }
```

Um diese Eigenschaft zu ändern, genügt es, das Element per POST oder PUT zu senden und die Elemente der Sammlung zu aktualisieren.

Um die Namen der benutzerdefinierten Variablen zu erfassen, müssen Sie die Konfigurationsseite der benutzerdefinierten Felder aufrufen.

{% hint style="info" %}
Achtung, alle **benutzerdefinierten Felder werden vom Server validiert**. Wenn eine Spalte nicht in der Konfiguration vorhanden ist, wird sie automatisch gelöscht.

Wenn ein Feld ungültig ist (z. B. wenn es nicht ausgefüllt ist, obwohl es als Pflichtfeld markiert ist), wird eine Ausnahme mit dem Code 400 ausgelöst.
{% endhint %}

## Einschränkungen

Sie können **Mehrfach-Felder (Kontrollkästchen (Mehrfach) und Selektor (Mehrfach)) nicht filtern**. Dies ist eine bekannte Einschränkung, an der wir arbeiten.
