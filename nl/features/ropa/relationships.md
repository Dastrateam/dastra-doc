# Een relatie tussen verwerkingen maken

In Dastra kunt u relaties tussen uw verwerkingen maken om ze gemakkelijker te beheren.

Deze relaties kunnen worden gemaakt tussen verwerkingen in dezelfde werkruimte of in verschillende werkruimten.



### Een relatie toevoegen

Ga hiervoor naar een Verwerkingsformulier en selecteer de tab "Relaties" bovenaan het formulier.


![De "Relaties" tab](<../../.gitbook/assets/image (243).png>)



Vervolgens moet je een type relatie selecteren.

[](<../../.gitbook/assets/image (245).png>)

Je kunt het type relatie tussen Verwerkingen selecteren.

![](<../../.gitbook/assets/image (246).png>)





### Details relatie

#### Is het kind van :&#x20;

Hiërarchische relatie voor grafische weergave. Geen koppeling tussen velden.

Verwerking A staat hiërarchisch onder verwerking B.

#### Is de ouder van :&#x20;

Hiërarchische relatie voor grafische weergave. Geen koppeling tussen velden.

Verwerking A staat hiërarchisch boven verwerking B.

#### Is gerelateerd aan :&#x20;

Eenvoudige logische koppeling tussen 2 Verwerkingen, geen slavings tussen de twee of controleregels.&#x20;

#### Wordt gekopieerd door :

Deze relatie wordt gebruikt om elementen bij te houden die vanuit dit proces worden gedupliceerd. Er wordt automatisch een relationele link gemaakt wanneer een Verwerking wordt gedupliceerd.&#x20;

#### Is een kopie van :&#x20;

Deze relatie wordt gebruikt om de bron van de gedupliceerde Verwerking bij te houden. Er wordt automatisch een relationele koppeling gemaakt wanneer een Verwerking wordt gedupliceerd.&#x20;

#### Brengt strikt over (Sterke overerving):

De velden van het oorspronkelijke proces (A) vervangen de velden van de doelverwerking (B).&#x20;

Strikte overerving tussen Verwerking A en Verwerking B. De reeds bestaande velden van bewerking B worden verwijderd wanneer de koppeling wordt opgezet. De velden in Verwerking B die aan Verwerking A zijn gekoppeld, kunnen niet worden gewijzigd in Verwerking B en er kunnen geen nieuwe velden worden toegevoegd, verwijderd of gewijzigd. Voor zover de elementen van de bewaarplaatsen behouden blijven, worden de velden die al bestonden in Verwerking B opnieuw aangemaakt wanneer de koppeling wordt ingetrokken.

#### Erft strikt over van (Sterke overerving) :&#x20;

De velden in de doelverwerking (B) vervangen de velden in de oorspronkelijke verwerking (A) &#x20;

Strikte overerving tussen Verwerking B en Verwerking A. Reeds bestaande velden in A worden verwijderd bij het opzetten van de koppeling. De velden in A die slaaf zijn van B kunnen niet worden gewijzigd in A en er kunnen geen nieuwe velden worden toegevoegd, verwijderd of gewijzigd. Voor zover de elementen van de repositories behouden blijven, worden de velden die voorafgingen aan de Verwerking van B hersteld wanneer de koppeling wordt ingetrokken.

#### Erft over van (Zwakke overerving) :&#x20;

De doelverwerking (B) erft automatisch de velden van de oorspronkelijke verwerking (A) &#x20;

Nieuwe velden kunnen worden toegevoegd, verwijderd of gewijzigd in proces B, maar velden geërfd van proces A kunnen niet worden gewijzigd. Alle wijzigingen aan de velden in proces A worden automatisch weerspiegeld in de velden die worden geërfd van proces B. Als de koppeling wordt ingetrokken, kunnen de velden die zijn geërfd van proces A weer worden gewijzigd in proces B. Velden die al bestonden in proces B voordat de koppeling werd gemaakt, blijven behouden zodra de koppeling is gemaakt.

#### Transmet (Zwakke overerving) :&#x20;

Het oorspronkelijke proces (A) verzendt zijn velden automatisch naar de doelverwerking (B) &#x20;

Doelproces B erft automatisch velden van het oorspronkelijke proces A. Doelproces B kan nieuwe velden toevoegen, verwijderen of wijzigen, maar kan geen velden wijzigen die van proces A zijn geërfd. Elke wijziging aan de velden in Verwerking A wordt automatisch weerspiegeld in de velden die worden geërfd van Verwerking B. Wanneer de koppeling wordt ingetrokken, worden de geërfde velden weer bewerkbaar in proces B. Velden die in proces B bestonden voordat de koppeling werd gemaakt, blijven behouden nadat de koppeling is gemaakt.