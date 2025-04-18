#Exercise 1 : Upcoming Holiday
"""
Instructions

Write a function that displays today’s date.
The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is New Years’ Eve in 30 days).
Hint: Use a module to find the datetime and name of the upcoming holiday.

"""

import datetime
import holidays

def upcoming_holiday(country='US'):
    # Date actuelle
    today = datetime.date.today()
    print("Aujourd'hui :", today.strftime('%A %d %B %Y'))

    # Chargement des jours fériés du pays (ex: 'US', 'FR'...)
    year = today.year
    all_holidays = holidays.CountryHoliday(country, years=[year, year + 1])

    # Recherche du prochain jour férié
    for date, name in sorted(all_holidays.items()):
        if date >= today:
            delta = (date - today).days
            print(f" Le prochain jour férié est '{name}' dans {delta} jour(s), le {date.strftime('%A %d %B %Y')}.")
            return

    print("Aucun jour férié trouvé à venir.")

# Exemple pour la France :
upcoming_holiday('FR')
