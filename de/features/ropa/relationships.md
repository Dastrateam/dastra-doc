# Beziehungen zwischen Verarbeitungen erstellen

In Dastra können Sie Beziehungen zwischen Ihren Verarbeitungstätigkeiten erstellen, um sie leichter zu verwalten.

Diese Beziehungen sind zwischen Verarbeitungstätigkeiten möglich, die sich im selben Mandanten befinden.

## Zweck von Beziehungen zwischen Verarbeitungstätigkeiten

Mit Beziehungen zwischen Verarbeitungstätigkeiten bilden Sie die Verantwortlichkeitsverhältnisse zwischen den verschiedenen für die Verarbeitung zuständigen Entitäten ab.

In einer Unternehmensgruppe können Sie zum Beispiel eine von der Muttergesellschaft durchgeführte Verarbeitungstätigkeit mit den Verarbeitungstätigkeiten ihrer Tochtergesellschaften verknüpfen. Das ist häufig bei Verarbeitungstätigkeiten der allgemeinen Verwaltung der Gruppe der Fall, etwa Personalverwaltung, Buchhaltung oder Lieferantenmanagement.

> Eine Muttergesellschaft X führt die Gehaltsabrechnung im Auftrag ihrer Tochtergesellschaften Y und Z durch. In der Entität X wird die Verarbeitungstätigkeit „Gehaltsabrechnung“ (P1) als Auftragsverarbeiter erstellt. Von P1 aus erstellen Sie eine Beziehung **Strenge Übertragung (starke Vererbung)** zu zwei Verarbeitungstätigkeiten (C1 und C2), die in Y und Z liegen und als Verarbeitungstätigkeiten des Verantwortlichen erstellt wurden.
>
> Jede Änderung an P1 wird dann automatisch an C1 und C2 weitergegeben.

## Eine Beziehung hinzufügen

Klicken Sie im Eintrag einer Verarbeitungstätigkeit in der Symbolleiste oben auf die Schaltfläche **Beziehungen zwischen Verarbeitungen**. Die Schaltfläche zeigt die Anzahl der bestehenden Beziehungen an.

<figure><img src="../../.gitbook/assets/screenshot-2023-02-06-103430.png" alt="Bereich Beziehungen einer Verarbeitungstätigkeit"><figcaption><p>Der Bereich Beziehungen einer Verarbeitungstätigkeit</p></figcaption></figure>

Der Bereich listet die bestehenden Beziehungen nach Art gruppiert auf, mit der Organisationseinheit jeder verbundenen Verarbeitungstätigkeit und dem Datum, an dem die Beziehung erstellt wurde. Klicken Sie auf eine Verarbeitungstätigkeit, um sie in einem neuen Tab zu öffnen, oder auf das Papierkorb-Symbol, um die Beziehung zu entfernen.

Um eine Beziehung zu erstellen, klicken Sie auf **Eine Beziehung hinzufügen** und gehen Sie dann so vor:

1. Wählen Sie die **Art der Beziehung**. Darunter erscheint eine Beschreibung der gewählten Art.
2. Wählen Sie **Bestehende Verarbeitung**, um bereits vorhandene Verarbeitungstätigkeiten zu verknüpfen, oder **Neue Verarbeitung**, um die verbundene Verarbeitungstätigkeit gleichzeitig zu erstellen.
3. Wählen Sie bei einer bestehenden Verarbeitungstätigkeit ihre **Organisationseinheit** und dann die Verarbeitungstätigkeit unter **Bitte wählen Sie die angehängten Objekte aus.**
4. Geben Sie bei einer neuen Verarbeitungstätigkeit den **Name der neuen Verarbeitung** ein, aktivieren Sie bei Bedarf **Verarbeitungstätigkeit als Auftragsverarbeiter** und wählen Sie ihre Organisationseinheit.
5. Klicken Sie auf **Hinzufügen**.

<figure><img src="../../.gitbook/assets/screenshot-2023-02-06-103745.png" alt="Fenster zum Hinzufügen einer Beziehung"><figcaption><p>Das Fenster zum Hinzufügen einer Beziehung</p></figcaption></figure>

Sie können Beziehungen zu mehreren Verarbeitungstätigkeiten gleichzeitig erstellen:

* Bei **Strenge Übertragung (starke Vererbung)** oder **Transmet (geringe Vererbung)** können Sie mehrere bestehende Verarbeitungstätigkeiten auswählen.
* Bei **Ist die Muttergesellschaft von**, **Bezieht sich auf**, **Strenge Übertragung (starke Vererbung)** oder **Transmet (geringe Vererbung)** können Sie mit der Option **Neue Verarbeitung** mehrere Organisationseinheiten auswählen: In jeder von ihnen wird eine neue Verarbeitungstätigkeit erstellt.

