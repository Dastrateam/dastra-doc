# Questions fréquentes

## Est ce que je peux faire un PIA sur plusieurs traitements ?&#x20;

Une analyse d'impact sur la protection des données peut porter sur un traitement ou un ensemble de traitements similaires. **Une seule et même AIPD peut être utilisée pour évaluer plusieurs opérations de traitement similaires en termes de nature, de portée, de contexte, de finalités et de risques.**

Par exemple :&#x20;

* des collectivités qui mettent chacune en place un système de vidéosurveillance similaire pourraient effectuer une seule analyse qui porterait sur ce système bien que celui-ci soit ultérieurement mis en œuvre par des responsables de traitements distincts ;
* un opérateur ferroviaire (responsable de traitement unique) pourrait effectuer une seule analyse d’impact sur le dispositif de la surveillance vidéo déployé dans plusieurs gares.

Dans Dastra, le modèle par défaut de PIA est rattaché à un seul traitement. **Il est possible de modifier le modèle que le PIA ne soit pas attaché à un traitement**. Dans ce cas, vous pouvez réaliser le PIA, l'exporter et le placer dans la documentation des traitements concernés. &#x20;

## Peut-on mettre en place un modèle de mail automatiquement à la création d'un audit ?

Vous pouvez créer un modèle de mail qui pourra être utilisé dans les invitations aux audits. Il n'est pas possible de réaliser des actions automatisées via les workflow par exemple. En effet, les audits ne peuvent pas être utilisés comme éléments déclencheurs.&#x20;

## En tant que répondant externe, est-ce que je peux mettre des images dans les réponses ?&#x20;

&#x20;Non, ce n'est pas possible. Cette possibilité est offerte si vous êtes un répondant interne (utilisateur de Dastra).

## Est-il possible de suggérer automatiquement une tâche à partir de  la réponse d'un questionnaire ?&#x20;

Oui, c'est possible depuis le type de question "texte long" en cochant la case "Suggérer automatiquement une tâche(s) à partir de la réponse".

## Est-il possible de publier un modèle de questionnaire pour tous les utilisateurs Dastra  ?&#x20;

Oui, c'est possible depuis le modèle de questionnaire en cliquant sur "Contribuer" :<br>

<div align="left"><figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-07-26 120545.png" alt=""><figcaption></figcaption></figure></div>

## A quoi correspondent les couleurs dans les réponses aux questionnaires ?

Dans les sections du questionnaire, des couleurs sont associées aux icones des questions.&#x20;

Voici la correspondance des couleurs :&#x20;

| Couleur                | Image                                                                         | Description                                                                             |
| ---------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Gris entouré de rouge  | ![](<../../.gitbook/assets/image (385).png>)                                  | Question obligatoire non répondue                                                       |
| Noir entouré de rouge  | ![](<../../.gitbook/assets/image (387).png>)                                  | Question obligatoire répondue                                                           |
| Gris                   | ![](<../../.gitbook/assets/image (388).png>)                                  | Question non obligatoire non répondue                                                   |
| Vert                   | ![](<../../.gitbook/assets/image (389).png>)                                  | Toutes les questions de la section ont un réponse. Question non obligatoire répondue    |
| Vert entouré de rouge  | <img src="../../.gitbook/assets/image (391).png" alt="" data-size="original"> | Toutes les questions de la section ont un réponse. Question obligatoire répondue        |
| Noir                   | <img src="../../.gitbook/assets/image (390).png" alt="" data-size="original"> | Question non obligatoire répondue. Il reste des questions sans réponse dans la section. |



### &#x20;Que faire lorsque l'on rencontre le message d'erreur "Error : there is a duplicate slug for the following questions" lors de l'enregistrement d'un questionnaire ? <a href="#slug-error" id="slug-error"></a>

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-11-04 170330.png" alt=""><figcaption></figcaption></figure>



\
Ce message signal qu'une ou plusieurs questions dans le questionnaire porte exactement le même "Nom de la variable"  ce qui crée l'erreur.&#x20;

<div align="left"><figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-11-04 163831.png" alt=""><figcaption></figcaption></figure></div>



Les questions ayant le même "Nom de la variable" sont identifiables grâce au message d'erreur "Le nom de la variable est présent dans une autre question" s'affichant au-dessus d'elles.

<div align="left"><figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-11-04 164534.png" alt=""><figcaption></figcaption></figure></div>



Pour résoudre ce problème, il faut donc modifier le "Nom de la variable" de chacune des questions ayant le même "Nom de la variable" de manière à la rendre unique pour chaque question, par exemple en ajoutant un \_ est un numéro incrémenté à la fin de chaque "Nom de la variable" .

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2024-11-04 165757.png" alt=""><figcaption></figcaption></figure>

Lorsque le questionnaire ne contiendra plus de "Nom de la variable" en doublon, il sera possible de l'enregistrer normalement. <br>

### &#x20;Que faire lorsque l'on rencontre le message "Bloqué car trop d'invitations" lors de l'envoi d'invitations par email aux répondants du questionnaire ?

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2026-02-05 091717.png" alt=""><figcaption></figcaption></figure>

\
Ce message apparait si 5 invitations par email ont déjà été envoyées à un répondant depuis le même questionnaire.\
\
Lorsque ce message apparait, vous pouvez encore inviter le répondant en lui transmettant le lien d'invitation au questionnaire disponible ici :&#x20;

<figure><img src="../../.gitbook/assets/Capture d&#x27;écran 2026-02-05 092802.png" alt=""><figcaption></figcaption></figure>
