---
description: Dastra integreert naadloos met uw favoriete cloudbestandsprovider
---

# integratie met OneDrive/Google Drive

### Waarom

Hoewel zeer veilig en praktisch in de meeste scenario's, kan het opslaan van bestanden in de Dastra-applicatie overlappen met andere EDM's of cloud file managers. Om dit probleem op te lossen integreert Dastra met de belangrijkste cloudbestandsproviders.

![](<../../.gitbook/assets/image (252) (1).png>)

### Configuratie

Het is heel eenvoudig om je cloud bestandsbeheerder te configureren:

* ga naar de [bestandsbeheerder](https://app.dastra.eu/workspace/0/referentials/folders)
* Klik op de **selector rechtsboven de bestanden** :&#x20;

![image.png](https://static.dastra.eu/richtextbackoffice/511cd52b-858d-482b-805f-e0ed97f018a7/image.png)

* Klik op **Bewaar cloudopslag**.
* Kies uw provider (momenteel Google Drive of OneDrive)

![](<../../.gitbook/assets/image (257) (1).png>)

* Klik op de "Toevoegen" knop, je wordt doorgestuurd naar de inlogpagina van de provider, die je zal vragen om de benodigde rechten om de verbinding met Dastra op te zetten.

### Hoe u bestanden uit uw cloud aan Dastra kunt koppelen

* Bewerk een entiteit**: taak, proces, actor...&#x20;
* Selecteer de gegevensbron** linksboven in het uploadvak voor bestanden.

![](<../../.gitbook/assets/image (254) (1).png>)

* Upload bestanden direct naar je Drive (Wijzig ze, verplaats ze)
* Klik op **selecteer in manager**. en kies het bestand om bij te voegen

![](<../../.gitbook/assets/image (255).png>)



### Beperkingen

**Google Drive**: houd er rekening mee dat alleen bestanden gemaakt in je Dastra ruimte kunnen worden toegevoegd of gewijzigd in je Google Drive. Dastra heeft geen toegangsrechten tot bestanden die door u zijn aangemaakt in de Drive. Dit is een beperking van deze connector. U kunt bestanden die zijn gemaakt in Dastra zonder problemen delen met andere medewerkers.

**One Drive:** het systeem is alleen getest op de persoonlijke versie van OneDrive.  Als u problemen ondervindt met de bedrijfsversies, neem dan [contact op met support](https://www.dastra.eu/en/contact?type=support).

Standaard maakt Dastra bestanden aan in de map "**ApplicationsDastraOneDrive**", die wordt beschouwd als de hoofdmap.

{% hint style="warning" %}
Waarschuwing! Het instellen van de OneDrive verbinding **geeft toegang tot alle bestanden in je persoonlijke schijf**. Je moet daarom heel voorzichtig zijn, omdat de connector beschikbaar zal zijn voor alle gebruikers met "Bestanden" leesrechten.

We raden je aan om een serviceaccount te gebruiken dat geen persoonlijke bestanden kan bevatten met een map die je kunt delen met andere gebruikers.
{% endhint %}