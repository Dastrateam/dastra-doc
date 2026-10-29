# Filerskeepers

## Over Filerskeepers

[Filerskeepers](https://www.filerskeepers.co/) is een dienst die kant-en-klare bewaartermijnschema's levert, met de wettelijke bewaarvereisten uit de hele wereld.\
De dienst helpt bedrijven te bepalen hoe lang ze elk type gegevens moeten bewaren of wissen om aan de toepasselijke regelgeving te voldoen.

### Vereisten

* Een betaalde Dastra-licentie.
* Een Filerskeepers-account. Hebt u er nog geen en bent u al klant van Dastra, dan kunt u [contact opnemen met ons verkoopteam](https://meetings-eu1.hubspot.com/yann-forveille/rendez-vous-avec-un-expert?message=Filerskeepers+Integration), dat u een voordelig tarief kan aanbieden.
* Een in de Filerskeepers-software ingestelde repository met bewaartermijnen (een "Schedule"). De integratie heeft deze repository nodig om toegang te krijgen tot uw cataloggegevens.

### Installatie

* Ga naar de Filerskeepers-integratiepagina in de integratiemarktplaats van Dastra:\
  [https://app.dastra.eu/workspace/0/settings/integrations/filerskeepers](https://app.dastra.eu/workspace/0/settings/integrations/filerskeepers)
* Klik op de knop **Integratie toevoegen**.
* Voer de inloggegevens van uw Filerskeepers-beheerdersaccount in (e-mailadres en wachtwoord). Met deze gegevens kunnen wij een toegangstoken voor de Filerskeepers-API aanmaken.
* Er verschijnt een configuratievenster. Deze configuratie is nodig om de installatie af te ronden. Selecteer in het formulier de "Schedule" die u met Dastra wilt configureren.

### Configuratie

* Selecteer de Filerskeepers-repository die u met Dastra wilt synchroniseren.
* Kies of u de bewaartermijnen automatisch wilt synchroniseren. (Datasets die met Filerskeepers zijn gesynchroniseerd, worden elke nacht om 00:00 UTC bijgewerkt.)
* Selecteer de personen die een melding moeten krijgen bij wijzigingen of nieuwe bewaartermijnen in de datasets. De geselecteerde persoon ontvangt een e-mail met details over de bijgewerkte datasets.
* Als u **Creëer gegevenssets als ze niet gesynchroniseerd zijn** aanvinkt, wordt voor elk gegevenstype dat in uw Filerskeepers-account is gedeclareerd een dataset aangemaakt.

{% hint style="info" %}
Let op: als u dit vakje aanvinkt, worden er automatisch veel datasets in uw werkruimte aangemaakt.
{% endhint %}

### De bewaartermijn selecteren

De Filerskeepers-connector biedt meerdere werkwijzen:

* Weergave van de keuzelijst voor bewaartermijnen op basis van uw Filerskeepers-repository met bewaartermijnen (in de software een "Schedule" genoemd).

Wanneer u vanaf nu in Dastra een dataset opent, verschijnt in de sectie **Bewaartermijnen** een knop om een bewaartermijn te selecteren: **Vul in met Filerskeepers**.

Met deze knop selecteert u rechtstreeks een dataset uit uw Filerskeepers-repository. Deze bewaartermijn wordt automatisch met Dastra gesynchroniseerd als u die optie in de integratieconfiguratie hebt ingeschakeld.

Selecteer een dataset met de knop **Selecteer**.

Zodra u de bewaartermijn hebt geselecteerd, sluit het venster en worden de details van de bewaartermijn getoond.

{% hint style="info" %}
Alleen bewaartermijnen die bij actieve gegevensopslag horen, worden gesynchroniseerd.
{% endhint %}

### Gegevenssynchronisatie tussen Dastra en Filerskeepers

Een aantal velden uit Filerskeepers wordt automatisch aan uw bewaartermijn gekoppeld:

* de bewaarduur (vanaf)
* de beschrijving van het bewaarbeleid
* de juridische motivering, de link en het rechtsgebied, die samen in het veld voor de motivering worden gezet
