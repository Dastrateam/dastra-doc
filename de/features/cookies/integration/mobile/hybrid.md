---
description: Integrieren Sie das Dastra-Cookie-Banner in eine hybride Anwendung.
---

# Hybride Anwendungen

Eine hybride Anwendung zeigt Webseiten in einer WebView an. Das SDK funktioniert dann genauso wie auf einer Website.

1. Fügen Sie den Banner-Code, den Sie aus dem Abschnitt **Installation** kopiert haben, in die Seiten ein, die von der WebView geladen werden. Siehe [Schnellstart](../quickstart/README.md).
2. Fügen Sie die Adresse dieser Seiten im Abschnitt **Konfiguration** des Banners im Feld **Zulässige URLs (CORS)** hinzu. Ohne diesen Eintrag erscheint das Banner nicht.
3. Um einen Einwilligungsnachweis einem Nutzer der Anwendung zuzuordnen, übergeben Sie dessen pseudonyme Kennung. Siehe [Nutzeridentifizierung](../identification.md).
4. Um die Einwilligung aus Ihrem Code zu lesen oder zu ändern, verwenden Sie die JavaScript-API des SDK. Siehe [Einwilligung programmatisch verwalten](../programmatic-consent.md).
5. Ergänzen Sie in der Anwendung eine Möglichkeit, das Banner mit `dastra.openCookieConsent()` erneut zu öffnen.

Die Tracker der Anwendung müssen Sie weiterhin manuell konfigurieren. Siehe [Cookie-Blockierung](../blocking/README.md).
