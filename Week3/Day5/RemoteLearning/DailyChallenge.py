#Instructions : Air Management System
"""
Your goal is to build an airplanes traffic management system.



Details

Your program should rely on four classes: Airline, Airplane, Flight and Airport.

Consider every plane can fly only once per day.



The Airline Class

Attributes:

id (str) A two letters code
name (str)
planes : A list of Airplanes belonging to this airline (see below the Airplane class)
This class has no methods



The Airplane Class

Attributes:

id (int)
current_location : The Airport where the airplane is currently located (see below the Airport class)
company : The airline this airplane belongs to (see above the Airline class)
next_flights : The list of Flights. Every future flights of the airplane, this list should always be sorted by datetime. (see below the Flight class)


Methods:

fly(self, destination): Make the airplane take off and land if a flight is scheduled for this destination (see below the Flight class)
location_on_date(self, date): Returns where the plane will be on this date
available_on_date(self, date, location) : Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).


The Flight Class

Attributes:

date : datetime.Date
destination : The destination airport. (see below the Airport class)
origin : The departure airport. (see below the Airport class)
plane : The plane used during this flight. (see above the Airplane class)
id (str) : The ID is an encoded string composed of the destination, the airlines code and the date.
Methods:

Those methods are here only to update the rest of the system:

take_off(self)
land(self) : change the location of the plane when it reaches its destination


The Airport Class

Attributes:

city : (str) The code of the city where the airport is located
planes : The list of every plane that is currently in this airport. (see above the Airplane class)
scheduled_departures : The list of flight - Every future flight from this airport, sorted by date. (see above the Flight class)
scheduled_arrivals : The list of flight - Every future flight that will arrive to this airport, sorted by date. (see above the Flight class)


Methods:

schedule_flight(self, destination, datetime) :
finds an available airplane from an airline, that serves the departure and the destination
schedule the airplane for the flight
info(self, start_date, end_date) : Displays every scheduled flight from start_date to end_date.


You are free to add any class/method/attribute to your code, be sure to document everything you write.

Write a small code to test your program.

"""

from datetime import date, timedelta

class Airline:
    def __init__(self, id, name):
        self.id = id  # e.g., "AF" for Air France
        self.name = name
        self.planes = []  # List of Airplane objects


class Airplane:
    def __init__(self, id, current_location, company):
        self.id = id
        self.current_location = current_location  # Airport instance
        self.company = company  # Airline instance
        self.next_flights = []  # List of Flight instances (future)

        # Add this plane to the airport and airline
        current_location.planes.append(self)
        company.planes.append(self)

    def fly(self, destination):
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                self.next_flights.remove(flight)
                break

    def location_on_date(self, date_check):
        # Start from initial location
        location = self.current_location
        for flight in sorted(self.next_flights, key=lambda f: f.date):
            if flight.date > date_check:
                break
            location = flight.destination
        return location

    def available_on_date(self, date_check, location):
        # Check if plane is at correct location and not flying already
        if self.location_on_date(date_check) != location:
            return False
        for flight in self.next_flights:
            if flight.date == date_check:
                return False
        return True


class Flight:
    def __init__(self, date, destination, origin, plane):
        self.date = date  # datetime.date
        self.destination = destination  # Airport instance
        self.origin = origin  # Airport instance
        self.plane = plane  # Airplane instance
        self.id = f"{destination.city}-{plane.company.id}-{date.isoformat()}"

    def take_off(self):
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)
        if self in self.origin.scheduled_departures:
            self.origin.scheduled_departures.remove(self)
        print(f"{self.id}: Plane {self.plane.id} took off from {self.origin.city}.")

    def land(self):
        self.plane.current_location = self.destination
        if self not in self.destination.planes:
            self.destination.planes.append(self.plane)
        if self in self.destination.scheduled_arrivals:
            self.destination.scheduled_arrivals.remove(self)
        print(f"{self.id}: Plane {self.plane.id} landed in {self.destination.city}.")


class Airport:
    def __init__(self, city):
        self.city = city  # Airport city code (str)
        self.planes = []  # List of airplanes currently at the airport
        self.scheduled_departures = []  # List of future Flight instances
        self.scheduled_arrivals = []  # List of future Flight instances

    def schedule_flight(self, destination, flight_date):
        for plane in self.planes:
            if plane.available_on_date(flight_date, self):
                new_flight = Flight(flight_date, destination, self, plane)
                plane.next_flights.append(new_flight)

                self.scheduled_departures.append(new_flight)
                destination.scheduled_arrivals.append(new_flight)

                # Sort the flight lists
                plane.next_flights = sorted(plane.next_flights, key=lambda f: f.date)
                self.scheduled_departures = sorted(self.scheduled_departures, key=lambda f: f.date)
                destination.scheduled_arrivals = sorted(destination.scheduled_arrivals, key=lambda f: f.date)

                print(f"Flight scheduled: {new_flight.id}")
                return new_flight
        print(f"No available airplane to schedule flight from {self.city} to {destination.city} on {flight_date}")
        return None

    def info(self, start_date, end_date):
        print(f"\nFlights from {self.city} between {start_date} and {end_date}:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"  {flight.id} - to {flight.destination.city} on {flight.date}")


# --------------------------------------------
# 🧪 Exemple d'utilisation du système
# --------------------------------------------

# Créer les compagnies
air_france = Airline("AF", "Air France")
ryanair = Airline("RY", "Ryanair")

# Créer les aéroports
paris = Airport("PAR")
london = Airport("LON")
madrid = Airport("MAD")

# Créer les avions
plane1 = Airplane(1, paris, air_france)
plane2 = Airplane(2, paris, ryanair)

# Planifier des vols
today = date.today()
tomorrow = today + timedelta(days=1)
after_tomorrow = today + timedelta(days=2)

paris.schedule_flight(london, today)
paris.schedule_flight(madrid, tomorrow)
london.schedule_flight(paris, after_tomorrow)

# Informations sur les vols
paris.info(today, after_tomorrow)
london.info(today, after_tomorrow)
madrid.info(today, after_tomorrow)

# Simuler un vol
print("\n--- Simulation de vol ---")
plane1.fly(london)  # Fait décoller le premier vol du plane1


"""
✅ Ce que ce code fait :
Gère les avions disponibles par compagnie et aéroport.
Permet de programmer des vols entre aéroports.
Suit la localisation des avions.
Permet de faire décoller/atterrir un vol programmé.
Affiche les vols planifiés sur une période donnée.

"""