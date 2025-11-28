---
description: >-
  Apprenez comment intégrer Dastra dans votre outil d'analyse de données préféré
  !
---

# Intégration dans les outils d'analyse de données (BI)



{% hint style="info" %}
Pour utiliser cette fonctionnalité, vous devez avoir dans votre souscription un abonnement avec le plan **Entreprise**
{% endhint %}

Dastra vous permettra très simplement d'importer [des rapports personnalisés](./) dans votre outil de BI préféré (Power BI, Google Looker, Tableau Software...). L'avantage d'utiliser cette fonctionnalité est que vous pouvez bénéficier de la puissance des outils de BI afin d'analyser en profondeur les données, tout en ayant des rapports qui se rafraîchissent automatiquement.<br>

### Mise en place dans Dastra

Rendez-vous dans le module des rapports personnalisés, accédez à l'un d'eux et cliquez sur le bouton "Intégrer à un outil BI".&#x20;



Une fenêtre modale s'ouvre, cliquez alors sur "Créer lien d'intégration".

**Copier alors le lien généré**



{% hint style="info" %}
Attention ! Ne transférez à personne le lien généré. Celui-ci permet d'accéder aux données brutes du rapport.&#x20;
{% endhint %}

## Mise en place dans l'outil BI :&#x20;

#### Microsoft Power BI

1. **Ouvrir Power BI Desktop :**
   * Lancez **Power BI Desktop** sur votre machine.
2. **Se connecter à la source de données Web :**
   * Dans Power BI Desktop, allez dans l'onglet **Accueil** (Home).
   * Cliquez sur **Obtenir des données** (Get Data), puis sélectionnez **Web**.
3. **Entrer l'URL du lien JSON :**
   * Dans la fenêtre **Obtenir des données Web** qui apparaît, entrez l'URL de votre fichier JSON ou de votre API (si vous avez un lien de partage JSON).
   * Assurez-vous que l'URL pointe vers un fichier JSON ou une API qui renvoie des données JSON.
   * Cliquez sur **OK**.
4. **Authentification (si nécessaire) :**
   * Si l'URL nécessite une authentification (par exemple, si elle est protégée par un mot de passe ou une clé API), Power BI vous demandera de vous connecter.
   * Sélectionnez le type d'authentification approprié (par exemple, **Anonyme**, **OAuth2**, **Clé API**, etc.) et entrez vos informations d'identification si nécessaire.
5. **Accéder aux données JSON :**
   * Power BI va se connecter à l'URL et récupérer le fichier JSON.
   * Une fois la connexion réussie, une fenêtre de prévisualisation des données JSON apparaîtra. Vous pourrez explorer les données sous forme de listes, objets ou tableaux imbriqués.

{% hint style="info" %}
* **Performance** : Si votre fichier JSON est volumineux ou contient des hiérarchies profondes, Power BI peut prendre un certain temps pour charger et transformer les données.
* **Rafraîchissement des données** : Si les données JSON sont mises à jour régulièrement (par exemple, par une API), vous pouvez configurer un **rafraîchissement des données** dans Power BI Service pour récupérer les dernières données automatiquement.
{% endhint %}



### Google Looker

Google Looker se connecte facilement à **Google BigQuery**, un entrepôt de données de Google Cloud qui peut stocker et traiter des fichiers JSON.

#### 1. **Utiliser un Google BigQuery comme source de données**

1. **Télécharger le fichier JSON sur Google Cloud Storage** :
   * Si votre fichier JSON est accessible via un lien de partage, commencez par télécharger le fichier sur **Google Cloud Storage**.
   * Rendez-le public ou configurez les permissions appropriées.
