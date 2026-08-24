---
description: >-
  Erfahren Sie, wie Sie Entitäten und Abteilungen in Dastra erstellen und
  einrichten.
---

# Organisationseinheiten erstellen und konfigurieren

### Einführung

Die Organisationseinheiten ermöglichen es, Ihren Mandanten zu strukturieren. Zwei Arten von Organisationseinheiten können erstellt werden:

* die **Entitäten**, die juristischen Personen entsprechen und einen Verantwortlichen repräsentieren,
* die **Abteilungen**, die die Organisation der Entitäten ermöglichen.

In Dastra ist der Begriff des Mandanten von dem der juristischen Entität getrennt. So kann **ein Mandant auf mehrere verschiedene juristische Entitäten** verweisen (wie z. B. in einem Konzern). Es kann jedoch nur einen einzigen gesetzlichen Vertreter pro juristische Entität geben.

{% hint style="info" %}
Jede Entität in Dastra gilt als ein Verantwortlicher.
{% endhint %}

### Auf das Modul "Organisationseinheiten" in Dastra zugreifen

Navigieren Sie zu "Einstellungen" auf der linken Seite des Bildschirms und klicken Sie dann auf "Organisationseinheiten".

![Schaltfläche zum Zugriff auf die Mandanten-Einstellungen](../../.gitbook/assets/screenshot-2024-10-17-123108.png)

![Zugriff auf die Einstellungen der Organisationseinheiten](<../../.gitbook/assets/Zugriffsverwaltung - Organsiationseinheiten.png>)

Sie gelangen so zur Ansicht für die **Erstellung und Einrichtung** der Organisationseinheiten:

![Verwaltungsoberfläche der Organisationseinheiten](<../../.gitbook/assets/Verwaltung von Organisationseinheiten.png>)

## Eine Entität erstellen oder bearbeiten

Um eine juristische Entität zu erstellen, klicken Sie einfach auf die Schaltfläche "Entität erstellen (Verantwortlicher)" im Modul "Entitäten und Abteilungen".

![Schaltfläche "Entität erstellen"](<../../.gitbook/assets/Schaltfläche - Entität erstellen.png>)

Füllen Sie die angeforderten Felder aus: Name und Land sind Pflichtfelder. Sie können den Namen des oder der Verantwortlichen (des gesetzlichen Vertreters) sowie den oder die Datenschutzbeauftragte(n) (falls vorhanden) und den Vertreter in der EU (falls zutreffend) angeben.

