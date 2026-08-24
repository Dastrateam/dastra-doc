---
description: (Geplante Veröffentlichung 2026)
hidden: true
---

# Zuordnung der SAP LeanIX Fact Sheets zu Dastra

### **Überblick**

Der LeanIX → Dastra-Konnektor bietet eine automatisierte und geplante Synchronisierung, die ausgewählte Informationen aus den **SAP LeanIX Fact Sheets vom Typ Application** in die **Dastra Assets** überträgt.\
Dastra fungiert als **Zielsystem** und empfängt die Metadaten der LeanIX-Anwendungen über die **LeanIX Pathfinder**-API:

```
GET /services/pathfinder/v1/factSheets (type = Application)
```

Bei jedem Synchronisierungszyklus analysiert der Konnektor die empfangenen LeanIX-Anwendungen und führt eine der folgenden Aktionen in Dastra aus:

* **Ein bestehendes Asset aktualisieren**, wenn ein entsprechendes LeanIX Fact Sheet bereits in Dastra vorhanden ist
* **Ein neues Asset erstellen**, wenn kein bestehendes Asset übereinstimmt
* **Ein bestehendes Asset markieren**, wenn das zugehörige LeanIX Fact Sheet gelöscht wurde

Dies gewährleistet eine **kontinuierliche Konsistenz** zwischen dem LeanIX-Anwendungsinventar und dem Dastra-Asset-Katalog.

***

### **Architekturübersicht**

Nachfolgend eine konzeptionelle Darstellung der End-to-End-Synchronisierung:

```
SAP LeanIX (Pathfinder API)
     |
     | GET /services/pathfinder/v1/factSheets (Application)
     v
 Fact Sheets (Applications)
     |
     |  Nächtliche Synchronisierung
     v
 Dastra (Assets)
```

Beim Import werden bestimmte Felder aus den LeanIX Fact Sheets direkt auf die Eigenschaften der Dastra Assets gemappt.

<figure><img src="../../.gitbook/assets/image-dastra-sap-leanix.png" alt=""><figcaption></figcaption></figure>

***

## **Synchronisierungsprozess**

### **1. Extraktion aus LeanIX**

Der Konnektor ruft alle LeanIX Fact Sheets vom Typ **Application** über die Pathfinder-API ab.

Jedes Fact Sheet enthält Identifikatoren, beschreibende Felder, Tags und relationale Attribute.\
Nur bestimmte Attribute werden in Dastra importiert.

***

### **2. Asset-Abgleich in Dastra**

Jede eingehende Anwendung wird mit den bestehenden Assets in Dastra anhand des **LeanIX Fact Sheet-Identifikators** (`ref`) verglichen.

Abgleichregeln:

* Wenn ein Asset mit derselben `ref` existiert → **das Asset wird aktualisiert**
* Wenn kein Asset übereinstimmt → **ein neues Asset wird erstellt**

***

### **3. Lifecycle-Management**

Wenn ein Dastra-Asset existiert, aber die zugehörige LeanIX-Anwendung nicht mehr in der API-Antwort erscheint:

* Dastra **löscht das Asset nicht**
* Stattdessen wendet Dastra einen spezifischen Tag an:

```
leanix-todelete
```

Dies ermöglicht ein kontrolliertes Lifecycle-Management anstelle einer automatischen Löschung.

***

### **4. Zeitplanung**

Die Synchronisierung wird standardmäßig **einmal pro Nacht** ausgeführt.\
Zusätzliche Trigger können je nach Systemkonfiguration hinzugefügt werden.

***

## **Feldzuordnung (LeanIX → Dastra)**

Die folgende Tabelle listet alle aus LeanIX importierten Felder und ihr Ziel in Dastra auf:

| LeanIX-Feld     | Dastra Asset-Feld  | Beschreibung                                                 |
| ---------------- | ------------------ | ------------------------------------------------------------ |
| displayName      | name               | Name der LeanIX-Anwendung                                   |
| description      | description        | Textbeschreibung der Anwendung                               |
| tags\[]          | tags               | LeanIX-Tags werden nach Dastra kopiert                       |
| user (wenn zugeordnet) | user         | Verknüpfter Nutzer in Dastra, nur wenn bereits vorhanden     |
| id               | ref                | Eindeutige Kennung des LeanIX Fact Sheets                   |
| (N/A)            | type               | Wird für importierte Assets immer auf "Software" gesetzt     |

***

## **Verhalten der Tags**

### **Übernommene Tags**

Alle aus LeanIX stammenden Tags werden bei der Erstellung oder Aktualisierung der Assets nach Dastra übertragen.

### **Löschungs-Tag**

Wenn eine LeanIX-Anwendung aus dem Portfolio verschwindet, fügt Dastra hinzu:

```
leanix-todelete
```

Dieser Tag bleibt bis zur manuellen Bearbeitung bestehen und ermöglicht es Administratoren:

* Das Asset zu archivieren
* Es zu entfernen
* Oder den Tag zu löschen, wenn die Anwendung wieder erscheint

***

## **Fehlerbehandlung und Diagnose**

Der Konnektor protokolliert Ereignisse im Zusammenhang mit der Datensynchronisierung, darunter:

* Die Anzahl der abgerufenen Anwendungen
* Erstellte oder aktualisierte Assets
* Zur Löschung markierte Assets
* API-Antwortcodes
* Zuordnungsinkonsistenzen oder fehlende Pflichtattribute

Administratoren können diese Protokolle in Dastra (geplante Log-Oberfläche) oder über externe Tools je nach Konfiguration einsehen.

***

## **Vorteile**

#### **Automatisierte Inventarabstimmung**

Stellt die Konsistenz des Dastra-Asset-Katalogs mit LeanIX ohne manuellen Eingriff sicher.

#### **Kontrolliertes Asset-Lifecycle-Management**

Die Markierung anstelle der Löschung verhindert Datenverlust und bewahrt die Nachvollziehbarkeit.

#### **Konsistente Tag-Übertragung**

LeanIX-Tagging-Strategien werden in Dastra gespiegelt und unterstützen Klassifizierung, Workflows und Berichtswesen.

#### **Standardisiertes Software-Asset-Modell**

Alle importierten Anwendungen verwenden einen einheitlichen Asset-Typ ("Software"), was Governance und Verarbeitung erleichtert.

***

## **Zukünftige Verbesserungen**&#x20;

In Prüfung befindliche potenzielle Erweiterungen:

* Bidirektionale Synchronisierung
* Anpassbare Feldzuordnungskonfiguration
* Unterstützung weiterer Fact Sheet-Typen (IT Component, Business Capability usw.)
* Echtzeit-Synchronisierungstrigger anstelle der nächtlichen Verarbeitung
