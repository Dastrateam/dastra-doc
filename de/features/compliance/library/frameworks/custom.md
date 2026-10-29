---
description: >-
  Mit Dastra erstellen Sie Ihr eigenes regulatorisches Framework und passen es
  mithilfe künstlicher Intelligenz an Ihre Bedürfnisse an
---

# Benutzerdefiniertes Framework erstellen

## Einführung

Mit einem benutzerdefinierten Framework bauen Sie ein Compliance-Framework auf, das **an den spezifischen Kontext der Organisation angepasst** ist: interne Richtlinie, branchenspezifisches Framework, KI-Initiative, Sicherheit, Qualität oder Governance.

Ein benutzerdefiniertes Framework kann:

* **vollständig von Grund auf** aufgebaut werden,
* oder als **gemeinsame Grundlage** für mehrere Compliance-Projekte dienen.

***

## Schritt 1: Das Framework erstellen

{% columns %}
{% column %}
Beim Erstellen eines benutzerdefinierten Frameworks legen Sie fest:

* **Den Namen des Frameworks** (z. B. _Custom AI_, _AI ISSP, Demo_)
* **Die Sprache des Frameworks**, die die Standardsprache der Anforderungen und Kontrollen bestimmt

Nach der Erstellung wird das Framework in der Bibliothek im Status **Entwurf** angelegt.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-448.png" alt="Fenster zum Erstellen eines Frameworks mit Name, Sprache und Logo"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

## Schritt 2: Ansicht und verfügbare Aktionen

Ein neu erstelltes Framework ist standardmäßig:

* **leer**
* **schreibgeschützt**

### Aktionen, die verfügbar sind, solange das Framework nicht geändert wurde

* **Exportieren**: das Framework im Format JSON / Excel abrufen
* **Duplizieren**: das Framework kopieren
* **In den Papierkorb verschieben**: das Framework aus der Bibliothek entfernen (**Wiederherstellen** holt es zurück, **Löschen** entfernt es endgültig)

**Solange sich das Framework nicht im Bearbeitungsmodus befindet, sind weder Ergänzungen noch Änderungen möglich.**

***

## Schritt 3: In den Bearbeitungsmodus wechseln

{% columns %}
{% column %}
Um das Framework zu ergänzen (Kapitel, Anforderungen, Kontrollen usw.), gehen Sie wie folgt vor:

1. Klicken Sie auf **Bearbeiten**
2. Schalten Sie das Framework in den **Bearbeitungsmodus**

Im Bearbeitungsmodus können Sie:

* **Kapitel** erstellen
* **Anforderungen** hinzufügen
* das Framework schrittweise strukturieren

{% hint style="warning" %}
Der Bearbeitungsmodus ist nur für eine Entwurfsversion verfügbar. Die Anforderungen einer veröffentlichten Version sind gesperrt und die Schaltfläche **Bearbeiten** ist deaktiviert: Erstellen Sie eine Version des Frameworks, um sie weiterzuentwickeln (siehe [Framework-Versionen](versions.md)). Name, Logo und Beschreibung bleiben bearbeitbar.
{% endhint %}


{% endcolumn %}

{% column %}


<figure><img src="../../../../.gitbook/assets/image-449.png" alt="Seite eines neu erstellten Frameworks, leer und schreibgeschützt"><figcaption></figcaption></figure>


{% endcolumn %}
{% endcolumns %}

***

## Anforderungen erstellen und strukturieren

Sobald das Framework erstellt und in den **Bearbeitungsmodus** geschaltet ist, können Sie beginnen, es in **Kapitel** und **Anforderungen** zu gliedern.\
In diesem Schritt übertragen Sie ein regulatorisches, normatives oder internes Regelwerk in Elemente, die in Dastra verwendbar sind.

***

### Mit Kapiteln gliedern

{% columns %}
{% column %}
<figure><img src="../../../../.gitbook/assets/image-450.png" alt="Fenster zum Erstellen eines Kapitels"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Kapitel ermöglichen es, das Framework übersichtlich und stimmig zu organisieren.
{% endcolumn %}
{% endcolumns %}

#### Regeln der Gliederung

Dastra erlaubt:

* **Kapitel der obersten Ebene**
* **Unterkapitel**

Die Tiefe ist bewusst auf **maximal zwei Ebenen** begrenzt, um:

* die Lesbarkeit des Frameworks zu gewährleisten
* zu komplexe Strukturen zu vermeiden
* die Verwendung der Anforderungen in Compliance-Projekten zu erleichtern

#### Auszufüllende Felder

Beim Erstellen eines Kapitels:

* **Referenz**: interne Kennung des Kapitels
* **Name**: fachlicher Titel des Kapitels

&#x20;

