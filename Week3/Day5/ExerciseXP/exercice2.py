 #Exercise 2: Working With JSON
"""
Instructions

import json

sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}


Access the nested “salary” key from the JSON-string above.
Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
Save the dictionary as JSON to a file.
######################################################################################
🧠 Explication de l’exercice

Tu as une chaîne JSON imbriquée (sampleJson) que tu dois manipuler en Python :

🎯 Objectifs :
Extraire la valeur de la clé "salary"
Ajouter une nouvelle clé "birth_date" au même niveau que "name"
Enregistrer le tout dans un fichier JSON


"""

import json

# Ceci est bien une chaîne JSON, donc ok pour json.loads
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Convertir en dictionnaire Python
data = json.loads(sampleJson)  

# Ajouter la clé birth_date
data["company"]["employee"]["birth_date"] = "1990-01-01"

# Afficher le salaire
salary = data["company"]["employee"]["payable"]["salary"]
print("Salaire :", salary)

# Enregistrer dans un fichier JSON
with open("updated_data.json", "w") as f:
    json.dump(data, f, indent=4)

