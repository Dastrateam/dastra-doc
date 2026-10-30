---
description: >-
  Erfahren Sie, wie Sie eine Authentifizierung verlangen, den Zugriff auf
  Dokumente steuern und die IP-Adressen Ihres Trust Centers filtern.
---

# Sicherheit

Der Abschnitt **Sicherheit** der Bearbeitungsseite fasst drei Einstellungen zusammen: die obligatorische Authentifizierung, die Genehmigung von Dokumenten-Downloads und die Filterung von IP-Adressen. Die Inhaber des Trust Centers legen Sie im Abschnitt **Konfiguration** fest.

<figure><img src="../../../.gitbook/assets/trust-center-security-1.png" alt="Abschnitt Sicherheit eines Trust Centers mit beiden Optionen und den IP-Filterregeln"><figcaption><p>Der Abschnitt Sicherheit eines Trust Centers</p></figcaption></figure>

## Obligatorische Authentifizierung

Aktivieren Sie **Authentifizierung erforderlich, um auf das Trust Center zuzugreifen**, um die Anmeldung verpflichtend zu machen. Besucher müssen sich dann mit einem Konto Ihrer Organisation bei Dastra anmelden, bevor sie das Portal öffnen. Wenn allen Nutzern ein SSO zugewiesen ist, werden sie zu diesem SSO weitergeleitet.

Wir empfehlen, [SSO](../../settings/sso/README.md) mit automatischer Erstellung von Nutzern zu konfigurieren: Alle Ihre Mitarbeitenden können dann ohne besondere Rolle oder Berechtigung auf das Trust Center zugreifen.

## Inhaber

Das Feld **Inhaber** befindet sich im Abschnitt **Konfiguration**. Siehe [Startseite und allgemeine Konfiguration](home.md).

## Zugriffskontrolle für Dokumente

Die Option **Erfordern Sie eine Genehmigung für das Herunterladen von Dateien** erscheint nur, wenn die Funktion **Dokumente** aktiviert ist. Sie ist für ein neues Trust Center aktiviert.

Wenn sie aktiviert ist:

1. Besucher sehen die Liste der Dokumente, können sie aber nicht direkt herunterladen. Sie stellen mit ihrer E-Mail-Adresse und einer Nachricht eine **Zugriffsanfrage**.
2. Die Inhaber des Trust Centers erhalten eine E-Mail mit einem Link zur Anfrage. Gibt es keinen Inhaber, erhalten die Inhaber der Organisation die E-Mail.
3. Der Inhaber öffnet die Anfrage, gibt bei Bedarf eine **Begründung der Entscheidung** ein und klickt dann auf **Den Zugriffsantrag genehmigen** oder **Den Antrag auf Zugang ablehnen**. Der Besucher erhält die Begründung per E-Mail.
4. Wird die Anfrage genehmigt, erhält der Besucher eine E-Mail mit einem Download-Link, der 30 Tage gültig ist.

Die Anfragen werden im Bildschirm **Anträge auf Zugang zu Dateien** bearbeitet, der alle Anfragen mit ihrem Status auflistet. Der Link in der Benachrichtigungs-E-Mail öffnet ihn direkt bei der betreffenden Anfrage.

{% hint style="info" %}
Sind Inhaber festgelegt, können nur sie Anfragen genehmigen oder ablehnen. Ohne Inhaber werden die Anfragen den Inhabern der Organisation gemeldet.
{% endhint %}

## IP-Adressfilterung

In diesem Abschnitt können Sie außerdem Regeln definieren, um den Zugriff auf Ihr Trust Center auf bestimmte IP-Bereiche zu beschränken. Standardmäßig ist Ihr Trust Center ohne Hinzufügen von IP-Filtern für jede Person mit dem Zugangslink zugänglich, sofern das Trust Center aktiviert ist.

Klicken Sie auf **Eine IP-Filterregel hinzufügen** und geben Sie dann den Namen der Regel sowie Anfang und Ende des IP-Bereichs ein. Eine IP-Adresse, die zu keinem der Bereiche gehört, wird abgelehnt.

{% hint style="info" %}
Diese Filterung ist **getrennt** von der [IP-Filterung der Organisation](../../settings/ip-filtering.md), die nicht für das Trust Center gilt.
{% endhint %}
