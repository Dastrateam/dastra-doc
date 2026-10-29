# Glossaire

Voici les termes utilisés dans le module de gestion des risques.

* **Vraisemblance (probabilité) :** évaluation de la fréquence d'occurrence d'un risque. C'est un score évalué de manière empirique, de 1 à 5 avec l'échelle par défaut. Chaque niveau correspond à une fréquence d'apparition du risque. L'application l'affiche sous le libellé **Vraisemblance**.
* **Gravité (impact) :** évaluation de la conséquence d'un évènement redouté sur l'organisation. L'application l'affiche sous le libellé **Gravité**.
* **Risque initial (ou inhérent) :** risque théorique lié à l'activité, avant toute mesure de maîtrise (contrôle interne). Il se calcule en multipliant l'impact initial par la probabilité initiale.
* **Risque résiduel :** risque subsistant après la mise en œuvre des dispositifs de maîtrise (contrôle interne). Il se calcule en multipliant l'impact résiduel par la probabilité résiduelle.
* **Risque courant :** niveau de risque à l'instant T, en fonction du niveau de remédiation de vos points de contrôle. Il se calcule ainsi : {Risque courant} = {Risque initial} - ({Risque initial} - {Risque résiduel}) \* {Taux de remédiation du risque}. Sans réponse aux points de contrôle, le risque courant est égal au risque initial.
* **Évènement redouté :** évènement incertain que l'on caractérise par sa fréquence et sa gravité. C'est la conséquence de l'occurrence d'un risque.
* **Type de risque :** regroupe un évènement redouté, ses menaces, ses sources, ses points de contrôle et une pré-évaluation. Il se réutilise sur autant d'objets que nécessaire.
* **Risque :** combinaison d'un type de risque et de son évaluation (impact et probabilité) sur un objet : unité organisationnelle, traitement, acteur (par exemple un sous-traitant), actif ou système d'IA. Les menaces (les évènements à l'origine de l'évènement redouté) et les sources (qui ou quoi peut les provoquer) complètent la description.
* **Point de contrôle :** (ou dispositif de management des risques). Respecter les points de contrôle est le moyen de ramener le risque courant vers le risque résiduel. Dans Dastra, la liste des points de contrôle est rattachée au type de risque.
* **Remédiation (taux de remédiation) :** part des mesures de contrôle effectivement en place pour un risque. Il se calcule ainsi : somme des points de la réponse en cours de chaque point de contrôle, divisée par la somme des points maximum de chaque point de contrôle, arrondie au pourcentage supérieur. Les réponses **Non applicable** sont exclues du calcul ; un point de contrôle sans réponse compte zéro point. Par exemple, avec trois points de contrôle dont les réponses ne valent que 0 ou 1 point, deux points de contrôle conformes sur trois donnent 67 % de remédiation.
