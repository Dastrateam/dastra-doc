---
description: Erfahren Sie, wie Sie Dastra in Ihr bevorzugtes Datenanalyse-Tool integrieren!
---

# Integration in Datenanalyse-Tools (BI)

{% hint style="info" %}
Um diese Funktion zu nutzen, benötigen Sie in Ihrem Abonnement den **Enterprise**-Plan
{% endhint %}

Dastra ermöglicht es Ihnen ganz einfach, [Personalisierte Berichte](./) in Ihr bevorzugtes BI-Tool (Power BI, Google Looker, Tableau Software...) zu importieren. Der Vorteil dieser Funktion besteht darin, dass Sie die Leistungsfähigkeit der BI-Tools nutzen können, um Daten eingehend zu analysieren, und dabei Berichte haben, die sich automatisch aktualisieren.<br>

### Einrichtung in Dastra

Navigieren Sie zum Modul der personalisierte Berichte, öffnen Sie einen davon und klicken Sie auf die Schaltfläche "In BI-Tool integrieren".

Ein modales Fenster öffnet sich, klicken Sie dann auf "Integrations-Link erstellen".

**Kopieren Sie anschließend den generierten Link**

{% hint style="info" %}
Achtung! Geben Sie den generierten Link an niemanden weiter. Dieser ermöglicht den Zugriff auf die Rohdaten des Berichts.
{% endhint %}

## Einrichtung im BI-Tool:

#### Microsoft Power BI

1. **Power BI Desktop öffnen:**
   * Starten Sie **Power BI Desktop** auf Ihrem Computer.
2. **Mit der Web-Datenquelle verbinden:**
   * Gehen Sie in Power BI Desktop zum Reiter **Start** (Home).
   * Klicken Sie auf **Daten abrufen** (Get Data) und wählen Sie **Web**.
3. **Die URL des JSON-Links eingeben:**
   * Geben Sie im Fenster **Daten aus dem Web abrufen** die URL Ihrer JSON-Datei oder Ihrer API ein (wenn Sie einen JSON-Freigabelink haben).
   * Stellen Sie sicher, dass die URL auf eine JSON-Datei oder eine API zeigt, die JSON-Daten zurückgibt.
   * Klicken Sie auf **OK**.
4. **Authentifizierung (falls erforderlich):**
   * Wenn die URL eine Authentifizierung erfordert (z. B. durch ein Passwort oder einen API-Schlüssel), fordert Power BI Sie zur Anmeldung auf.
   * Wählen Sie den passenden Authentifizierungstyp (z. B. **Anonym**, **OAuth2**, **API-Schlüssel** usw.) und geben Sie bei Bedarf Ihre Anmeldedaten ein.
5. **Auf die JSON-Daten zugreifen:**
   * Power BI verbindet sich mit der URL und ruft die JSON-Datei ab.
   * Nach erfolgreicher Verbindung wird ein Vorschaufenster der JSON-Daten angezeigt. Sie können die Daten in Form von Listen, Objekten oder verschachtelten Tabellen durchsuchen.

{% hint style="info" %}
* **Leistung**: Wenn Ihre JSON-Datei groß ist oder tiefe Hierarchien enthält, kann Power BI einige Zeit zum Laden und Transformieren der Daten benötigen.
* **Datenaktualisierung**: Wenn die JSON-Daten regelmäßig aktualisiert werden (z. B. durch eine API), können Sie eine **Datenaktualisierung** im Power BI Service konfigurieren, um die neuesten Daten automatisch abzurufen.
{% endhint %}

### Google Looker

Google Looker verbindet sich einfach mit **Google BigQuery**, einem Daten-Warehouse von Google Cloud, das JSON-Dateien speichern und verarbeiten kann.

#### 1. **Google BigQuery als Datenquelle verwenden**

1. **JSON-Datei auf Google Cloud Storage hochladen**:
   * Wenn Ihre JSON-Datei über einen Freigabelink zugänglich ist, laden Sie die Datei zunächst auf **Google Cloud Storage** hoch.
   * Machen Sie sie öffentlich oder konfigurieren Sie die entsprechenden Berechtigungen.
2. **JSON-Daten in BigQuery laden**:
   * Rufen Sie die **Google Cloud Platform**-Konsole (Google Cloud Console) auf.
   * Gehen Sie zu **BigQuery** und wählen oder erstellen Sie ein **Projekt**.
   * Wählen Sie in **BigQuery** Ihren **Dataset** (Datensatz) aus und klicken Sie auf **Tabelle erstellen**.
   * Wählen Sie **Google Cloud Storage** als Quelle und geben Sie die URL Ihrer JSON-Datei im Feld **URI** ein.
   * Konfigurieren Sie das Datenformat als **JSON** und stellen Sie sicher, dass BigQuery die Struktur Ihrer Datei korrekt interpretieren kann.