{% hint style="info" %}
_Bewährte Vorgehensweise_: Gliedern Sie die Kapitel nach großen Themen\
(z. B. Governance, Sicherheit, Betrieb, Nutzungen usw.).
{% endhint %}

***

### Eine Anforderung erstellen

{% columns %}
{% column %}
Anforderungen drücken die **Compliance-Erwartungen** aus, die die Organisation erfüllen muss.\
Sie bilden die direkte Verbindung zwischen dem Framework und den operativen Kontrollen.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-451.png" alt="Fenster zum Erstellen einer Anforderung"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

#### Verfügbare Felder

* **Referenz (Pflichtfeld)**\
  Eindeutige Kennung der Anforderung innerhalb des Frameworks
* **Name (Pflichtfeld)**\
  Knappe Formulierung der Anforderung
* **Beschreibung (optional)**\
  Details zu Inhalt, Geltungsbereich und Zielen der Anforderung

***

### KI-Unterstützung für die Referenz der Anforderung

{% columns %}
{% column %}
<figure><img src="../../../../.gitbook/assets/image-452.png" alt="Fenster zum Erstellen einer Anforderung mit der von der KI vorgeschlagenen Referenz"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Beim Erstellen einer Anforderung bietet Dastra eine **KI-Unterstützung** an, die automatisch eine Referenz erzeugt, die stimmig ist mit:

* dem Namen der Anforderung
* dem übergeordneten Kapitel
* dem Kontext des Frameworks


{% endcolumn %}
{% endcolumns %}

Diese Funktion ermöglicht es,

* die Namenskonventionen zu vereinheitlichen
* Inkonsistenzen oder Duplikate zu vermeiden
* beim Erstellen benutzerdefinierter Frameworks Zeit zu sparen

Sie können die vorgeschlagene Referenz weiterhin frei ändern.

***

### Anforderungen organisieren und verwalten

<figure><img src="../../../../.gitbook/assets/image-476.png" alt="Menü zum Verschieben einer Anforderung in der Baumstruktur des Frameworks"><figcaption></figcaption></figure>

Nach dem Erstellen können Anforderungen:

* in ein anderes Kapitel verschoben werden
* gelöscht werden
* schrittweise ergänzt werden

Jede Anforderung zeigt außerdem Kennzahlen im Überblick (Verknüpfungen mit Kontrollen, Risiken, Tests), die den Grad ihrer Abdeckung leichter erkennen lassen.

***

### Kontrollen einer Anforderung zuordnen

{% columns %}
{% column %}
Kontrollen sind die **operativen** Elemente, mit denen sich die Einhaltung einer oder mehrerer Anforderungen nachweisen lässt.

Um einer Anforderung Kontrollen zuzuordnen, gibt es zwei Vorgehensweisen.
{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-453.png" alt="Auswahl zwischen dem Zuordnen bestehender Kontrollen und dem Erstellen von Kontrollen mit der KI"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

#### Option 1: Bestehende Kontrollen zuordnen

{% columns %}
{% column %}


Sie können eine oder mehrere Kontrollen auswählen, die bereits in der Bibliothek vorhanden sind, und sie der Anforderung zuordnen.


{% endcolumn %}

{% column %}
<figure><img src="../../../../.gitbook/assets/image-454.png" alt="Liste der bestehenden Kontrollen, die einer Anforderung zugeordnet werden können"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

Eine einzelne Kontrolle kann **mehreren Anforderungen** zugeordnet werden, was fördert:

* die gemeinsame Nutzung
* die Kohärenz des Frameworks
* eine bessere Nachvollziehbarkeit

***

#### Option 2: Kontrollen mit KI erstellen oder zuordnen

{% columns %}
{% column %}
<figure><img src="../../../../.gitbook/assets/image-455.png" alt="Kontrollen für eine Anforderung mit der KI erstellen oder zuordnen"><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Dastra bietet eine KI-Unterstützung, die es ermöglicht,

* automatisch **relevante bestehende Kontrollen** zu identifizieren
* bei Bedarf die **Erstellung neuer Kontrollen** vorzuschlagen

Die KI stützt sich auf:

* den Inhalt der Anforderung
* den Kontext des Frameworks
* die bereits in der Bibliothek vorhandenen Kontrollen
{% endcolumn %}
{% endcolumns %}

Mit der KI erstellte Kontrollen können automatisch enthalten:

* ihre Beschreibung
* ihre Zuordnung zur Anforderung
* die zugehörigen Tests

***

### Vorteile dieses Ansatzes

Dieser Ansatz ermöglicht:

* eine **schrittweise Strukturierung** des Frameworks
* **gewollte Überschneidungen** zwischen Anforderungen
* die Erstellung übergreifender Kontrollen, die mehrere Anforderungen abdecken
* eine solide Grundlage für das Risikomanagement und die Compliance-Projekte
