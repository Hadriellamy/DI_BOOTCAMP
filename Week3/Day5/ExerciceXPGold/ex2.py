#Exercise 2 : Giphy API #1
"""
Instruction

Hint: For this exercise, check out the documentation of the Giphy API

You will work with this part of the documention

You will use this Gif URL: https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
Explanation of the Gif URL

q Request Paramater: Search query term or phrase. We are searching for “hilarious” gifs

rating Request Paramater: Filters results by specified rating. We are searching for Level 1 gifs. Check out the ratings documentation

api_key Request Paramater : GIPHY API Key. Our API KEY is hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
Fetch the giphs from the Gif URL provided above.

Use f-strings and variables to build the URL string we’re using for the fetch.
If the status code is 200 return the result as a JSON object.
Only return gifs which have a height bigger then 100.
Return the length of the object you received in the previous question.
Only return the first 10 gifs. Hint: In the Giphy Documentation, check out the relevant Request Parameters.
############################################################################################################################################################
🧠 Explication de l’exercice :

Tu vas interagir avec l’API publique de Giphy, un moteur de recherche de GIFs animés.

✅ Objectifs :
Envoyer une requête GET à l’API Giphy avec des paramètres spécifiques (recherche du mot "hilarious", classement "g", et une clé API donnée).
Construire dynamiquement l’URL avec des f-strings et des variables.
Vérifier le statut de la réponse (200 signifie succès).
Filtrer les GIFs : ne garder que ceux avec une hauteur > 100 pixels.
Afficher la longueur de la liste filtrée.
Limiter le nombre de GIFs à 10 au maximum, en utilisant les paramètres de l’API pour cela.
"""


import requests

# Paramètres de recherche
search_query = "hilarious"
rating = "g"
api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
limit = 10

# Construction de l'URL avec f-strings
url = (
    f"https://api.giphy.com/v1/gifs/search"
    f"?q={search_query}"
    f"&rating={rating}"
    f"&api_key={api_key}"
    f"&limit={limit}"
)

# Envoi de la requête GET
response = requests.get(url)

# Vérifie si la requête est réussie
if response.status_code == 200:
    data = response.json()  # Convertit la réponse JSON en dictionnaire Python

    # Filtrer les gifs avec une hauteur > 100 pixels
    filtered_gifs = [
        gif for gif in data["data"]
        if int(gif["images"]["original"]["height"]) > 100
    ]

    # Afficher la longueur de la liste filtrée
    print(f"Nombre de GIFs avec hauteur > 100 : {len(filtered_gifs)}")

    # Afficher les 10 premiers GIFs filtrés (peut être moins si filtre en supprime)
    print("Voici les GIFs filtrés (max 10) :\n")
    for gif in filtered_gifs[:10]:
        print(f"- {gif['title']} : {gif['url']}")

else:
    print(f"Erreur dans la requête. Code: {response.status_code}")




#Explication 
"""
🧪 Ce que fait le code :

Il envoie une requête vers l’API de Giphy.
Il récupère une liste de GIFs correspondant au mot-clé "hilarious".
Il filtre cette liste pour ne garder que les GIFs dont la hauteur dépasse 100 pixels.
Il affiche :
Le nombre de GIFs filtrés.
Jusqu’à 10 GIFs maximum, en imprimant leur titre et leur URL.


🧩 Paramètre limit=10 :

Le paramètre limit est directement pris en charge par l’API Giphy. Il indique que tu ne veux que 10 résultats maximum. Cela évite de récupérer inutilement trop de données.
"""

