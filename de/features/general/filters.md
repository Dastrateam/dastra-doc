---
description: >-
  Verfeinern Sie die Anzeige der Datentabellen aller Module mit erweiterten
  Filtern, benutzerdefinierten Spalten und benutzerdefinierten Ansichten.
---

# Erweiterte Filter

## Verwendung

Mit erweiterten Filtern filtern Sie Ihre Daten nach nahezu jedem Feld Ihrer Entitäten.

1. Öffnen Sie ein Dastra-Modul, zum Beispiel das Modul der Betroffenenanfragen.
2. Klicken Sie oben rechts in der Datentabelle auf die Schaltfläche **Filter**.
3. Wenden Sie im sich öffnenden Fenster einen der am häufigsten verwendeten Standardfilter an: Die Tabelle aktualisiert sich automatisch.

<figure><img src="../../.gitbook/assets/general-filters-1.png" alt="Filterfenster einer Liste mit den Standardfiltern und der Schaltfläche Filter hinzufügen"><figcaption><p>Die Standardfilter einer Liste von Betroffenenanfragen</p></figcaption></figure>

{% hint style="info" %}
Filter addieren sich.

_Wenn Sie zum Beispiel nach den Tags „komplex“ und „ausstehend“ und nach der Organisationseinheit „Contoso“ filtern, zeigt die Tabelle die Zeilen, die beide Tags tragen **und** zur Organisationseinheit „Contoso“ gehören._
{% endhint %}

4. Passt kein Standardfilter, klicken Sie auf **Filter hinzufügen**, um die Kombination von Bedingungen zu erstellen, die Ihrem Bedarf entspricht.

Jede Änderung wird sofort angewendet. Die Schaltfläche **Filter löschen** setzt die Tabelle in ihren Ausgangszustand zurück.

Dastra speichert die ausgewählten Filter: Wenn Sie die Seite wechseln oder Ihren Browser aktualisieren, bleiben sie erhalten. Sie gelten für Ihren Browser, für die Liste und für Ihren Mandanten und werden im **LocalStorage** Ihres Browsers gespeichert.

## Spalten anpassen

Die Schaltfläche **Spalten anpassen** in der letzten Zelle der Kopfzeile jeder Liste ermöglicht es, die angezeigten Spalten auszuwählen (**Sichtbare Spalten** und **Versteckte Spalten**), einschließlich der benutzerdefinierten Felder, und ihre Reihenfolge festzulegen. Klicken Sie auf **Anwenden**, um zu bestätigen, oder auf **Zurücksetzen**, um zur ursprünglichen Auswahl zurückzukehren.

Sie können Spalten auch direkt in der Kopfzeile der Liste neu anordnen: Wenn Sie mit der Maus über eine Spaltenüberschrift fahren, erscheint links vom Spaltennamen ein Ziehpunkt. Ziehen Sie die Spalte an die gewünschte Position: Die neue Reihenfolge gilt sofort. Einige feste Spalten lassen sich nicht verschieben.

Wenn Sie mit der Maus über eine Spaltenüberschrift fahren, wird die zusätzliche Erklärung der Spalte angezeigt, sofern es eine gibt. Ihre Spaltenauswahl wird in Ihrem Konto gespeichert.

## Benutzerdefinierte Ansichten

Eine **benutzerdefinierte Ansicht** speichert den aktuellen Zustand Ihrer Filter und Ihre Spaltenauswahl unter einem Namen. Die Ansichtsauswahl befindet sich oben links in jeder Liste: Sie zeigt **Alle Elemente** (die Standardansicht) oder den Namen der aktiven Ansicht, gefolgt von einem Sternchen, wenn Sie sie geändert haben, ohne zu speichern.

So erstellen Sie eine Ansicht:

1. Wenden Sie die gewünschten Filter und die gewünschte Spaltenauswahl an.
2. Öffnen Sie die Ansichtsauswahl und klicken Sie auf **Benutzerdefinierte Ansicht speichern**.
3. Geben Sie den **Namen Ihrer benutzerdefinierten Ansicht** ein und bestätigen Sie.

<figure><img src="../../.gitbook/assets/general-filters-2.png" alt="Geöffnete Auswahl der benutzerdefinierten Ansichten mit der Standardansicht, Meine Ansichten, Gemeinsame Ansichten und Benutzerdefinierte Ansicht speichern"><figcaption><p>Die Auswahl der benutzerdefinierten Ansichten</p></figcaption></figure>

