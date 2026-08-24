---
description: Erfahren Sie, wie Sie Rollen und Berechtigungen in Dastra verwalten.
---

# Rollen und Berechtigungen verwalten

Beim Einladen eines Nutzers bietet Dastra standardmäßig **drei Rollen** an:

* **Administrator**: Administratoren haben die Rechte der Mitwirkenden und können die Mandanten-Einstellungen verwalten. Administratoren sind die einzigen, die eine Verarbeitung auf den Status "veröffentlicht" setzen, Organisationseinheiten erstellen und neue Nutzer in den Mandanten einladen können.
* **Mitwirkender**: Mitwirkende können den Inhalt der Mandanten lesen und bearbeiten. Sie können Elemente erstellen und noch nicht veröffentlichte Entwürfe bearbeiten. Sie können die Mandanten-Einstellungen nicht ändern.
* **Leser:** Leser können den Inhalt des Mandanten nur einsehen. Sie können weder den Inhalt bearbeiten noch die Mandanten-Einstellungen ändern.

{% hint style="info" %}
Nur **Inhaber** können die Organisationskonto-Einstellungen ändern und Mandanten erstellen.
{% endhint %}

### Einem Nutzer eine Rolle zuweisen

In Dastra kann ein Nutzer mehrere verschiedene Rollen kumulieren. Um einem Nutzer mehrere Rollen zuzuweisen, navigieren Sie zum Abschnitt "Nutzer" in den Einstellungen,

{% hint style="info" %}
<img src="../../.gitbook/assets/nutzer.png" alt="" data-size="original">

dann die Optionen des Nutzers anzeigen

<img src="../../.gitbook/assets/rollen zuweisen.png" alt="" data-size="original">

und die entsprechende "Rolle" für den betreffenden Nutzer auswählen.
{% endhint %}

Es ist jedoch möglich, individuelle Rollen zu erstellen, die möglicherweise besser zu Ihrer Organisation passen.

### Eine benutzerdefinierte Rolle erstellen

Um eine benutzerdefinierte Rolle zu erstellen, müssen Sie Inhaber der Organisation sein. Klicken Sie einfach auf das Profilsymbol oben rechts auf dem Bildschirm und dann auf den Tab "**Konfiguration der Organisation**" in der Dropdown-Liste.

![](<../../.gitbook/assets/Konfiguration der Organisation.png>)

Im Konfigurationspanel klicken Sie auf die Schaltfläche "**Rollen und Berechtigungen**" im Abschnitt "**Organisation**". Die Liste der Rollen und Berechtigungen wird dann angezeigt:

![Die Rolle "Datenschutzkoordinator" wurde benutzerdefiniert erstellt](<../../.gitbook/assets/Rollen und Berechtigungen (1).png>)

{% hint style="info" %}
Nur Inhaber der Organisation haben Zugang zur Verwaltung der Rollen und Berechtigungen.
{% endhint %}

Um eine neue Rolle zu erstellen, klicken Sie auf "Eine Rolle hinzufügen", geben Sie ihr einen Namen und aktivieren Sie die Optionen "Lesen", "Bearbeiten", "Import" und "Export" für jede Funktion. Wenn Sie fertig sind, klicken Sie auf die Schaltfläche "Speichern" unten auf dem Bildschirm.

{% hint style="info" %}
Damit die neue Rolle wirksam wird, muss sie einem oder mehreren Nutzern zugewiesen werden. Navigieren Sie dazu zum Abschnitt "Nutzer" und klicken Sie auf die Schaltfläche "Rolle" des betreffenden Nutzers.
{% endhint %}

Das war's, die Rollen und Berechtigungen sind eingerichtet! Sie können jetzt das Tutorial ansehen oder die Funktionen von Dastra selbst erkunden.

{% content-ref url="../tutoriel/" %}
[tutoriel](../tutoriel/)
{% endcontent-ref %}
