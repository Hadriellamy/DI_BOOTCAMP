#Exercise 1 : Call History
"""
Instructions

Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

Add a method called show_call_history. This method should print the call_history.

Add another attribute called messages to your __init__() method which value is an empty list.

Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
to : the number of another Phone object
from : your phone number (also a Phone object)
content

Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

Test your code !!!

"""

class Phone :
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []


    def call(self, other_phone):
        call_info = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_info)
        self.call_history.append(call_info)   

    def show_call_history(self):
           print("Call History:")
           for call in self.call_history:
            print(call)


    def send_message(self, other_phone, content):
        message = {
            'to': other_phone.phone_number,
            'from': self.phone_number,
            'content': content
        }
        self.messages.append(message)
        other_phone.messages.append(message)        



    def show_outgoing_messages(self):
        print("Outgoing Messages:")
        for msg in self.messages:
            if msg['from'] == self.phone_number:
                print(msg)

    def show_incoming_messages(self):
        print("Incoming Messages:")
        for msg in self.messages:
            if msg['to'] == self.phone_number:
                print(msg)

    def show_messages_from(self, number):
        print(f"Messages from {number}:")
        for msg in self.messages:
            if msg['from'] == number and msg['to'] == self.phone_number:
                print(msg)





# =======================
# ✅ TEST DU CODE :
# =======================

# Création de deux téléphones
phone1 = Phone("123-456")
phone2 = Phone("789-012")

# Appels
phone1.call(phone2)
phone2.call(phone1)

# Historique des appels
phone1.show_call_history()
phone2.show_call_history()

# Envoi de messages
phone1.send_message(phone2, "Salut, comment ça va ?")
phone2.send_message(phone1, "Tout va bien, et toi ?")
phone1.send_message(phone2, "On se voit ce soir ?")

# Affichage des messages sortants
print("\n--- Messages sortants de phone1 ---")
phone1.show_outgoing_messages()

print("\n--- Messages entrants de phone2 ---")
phone2.show_incoming_messages()

print("\n--- Messages que phone2 a reçus de phone1 ---")
phone2.show_messages_from("123-456")                