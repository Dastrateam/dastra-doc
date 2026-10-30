---
description: Erfahren Sie, wie Sie das Verzeichnis „Auftragsverarbeiter“ von Dastra verwenden.
---

# Verzeichnis „Auftragsverarbeiter“

## Einführung

Artikel 30 der DSGVO legt besondere Pflichten für das _Verzeichnis des Verantwortlichen_ und das _Verzeichnis des Auftragsverarbeiters_ fest. Wenn Ihre Organisation sowohl als Auftragsverarbeiter als auch als Verantwortlicher tätig ist, muss Ihr Verzeichnis die beiden Kategorien von Tätigkeiten daher klar unterscheiden.

**In der Praxis empfiehlt die CNIL in diesem Fall, zwei Verzeichnisse zu führen:**

1. eines für die Verarbeitungen personenbezogener Daten, für die Sie selbst verantwortlich sind,
2. ein weiteres für die Verarbeitungen, die Sie als Auftragsverarbeiter im Auftrag Ihrer Kunden durchführen.

Der Rest dieser Seite behandelt ausschließlich das Verzeichnis „Auftragsverarbeiter“.

## Das Verzeichnis „Auftragsverarbeiter“

Jeder Auftragsverarbeiter muss ein weniger umfangreiches Verzeichnis führen.

Dieses Verzeichnis enthält:

* die **Kontaktdaten des Auftragsverarbeiters**, gegebenenfalls seines Vertreters und seines Datenschutzbeauftragten
* die **Kontaktdaten aller Verantwortlichen, in deren Auftrag der Auftragsverarbeiter tätig ist** (in der Regel die Kunden)
* die **Kategorien der verarbeiteten Daten**
* die **Empfänger**
* die **Übermittlungen** außerhalb des EWR
* die **Sicherheitsmaßnahmen**

In Dastra wird eine als Auftragsverarbeiter angelegte Verarbeitungstätigkeit in 12 Abschnitten dokumentiert: **Allgemeines**, **Interessengruppen**, **Zweck**, **Assets**, **Daten**, **Kunden**, **Betroffene Person**, **Rechte von Personen**, **Empfänger**, **Maßnahmen**, **Dokumentation** und **Zusammenfassung**.

Im Vergleich zu einer Tätigkeit als Verantwortlicher können Sie im Abschnitt **Kunden** die Verantwortlichen angeben, in deren Auftrag Sie tätig sind (in der Regel Ihre Kunden). Einen Abschnitt **Folgenabschätzung** gibt es nicht.

<figure><img src="../../.gitbook/assets/ropa-processor-1.png" alt="Navigation durch die Abschnitte einer Verarbeitungstätigkeit als Auftragsverarbeiter"><figcaption><p>Die verschiedenen Abschnitte einer Verarbeitungstätigkeit „Auftragsverarbeiter“ in Dastra</p></figcaption></figure>

## Der Abschnitt Kunden

Der Abschnitt **Kunden** listet die Verantwortlichen auf, in deren Auftrag Sie die Daten verarbeiten, in der Regel Ihre Kunden. Mit jedem von ihnen müssen Sie einen Vertrag schließen, der die in Artikel 28 der DSGVO vorgesehenen Klauseln enthält.

<figure><img src="../../.gitbook/assets/ropa-processor-2.png" alt="Abschnitt Kunden einer Verarbeitungstätigkeit als Auftragsverarbeiter mit der Schaltfläche Kunden/RT hinzufügen"><figcaption><p>Der Abschnitt Kunden einer Verarbeitungstätigkeit als Auftragsverarbeiter</p></figcaption></figure>

So geben Sie einen Verantwortlichen an:

1. Klicken Sie auf **Kunden/RT hinzufügen**.
2. Wählen Sie **Verzeichnis der Stakeholder (empfohlen)**, um einen Stakeholder Ihres Verzeichnisses auszuwählen, oder **Bitte wählen Sie eine Organisationseinheit aus**.
3. Beschreiben Sie bei Bedarf Ihre Vorgänge unter **Beschreibung der mit den Daten durchgeführten Vorgänge**.
4. Wenn der Verantwortliche die Daten auch erhält, aktivieren Sie **Ist der Kunde/Verantwortliche für die Datenverarbeitung der Empfänger der Daten?**. Wählen Sie unter **Auf welche Daten hat er Zugriff?** den Eintrag **Zugriff auf alle Daten (Standard)** oder **Zugriff auf bestimmte Datensätze** und aktivieren Sie die betreffenden Datenkategorien.
5. Bestätigen Sie.

Um mehrere Verantwortliche gleichzeitig hinzuzufügen, klicken Sie auf den Pfeil rechts neben **Kunden/RT hinzufügen** und wählen dann **Mehrere Stakeholder gleichzeitig hinzufügen**, um mehrere Stakeholder auszuwählen, oder **Organisationseinheiten in großer Anzahl hinzufügen**, um mehrere Organisationseinheiten auszuwählen.

Das Menü am Ende jeder Zeile bietet **Bearbeiten**, **Stakeholder bearbeiten** und **Löschen**. Wenn Ihr Mandant das Modul Verträge nutzt, erstellt **DPA generieren** die Auftragsverarbeitungsvereinbarung des Verantwortlichen. Um mehrere Verantwortliche zu löschen, aktivieren Sie sie und klicken auf **Löschen**.

Um einem Verantwortlichen nur seine eigenen Daten zu senden, verwenden Sie die Option **Für einen Kunden exportieren** im Exportfenster: Die Datei enthält dann nicht die anderen Verantwortlichen (siehe [Verzeichnis exportieren / importieren](export-import.md)).

***

{% hint style="info" %}
Sie können den Typ einer Verarbeitungstätigkeit ändern (von einer als Verantwortlicher angelegten zu einer als Auftragsverarbeiter angelegten und umgekehrt). Die Vorgehensweise finden Sie in den [häufig gestellten Fragen](faq.md#wie-andere-ich-den-typ-einer-verarbeitungstatigkeit-von-verantwortlicher-zu-auftragsverarbeiter-und-umgekehrt).

Wenn Sie eine Tätigkeit als Auftragsverarbeiter wieder in eine Tätigkeit als Verantwortlicher umwandeln, werden die damit verknüpften Kunden entfernt.
{% endhint %}

## Weiterführende Informationen

{% content-ref url="controller.md" %}
[Verzeichnis „Verantwortlicher“](controller.md)
{% endcontent-ref %}
