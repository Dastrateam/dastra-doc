---
description: >-
  Erfahren Sie, wie Sie eine Fragebogenvorlage in Dastra erstellen und
  bearbeiten.
---

# Eine Fragebogenvorlage erstellen

## Einführung

Das Erstellen oder Bearbeiten einer Fragebogenvorlage in Dastra ist kinderleicht. Navigieren Sie dazu zur Funktion "**Fragebögen**".

## Eine Fragebogenvorlage erstellen oder bearbeiten

Um eine Fragebogenvorlage zu erstellen, klicken Sie auf die Schaltfläche "**Vorlage erstellen**" in der Registerkarte "**Fragebögen**". Anschließend können Sie einen der in Dastra verfügbaren Vorlagentypen auswählen: automatisierter Fragebogen, benutzerdefinierter Fragebogen oder aus einer Datei importiert.

<figure><img src="../../../.gitbook/assets/Vorlage erstellen.png" alt=""><figcaption></figcaption></figure>

Sie gelangen zur Auswahlansicht der Vorlagentypen:

![Auswahl der Vorlagentypen](<../../../.gitbook/assets/Vorlage erstellen1.png>)

* Durch Klicken auf die Registerkarte "**Basierend auf einer Vorlage**" wählen Sie eine vordefinierte Fragebogenvorlage aus der Dastra-Bibliothek aus.
* Durch Klicken auf "**Von Grund auf neu**" können Sie Ihre eigene Fragebogenvorlage erstellen.

{% hint style="info" %}
Im Gegensatz zu Fragebögen n welche auf einer Vorlage basieren, sind benutzerdefinierte Fragebögen vollständig anpassbar. Abhängig von den Antworten der Befragten können Sie automatisch einen Maßnahmenplan generieren oder die mit der Vorlage verbundenen Risiken kartieren.
{% endhint %}

## Automatisierte Fragebogenvorlagen

Dastra bietet zahlreiche automatisierte Fragebogenvorlagen zur Dokumentation der Compliance und zur Steuerung von Prozessen. Diese Vorlagen umfassen unter anderem DSFA/PIA, TIA, LIA, Fragebögen für Auftragsverarbeiter und vieles mehr.

![Schaltfläche zur Bibliotheksauswahl](<../../../.gitbook/assets/Vorlage erstellen2.png>)

Sobald die Vorlage ausgewählt ist, gelangen Sie zum Planungsbildschirm, auf dem Sie:

* entweder **die Vorlage bearbeiten** können, indem Sie auf die Schaltfläche "**Vorlage bearbeiten**" klicken
* oder einen Fragebogen planen können, indem Sie auf die Schaltfläche "**Fragebogen planen**" klicken

{% hint style="info" %}
Bestimmte Fragebogentypen (DSFA, TIA, LIA) können auch direkt von einer Verarbeitung aus gestartet werden — beispielsweise über die Registerkarten "Folgenabschätzung", "Empfänger" oder "Zwecke". Weitere Details finden Sie auf den entsprechenden Seiten unten.
{% endhint %}

## Benutzerdefinierte Fragebogenvorlagen

In Dastra ist es möglich, Ihre eigene benutzerdefinierte Fragebogenvorlage zu erstellen. Klicken Sie dazu auf "**Vorlage erstellen**" und anschließend die Option "**Von Grund auf neu**". Sie gelangen dann zur Bearbeitungsoberfläche für Fragebogenvorlagen.

Erstellen Sie die gewünschte Fragebogenvorlage und klicken Sie auf "**Anlegen**".

![Beispiel einer anpassbaren Fragebogenvorlage.](<../../../.gitbook/assets/asdasd (1).png>)

### Bewertete Elemente

Sie können Fragebögen mit Elementen in Dastra verknüpfen. Durch die Auswahl des Typs des bewerteten Elements erzwingen Sie, dass alle auf dieser Vorlage basierenden Antworten mit einem Objekt des gewählten Typs verknüpft werden. Beispielsweise können Sie festlegen, dass diese Fragebogenvorlage immer mit einer Verarbeitung verknüpft wird.

<figure><img src="../../../.gitbook/assets/Vorlage erstellen4.png" alt=""><figcaption></figcaption></figure>

Sie können auch entscheiden, einen Fragebogen nicht mit einem bestimmten Objekt zu verknüpfen. In diesem Fall wird die Antwort immer mit einer Organisationseinheit verknüpft. Dies kann beispielsweise bei globalen Compliance-Fragebögen der Fall sein.

### Vorlagentypen

Bei der Erstellung einer benutzerdefinierten Vorlage müssen Sie einen Vorlagentyp auswählen.

<figure><img src="../../../.gitbook/assets/Vorlage erstellen3.png" alt=""><figcaption></figcaption></figure>

Diese Typen ermöglichen eine gewisse Anpassung der Fragebogenvorlagen.

* **Standardfragebogen**: Dies ist ein klassischer Fragebogen
* **Compliance-Fragebogen**: Derzeit handelt es sich um einen klassischen Fragebogen
* **Folgenabschätzung**: Diese Vorlage ermöglicht die Anzeige einer Risikomatrix (mit der erforderlichen Konfiguration) und kann beim DSFA-Schritt einer Verarbeitung aufgerufen werden
* **Fragebogen für Auftragsverarbeiter**: Diese Vorlage wird beim Schritt "Empfänger Auftragsverarbeiter" einer Verarbeitung aufgerufen
* **Transferfolgenabschätzung (TIA)**: Fragebogen zur Analyse der Risiken im Zusammenhang mit einer Datenübermittlung außerhalb der EU
* **Analyse der Rechtsgrundlage (LIA)**: Fragebogen zur Rechtsgrundlage der berechtigten Interessen, um sicherzustellen, dass die Interessen die Rechte und Freiheiten der Personen nicht überwiegen
* **Schulungsfragebogen**: Fragebogen zur Durchführung von Schulungsquizzen. Dieser Fragebogentyp ermöglicht es, eine richtige Antwort unter den Antworten auszuwählen und die richtigen Antworten am Ende des Fragebogens anzuzeigen.

## Eine eigene Fragebogenvorlage laden

Schließlich ist es möglich, eine Ihrer Fragebogenvorlagen im JSON-Format zu importieren. Wählen Sie dazu bei der Erstellung des Fragebogens die Option "Vorlage laden".

## Analyseblöcke

## Weiterführende Informationen

{% content-ref url="../planifier-un-audit.md" %}
[planifier-un-audit.md](../planifier-un-audit.md)
{% endcontent-ref %}

{% content-ref url="../rapport-daudit.md" %}
[rapport-daudit.md](../rapport-daudit.md)
{% endcontent-ref %}

{% content-ref url="../pia-aipd.md" %}
[pia-aipd.md](../pia-aipd.md)
{% endcontent-ref %}

{% content-ref url="../tia.md" %}
[tia.md](../tia.md)
{% endcontent-ref %}

{% content-ref url="../lia.md" %}
[lia.md](../lia.md)
{% endcontent-ref %}
