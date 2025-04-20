"""
What You Will Learn

Python functions, loops, conditionals
Python Modules


Building A Weather App

The current weather data can be retrieved from OpenWeatherMap using the Observation module in PyOWM (Python OpenWeatherMap).
Use this documentation for this Mini Project.

Get the current weather in Tel Aviv.
Get current wind info of Tel Aviv.
Get today’s sunrise and sunset times of Tel Aviv.
Display all these information in a user friendly way.

Recreate these steps, but this time, ask the user for a location (display the information in a user friendly way).
Instead of working with the name of the city, retrieve the id of the city.
Check out the documentation section : “Identifying cities and places via city IDs”.

Retrieve weather forecasts : The OpenWeatherMap free tier gives you access to 5 day forecasts. The forecasts contain the weather data in three-hour intervals.
The methods for retrieving the forecast are:
forecast_at_place('Los Angeles, US', '3h')
forecast_at_id(5391959, '3h')
forecast_at_coords(lat=37.774929, lon=-122.419418, interval='3h')
Forecasts are useful if you want to know what the weather conditions will be throughout the day/week.

Use this API to retrieve the Air Pollution in a specific city.
Mini Project : XP Ninja

BONUS: Your goal is to produce a weather GUI that shows the three-day humidity forecast for a city of your choice.
If you’ve never built a GUI with Python, don’t worry! We’ll be going through step by step how to build it. We will be using Matplotlib to
plot the weather data. Matplotlib uses Tkinter behind the scenes to display the interactive GUI.



You have to reproduce this bar chart:





You will have to use :

the matplotlib module for the bar chart
the pytz and datetime module for the date
the pyowm module for the weather


Instructions:

Start by updating the values for the ylabel and title by creating a function called init_plot().
Create a function called plot_temperatures() to determine the details of the bar chart.
Create a function called write_humidity_on_bar_chart() to display the % humidity in the bar chart.
Style the bar chart

###########################################

🧰 Prérequis à installer
Assure-toi d’avoir installé les bibliothèques nécessaires :

pip install pyowm matplotlib pytz
🧠 Organisation du code

On va diviser le projet en plusieurs étapes :

Récupérer les infos météo avec PyOWM
Afficher les infos météo basiques (vent, lever/coucher du soleil)
Afficher la prévision d’humidité sur 3 jours dans un graphique
Créer une interface utilisateur simple (via Matplotlib GUI)


"""

import matplotlib.pyplot as plt
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils.timestamps import tomorrow
from datetime import datetime
import pytz

API_KEY = 'ed8620e8f02c4c81a5e37c697f64688e'  

# Initialisation de l’API OWM
config_dict = get_default_config()
config_dict['language'] = 'en'
owm = OWM(API_KEY, config_dict)
mgr = owm.weather_manager()

def get_forecast(city_name):
    forecast = mgr.forecast_at_place(city_name, '3h').forecast
    humidity_data = {}

    for weather in forecast:
        time = weather.reference_time(timeformat='date')
        date = time.date()
        if len(humidity_data) < 3:
            if date not in humidity_data:
                humidity_data[date] = []
            humidity_data[date].append(weather.humidity)

    # Moyenne d’humidité par jour
    humidity_avg = {str(day): sum(values)//len(values) for day, values in humidity_data.items()}
    return humidity_avg

def init_plot():
    plt.ylabel("Humidity (%)")
    plt.title("3-Day Humidity Forecast")
    plt.ylim(0, 100)

def plot_humidity(humidity_dict):
    days = list(humidity_dict.keys())
    humidity = list(humidity_dict.values())

    bars = plt.bar(days, humidity, color='skyblue', edgecolor='black')
    write_humidity_on_bar_chart(bars, humidity)
    plt.tight_layout()
    plt.show()

def write_humidity_on_bar_chart(bars, humidity):
    for bar, h in zip(bars, humidity):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                 f'{h}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

def main():
    city = input("Enter a city (e.g. Tel Aviv, IL): ").strip()
    try:
        humidity_data = get_forecast(city)
        init_plot()
        plot_humidity(humidity_data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



#Explication
"""
🔍 Explication des fonctions

get_forecast(city_name) : récupère les prévisions météo toutes les 3 heures, extrait les données d’humidité pour 3 jours et calcule la moyenne par jour.
init_plot() : initialise le titre et l’axe Y du graphique.
plot_humidity() : affiche un graphique avec les données d’humidité.
write_humidity_on_bar_chart() : affiche les % d’humidité au-dessus de chaque barre.
main() : point d’entrée, demande une ville à l’utilisateur et génère le graphique.
"""