#Exercise 6 : Birthday And Minutes
"""
Instructions

Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

"""

from datetime import datetime

def minutes_lived(birthdate):
    # Convertir la date de naissance en objet datetime
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    # Obtenir l'heure actuelle
    now = datetime.now()
    
    # Calculer la différence entre la date actuelle et la date de naissance
    delta = now - birthdate
    
    # Convertir la différence en minutes
    minutes = delta.total_seconds() / 60
    
    # Afficher le message
    print(f"You have lived {int(minutes)} minutes so far.")

# Exemple d'appel de la fonction avec ma date de naissance 
minutes_lived("1997-12-11")
