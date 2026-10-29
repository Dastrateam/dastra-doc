---
description: Erfahren Sie, wie Sie die auf Ihrer Website gesetzten Cookies scannen.
---

# Cookies scannen

Dastra scannt die auf Ihrer Website gesetzten Cookies mit der Funktion **Cookie-Scan** des Moduls **Cookie-Banner**. Der Scan ist der Ausgangspunkt für die Erstellung Ihres Banners.

## Auf die Scan-Funktion zugreifen

Melden Sie sich bei Ihrem Dastra-Mandanten an. Wie das geht, erfahren Sie auf der folgenden Seite:

{% content-ref url="../../../getting-started/tutorial/README.md" %}
[Tutorial](../../../getting-started/tutorial/README.md)
{% endcontent-ref %}

1. Klicken Sie im Menü auf **Cookie-Banner**. Die Liste der Banner erscheint.
2. Klicken Sie auf **Banner erstellen**.

<figure><img src="../../../.gitbook/assets/cookies-scan-1.png" alt="Das Menü Cookie-Banner mit den Untermenüs Banner, Statistiken und Einwilligungen"><figcaption><p>Das Modul „Cookie-Banner“ im Menü</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/cookies-scan-2.png" alt="Die Liste der Banner mit der Schaltfläche Banner erstellen"><figcaption><p>Die Schaltfläche „Banner erstellen“</p></figcaption></figure>

Dastra fragt: **Wie möchten Sie Ihr Banner gestalten?** Zwei Möglichkeiten stehen zur Auswahl:

* **Website-Analyse**: Dastra analysiert die Cookies Ihrer Website und schlägt ein Banner mit den erkannten Diensten vor;
* **Manuelle Konfiguration**: Sie erstellen das Banner von Grund auf und deklarieren die URLs, Dienste und Cookies selbst.

<figure><img src="../../../.gitbook/assets/cookies-scan-3.png" alt="Die Auswahl, wie das Banner erstellt wird"><figcaption><p>Die Wahl zwischen „Website-Analyse“ und „Manuelle Konfiguration“</p></figcaption></figure>

Wählen Sie **Website-Analyse**, um auf dieser Seite fortzufahren.

## Die auf Ihrer Website gesetzten Cookies scannen

1. Geben Sie im Feld für den Domainnamen die Adresse Ihrer Website ein, zum Beispiel `https://www.example.com`. Wenn Sie `https://` weglassen, ergänzt Dastra es.
2. Klicken Sie auf **Bestätigen**.

<figure><img src="../../../.gitbook/assets/cookies-scan-4.png" alt="Das Feld zur Eingabe des zu scannenden Domainnamens"><figcaption><p>Die Adresse der zu scannenden Website eingeben</p></figcaption></figure>

{% hint style="info" %}
Der Scan muss Ihre Website öffnen können. Blockiert eine Authentifizierung oder eine Firewall den Zugriff, meldet Dastra das: Verwenden Sie dann stattdessen die **Manuelle Konfiguration**.
{% endhint %}

Der Scan durchsucht bis zu 20 Seiten Ihrer Website, um die zuverlässigste Cookie-Analyse zu erhalten. Während der Analyse erscheint ein Fortschrittsbalken.

<figure><img src="../../../.gitbook/assets/cookies-scan-5.png" alt="Der Fortschrittsbalken während des Scans"><figcaption><p>Der Scan läuft</p></figcaption></figure>

Wenn der Scan endet, erscheinen die Ergebnisse: die in der Dastra-Cookie-Datenbank erkannten Dienste, die gefundenen Cookies und ihre Aufteilung nach Kategorien. Klicken Sie auf **Erneut scannen**, um die Analyse zu wiederholen, oder auf **Banner erstellen**, um das Banner aus diesen Ergebnissen zu erstellen.

<figure><img src="../../../.gitbook/assets/cookies-scan-6.png" alt="Die Scan-Ergebnisse mit den Tabs Dienstleistungen, Gefundene Cookies und Aufteilung der Cookie-Kategorien"><figcaption><p>Die Scan-Ergebnisse</p></figcaption></figure>

Sobald die Cookies Ihrer Website gescannt sind, können Sie sie klassifizieren.

{% content-ref url="classify.md" %}
[Cookies nach Einwilligungskategorien klassifizieren](classify.md)
{% endcontent-ref %}

***

## Nicht klassifizierte Cookies behandeln

Der Scan vergleicht die erkannten Cookies mit der Dastra-Dienstbibliothek. Ein Cookie, das zu keinem Dienst passt, ist ein nicht klassifiziertes Cookie: Es ist mit keinem Dienst verknüpft, wird im öffentlichen Banner nie angezeigt, und die Besucher können ihm daher nicht zustimmen.

In den Scan-Ergebnissen zeigt ein Warnhinweis neben der Zusammenfassung des Scans die Anzahl der nicht klassifizierten Cookies an (zum Beispiel „3 nicht klassifizierte Cookies“). Diese Cookies sind im Tab **Nicht klassifizierte Cookies** zusammengefasst, neben den Tabs **Dienstleistungen**, **Gefundene Cookies** und **Aufteilung der Cookie-Kategorien**.

<figure><img src="../../../.gitbook/assets/cookies-scan-unclassified-cookies-tab.png" alt="Der Tab Nicht klassifizierte Cookies in den Scan-Ergebnissen"><figcaption><p>Der Tab „Nicht klassifizierte Cookies“ der Scan-Ergebnisse, mit dem Hinweis zu ihrer Anzahl</p></figcaption></figure>

Wählen Sie mit den Kontrollkästchen ein oder mehrere Cookies aus (das Kontrollkästchen in der Kopfzeile wählt die gesamte Liste aus) und wählen Sie dann eine der verfügbaren Aktionen.