Es können bis zu 50 Verarbeitungstätigkeiten oder Organisationseinheiten gleichzeitig ausgewählt werden.

{% hint style="info" %}
Beziehungen können nur mit Verarbeitungstätigkeiten erstellt werden, die sich im selben Mandanten befinden.
{% endhint %}

## Arten von Beziehungen

Es gibt zwei Arten von Beziehungen:

1. **Deklarative Beziehungen**: Sie stellen eine einfache Verknüpfung zwischen zwei Verarbeitungstätigkeiten her, ohne funktionale Abhängigkeit.
2. **Funktionale Beziehungen**: Sie übertragen Felder von einer Verarbeitungstätigkeit auf eine andere oder lassen eine Verarbeitungstätigkeit Felder erben.

Die Bezeichnungen der Beziehungsarten stehen so in der Anwendung. Einige lesen sich im Deutschen missverständlich, daher beschreibt jeder Abschnitt, was die Beziehung bedeutet.

### Deklarative Beziehungen

#### Ist das Ergebnis von

Hierarchische Beziehung, die eine strukturierte Lesart der Verarbeitungstätigkeiten ermöglicht, **ohne funktionale Abhängigkeit** zwischen den Feldern. Die Bezeichnung entspricht der Beziehung „ist untergeordnet“.

> Verarbeitungstätigkeit A ist hierarchisch Verarbeitungstätigkeit B zugeordnet.

#### Ist die Muttergesellschaft von

Hierarchische Beziehung, die eine strukturierte Lesart der Verarbeitungstätigkeiten ermöglicht, **ohne funktionale Abhängigkeit** zwischen den Feldern.

> Verarbeitungstätigkeit A steht hierarchisch über Verarbeitungstätigkeit B.

#### Bezieht sich auf

Einfache logische Verknüpfung zwischen zwei Verarbeitungstätigkeiten, **ohne jede Abhängigkeit** zwischen ihren Feldern.

> Verarbeitungstätigkeit A steht in Beziehung zu Verarbeitungstätigkeit B.

#### Kopiert von

Diese Beziehung hält fest, welche Kopien von dieser Verarbeitungstätigkeit angefertigt wurden. Sie wird automatisch erstellt, wenn Sie bei einer Verarbeitungstätigkeit **Duplizieren** verwenden.

> Verarbeitungstätigkeit A ist die Quelle (der Kopie) von Verarbeitungstätigkeit B.

#### Dies ist eine Kopie von

Diese Beziehung hält fest, von welcher Verarbeitungstätigkeit eine Kopie angefertigt wurde. Sie wird automatisch erstellt, wenn Sie bei einer Verarbeitungstätigkeit **Duplizieren** verwenden.

> Verarbeitungstätigkeit A ist eine Kopie von Verarbeitungstätigkeit B.

{% hint style="info" %}
**Kopiert von** und **Dies ist eine Kopie von** werden nur automatisch erstellt: Sie lassen sich im Fenster **Eine Beziehung hinzufügen** nicht auswählen.
{% endhint %}

### Funktionale Beziehungen

Funktionale Beziehungen übertragen Felder von einer Verarbeitungstätigkeit auf eine andere oder lassen eine Verarbeitungstätigkeit Felder erben.

#### Strenge Übertragung (starke Vererbung)

Die Quell-Verarbeitungstätigkeit **A** überträgt ihre Felder auf die abhängige Verarbeitungstätigkeit **B**.

{% hint style="warning" %}
Ausgenommen sind die Felder des Tabs 1 **Allgemeines** und die in Tab 11 **Dokumentation** hochgeladenen Dokumente der Verarbeitungstätigkeit.
{% endhint %}

Damit entsteht eine strenge Beziehung zwischen **A (Quelle)** und **B (abhängig)**:

* Die bereits vorhandenen Felder von **B** werden beim Erstellen der Beziehung gelöscht.
* Die von **A** geerbten Felder können in **B** weder geändert noch gelöscht werden, und in **B** kann kein neues Feld hinzugefügt werden.
* Jede Änderung in **A** wird automatisch in **B** übernommen.

Wenn Sie die Beziehung entfernen, sind die geerbten Felder wieder bearbeitbar, und die ursprünglichen Felder von **B** werden wiederhergestellt (die Elemente Ihrer Referenzdaten bleiben erhalten).

#### Strenge Vererbung (starke Vererbung)

Die Verarbeitungstätigkeit **A** hängt von der Verarbeitungstätigkeit **B** ab und erbt ihre Felder.

