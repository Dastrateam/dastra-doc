# Bekende problemen

## Gebruiker niet herkend door SSO

Er zijn een aantal redenen waarom de SSO-verbinding van een gebruiker kan mislukken &#x20;

Als een fout aangeeft dat de gebruiker geen toegang kan krijgen tot de applicatie, controleer dan het volgende:&#x20;

* Hebt u gecontroleerd of de SSO-configuratie geen fouten bevat? U kunt dit controleren door op de knop Test van de verbinding te drukken. Als het werkt, dan is de configuratie correct. Zo niet, dan is er een fout in de configuratie geslopen &#x20;
* Is de gebruiker goed gekoppeld aan de organisatie? De gebruiker moet aanwezig zijn in de gebruikerslijst van de organisatie. SSO is namelijk gekoppeld aan de organisatie &#x20;
* Als de gebruiker al een gebruikersaccount heeft aangemaakt (bijvoorbeeld in een andere organisatie of als onderdeel van een testaccount), controleer dan of de organisatie waarin u SSO hebt geconfigureerd ook daadwerkelijk hun hoofdorganisatie is (ga hiervoor naar de [lijst met organisatiegebruikers](https://app.dastra.eu/general-settings/users)). De gebruiker moet verschijnen als een interne gebruiker. Als dit niet het geval is, betekent dit dat een organisatie zijn verbinding met Dastra (zijn hoofdorganisatie) beheert, in welk geval het als een externe gebruiker wordt weergegeven &#x20;
* Als de gebruiker nooit een account heeft aangemaakt &#x20;

## Foutmelding

Je krijgt een foutmelding van dit type:

<figure><img src="../../..gitbook/assets/image (1) (6).png" alt=""><figcaption></figcaption></figure>

1. Zorg ervoor dat je een geldig certificaat hebt.
2. Controleer of de kopie/paste van het certificaat geen regeleinden of spaties bevat.
