---
description: >-
  Erfassen Sie die Unternehmen und Personen, mit denen Sie arbeiten
  (Auftragsverarbeiter, Herausgeber, Empfänger, DSB, Kunden), ihre
  Unterauftragsverarbeiter und die Assets, die sie herausgeben.
---

# Stakeholder

Stakeholder sind die Unternehmen und Personen, die mit Ihren Datenverarbeitungen verbunden sind: Auftragsverarbeiter, Software-Herausgeber, Anbieter von KI-Modellen, gemeinsam Verantwortliche, öffentliche Stellen, Kunden und so weiter. Anders als Nutzer melden sie sich nicht bei Dastra an.

Erfassen Sie jeden Stakeholder einmal in dieser Referenzliste. Assets, Verarbeitungstätigkeiten, Verträge und Datenschutzverletzungen verweisen dann auf ihn, sodass sich eine Änderung seiner Angaben überall auswirkt.

## Einen Stakeholder hinzufügen

Öffnen Sie **Metadaten** > **Stakeholder**. Sie haben folgende Möglichkeiten:

* Klicken Sie auf **Stakeholder erstellen** und wählen Sie dann **Basierend auf einer Vorlage**, um von einer Vorlage der Bibliothek auszugehen, oder **Von Grund auf neu**, um bei null zu beginnen;
* klicken Sie auf die KI-Schaltfläche links von **Stakeholder erstellen**, um den Stakeholder zu beschreiben und den Assistenten einen Entwurf erstellen zu lassen (diese Option hängt von den Funktionen ab, die für Ihre Organisation aktiviert sind);
* klicken Sie auf den Pfeil neben **Stakeholder erstellen** und dann auf **Erstellen Sie auf der Grundlage von Vorlagen**;
* importieren Sie Stakeholder aus einer Datei: Pfeil neben **Stakeholder erstellen** und dann **Importieren**. Siehe [Daten importieren (Excel, CSV)](../../general/import.md);
* machen Sie aus E-Mails Stakeholder: Pfeil neben **Stakeholder erstellen** und dann **E-Mails in Stakeholder verwandeln**. Das öffnet die Integration für eingehende E-Mails in den Mandanteneinstellungen.

<figure><img src="../../../.gitbook/assets/repositories-stakeholders-1.png" alt="Liste der Stakeholder mit geöffnetem Menü Stakeholder erstellen"><figcaption><p>Die Liste der Stakeholder</p></figcaption></figure>

## Das Stakeholder-Formular ausfüllen

| Abschnitt | Feld | Inhalt |
| --- | --- | --- |
| **Allgemeine Informationen** | **Natürliche Person** oder **Juristische Person** | Die Art des Stakeholders. Das Namensfeld heißt **Vollständiger Name** bei einer Person und **Name der Organisation** bei einem Unternehmen und ist erforderlich. |
| | **Interne Referenz**, **Organisationseinheit** | Ihre Referenz und die Einheit, die den Stakeholder sehen kann. Ohne Einheit sehen ihn alle Einheiten. |
| | **Inhaber des Stakeholders** | Der Nutzer, der für den Stakeholder zuständig ist. |
| | **Beschreibung**, **URL der Website** | Eine freie Beschreibung und die Adresse der Website. |
| | **Unternehmensidentifikationsnummer** | Nur bei Unternehmen. Ist die SIRET-Integration aktiviert, können Sie die SIRET-Datenbank durchsuchen, und die Adresse wird für Sie ausgefüllt. |
| | **Adresse** | **Land**, **Adresse**, **Stadt**, **Postleitzahl** und **Region**. |
| | **Kontaktdaten** | **Name des Ansprechpartners**, **Position des Ansprechpartners**, **E-Mail-Adresse des Ansprechpartners** und **Telefonnummer des Ansprechpartners**. |
| **Unterauftragsverarbeiter** | | Die Unterauftragsverarbeiter des Stakeholders, oft im DPA genannt. Wählen Sie sie in der Liste aus oder erstellen Sie sie, und geben Sie dann für jeden das **Land, in dem sich die Daten befinden**, und eine Beschreibung ein. So kartieren Sie die gesamte Unterauftragskette. |
| **Verbundene Assets** | | Die vom Stakeholder herausgegebenen Assets. Wenn Sie ein Asset auswählen, wird der Stakeholder sein **Herausgeber**: Hat das Asset bereits einen anderen Herausgeber, bittet Dastra Sie, den Austausch zu bestätigen. |

Die für Stakeholder definierten [benutzerdefinierten Felder](../../general/custom-fields.md) werden dem Formular hinzugefügt, und Sie können ein Logo und [Tags](../../general/tags.md) anhängen.

Die Symbolleiste des Formulars gibt je nach Ihren Berechtigungen und den aktivierten Funktionen Zugriff auf die angehängten Dokumente, Kommentare, Fragebögen, Aufgaben, Verträge und Risiken, die mit dem Stakeholder verknüpft sind. Sie enthält außerdem:

* **Verknüpfte Elemente**: die [generischen Beziehungen](../relationships.md) des Stakeholders;
* **Verarbeitungen**: die Verarbeitungstätigkeiten, die den Stakeholder verwenden, mit einer Schaltfläche **Verknüpfung mit Verarbeitungen (RT, Empfänger usw.)**, um weitere hinzuzufügen;
* **Aktivitätsverlauf**;
* die regelmäßige Überprüfung des Stakeholders. Siehe [Regelmäßige Überprüfung (Aktualität)](../../regular-review.md);
* den Workflow-Schritt des Stakeholders, wenn Workflow-Schritte definiert sind.

Das Aktionsmenü des Formulars bietet **Duplizieren**, **Zusammenführen**, **Exportieren** und **Löschen**.

## Stakeholder in der Liste finden

Neben den unter [Metadaten](README.md) beschriebenen Filtern bietet die Liste:

* den Filter **Verantwortung**: Software-Herausgeber (Herausgeber von mindestens einem Asset), Anbieter von KI-Modellen (Herausgeber von mindestens einem KI-Modell) oder Empfänger in einer Verarbeitungstätigkeit (Auftragsverarbeiter, gemeinsam Verantwortlicher, öffentliche Stelle usw.);
* die Filter **Typ**, **Land**, **Schritte** und **Nach Tags filtern** sowie die Organisationseinheit;
* die Tabellen- und die Kartenansicht;
* die standardmäßig ausgeblendeten Spalten **Unterauftragsverarbeiter** und **Related contracts** unter **Spalten anpassen**.

Bei einer Auswahl stehen unter den Sammelaktionen **Verknüpfung mit Verarbeitungen (RT, Empfänger usw.)**, **Fragebögen versenden**, **Überprüfung**, **Zusammenführen** und **Exportieren** zur Verfügung.

## Wo Stakeholder verwendet werden

* In einer Verarbeitungstätigkeit kann ein Stakeholder Verantwortlicher, gemeinsam Verantwortlicher, Auftragsverarbeiter oder ein anderer Empfänger sein. Siehe [Stakeholder](../../ropa/activity/stakeholders.md) und [Empfänger](../../ropa/activity/recipients/README.md) der Tätigkeit.
* Als **Herausgeber** eines Assets. Siehe [Assets](assets.md).
* In Verträgen, Datenschutzverletzungen, Risiken und Fragebögen.

{% hint style="warning" %}
Das Löschen eines Stakeholders entfernt seine Verweise in Verarbeitungstätigkeiten (Empfänger, Verantwortlicher, Stakeholder), Vorfällen, Organisationseinheiten und Diskussionen. Aufgaben, Fragebögen und angehängte Dateien bleiben erhalten.
{% endhint %}
