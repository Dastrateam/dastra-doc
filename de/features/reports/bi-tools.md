---
description: >-
  Verbinden Sie Ihre personalisierten Dastra-Berichte mit Power BI, Google
  Looker oder Tableau, mit automatisch aktualisierten Daten.
---

# Integration in Datenanalyse-Tools (BI)

{% hint style="info" %}
Um diese Funktion zu nutzen, muss Ihr Abonnement den Tarif **Enterprise** enthalten, und Sie benötigen die Berechtigung **Erweiterte Konfiguration**.
{% endhint %}

Dastra lässt Sie [personalisierte Berichte](README.md) in Ihr BI-Tool importieren (Power BI, Google Looker, Tableau Software usw.). Sie analysieren die Daten mit Ihrem Tool ausführlich, und die Berichte werden automatisch aktualisiert.

## In Dastra einrichten

1. Öffnen Sie im Modul **Personalisierte Berichte** einen Bericht und klicken Sie auf **BI-Tools verbinden**.
2. Klicken Sie im sich öffnenden Fenster auf **Link erstellen**. Der Link wird in Ihre Zwischenablage kopiert.

Das Fenster zeigt dann zwei Tabs, je nachdem, wie sich Ihr Tool verbindet:

* **Link**: die öffentliche Adresse des Berichts, die Sie in das Tool einfügen. Jeder, der diesen Link hat, kann auf die Rohdaten des Berichts zugreifen.
* **Authentifizierung (Bearer)**: die **URL des Dienstes** und das **Authentifizierungs-Token**, die Sie getrennt eingeben. Ihr Tool sendet das Token im HTTP-Header `Authorization: Bearer <token>`. Bevorzugen Sie diesen Tab, wenn Ihr Tool einen Header hinzufügen kann: Die Adresse allein gibt dann keinen Zugriff auf die Daten.

<figure><img src="../../.gitbook/assets/reports-bi-tools-1.png" alt="Das Fenster zur Verbindung von BI-Tools mit den Tabs Link und Authentifizierung (Bearer)"><figcaption><p>Das Fenster zur Verbindung von BI-Tools</p></figcaption></figure>

{% hint style="warning" %}
Geben Sie den Link oder das Token nicht an Personen weiter, die die Daten des Berichts nicht sehen sollen.
{% endhint %}

Um den Zugriff zu beenden, klicken Sie im selben Fenster auf **Anmeldung löschen** und bestätigen Sie. Der Link und das Token funktionieren dann nicht mehr: Sie können mit **Link erstellen** eine neue Verbindung anlegen.

## Im BI-Tool einrichten

### Microsoft Power BI

1. **Power BI Desktop öffnen:**
   * Starten Sie Power BI Desktop auf Ihrem Rechner.
2. **Mit der Webdatenquelle verbinden:**
   * Gehen Sie in Power BI Desktop zum Tab Start.
   * Klicken Sie auf Daten abrufen und wählen Sie dann **Web**.
3. **Die URL des JSON-Links eingeben:**
   * Geben Sie im Fenster Daten abrufen (Web) die URL Ihrer JSON-Datei oder API ein (wenn Sie einen JSON-Freigabelink haben).
   * Stellen Sie sicher, dass die URL auf eine JSON-Datei oder API verweist, die JSON-Daten zurückgibt.
   * Klicken Sie auf OK.
4. **Authentifizierung (falls erforderlich):**
   * Mit dem Link aus dem Tab **Link** ist keine Authentifizierung nötig: Wählen Sie **Anonym**.
   * Geben Sie beim Tab **Authentifizierung (Bearer)** in Schritt 3 die **URL des Dienstes** ein, klicken Sie dann auf **Erweitert** und fügen Sie bei den Parametern des HTTP-Anfrage-Headers den Header `Authorization` mit dem Wert `Bearer ` gefolgt vom Token hinzu. Wählen Sie dann **Anonym**.
5. **Auf die JSON-Daten zugreifen:**
   * Power BI verbindet sich mit der URL und ruft die JSON-Datei ab.
   * Nach erfolgreicher Verbindung erscheint ein Vorschaufenster für die JSON-Daten. Sie können die Daten als verschachtelte Listen, Objekte oder Tabellen erkunden.

{% hint style="info" %}
* **Leistung**: Ist Ihre JSON-Datei groß oder tief verschachtelt, kann Power BI einige Zeit zum Laden und Umwandeln der Daten brauchen.
* **Datenaktualisierung:** Werden die JSON-Daten regelmäßig aktualisiert (zum Beispiel durch eine API), können Sie im Power BI Service eine Datenaktualisierung einrichten, um automatisch die neuesten Daten abzurufen.
{% endhint %}

### Google Looker <a href="#google-looker" id="google-looker"></a>

Google Looker verbindet sich mit Google BigQuery, einem Data Warehouse von Google Cloud, das JSON-Dateien speichern und verarbeiten kann.