### Cookies zu einem bestehenden Dienst hinzufügen

1. Wählen Sie die Cookies aus und klicken Sie dann auf **Zu einem bestehenden Dienst hinzufügen**.
2. Wählen Sie im Feld **Zielgruppe** den Dienst aus, mit dem die Cookies verknüpft werden sollen.
3. Bestätigen Sie.

Alle ausgewählten Cookies werden auf einmal zum Dienst hinzugefügt. Ein Cookie, das im Dienst bereits vorhanden ist (gleicher Name und gleiche Domäne), wird nicht ein zweites Mal hinzugefügt.

### Einen Dienst aus einer Auswahl erstellen

1. Wählen Sie die Cookies aus und klicken Sie dann auf **Einen neuen Dienst anlegen**.
2. Das Formular des Dienstes öffnet sich, vorausgefüllt mit der häufigsten Domäne unter den ausgewählten Cookies (Name des Dienstes, Domäne und Logo), und enthält die ausgewählten Cookies.
3. Prüfen Sie die vorgeschlagenen Informationen, insbesondere den Zweck des Dienstes, und speichern Sie dann.

Nur die Cookies, die im Dienst bleiben, verlassen die Liste der nicht klassifizierten Cookies.

### Cookies löschen

Wählen Sie die Cookies aus, klicken Sie auf **Löschen** und bestätigen Sie dann. Die Cookies werden aus der Liste der nicht klassifizierten Cookies entfernt.

### Ein Cookie aus einem Dienst entfernen

Klappen Sie im Tab **Dienstleistungen** der Scan-Ergebnisse die Cookie-Liste eines Dienstes auf und klicken Sie dann auf das Papierkorb-Symbol neben dem Cookie (Tooltip **Von diesem Dienst entfernen**). Das Cookie wird vom Dienst getrennt und wechselt in den Tab **Nicht klassifizierte Cookies**.

Nach jeder Aktion werden die Zähler der Tabs, der Hinweis und das Aufteilungsdiagramm sofort aktualisiert.

### Nicht klassifizierte Cookies im Banner-Editor behandeln

Sie müssen nicht jedes Cookie behandeln, bevor Sie das Banner erstellen: Nicht behandelte Cookies bleiben dem Banner zugeordnet und können später behandelt werden. Im Banner-Editor zeigt der Titel des Abschnitts **Dienstleistungen** die Anzahl der nicht klassifizierten Cookies an, und der Tab **Nicht klassifizierte Cookies** dieses Abschnitts bietet dieselben Aktionen: **Löschen**, **Zu einem bestehenden Dienst hinzufügen** und **Einen neuen Dienst anlegen**.

Sind alle Cookies mit einem Dienst verknüpft, zeigt der Tab die Meldung „Alle Cookies sind klassifiziert“ an.

### Ein bestehendes Banner erneut scannen

Klicken Sie im Tab **Dienstleistungen** des Banner-Editors auf **Cookie-Scan**, um die Website erneut zu scannen. In den Ergebnissen kennzeichnet ein grünes Häkchen (Tooltip **Bereits in Ihrer Konfiguration enthalten**) die Dienste, die im Banner bereits deklariert sind. Erkannte Cookies, die zu den Cookies eines bereits deklarierten Dienstes passen, auch eines benutzerdefinierten Dienstes, werden mit diesem Dienst verknüpft und erscheinen nicht unter den nicht klassifizierten Cookies.

{% hint style="warning" %}
Nicht klassifizierte Cookies werden im öffentlichen Banner nie angezeigt. Verknüpfen Sie jedes Cookie, das Ihre Website tatsächlich setzt, mit einem Dienst, damit die Besucher ihm zustimmen können.
{% endhint %}

***

## Einschränkungen und bewährte Vorgehensweisen

### Nach der Einwilligung gesetzte Cookies (Opt-in-Dienste)

Ein Cookie-Scanner durchsucht Ihre Website standardmäßig, ohne eine Einwilligung zu erteilen. Cookies, die erst nach einem Opt-in gesetzt werden (Analyse, Marketing usw.), werden nie ausgelöst und können daher nicht erkannt werden.

**Ausnahme: Wenn das Dastra-SDK bereits in Ihre Website integriert ist**, kann der Scanner das Einwilligungsbanner umgehen und alle tatsächlich gesetzten Cookies erfassen, auch die von Opt-in-Diensten. In diesem Fall liefert der Scan ohne manuelles Eingreifen ein vollständiges Ergebnis.

Ist das Dastra-SDK auf der gescannten Website noch nicht vorhanden, müssen Opt-in-Dienste über die Dienstbibliothek **manuell hinzugefügt** werden.

### Manuell hinzugefügte Dienste: überzählige Cookies

Wenn Sie einen Dienst aus der Dastra-Bibliothek hinzufügen (zum Beispiel Google Analytics, Meta Pixel), importiert Dastra die vollständige Liste der Cookies, die dieser Dienst in all seinen möglichen Konfigurationen setzen *kann*. Ihre Implementierung verwendet wahrscheinlich nur eine Teilmenge davon.

Es empfiehlt sich, **Cookies zu entfernen, die Ihre konkrete Implementierung tatsächlich nicht setzt**. Cookies zu deklarieren, die Sie nicht verwenden, führt Besucher in die Irre und kann bei einem Compliance-Audit Fragen aufwerfen.

Um zu erkennen, welche Cookies Sie behalten sollten, gleichen Sie die Ergebnisse des automatischen Scans (die erkennen, was tatsächlich gesetzt wird) mit der aus der Bibliothek importierten Liste ab und entfernen Sie Einträge, die im Scan nicht vorkommen.