{% hint style="info" %}
Im Gegensatz zu Abteilungen ist die Anzahl der Entitäten (Verantwortliche), die in Dastra eingetragen werden können, durch ein Kontingent begrenzt, das von Ihrem Abonnement abhängt. Wenn Sie dieses Kontingent erhöhen möchten, [kontaktieren Sie den Vertrieb](https://www.dastra.eu/de/contacts).
{% endhint %}

Um eine Entität zu bearbeiten, klicken Sie auf die 3 Punkte rechts neben der betreffenden Entität und dann auf "Bearbeiten"

![Dropdown-Menü einer Entität.](<../../.gitbook/assets/Entität bearbeiten.png>)

Nehmen Sie die gewünschten Änderungen vor und klicken Sie auf "Speichern".

## Eine Abteilung erstellen oder bearbeiten

Um eine Abteilung zu erstellen, klicken Sie einfach auf die Schaltfläche "Abteilung erstellen" im Modul "Organisationseinheiten" und füllen Sie die angeforderten Felder aus.

![Schaltfläche "Abteilung erstellen"](<../../.gitbook/assets/Abteilung erstellen.png>)

Um eine Abteilung zu bearbeiten, klicken Sie auf die 3 Punkte rechts neben der zu bearbeitenden Abteilung, klicken Sie auf "Bearbeiten" und füllen Sie die angeforderten Felder aus, bevor Sie auf "Speichern" klicken.

![Dropdown-Menü einer Abteilung](<../../.gitbook/assets/Abteilung bearbeiten.png>)

## Organisationseinheiten importieren

Sie können eine Liste von Organisationseinheiten über eine Importdatei importieren. Diese Datei kann heruntergeladen werden, indem Sie auf die Schaltfläche "Importieren" in der Verwaltungsoberfläche der Organisationseinheiten klicken.

<figure><img src="../../.gitbook/assets/Org import.png" alt=""><figcaption></figcaption></figure>

Klicken Sie dann auf "**Laden Sie die Dateivorlage herunter**"

<figure><img src="../../.gitbook/assets/Organisationseinheiten importieren.png" alt=""><figcaption></figcaption></figure>

Sie können sie auch direkt hier herunterladen

Die Datei muss mit folgenden Pflichtfeldern ausgefüllt werden:

* **Id**: Die eindeutige Kennung der Organisationseinheit (5-stellige Zahl)
* **Label**: Der Name der Organisationseinheit (Zeichenkette)
* **CountryCode**: Das Land der Organisationseinheit (2-stellige Ländercodes gemäß [ISO 3166](https://www.ble.de/SharedDocs/Downloads/EN/Climate-Energy/Information-Nabisy/CountryCodes.pdf?__blob=publicationFile\&v=1))
* **Type**: Art der Organisationseinheit ("Entity" für Entität und "Area" für Abteilung)<br>

Das Feld **ParentId** ist nicht obligatorisch, ermöglicht aber die Identifizierung der übergeordneten Organisationseinheit (falls vorhanden) über deren ID (5-stellige Zahl).

{% hint style="warning" %}
Es ist wichtig, die Anzahl der Hierarchieebenen auf 7 Stufen (Eltern-Kind-Beziehungen) zu begrenzen, um eine korrekte Datenverarbeitung sicherzustellen.
{% endhint %}

Beispiel:

<table><thead><tr><th>Id</th><th>ParentId</th><th width="492">Label</th><th>CountryCode</th><th>Type</th></tr></thead><tbody><tr><td>20996</td><td></td><td>HOLDING</td><td>FR</td><td>Entity</td></tr><tr><td>21009</td><td>20996</td><td>Informatique</td><td>BE</td><td>Area</td></tr></tbody></table>

Nachdem Sie die Datei ausgefüllt haben, laden Sie sie im Upload-Bereich hoch und folgen Sie den Anweisungen.

## Entitäten und Abteilungen über das Organigramm visualisieren und einrichten

In Dastra können Sie Entitäten und Abteilungen auch grafisch visualisieren und direkt über das Organigramm einrichten.

Klicken Sie dazu auf die Ansicht "**Organigramm**" im Modul "Organisationseinheiten".

![Ansicht "Organigramm"](../../.gitbook/assets/Organigramm.png)

So können Sie das Organisationsschema Ihrer Struktur grafisch visualisieren:

![Beispiel eines Organigramms in Dastra](<../../.gitbook/assets/Organigramm Beispiel.png>)

{% hint style="info" %}
In der Ansicht "Organigramm" können Sie die meisten Operationen durchführen, die auch in der Ansicht "Organisationseinheiten" verfügbar sind.
{% endhint %}

## Den Zugriff auf den Inhalt einer Organisationseinheit einschränken

Mithilfe des Nutzer-Teams-Systems können Sie den Zugriff auf den Inhalt einer Organisationseinheit einschränken.

Dazu müssen Teams den Organisationseinheiten zugeordnet werden.

Das System ist hierarchisch aufgebaut. Das bedeutet, dass ein Team, um auf eine untergeordnete Organisationseinheit zugreifen zu können, auch Zugriff auf die übergeordnete Organisationseinheit haben muss.

## Weiterführende Informationen

{% content-ref url="creer-puis-affectez-des-equipes.md" %}
[creer-puis-affectez-des-equipes.md](creer-puis-affectez-des-equipes.md)
{% endcontent-ref %}
