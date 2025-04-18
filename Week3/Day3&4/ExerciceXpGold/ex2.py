#Exercise 2 : How Old Are You On Jupiter?
"""
Instructions

Given an age in seconds, calculate how old someone would be on all those planets :

Earth: orbital period 365.25 Earth days, or 31557600 seconds
Example : if someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years

# Instructions traduites :

Écris une fonction qui, à partir d’un âge en secondes, calcule l’âge de quelqu’un sur chaque planète du système solaire selon leur période orbitale.

"""


def age_on_planets(age_seconds):
    earth_year_seconds = 31557600  # 365.25 * 24 * 60 * 60
    orbital_periods = {
        'Earth': 1.0,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }
     #Sachant qu’une année terrestre dure 31_557_600 secondes, on peut faire les conversions.

    print(f"Age en secondes : {age_seconds}")
    for planet, period in orbital_periods.items():
        age_years = age_seconds / (earth_year_seconds * period)
        print(f" Sur {planet}, vous avez {age_years:.2f} ans.")

# Exemple : 1 milliard de secondes
age_on_planets(1_000_000_000)
