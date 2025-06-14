"""
Instructions

Using this REST Countries API(https://restcountries.com), create the functionality which will write 10 random countries to your database.

These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

"""

import sqlite3
import requests
import random

# Étape 1 : Créer la base de données et la table
def create_table():
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            capital TEXT,
            flag TEXT,
            subregion TEXT,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Étape 2 : Récupérer 10 pays aléatoires depuis l'API
def fetch_random_countries(n=10):
    url = 'https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    selected = random.sample(data, n)
    countries = []

    for country in selected:
        name = country.get('name', {}).get('common', 'Unknown')
        capital = country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A'
        flag = country.get('flags', {}).get('svg', '')
        subregion = country.get('subregion', 'N/A')
        population = country.get('population', 0)

        countries.append((name, capital, flag, subregion, population))

    return countries

# Étape 3 : Insérer les pays dans la base de données
def insert_countries(countries):
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM countries')  # Optionnel : vider la table
    cursor.executemany('''
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (?, ?, ?, ?, ?)
    ''', countries)

    conn.commit()
    conn.close()

# Étape 4 : Lancer le tout
if __name__ == '__main__':
    create_table()
    countries = fetch_random_countries()
    insert_countries(countries)
    print("✅ 10 pays insérés dans la base de données.")
