# Questions fréquentes

## Pourquoi le menu Gestion des risques n'apparaît-il pas ?

Le module doit être activé pour votre espace de travail, et votre rôle doit comprendre le droit de lecture sur les risques. Créer ou modifier un risque demande le droit d'écriture. Contactez l'administrateur de votre espace de travail.

## Pourquoi ne puis-je pas faire passer un risque à l'étape suivante ?

Seul le propriétaire d'un risque peut changer son état : valider l'évaluation, valider la réponse, archiver ou revenir à une étape précédente. Son nom est indiqué dans la section **Identification** du risque. Pour confier le risque à une autre personne, changez le **Propriétaire du risque** dans cette section.

## Quelle est la différence entre risque initial, résiduel et courant ?

Le risque initial est le risque avant toute mesure de maîtrise. Le risque résiduel est celui que vous visez une fois les mesures en place. Le risque courant se situe entre les deux, selon le taux de remédiation de vos points de contrôle. Les formules figurent dans le [glossaire](glossary.md).

## Pourquoi mon risque courant ne change-t-il pas malgré mes points de contrôle ?

Vérifiez les points suivants :

* l'option de traitement est **Réduction et contrôles** : les autres options ne calculent pas de remédiation ;
* le risque a un niveau initial et un niveau résiduel ;
* des points de contrôle sont attribués au type de risque et ont reçu une réponse. Un point de contrôle sans réponse compte zéro point ;
* les réponses ne sont pas toutes **Non applicable** : ces réponses sont exclues du calcul.

## Que se passe-t-il si je change d'échelle de risques ?

Activer une autre échelle modifie les statistiques de tous les risques de l'espace de travail, et Dastra demande une confirmation avant de le faire. Choisissez votre échelle avant de saisir vos premiers risques. Voir [Configurer l'échelle de risques](process/assess.md#configurer-lechelle-de-risques).

## Comment évaluer le même risque sur plusieurs traitements ou actifs ?

Utilisez la **Création de risques en masse** : sélectionnez le type de risque et tous les objets concernés, et Dastra crée un risque par objet. Voir [Gestion des risques](README.md).
