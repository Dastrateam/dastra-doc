---
description: >-
  Connectez vos rapports personnalisés Dastra à Power BI, Google Looker ou
  Tableau, avec des données rafraîchies automatiquement.
---

# Intégration dans les outils d'analyse de données (BI)

{% hint style="info" %}
Pour utiliser cette fonctionnalité, votre abonnement doit inclure le plan **Entreprise** et vous devez disposer de la permission **Configuration avancée**.
{% endhint %}

Dastra permet d'importer [des rapports personnalisés](README.md) dans votre outil de BI (Power BI, Google Looker, Tableau Software, etc.). Vous analysez les données en profondeur avec votre outil, et les rapports se rafraîchissent automatiquement.

## Mise en place dans Dastra

1. Dans le module **Rapports personnalisés**, ouvrez un rapport et cliquez sur **Connecter outils BI**.
2. Dans la fenêtre qui s'ouvre, cliquez sur **Créer lien de connexion**. Le lien est copié dans votre presse-papiers.

La fenêtre affiche ensuite deux onglets, selon la façon dont votre outil se connecte :

* **Lien** : l'adresse publique du rapport, à coller dans l'outil. Toute personne qui possède ce lien accède aux données brutes du rapport.
* **Authentification (Bearer)** : l'**Url du service** et le **Jeton d'Authentification** à renseigner séparément. Votre outil envoie le jeton dans l'en-tête HTTP `Authorization: Bearer <jeton>`. Préférez cet onglet lorsque votre outil sait ajouter un en-tête : l'adresse seule ne donne alors pas accès aux données.

<figure><img src="../../.gitbook/assets/reports-bi-tools-1.png" alt="La fenêtre de connexion aux outils BI avec les onglets Lien et Authentification (Bearer)"><figcaption><p>La fenêtre de connexion aux outils BI</p></figcaption></figure>

{% hint style="warning" %}
Ne transmettez ni le lien ni le jeton à quiconque n'a pas à voir les données du rapport.
{% endhint %}

Pour couper l'accès, cliquez sur **Supprimer connexion** dans la même fenêtre, puis confirmez. Le lien et le jeton cessent de fonctionner : vous pouvez créer une nouvelle connexion avec **Créer lien de connexion**.

## Mise en place dans l'outil BI

### Microsoft Power BI

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
   * Avec le lien de l'onglet **Lien**, aucune authentification n'est nécessaire : sélectionnez **Anonyme**.
   * Avec l'onglet **Authentification (Bearer)**, saisissez l'**Url du service** à l'étape 3, puis cliquez sur **Avancé** et ajoutez, dans les paramètres d'en-tête de requête HTTP, l'en-tête `Authorization` avec la valeur `Bearer ` suivie du jeton. Sélectionnez ensuite **Anonyme**.
5. **Accéder aux données JSON :**
   * Power BI va se connecter à l'URL et récupérer le fichier JSON.
   * Une fois la connexion réussie, une fenêtre de prévisualisation des données JSON apparaîtra. Vous pourrez explorer les données sous forme de listes, objets ou tableaux imbriqués.

{% hint style="info" %}
* **Performance** : Si votre fichier JSON est volumineux ou contient des hiérarchies profondes, Power BI peut prendre un certain temps pour charger et transformer les données.
* **Rafraîchissement des données** : Si les données JSON sont mises à jour régulièrement (par exemple, par une API), vous pouvez configurer un **rafraîchissement des données** dans Power BI Service pour récupérer les dernières données automatiquement.
{% endhint %}

### Google Looker

Google Looker se connecte à **Google BigQuery**, un entrepôt de données de Google Cloud qui peut stocker et traiter des fichiers JSON.

#### 1. **Utiliser un Google BigQuery comme source de données**

1. **Télécharger le fichier JSON sur Google Cloud Storage** :
   * Si votre fichier JSON est accessible via un lien de partage, commencez par télécharger le fichier sur **Google Cloud Storage**.
   * Rendez-le public ou configurez les permissions appropriées.
2. **Charger les données JSON dans BigQuery** :
   * Accédez à la console **Google Cloud Platform** (Google Cloud Console).
   * Allez dans **BigQuery** et choisissez ou créez un **projet**.
   * Dans **BigQuery**, sélectionnez votre **Dataset** (ensemble de données) et cliquez sur **Créer une table**.
   * Sélectionnez **Google Cloud Storage** comme source et entrez l'URL de votre fichier JSON dans le champ **URI**.
   * Configurez le format des données en **JSON** et assurez-vous que BigQuery peut correctement interpréter la structure de votre fichier.
3. **Connecter BigQuery à Looker** :
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
* Dans la fenêtre de sélection des sources de données, cliquez sur **Web Data Connector**. Cette option se connecte à des données de diverses sources web, y compris des fichiers JSON via une API ou une URL.

**3. Entrer l'URL JSON :**

* Vous devrez entrer l'URL du fichier JSON ou de l'API dans la fenêtre qui apparaît.

**4. Authentification (si nécessaire) :**

* Avec le lien de l'onglet **Lien**, aucune authentification n'est nécessaire.
* Si votre connecteur permet d'ajouter un en-tête HTTP, utilisez l'onglet **Authentification (Bearer)** : renseignez l'**Url du service** et l'en-tête `Authorization: Bearer <jeton>`.

**5. Analyser les données JSON dans Tableau :**

* Tableau va se connecter à l'URL, télécharger le fichier JSON et tenter de le convertir en un format tabulaire compréhensible (une table ou une vue de données structurées).
* Tableau peut automatiquement détecter la structure des données JSON, mais dans certains cas, si le fichier est très complexe ou imbriqué, vous devrez peut-être effectuer des ajustements dans **l'éditeur de données** pour aplatir ou transformer les données dans un format approprié.

{% hint style="info" %}
- **Limites du fichier JSON :** Si votre fichier JSON est volumineux ou très imbriqué, Tableau peut avoir des difficultés à l'analyser correctement. Parfois, il peut être nécessaire de le transformer ou de le simplifier avant de l'intégrer.
- **Authentification et sécurité :** Si votre lien JSON nécessite une clé d'API, assurez-vous de bien gérer les autorisations et les informations d'identification. Certaines API peuvent avoir des limitations sur le nombre de requêtes ou nécessiter des autorisations spécifiques.
- **Rafraîchissement des données :** Si les données JSON changent régulièrement (par exemple, via une API qui fournit des mises à jour en temps réel), vous pouvez configurer Tableau pour **rafraîchir automatiquement les données** à intervalles réguliers pour garder vos rapports à jour.
{% endhint %}
