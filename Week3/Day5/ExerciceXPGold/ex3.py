#Exercise 3 : Giphy API #2
"""
Instructions

Hint: For this exercise, You will work with this part of the documention
You will use this API KEY : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My

Create a small Python program which asks the user for a term or phrase and returns all the relevant gifs. (Example: all the “hilarious” gifs)
If the term or phrase doesn’t exist or if the user didn’t enter a correct term or phrase, return the trending gifs of the day and a message stating that you couldn’t find the requested term or phrase.
Note from the documentation : GIPHY Trending returns a list of the most relevant and engaging content each and every day.


###############################################################################################################

🧠 Objectif de l’exercice

Créer un programme Python qui :

Demande à l’utilisateur un mot ou une phrase à chercher.
Fait une requête à l’API Giphy pour obtenir les GIFs associés.
Si la recherche ne renvoie aucun résultat (ou que la saisie est vide), il doit :
Afficher les GIFs tendance du jour (via l’endpoint Trending).
Afficher un message disant qu’aucun GIF n’a été trouvé pour le terme demandé.


"""


import requests

# Clé API
API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"

# Fonction pour chercher des GIFs
def search_gifs(query):
    url = (
        f"https://api.giphy.com/v1/gifs/search"
        f"?q={query}"
        f"&api_key={API_KEY}"
        f"&limit=10"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        return None

# Fonction pour récupérer les GIFs tendances
def trending_gifs():
    url = f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        return None

# Fonction pour afficher les résultats
def show_gifs(gifs):
    for gif in gifs:
        print(f"- {gif['title']} : {gif['url']}")

# === Programme principal ===

user_input = input("Quel mot ou phrase veux-tu chercher sur Giphy ? ").strip()

# Si l'utilisateur a bien tapé quelque chose
if user_input:
    gifs = search_gifs(user_input)

    # S'il y a des résultats
    if gifs:
        if len(gifs) > 0:
            print(f"\n🎯 Voici les GIFs pour le terme : \"{user_input}\"\n")
            show_gifs(gifs)
        else:
            print(f"\n❌ Aucun résultat trouvé pour \"{user_input}\". Voici les GIFs tendances :\n")
            gifs = trending_gifs()
            show_gifs(gifs)
    else:
        print("❌ Une erreur s’est produite lors de la recherche.")
else:
    print("\n⚠️ Terme vide ! Voici les GIFs tendances :\n")
    gifs = trending_gifs()
    show_gifs(gifs)

