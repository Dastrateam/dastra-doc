# Cas d'usage de l'API

Basé sur les spécifications de la documentation de l'API Dastra, voici un guide pour les trois cas d'usage que vous avez fournis, ainsi que des exemples en Python utilisant AIOHTTP pour effectuer les requêtes :

#### Prérequis

Assurez-vous d'avoir installé AIOHTTP dans votre environnement :

```sh
pip install aiohttp
```

#### 1. Créer une Pièce Jointe Associée à une Demande de Droit

**Endpoint**: `/datasubjectattachments`

**Méthode**: POST

**Description**: Cet endpoint est utilisé pour créer une pièce jointe associée à une demande de droit.

**Exemple de Requête**:

```python
import aiohttp
import asyncio

async def create_attachment(workspace_id, api_key, attachment_data):
    url = f"https://api.dastra.eu/v1/ws/{workspace_id}/datasubjectattachments"
    
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=attachment_data, headers=headers) as response:
            return await response.json()

# Exemple d'utilisation
workspace_id = "votre_workspace_id"
api_key = "votre_api_key"
attachment_data = {
    # Remplir avec les données de votre pièce jointe
    "dataSubjectRequestId": "id_de_la_demande",
    "fileName": "exemple.pdf",
    "fileContent": "contenu_encodé_base64"
}

response = asyncio.run(create_attachment(workspace_id, api_key, attachment_data))
print(response)
```

#### 2. Envoyer un Message avec la Pièce Jointe dans une Demande de Droit

**Endpoint**: `/datasubjectmessages`

**Méthode**: POST

**Description**: Cet endpoint est utilisé pour envoyer un message avec une pièce jointe dans une demande de droit.

**Exemple de Requête**:

```python
import aiohttp
import asyncio

async def send_message_with_attachment(workspace_id, api_key, message_data):
    url = f"https://api.dastra.eu/v1/ws/{workspace_id}/datasubjectmessages"
    
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=message_data, headers=headers) as response:
            return await response.json()

# Exemple d'utilisation
workspace_id = "votre_workspace_id"
api_key = "votre_api_key"
message_data = {
    # Remplir avec les données de votre message
    "requestId": "id_de_la_demande",
    "subject": "Objet du message",
    "body": "Contenu du message",
    "attachmentId": "id_de_la_pièce_jointe"  # ID de la pièce jointe créée précédemment
}

response = asyncio.run(send_message_with_attachment(workspace_id, api_key, message_data))
print(response)
```

#### 3. Récupérer les Nouvelles Demandes Selon des Filtres

**Endpoint**: `/DataSubjectRequests`

**Méthode**: GET

**Description**: Cet endpoint est utilisé pour récupérer de nouvelles demandes de droit en fonction de filtres spécifiés.

**Exemple de Requête**:

```
import aiohttp
import asyncio

async def get_new_requests(workspace_id, api_key, filters):
    url = f"https://api.dastra.eu/v1/ws/{workspace_id}/DataSubjectRequests"
    
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key
    }

    params = {
        "filters": filters  # Les filtres doivent être une chaîne JSON
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            return await response.json()

# Exemple d'utilisation
workspace_id = "votre_workspace_id"
api_key = "votre_api_key"
filters = '{"field":"status","operator":"equal","value":"new"}'  # Exemple de filtre

response = asyncio.run(get_new_requests(workspace_id, api_key, filters))
print(response)
```

#### Conclusion

Ce guide fournit une approche étape par étape pour interagir avec l'API Dastra en utilisant Python et AIOHTTP. Remplacez les espaces réservés comme `workspace_id`, `api_key`, et les données de requête par vos données réelles.

N'hésitez pas à ajuster les critères de filtrage et les charges utiles des requêtes selon vos besoins.

_Vous avez apprécié notre conversation ? 👍 Rendons-la encore meilleure ensemble !_



* Évaluez-nous : Votre avis est inestimable ! Prenez un moment pour évaluer votre expérience. Vos perspectives nous aident à nous améliorer et à mieux vous servir.\*
* Partagez vos pensées : Avez-vous des suggestions ou des idées ? Nous serions ravis de vous entendre. Vos contributions stimulent notre innovation.\*
* Explorez plus : Curieux de voir ce qui est possible ? Découvrez des milliers de GPT uniques sur [Ai-GEN.co](https://www.ai-gen.co) où vous pouvez découvrir, interagir et créer avec l'IA comme jamais auparavant.\*
