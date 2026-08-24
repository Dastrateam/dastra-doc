# Die wichtigen Begriffe

Bevor Sie Dastra nutzen, ist es wichtig, die grundlegenden Begriffe zu verstehen, die die Plattform strukturieren.\
Sie ermöglichen es Ihnen, Ihre Verarbeitungen, Teams und Verantwortlichkeiten effizient zu organisieren.

***

### 📚 Inhaltsverzeichnis

* [Organisation](key-concepts.md#organisation)
* [Mandant](key-concepts.md#espace-de-travail)
* [Organisationseinheit](key-concepts.md#unite-organisationnelle)
* [Entität](key-concepts.md#entite)
* [Abteilung](key-concepts.md#departement)
* [Inhaber der Organisation](key-concepts.md#proprietaire-de-lorganisation)

***

### 🏢 Organisation

Eine **Organisation** fasst die Konten und Nutzer zusammen, die mit Ihrem Dastra-Abonnement verknüpft sind.\
Sie ist die "Wurzel"-Struktur, die alle Ihre Mandanten, Ihre Abrechnungseinstellungen und Ihre API-Schlüssel enthält.

Sie können den Namen Ihrer Organisation oben rechts in der Benutzeroberfläche unter Ihrem Nutzerprofil sehen.

{% hint style="info" %}
Eine Organisation kann mehrere **Mandanten** enthalten, die jeweils einem anderen Projekt, einer anderen Entität oder einem anderen Team gewidmet sind.\
Ein Nutzer kann mehreren Organisationen angehören.
{% endhint %}

***

### 🧰 Mandant

Ein **Mandant** (Workspace) ist die Umgebung, in der Sie mit Ihrem Team zusammenarbeiten.\
Er bündelt die Module und Daten Ihrer Entitäten: Verarbeitungen, Audits, Risiken, Datenschutzvorfälle, Betroffenenanfragen usw.

Sie wählen Ihren Mandanten bei der Anmeldung über die **Zugangs-Kacheln** auf Ihrem Dashboard aus.

{% hint style="info" %}
Benennen Sie Ihre Mandanten klar und verständlich (z. B. "Compliance Konzern", "Entitäten Deutschland").\
Dies erleichtert die Navigation und die Verwaltung mehrerer Entitäten.
{% endhint %}

***

### 🧩 Organisationseinheit

Die **Organisationseinheiten** ermöglichen es Ihnen, Ihren Workspace entsprechend Ihrer internen Organisation zu strukturieren.\
Sie dienen dazu, Entitäten, Abteilungen, Nutzer und Verarbeitungen in einer hierarchischen Logik zu gruppieren.

Jede Einheit kann enthalten:

* **Entitäten** (juristische Strukturen),
* **Abteilungen** (interne Teams),
* **Nutzer**,
* **Verarbeitungen** oder **Aufgaben**.

{% hint style="info" %}
Organisationseinheiten erleichtern die Delegation, Governance und Rückverfolgbarkeit in Compliance-Projekten.\
Sie dienen häufig als Referenz für Berichte oder Zugriffsberechtigungen.
{% endhint %}

***

### 🏛️ Entität

Eine **Entität** entspricht in der Regel einer **juristischen Person** oder einem **Verantwortlichen** (z. B. eine Gesellschaft, eine Tochtergesellschaft, ein Verein).\
Auf dieser Ebene ordnen Sie die Verarbeitungen und die wichtigsten rechtlichen Informationen zu.

Jede Entität kann enthalten:

* die Kontaktdaten des **Verantwortlichen**,
* den **Datenschutzbeauftragten** (DSB),
* die zuständigen **Aufsichtsbehörden**,
* und die zugehörigen **Abteilungen**.

Beispiel:

> Entität: _Dastra Deutschland GmbH_\
> Abteilung: _Marketing_\
> DSB: _Max Mustermann_ :::

***

### 🧭 Abteilung

Eine **Abteilung** repräsentiert einen Bereich oder eine Abteilung einer Entität (z. B. HR, IT, Marketing, Recht).\
Sie ermöglicht eine feinere Verteilung der Aktivitäten innerhalb einer Entität und die Nachverfolgung der Verantwortlichkeiten pro Team.

Abteilungen dienen insbesondere dazu:

* Verarbeitungen oder Audits nach Bereich zu filtern,
* Aufgaben oder Anfragen einer gezielten Gruppe zuzuweisen,
* interne Informationsflüsse besser zu visualisieren.

{% hint style="info" %}
Abteilungen sind optional, werden aber für mittlere bis große Organisationen dringend empfohlen.\
Sie erleichtern die Verwaltung der Verantwortlichkeiten und die operative Nachverfolgung.
{% endhint %}

***

### 👑 Inhaber der Organisation

Der **Inhaber** (Owner) ist der Hauptadministrator der Dastra-Organisation.\
Er verfügt über sämtliche Verwaltungsrechte, einschließlich der Erstellung und Löschung von Mandanten, der Konfiguration von API-Schlüsseln und der Rollenverwaltung.

Seine Hauptverantwortlichkeiten:

* **Nutzer und Teams** auf globaler Ebene verwalten,
* Die **Mandanten** beaufsichtigen,
* Auf **erweiterte Einstellungen** zugreifen (API, Sicherheit, Abrechnung),
* Ein Konto oder eine Organisation löschen.

{% hint style="info" %}
Beschränken Sie die Anzahl der Inhaber, um die Sicherheit und Konsistenz der Governance zu gewährleisten.\
Anderen Nutzern können angepasste Rollen zugewiesen werden (Admin, Mitwirkender, Leser usw.).
{% endhint %}

***