2. **Charger les données JSON dans BigQuery** :
   * Accédez à la console **Google Cloud Platform** (Google Cloud Console).
   * Allez dans **BigQuery** et choisissez ou créez un **projet**.
   * Dans **BigQuery**, sélectionnez votre **Dataset** (ensemble de données) et cliquez sur **Créer une table**.
   * Sélectionnez **Google Cloud Storage** comme source et entrez l'URL de votre fichier JSON dans le champ **URI**.
   * Configurez le format des données en **JSON** et assurez-vous que BigQuery peut correctement interpréter la structure de votre fichier.
3. **Connecter BigQuery à Looker** :
   * Une fois le fichier JSON chargé dans **BigQuery**, vous pouvez connecter **Looker** à BigQuery.
   * Dans Looker, allez dans **Admin** > **Connections** et ajoutez BigQuery comme source de données.
   * Une fois la connexion établie, vous pouvez interroger les données de BigQuery directement dans Looker et les visualiser.

#### 2. **Utiliser des outils ETL pour intégrer JSON dans Looker**

Si vous avez besoin d'automatiser l'intégration de données JSON depuis une API ou un fichier externe dans Looker, vous pouvez utiliser des outils **ETL** (Extract, Transform, Load) comme **Fivetran**, **Stitch**, ou **Airflow**. Ces outils peuvent extraire les données JSON, les transformer et les charger dans un entrepôt de données compatible avec Looker.

**Exemple avec Fivetran :**

1. **Connectez une API REST ou une source JSON dans Fivetran**.
2. **Transformez les données** pour qu'elles correspondent aux exigences de votre entrepôt de données.
3. **Chargez les données dans l'entrepôt** (par exemple, BigQuery).
4. **Connectez Looker à cet entrepôt de données** pour commencer à interroger et visualiser les données.



### Tableau Software

\
**1. Ouvrir Tableau Desktop :**

* Lancez **Tableau Desktop** sur votre machine.

**2. Se connecter à une source de données Web :**

* Dans **Tableau Desktop**, allez dans le menu **Fichier** et sélectionnez **Nouvelle source de données**.
* Dans la fenêtre de sélection des sources de données, cliquez sur **Web Data Connector**. Cette option permet de se connecter à des données à partir de diverses sources web, y compris des fichiers JSON via une API ou une URL.

**3. Entrer l'URL JSON :**

* Vous devrez entrer l'URL du fichier JSON ou de l'API dans la fenêtre qui apparaît.

**4. Authentification (si nécessaire) :**

* Si l'URL JSON nécessite une forme d'authentification (par exemple une clé API, un jeton OAuth, ou des identifiants de connexion), Tableau vous demandera les informations d'identification pour y accéder.
* Sélectionnez le type d'authentification approprié (par exemple, **Clé API** ou **OAuth**) et entrez les informations nécessaires.

**5. Analyser les données JSON dans Tableau :**

* Tableau va se connecter à l'URL, télécharger le fichier JSON et tenter de le convertir en un format tabulaire compréhensible (une table ou une vue de données structurées).
* Tableau peut automatiquement détecter la structure des données JSON, mais dans certains cas, si le fichier est très complexe ou imbriqué, vous devrez peut-être effectuer des ajustements dans **l'éditeur de données** pour aplatir ou transformer les données dans un format approprié.

{% hint style="info" %}
- **Limites du fichier JSON :** Si votre fichier JSON est volumineux ou très imbriqué, Tableau peut avoir des difficultés à l'analyser correctement. Parfois, il peut être nécessaire de le transformer ou de le simplifier avant de l'intégrer.
- **Authentification et sécurité :** Si votre lien JSON nécessite une clé API, assurez-vous de bien gérer les autorisations et les informations d'identification. Certaines API peuvent avoir des limitations sur le nombre de requêtes ou nécessiter des autorisations spécifiques.
- **Rafraîchissement des données :** Si les données JSON changent régulièrement (par exemple, via une API qui fournit des mises à jour en temps réel), vous pouvez configurer Tableau pour **rafraîchir automatiquement les données** à intervalles réguliers, afin de garder vos rapports à jour.
{% endhint %}
