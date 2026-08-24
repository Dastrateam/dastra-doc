---
description: >-
  Diese Dokumentationsseite erklärt, wie Dastra sich nativ mit Ihrem bevorzugten
  Cloud-Dateianbieter für die Speicherung der DMS-Dateien integriert
---

# OneDrive/Google Drive-Integrationen

### Interesse an benutzerdefiniertem Cloud-Speicher

Standardmäßig nutzt das [DMS von Dastra](../gestion-de-documents-ged/) ein standardmäßiges, sicheres Speichersystem basierend auf Azure Blob Storage. Die Dateien werden verschlüsselt und von einem Antivirus analysiert. Die Dateien werden auf einem anderen Server redundant gespeichert. Weitere Informationen finden Sie in [unserer Dokumentation zur Sicherheit von Dastra](../../security/general.md)

Obwohl sehr sicher und in den meisten Szenarien praktisch, kann die Speicherung von Dateien in der Dastra-Anwendung mit anderen DMS oder Cloud-Dateimanagern redundant sein. Um dieses Problem zu lösen, integriert sich Dastra nativ mit den wichtigsten Cloud-Dateianbietern.

<figure><img src="../../.gitbook/assets/image-252-1.png" alt=""><figcaption><p>Die DMS-Dateien von Dastra können an verschiedenen Speicherorten gespeichert werden</p></figcaption></figure>

### Benutzerdefinierten Cloud-Speicher konfigurieren

Um Ihren Cloud-Dateimanager zu konfigurieren, ist es ganz einfach:

* Gehen Sie zum [Dateimanager](https://app.dastra.eu/workspace/0/documents/folders/Dastra)

<figure><img src="../../.gitbook/assets/Erweiterte Konfiguration24.png" alt=""><figcaption></figcaption></figure>

* Klicken Sie auf den **Selektor oben links bei den Dateien**:

![image.png](<../../.gitbook/assets/Erweiterte Konfiguration25.png>)

* Klicken Sie auf **Cloud-Speicher verwalten**
* Wählen Sie Ihren Anbieter (Google Drive oder OneDrive)

![](<../../.gitbook/assets/Erweiterte Konfiguration26.png>)

* **Klicken Sie auf die Schaltfläche „Hinzufügen"**, Sie werden zur Login-Seite des Anbieters weitergeleitet, die Sie um die erforderlichen Berechtigungen zur Herstellung der Verbindung mit Dastra bittet.
* Am Ende des Prozesses wählen Sie das Laufwerk des Drive aus, das Sie verwenden möchten (ein Google Drive oder ein SharePoint-Laufwerk für OneDrive)

### Dateien aus Ihrem Cloud an Dastra anhängen

* **Bearbeiten Sie eine beliebige Entität**: Aufgabe, Verarbeitung, Akteur...
* **Wählen Sie die Datenquelle** oben links im Datei-Upload-Bereich.

![](../../.gitbook/assets/image-254-1.png)

* Senden Sie Dateien direkt auf Ihr Drive (Bearbeiten Sie sie, verschieben Sie sie)
* Klicken Sie auf **Im Manager auswählen** und wählen Sie die anzuhängende Datei

![](../../.gitbook/assets/image-255.png)

### Einschränkungen

**Google Drive**: Achtung, nur Dateien, die aus Ihrem Dastra-Bereich erstellt wurden, können zu Ihrem Google Drive hinzugefügt oder darin bearbeitet werden. Dastra hat keine Zugriffsrechte auf Dateien, die Sie selbst im Drive erstellt haben. Dies ist eine Einschränkung dieses Konnektors. Sie können in Dastra erstellte Dateien problemlos mit anderen Mitarbeitern teilen.

**OneDrive:** Das System wurde nur mit der persönlichen Version von OneDrive getestet. Wenn Sie Probleme mit den Enterprise-Versionen haben, zögern Sie nicht, [den Support zu kontaktieren](https://www.dastra.eu/fr/contact?type=support)

Standardmäßig erstellt Dastra Dateien im Verzeichnis „**Applications\DastraOneDrive**", das es als sein Stammverzeichnis betrachtet

{% hint style="warning" %}
Achtung! Die Einrichtung der OneDrive-Verbindung **gewährt Zugriff auf alle Dateien Ihres persönlichen Drive**. Es ist daher große Vorsicht geboten, da der Konnektor allen Nutzern mit Leseberechtigung „Dateien" zur Verfügung gestellt wird.

Es wird empfohlen, ein dediziertes OneDrive-Laufwerk zu erstellen. Sie können dieser [Anleitung zur Erstellung einer dedizierten SharePoint-Website](https://learn.microsoft.com/en-us/sharepoint/create-site-collection) folgen.
{% endhint %}
