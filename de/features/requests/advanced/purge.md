# Löschregeln für Anfragen

{% hint style="info" %}
Sie benötigen **Administratorrechte** für den Mandanten, um auf diese Funktion zuzugreifen.
{% endhint %}

Sie können die **automatische Löschung von Anfragen im Papierkorb** einrichten, um Ihre internen Aufbewahrungsrichtlinien und insbesondere den Grundsatz der Speicherbegrenzung der DSGVO einzuhalten.

Sie legen fest:

* den **Umfang** der Anfragen, für die die Löschung gilt,
* den **Löschmodus** (Löschung oder Anonymisierung),
* die **maximale Aufbewahrungsdauer**, bevor die Löschung automatisch erfolgt.

Um sie einzurichten, öffnen Sie die Mandanteneinstellungen, gehen Sie zum Bereich **Prozess**, dann zu **Anfragen** und zum Abschnitt **Löschregeln**.

***

## Betroffene Anfragen

Die Löschung gilt **ausschließlich für Anfragen im Papierkorb**. Offene, geschlossene oder archivierte Anfragen sind nicht betroffen.

Jede Nacht prüft Dastra die Anfragen anhand ihres **Datums der Verschiebung in den Papierkorb**. Eine Anfrage, die die von Ihnen festgelegte maximale Dauer überschreitet (zum Beispiel 180 Tage), wird gelöscht. Die Löschung umfasst:

* Anfragen, die länger als die konfigurierte Dauer im Papierkorb liegen;
* alle Anfragetypen (Auskunft, Löschung, Widerspruch usw.);
* alle Anfragen, unabhängig von ihrer Herkunft (Portal, API, Import).

***

## Löschmodi

Wählen Sie im Abschnitt zum Bereinigungsmodus einen der beiden Modi aus.

### Löschung von Anfragen

Die betroffenen Anfragen werden **endgültig** aus Dastra gelöscht. Diese Aktion ist **unumkehrbar**.

* Personenbezogene Daten und der Inhalt des Austauschs werden gelöscht.
* Anhänge und zugehörige Dateien werden entfernt.
* Die Audit-Protokolle behalten nur technische Metadaten (Zeitstempel, Nutzer, Vorgang).

### Anonymisierung von Anfragen

Die Anfragen bleiben in Dastra sichtbar, ihre **personenbezogenen Daten** werden jedoch durch Zufallswerte ersetzt, die keinen Bezug zum Antragsteller haben. Dieser Modus bewahrt eine nicht identifizierbare statistische Spur für Ihre Berichte und Kennzahlen.

* Die Felder mit personenbezogenen Daten (Name, Vorname, E-Mail, Adresse, Ort, Postleitzahl) werden durch generierte Werte ersetzt, und der Text der Anfrage wird ersetzt.
* Die ausgetauschten Nachrichten und die Anhänge werden gelöscht.
* Nicht identifizierende Metadaten (Anfragetyp, Status, Daten) bleiben für das Reporting erhalten.
* Die zugehörigen Aktivitätsprotokolle werden gelöscht.

<figure><img src="../../../.gitbook/assets/requests-purge-1.png" alt="Der Abschnitt Löschregeln mit dem Schalter zum Aktivieren, der Auswahl des Modus und der maximalen Aufbewahrungsdauer"><figcaption><p>Die Löschregeln konfigurieren</p></figcaption></figure>

***

## Aufbewahrungsdauer vor der Löschung

Geben Sie unter **Maximale Aufbewahrungsdauer im Papierkorb (in Tagen)** das maximale Alter einer Anfrage im Papierkorb an, bevor sie gelöscht wird, zum Beispiel 180 Tage. Die Dauer wird ab dem **Datum der Verschiebung der Anfrage in den Papierkorb** gezählt.

Jede Nacht gegen 2:30 Uhr UTC ruft Dastra die betroffenen Anfragen ab und führt die Löschung im gewählten Modus durch.

***

## Konfigurationsbeispiel

* **Löschmodus**: Löschung von Anfragen
* **Maximale Dauer**: 180 Tage (6 Monate)

Jede Nacht werden alle Anfragen, die seit mehr als 180 Tagen im Papierkorb liegen, automatisch gelöscht.

***

## Empfehlungen

* Legen Sie eine Dauer fest, die zu Ihrer internen Aufbewahrungsrichtlinie für Anfragen passt (zum Beispiel 5 Jahre, also 1.825 Tage).
* Wählen Sie die Löschung für eine vollständige Entfernung.
* Wählen Sie die Anonymisierung, wenn Sie Statistiken zur Aktivität behalten möchten.
* Prüfen Sie, dass **Automatische Bereinigung von Anfragen im Papierkorb aktivieren** eingeschaltet ist: Andernfalls findet keine Löschung statt.