{% hint style="warning" %}
Ausgenommen sind die Felder des Tabs 1 **Allgemeines** und die in Tab 11 **Dokumentation** hochgeladenen Dokumente der Verarbeitungstätigkeit.
{% endhint %}

Damit entsteht eine strenge Beziehung zwischen **B (Quelle)** und **A (abhängig)**:

* Die bereits vorhandenen Felder von **A** werden beim Erstellen der Beziehung gelöscht.
* Die von **B** geerbten Felder können in **A** weder geändert noch gelöscht werden, und in **A** kann kein neues Feld hinzugefügt werden.
* Jede Änderung in **B** wird automatisch in **A** übernommen.

Wenn Sie die Beziehung entfernen, sind die geerbten Felder wieder bearbeitbar, und die ursprünglichen Felder von **A** werden wiederhergestellt (die Elemente Ihrer Referenzdaten bleiben erhalten).

Eine Verarbeitungstätigkeit, die in strenger Vererbung von einer anderen abhängt, zeigt ein Banner **Erbe der Datenverarbeitung** mit einem Link zu ihrer Quelle an, und ihre geerbten Tabs sind gesperrt.

{% hint style="danger" %}
Eine Verarbeitungstätigkeit kann nur von **einer Quell-Verarbeitungstätigkeit gleichzeitig** abhängen.
{% endhint %}

#### Transmet (geringe Vererbung)

Die Quell-Verarbeitungstätigkeit **A** überträgt ihre Felder automatisch auf die abhängige Verarbeitungstätigkeit **B**.

{% hint style="warning" %}
Ausgenommen sind die Felder des Tabs 1 **Allgemeines** und die in Tab 11 **Dokumentation** hochgeladenen Dokumente der Verarbeitungstätigkeit.
{% endhint %}

Damit entsteht eine Beziehung mit weicher Vererbung zwischen **A (Quelle)** und **B (abhängig)**:

* Die von **A** geerbten Felder können in **B** nicht geändert werden.
* **B** kann eigene Felder hinzufügen, ändern oder löschen.
* Jede Änderung in **A** wird automatisch in **B** übernommen.

Wenn Sie die Beziehung entfernen, sind die geerbten Felder wieder bearbeitbar, und die vorhandenen Felder von **B** bleiben erhalten.

#### Erbschaft (geringe Erbschaft)

Die Verarbeitungstätigkeit **A** hängt von der Verarbeitungstätigkeit **B** ab und erbt ihre Felder automatisch.

{% hint style="warning" %}
Ausgenommen sind die Felder des Tabs 1 **Allgemeines** und die in Tab 11 **Dokumentation** hochgeladenen Dokumente der Verarbeitungstätigkeit.
{% endhint %}

Damit entsteht eine Beziehung mit weicher Vererbung zwischen **B (Quelle)** und **A (abhängig)**:

* Die von **B** geerbten Felder können in **A** nicht geändert werden.
* **A** kann eigene Felder hinzufügen, ändern oder löschen.
* Jede Änderung in **B** wird automatisch in **A** übernommen.

Wenn Sie die Beziehung entfernen, sind die geerbten Felder wieder bearbeitbar, und die vorhandenen Felder von **A** bleiben erhalten.

{% hint style="danger" %}
Eine Verarbeitungstätigkeit kann nur von **einer Quell-Verarbeitungstätigkeit gleichzeitig** abhängen.
{% endhint %}

## Übersicht der Beziehungen

| Art der Beziehung | Tab 1, Allgemeines | Tabs 2 bis 10 (fachliche Felder) | In Tab 11 (Dokumentation) hochgeladene Dokumente | Eigene Felder der abhängigen Verarbeitungstätigkeit |
| --- | --- | --- | --- | --- |
| **Deklarative Beziehungen** (Ist das Ergebnis von / Ist die Muttergesellschaft von / Bezieht sich auf / Kopiert von / Dies ist eine Kopie von) | Keine Auswirkung | Keine Auswirkung | Keine Auswirkung | Keine Auswirkung |
| **Strenge Übertragung (starke Vererbung)** | Nicht übertragen | Übertragen | Nicht übertragen | Können nicht hinzugefügt, geändert oder gelöscht werden |
| **Strenge Vererbung (starke Vererbung)** | Nicht geerbt | Geerbt | Nicht geerbt | Können nicht hinzugefügt, geändert oder gelöscht werden |
| **Transmet (geringe Vererbung)** | Nicht übertragen | Übertragen | Nicht übertragen | Können hinzugefügt, geändert oder gelöscht werden |
| **Erbschaft (geringe Erbschaft)** | Nicht geerbt | Geerbt | Nicht geerbt | Können hinzugefügt, geändert oder gelöscht werden |
