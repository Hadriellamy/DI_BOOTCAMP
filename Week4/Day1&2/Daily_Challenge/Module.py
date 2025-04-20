#Instructions :
"""
Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
Test your code with multiple sites such as google, ynet, imdb, etc.
##################################################################

Objectif
Nous voulons mesurer le temps qu'il faut pour charger une page web en utilisant deux modules Python : requests pour envoyer une requête HTTP et time pour mesurer la durée de cette requête.

Étapes :
Fonction measure_load_time(url) :
Entrée : un URL sous forme de chaîne de caractères (par exemple, "https://www.google.com").
Sortie : le temps qu'il a fallu pour charger la page, en secondes.
Mesure du temps :
Avant d'envoyer la requête HTTP avec requests.get(url), nous capturons l'heure actuelle avec time.time() (qui retourne le nombre de secondes depuis le 1er janvier 1970, au format flottant).
Après avoir envoyé la requête et récupéré la réponse du serveur, nous capturons à nouveau l'heure actuelle.
La différence entre l'heure à la fin et l'heure au début nous donne le temps que cela a pris pour charger la page.
Exécution de tests :
Nous testons cette fonction avec plusieurs sites web comme google.com, ynet.co.il et imdb.com.
Pour chaque site, nous appelons la fonction measure_load_time() et affichons le temps qu'il a fallu pour charger la page.

"""

import requests
import time

def measure_load_time(url):
    """Returns the time it takes to load a webpage in seconds."""
    start_time = time.time()  # Record the start time
    response = requests.get(url)  # Send GET request to the URL
    end_time = time.time()  # Record the end time

    load_time = end_time - start_time  # Calculate the load time
    return load_time

# Test the function with multiple websites
websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for site in websites:
    load_time = measure_load_time(site)
    print(f"Time to load {site}: {load_time:.4f} seconds")



#Explications 
"""
Explication du code :
measure_load_time(url) :
La fonction prend une URL (l'adresse du site à tester) en argument.
Elle envoie une requête GET à ce site, et mesure combien de temps il faut pour obtenir une réponse.
La durée est calculée en soustrayant l'heure de début (avant la requête) de l'heure de fin (après la réponse).
Test de la fonction :
Nous testons la fonction avec une liste de sites : google.com, ynet.co.il, et imdb.com.
Pour chaque site, nous affichons le temps qu'il a fallu pour le charger, en secondes.

Exemple de sortie :
Temps pour charger https://www.google.com: 0.1573 secondes
Temps pour charger https://www.ynet.co.il: 0.3012 secondes
Temps pour charger https://www.imdb.com: 0.8765 secondes

"""