Die Auswahl listet die Standardansicht **Alle Elemente**, die Ihre Filter und Spalten zurücksetzt, Ihre eigenen Ansichten unter **Meine personalisierten Ansichten** und die Ihrer Kollegen unter **Gemeinsame Ansichten** auf. Fahren Sie mit der Maus über eine Ansicht, um sie zu bearbeiten (Stift) oder zu löschen (Papierkorb). Wurde die aktive Ansicht geändert, ersetzt der Eintrag **Aktualisieren** sie durch die aktuellen Filter und Spalten.

Um eine Ansicht mit den anderen Nutzern Ihres Mandanten zu **teilen**, aktivieren Sie beim Speichern die Option **Diese personalisierte Ansicht mit anderen Nutzern teilen**. Die Option wird nur Nutzern mit erweitertem Zugriff angeboten, die auch als Einzige eine geteilte Ansicht bearbeiten oder löschen können.

<figure><img src="../../.gitbook/assets/general-filters-3.png" alt="Fenster Benutzerdefinierte Ansicht speichern mit dem Namen der Ansicht und der Option zum Teilen"><figcaption><p>Eine benutzerdefinierte Ansicht speichern, mit der Option zum Teilen</p></figcaption></figure>

Benutzerdefinierte Ansichten sind in den meisten Listen verfügbar: Betroffenenanfragen, Verarbeitungsverzeichnis, Assets, Verträge, KI-Systeme, Datenschutzvorfälle usw.

## Bedingungsgruppen

Mit erweiterten Filtern können Sie Bedingungen innerhalb eines einzigen Filters mit den Operatoren **Und** und **Oder** kombinieren.

### Funktionsprinzip

Standardmäßig sind alle Bedingungen eines Filters durch **Und** verknüpft: Eine Zeile muss _alle_ Bedingungen erfüllen. Sobald eine Gruppe mindestens zwei Elemente (Bedingungen oder Gruppen) enthält, erscheint an ihrem Rand eine Schaltfläche **Und**: Klicken Sie darauf, um sie auf **Oder** umzustellen, und umgekehrt. Jede Gruppe hat ihren eigenen Operator, ebenso der Filter als Ganzes.

Beispiel:

```
Gruppe 1: Status = "In Bearbeitung" UND Priorität = "Hoch"
ODER
Gruppe 2: Status = "Überfällig"
```

Dieser Filter zeigt alle Anfragen, die in Bearbeitung sind und eine hohe Priorität haben, sowie alle überfälligen Anfragen, unabhängig von ihrer Priorität.

### Eine Bedingungsgruppe erstellen

1. Öffnen Sie das Filterfenster und klicken Sie auf **Filter hinzufügen**.
2. Klicken Sie auf **Eine Bedingung hinzufügen** und wählen Sie dann das Feld, den Vergleichsoperator und den Wert aus.
3. Klicken Sie auf **Eine Gruppe von Bedingungen hinzufügen**, um einen unabhängigen Block zu erstellen, und fügen Sie dann seine Bedingungen hinzu.
4. Klicken Sie auf die Schaltfläche **Und** oder **Oder**, um festzulegen, wie die Bedingungen einer Gruppe oder die Gruppen untereinander kombiniert werden.
5. Löschen Sie eine Bedingung oder eine Gruppe mit dem Papierkorb-Symbol.

<figure><img src="../../.gitbook/assets/generalites-advanced-filters-condition-groups.png" alt="Fenster der erweiterten Filter mit zwei durch Oder verbundenen Bedingungsgruppen"><figcaption><p>Zwei durch Oder verbundene Bedingungsgruppen, mit den Schaltflächen Eine Bedingung hinzufügen und Eine Gruppe von Bedingungen hinzufügen</p></figcaption></figure>

{% hint style="info" %}
Eine Gruppe kann keine weitere Gruppe enthalten, und ein Filter enthält höchstens 10 Bedingungen. Filter und benutzerdefinierte Ansichten, die vor den Gruppen erstellt wurden, bleiben nutzbar.
{% endhint %}

## Bekannte Probleme

### Meine Daten werden nicht mehr angezeigt

Wenn Sie durch einen Filter die Anzeige Ihrer Daten verlieren, löschen Sie die Daten Ihres Browsers (Cookies, LocalStorage usw.). Dadurch werden die Filter und die aktive Ansicht Ihres Mandanten zurückgesetzt. Sie können auch auf **Filter löschen** klicken und dann die Ansicht **Alle Elemente** wählen.

### Einige Spalten fehlen in den erweiterten Filtern

Aus technischen Gründen lassen sich einige Spalten nicht filtern. Exportieren Sie in diesem Fall die Rohdaten und erstellen Sie Ihren Bericht in einem Tool wie Excel.

Ist ein Filter für Ihre Tätigkeit unverzichtbar, reichen Sie einen Funktionswunsch [über die Dastra-Community oder das Anfragesystem](../../getting-started/support/request.md) ein.
