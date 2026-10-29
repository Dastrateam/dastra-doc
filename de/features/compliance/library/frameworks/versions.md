---
description: >-
  Entwickeln Sie ein Framework über aufeinanderfolgende Versionen weiter,
  veröffentlichen Sie sie, legen Sie die aktuelle Version fest und aktualisieren
  Sie die Compliance-Projekte, die es verwenden.
---

# Framework-Versionen

Jedes Framework der Bibliothek ist versioniert. Eine Version hat eine automatisch vergebene Nummer (_Version 1_, _Version 2_ usw.), einen Versionshinweis und einen Status (Entwurf oder veröffentlicht). Mit Versionen entwickeln Sie ein Framework weiter (Aktualisierung der Rechtsvorschriften, hinzugefügte oder umformulierte Anforderungen, umgestellte Kapitel), ohne die Compliance-Projekte zu ändern, die eine frühere Version verwenden.

<figure><img src="../../../../.gitbook/assets/compliance-framework-detail-version-header.png" alt="Kopfbereich eines Frameworks mit Versionsnummer, dem Label Aktuelle Version und dem Status Veröffentlicht"><figcaption><p>Versionsnummer, das Label Aktuelle Version und der Status werden unter dem Namen des Frameworks angezeigt</p></figcaption></figure>

***

## Versionsnummer und aktuelle Version

Die Versionsnummer steht unter dem Namen des Frameworks, auf seiner Karte in der Liste der Frameworks und im Tab **Details** (Karte **Versionsinformationen**, zusammen mit dem Versionshinweis).

Das Label **Aktuelle Version** kennzeichnet die Version, die standardmäßig installiert wird, wenn das Framework einem Projekt hinzugefügt wird. Ein Framework hat nur eine aktuelle Version.

Die Liste der Frameworks in der Bibliothek zeigt die aktuelle Version jedes Frameworks. Die anderen Versionen finden Sie im Tab **Versionen** des Frameworks.

***

## Den Versionsverlauf anzeigen

Der Tab **Versionen** eines Frameworks listet alle seine Versionen auf, von der neuesten zur ältesten. Jede Zeile zeigt:

* die Versionsnummer und gegebenenfalls das Label **Aktuelle Version**,
* den Status (Entwurf oder veröffentlicht),
* den Versionshinweis,
* das Erstellungsdatum und den Autor der Version.

Klicken Sie auf eine Version (oder im Aktionsmenü auf **Anzeigen**), um sie zu öffnen. Eine veröffentlichte Version öffnet sich im Lesemodus.

Je nach Status bietet das Aktionsmenü jeder Version:

* **Anzeigen**: die Version öffnen,
* **Versionshinweise bearbeiten**,
* **Als aktuelle Version festlegen** (veröffentlichte Version, die nicht die aktuelle Version ist),
* **Veröffentlichen** (Entwurfsversion),
* **Veröffentlichung rückgängig machen** (veröffentlichte Version),
* **Löschen** (Entwurfsversion).

***

## Eine Version erstellen

1. Öffnen Sie das Framework und dann den Tab **Versionen**.
2. Klicken Sie auf **Eine neue Version erstellen**.
3. Das Fenster zeigt die automatisch vergebene Nummer (**Neue Version:** _Version n_). Geben Sie optional **Versionshinweise** ein (bis zu 3000 Zeichen), zum Beispiel _Aktualisierung der Rechtsvorschriften 2026_.
4. Klicken Sie auf **Bestätigen**.

Die Version übernimmt die Struktur des Frameworks (Kapitel, Anforderungen und verknüpfte Kontrollen) und wird als **Entwurf** erstellt. Sie öffnet sich direkt: Klicken Sie auf **Bearbeiten**, um ihre Kapitel und Anforderungen weiterzuentwickeln (siehe [Benutzerdefiniertes Framework erstellen](custom.md)).

Mit der Schaltfläche **Eine neue Version importieren** im Tab **Versionen** können Sie eine Version auch aus einer JSON- oder Excel-Datei erstellen.

Den Versionshinweis können Sie jederzeit über das Aktionsmenü der Version ändern (**Versionshinweise bearbeiten**).

{% hint style="info" %}
Die Versionen eines Frameworks werden nicht gesondert auf das Framework-Kontingent angerechnet: Das Erstellen oder Importieren einer Version verbraucht keinen Framework-Credit.
{% endhint %}

***

## Eine Version veröffentlichen, die Veröffentlichung rückgängig machen oder sie löschen