**1. Google BigQuery als Datenquelle verwenden**

1. **Die JSON-Datei in Google Cloud Storage hochladen:**
   * Ist Ihre JSON-Datei über einen Freigabelink erreichbar, laden Sie sie zunächst in **Google Cloud Storage** hoch.
   * Machen Sie sie öffentlich oder legen Sie die passenden Berechtigungen fest.
2. **Die JSON-Daten in BigQuery laden:**
   * Öffnen Sie die Google Cloud Platform Console (Google Cloud Console).
   * Gehen Sie zu **BigQuery** und wählen Sie ein Projekt aus oder erstellen Sie eines.
   * Wählen Sie in **BigQuery** Ihr Dataset und klicken Sie auf **Tabelle erstellen.**
   * Wählen Sie **Google Cloud Storage** als Quelle und geben Sie die URL Ihrer JSON-Datei im Feld **URL** ein.
   * Legen Sie das Datenformat auf **JSON** fest und stellen Sie sicher, dass **BigQuery** die Struktur Ihrer Datei richtig interpretieren kann.
3. **BigQuery mit Looker verbinden:**
   * Sobald die JSON-Datei in BigQuery geladen ist, können Sie Looker mit BigQuery verbinden.
   * Gehen Sie in Looker zu Admin > Connections und fügen Sie BigQuery als Datenquelle hinzu.
   * Sobald die Verbindung steht, können Sie die BigQuery-Daten direkt in Looker abfragen und visualisieren.

**2. ETL-Tools verwenden, um JSON in Looker zu integrieren**

Wenn Sie die Integration von JSON-Daten aus einer API oder einer externen Datei in Looker automatisieren müssen, können Sie ETL-Tools (Extract, Transform, Load) wie Fivetran, Stitch oder Airflow verwenden. Diese Tools können JSON-Daten extrahieren, umwandeln und in ein mit Looker kompatibles Data Warehouse laden.

**Beispiel mit Fivetran:**

1. Verbinden Sie eine REST-API oder eine JSON-Quelle mit Fivetran.
2. Wandeln Sie die Daten so um, dass sie den Anforderungen Ihres Data Warehouse entsprechen.
3. Laden Sie die Daten in das Data Warehouse (zum Beispiel BigQuery).
4. Verbinden Sie Looker mit diesem Data Warehouse, um die Daten abzufragen und zu visualisieren.

### Tableau Software <a href="#tableau-software" id="tableau-software"></a>

**1. Tableau Desktop öffnen:**

* Starten Sie Tableau Desktop auf Ihrem Rechner.

**2. Mit einer Webdatenquelle verbinden:**

* Gehen Sie in Tableau Desktop zum Menü Datei und wählen Sie Neue Datenquelle.
* Klicken Sie im Fenster zur Auswahl der Datenquelle auf Web Data Connector. Mit dieser Option verbinden Sie sich mit Daten aus verschiedenen Webquellen, darunter JSON-Dateien über eine API oder eine URL.

**3. Die JSON-URL eingeben:**

* Im angezeigten Fenster geben Sie die URL der JSON-Datei oder API ein.

**4. Authentifizierung:**

* Mit dem Link aus dem Tab **Link** ist keine Authentifizierung nötig.
* Kann Ihr Connector einen HTTP-Header hinzufügen, verwenden Sie den Tab **Authentifizierung (Bearer)**: Geben Sie die **URL des Dienstes** und den Header `Authorization: Bearer <token>` ein.

**5. JSON-Daten in Tableau analysieren:**

* Tableau verbindet sich mit der URL, lädt die JSON-Datei herunter und versucht, sie in ein verständliches Tabellenformat (eine Tabelle oder eine strukturierte Datenansicht) umzuwandeln.
* Tableau kann die Struktur von JSON-Daten automatisch erkennen, doch bei sehr komplexen oder verschachtelten Dateien müssen Sie im Dateneditor gegebenenfalls Anpassungen vornehmen, um die Daten abzuflachen oder in ein geeignetes Format umzuwandeln.

{% hint style="info" %}
* **Grenzen der JSON-Datei:** Ist Ihre JSON-Datei groß oder stark verschachtelt, kann Tableau sie möglicherweise nicht richtig lesen.\
  Manchmal muss sie vor der Integration umgewandelt oder vereinfacht werden.
* **Authentifizierung und Sicherheit:** Erfordert Ihr JSON-Link einen API-Schlüssel, verwalten Sie Berechtigungen und Zugangsdaten sorgfältig. Manche APIs begrenzen die Anzahl der Anfragen oder verlangen besondere Berechtigungen.
* **Datenaktualisierung:** Ändern sich die JSON-Daten regelmäßig (zum Beispiel über eine API mit Echtzeit-Updates), können Sie Tableau so konfigurieren, dass die Daten in regelmäßigen Abständen automatisch aktualisiert werden und Ihre Berichte aktuell bleiben.
{% endhint %}