3. **BigQuery mit Looker verbinden**:
   * Sobald die JSON-Datei in **BigQuery** geladen ist, können Sie **Looker** mit BigQuery verbinden.
   * Gehen Sie in Looker zu **Admin** > **Connections** und fügen Sie BigQuery als Datenquelle hinzu.
   * Nach erfolgreicher Verbindung können Sie die BigQuery-Daten direkt in Looker abfragen und visualisieren.

#### 2. **ETL-Tools verwenden, um JSON in Looker zu integrieren**

Wenn Sie die Integration von JSON-Daten aus einer API oder einer externen Datei in Looker automatisieren müssen, können Sie **ETL**-Tools (Extract, Transform, Load) wie **Fivetran**, **Stitch** oder **Airflow** verwenden. Diese Tools können JSON-Daten extrahieren, transformieren und in ein mit Looker kompatibles Daten-Warehouse laden.

**Beispiel mit Fivetran:**

1. **Verbinden Sie eine REST-API oder eine JSON-Quelle in Fivetran**.
2. **Transformieren Sie die Daten**, damit sie den Anforderungen Ihres Daten-Warehouses entsprechen.
3. **Laden Sie die Daten in das Warehouse** (z. B. BigQuery).
4. **Verbinden Sie Looker mit diesem Daten-Warehouse**, um Daten abzufragen und zu visualisieren.

### Tableau Software

\
**1. Tableau Desktop öffnen:**

* Starten Sie **Tableau Desktop** auf Ihrem Computer.

**2. Mit einer Web-Datenquelle verbinden:**

* Gehen Sie in **Tableau Desktop** zum Menü **Datei** und wählen Sie **Neue Datenquelle**.
* Klicken Sie im Fenster zur Auswahl der Datenquellen auf **Web Data Connector**. Diese Option ermöglicht die Verbindung zu Daten aus verschiedenen Webquellen, einschließlich JSON-Dateien über eine API oder URL.

**3. JSON-URL eingeben:**

* Sie müssen die URL der JSON-Datei oder der API im erscheinenden Fenster eingeben.

**4. Authentifizierung (falls erforderlich):**

* Wenn die JSON-URL eine Form der Authentifizierung erfordert (z. B. einen API-Schlüssel, ein OAuth-Token oder Anmeldedaten), fragt Tableau nach den Zugangsinformationen.
* Wählen Sie den passenden Authentifizierungstyp (z. B. **API-Schlüssel** oder **OAuth**) und geben Sie die erforderlichen Informationen ein.

**5. JSON-Daten in Tableau analysieren:**

* Tableau verbindet sich mit der URL, lädt die JSON-Datei herunter und versucht, sie in ein verständliches tabellarisches Format umzuwandeln (eine Tabelle oder eine strukturierte Datenansicht).
* Tableau kann die Struktur der JSON-Daten automatisch erkennen, aber in einigen Fällen, wenn die Datei sehr komplex oder verschachtelt ist, müssen Sie möglicherweise Anpassungen im **Dateneditor** vornehmen, um die Daten zu verflachen oder in ein geeignetes Format zu transformieren.

{% hint style="info" %}
- **Einschränkungen der JSON-Datei:** Wenn Ihre JSON-Datei groß oder sehr verschachtelt ist, kann Tableau Schwierigkeiten bei der korrekten Analyse haben. Manchmal ist es notwendig, die Datei zu transformieren oder zu vereinfachen, bevor sie integriert wird.
- **Authentifizierung und Sicherheit:** Wenn Ihr JSON-Link einen API-Schlüssel erfordert, stellen Sie sicher, dass Sie die Berechtigungen und Anmeldedaten ordnungsgemäß verwalten. Einige APIs können Einschränkungen bei der Anzahl der Anfragen haben oder spezifische Berechtigungen erfordern.
- **Datenaktualisierung:** Wenn sich die JSON-Daten regelmäßig ändern (z. B. über eine API, die Echtzeit-Updates bereitstellt), können Sie Tableau so konfigurieren, dass die **Daten automatisch in regelmäßigen Abständen aktualisiert** werden, um Ihre Berichte aktuell zu halten.
{% endhint %}