* **Veröffentlichen**: über das Aktionsmenü der Version oder mit der Schaltfläche **Veröffentlichen** oben auf der Seite des Frameworks. Eine veröffentlichte Version wird angeboten, wenn das Framework einem Projekt hinzugefügt wird. Mehrere veröffentlichte Versionen desselben Frameworks können nebeneinander bestehen.
* **Veröffentlichung rückgängig machen**: Die Version wird wieder zum Entwurf und wird beim Hinzufügen des Frameworks zu einem Projekt nicht mehr angeboten. Die aktuelle Version kann nicht zurückgezogen werden: Legen Sie zuerst eine andere Version als aktuelle Version fest.
* **Löschen**: Nur eine Entwurfsversion kann gelöscht werden. Die anderen Versionen des Frameworks sind davon nicht betroffen.

{% hint style="warning" %}
Die Anforderungen einer veröffentlichten Version sind gesperrt: Die Schaltfläche **Bearbeiten** ist deaktiviert. Um Kapitel oder Anforderungen zu ändern, erstellen Sie eine Version. Name, Logo und Beschreibung des Frameworks (Tab **Details**) bleiben auch bei einer veröffentlichten Version bearbeitbar.
{% endhint %}

***

## Die aktuelle Version festlegen

Öffnen Sie im Tab **Versionen** das Aktionsmenü einer veröffentlichten Version und klicken Sie auf **Als aktuelle Version festlegen**.

Diese Version wird dann standardmäßig angeboten und installiert, wenn das Framework einem Projekt hinzugefügt wird. Projekte, die eine andere Version verwenden, bleiben unverändert.

***

## Aus dem Quellreferenzwerk aktualisieren

Wurde ein Framework aus einer Vorlage erstellt und ist eine neuere Version dieses Quellreferenzwerks verfügbar, dann:

* zeigt die Karte des Frameworks in der Liste das Badge **Update verfügbar**,
* zeigt die Seite des Frameworks das Banner _Eine aktuellere Version des Quell-Repositorys ist verfügbar_, gefolgt vom Link **aktualisieren**.

Klicken Sie auf **aktualisieren**, um das Fenster **Aus dem Quellreferenzwerk aktualisieren** zu öffnen. Es zeigt eine Vorschau der Änderungen an Kontrollen, Tests, Risikoszenarien und Bedrohungen. Elemente, die im Quellreferenzwerk entfernt wurden, sind mit dem Label **In der Quelle nicht enthalten** gekennzeichnet.

Klicken Sie auf **Bestätigen**: Aus der Quelle wird eine veröffentlichte Version des Frameworks erstellt, die zur aktuellen Version wird. Frühere Versionen und die Projekte, die sie verwenden, sind davon nicht betroffen.

***

## Versionen und Compliance-Projekte

### Die zu installierende Version wählen

Wenn Sie ein Framework einem Projekt hinzufügen (**Ein Framework zum Projekt hinzufügen**), werden nur veröffentlichte Versionen angeboten. Gibt es mehrere veröffentlichte Versionen, erscheint neben dem Namen des Frameworks eine Dropdown-Liste (**Zu installierende Version**), in der die aktuelle Version vorausgewählt ist. Das Projekt wird dann an die installierte Version gebunden.

### Ein zu aktualisierendes Projekt erkennen

In der Projektübersicht zeigt die Karte jedes Frameworks die Nummer der verwendeten Version. Das Badge **Update verfügbar** zeigt an, dass das Projekt eine Version verwendet, die nicht mehr die aktuelle Version des Frameworks ist.

<figure><img src="../../../../.gitbook/assets/compliance-project-overview-framework-update-available.png" alt="Framework-Karte in einem Projekt mit Versionsnummer und dem Badge Update verfügbar"><figcaption><p>Das Badge Update verfügbar kennzeichnet ein Projekt, das an eine frühere Version des Frameworks gebunden ist</p></figcaption></figure>

### Ein Projekt auf eine andere Version umstellen

1. Öffnen Sie in der Projektübersicht das Aktionsmenü der Framework-Karte und klicken Sie auf **Die Version des Frameworks aktualisieren**.
2. Wählen Sie die **Zielversion** unter den anderen veröffentlichten Versionen. Ihr Versionshinweis und eine Vorschau der Elemente, die dem Projekt hinzugefügt werden, werden angezeigt.
3. Klicken Sie auf **Bestätigen**.

Bei der Migration gilt:

* Die Elemente, die die Zielversion einführt, werden dem Projekt hinzugefügt.
* Bezeichnungen, Beschreibungen und Tags der vorhandenen Kontrollen, Tests, Risikoszenarien und Bedrohungen werden aus der Zielversion aktualisiert.
* Ergebnisse und Nachweise bleiben erhalten.
* Kontrollen, die in der Zielversion nicht enthalten sind, werden von den Anforderungen getrennt, bleiben aber im Projekt (eine Meldung zeigt vor der Bestätigung, wie viele es sind).

{% hint style="warning" %}
Die Migration erfolgt immer manuell: Ein Projekt wird nie automatisch auf die aktuelle Version umgestellt. Sie ist nicht möglich, solange im Projekt ein Audit läuft.
{% endhint %}
