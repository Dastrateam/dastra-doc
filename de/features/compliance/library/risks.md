---
description: >-
  Die Risikobibliothek ermöglicht die Identifizierung, Qualifizierung und
  Überwachung von Risiken im Zusammenhang mit den Anforderungen und Kontrollen,
  die in den Compliance-Frameworks definiert sind.
---

# Risiken

In Dastra stellt ein Risiko ein **befürchtetes Ereignis** dar, das negative Auswirkungen auf die Organisation haben kann, im Zusammenhang mit der Nutzung, Entwicklung oder dem Betrieb von Systemen (z. B. KI-Systeme).

Die Risiken sind ein **Schlüsselelement der Steuerung**: Sie ermöglichen die Messung der Risikoexposition der Organisation und die Bewertung der tatsächlichen Wirksamkeit der umgesetzten Kontrollen.

***

### Risiken und Kontrollen: eine zentrale Beziehung

Ein wesentlicher Punkt zum Verständnis ist, dass **Risiken niemals isoliert sind**.

👉 In Dastra:

* ein **Risiko wird durch eine oder mehrere Kontrollen abgedeckt**
* eine **Kontrolle trägt zur Reduzierung eines oder mehrerer Risiken bei**

Die Kontrollen bilden daher die **Maßnahmen zur Risikobeherrschung**.\
Sie ermöglichen die Reduzierung:

* der **Wahrscheinlichkeit** des Risikoeintritts,
* und/oder seiner **Auswirkung** auf die Organisation.

Diese Beziehung ermöglicht den Übergang von einem deklarativen Ansatz zu einem **operativen Risikomanagement**, das auf konkreten und überprüfbaren Maßnahmen basiert.

***

### Bibliotheksansicht der Risiken

<figure><img src="../../../.gitbook/assets/Compliance24.png" alt=""><figcaption></figcaption></figure>

Die Risikobibliothek bietet einen Gesamtüberblick über die identifizierten Risiken, insbesondere:

* ihre Referenz und Beschreibung,
* die zugehörigen Tags (Vertraulichkeit, Leistung, Robustheit usw.),
* die anfänglichen Auswirkungs- und Wahrscheinlichkeitsstufen,
* Filter zur Erleichterung der übergreifenden Analyse.

👉 Diese Ansicht ermöglicht:

* die Hauptrisiken zu identifizieren,
* ihre Abdeckung durch Kontrollen zu überprüfen,
* die Compliance-Bemühungen zu priorisieren.

***

### Erstellung und Beschreibung eines Risikos

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/Compliance25.png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
Bei der Erstellung oder Bearbeitung eines Risikos gibt der Nutzer an:

* **den Namen und die Referenz des Risikos**
* eine **Beschreibung** zur Qualifizierung des Risikoszenarios
* **Tags** zur Erleichterung der Kategorisierung
{% endcolumn %}
{% endcolumns %}

***

### Risikobewertung

Jedes Risiko wird in zwei unterschiedlichen Bewertungen erfasst:

#### Anfangsrisiko

Das **Anfangsrisiko** entspricht dem Risikoniveau **vor der Umsetzung der Kontrollen**.

Es wird bewertet anhand:

* einer **Wahrscheinlichkeit**
* einer **Auswirkung**

Diese beiden Dimensionen werden auf einer **standardisierten Risikomatrix** positioniert.

***

#### Restrisiko

Das **Restrisiko** entspricht dem Risikoniveau **nach Anwendung der zugehörigen Kontrollen**.

👉 Der Vergleich zwischen Anfangsrisiko und Restrisiko ermöglicht:

* die Wirksamkeit der Kontrollen zu messen,
* die Risikoreduktion zu visualisieren,
* die Abhilfemaßnahmen zu begründen.

📌 Derzeit ist die **Risikomatrix fest** und für alle Risiken gleich, um eine homogene und vergleichbare Bewertung zu gewährleisten.

***

### Zuordnung von Kontrollen

{% columns %}
{% column %}
Ein Risiko muss einem oder mehreren **Kontrollen** zugeordnet werden, die die zur Beherrschung umgesetzten Maßnahmen darstellen.

Die Zuordnung ermöglicht:

* die Hebel zur Risikoreduktion klar zu identifizieren,
* die Auswirkung der Kontrollen auf das Restrisiko zu verfolgen,
* die Nachvollziehbarkeit zwischen Compliance und Risikomanagement sicherzustellen.
{% endcolumn %}

{% column %}
<figure><img src="../../../.gitbook/assets/Compliance26.png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

***

### Zuordnung von Bedrohungen

Die Risiken können auch mit **Bedrohungen** verknüpft werden, die die **Ereignisse oder Ursachen** darstellen, die ein Risiko auslösen können.

👉 Beispiel:

* **Bedrohung**: fehlende Überwachung der KI-Logs
* **Risiko**: Informationsabfluss über KI-Anfragen

Diese Unterscheidung ermöglicht eine feinere und strukturiertere Analyse der Risikoszenarien.

***

### Warum Risiken in die Bibliothek integrieren

Die Zentralisierung der Risiken in der Bibliothek ermöglicht:

* einen übergreifenden Blick auf die Risiken über alle Frameworks hinweg
* eine bessere Kohärenz bei ihrer Bewertung
* eine direkte Verbindung zwischen Risiken, Kontrollen und Anforderungen
* eine effizientere Steuerung der Compliance und der Sicherheit
