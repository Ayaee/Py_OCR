# -*- coding: utf8 -*- # Pour afficher les accents

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chimpunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]

def get_random_item_in(my_list):
    # Donner un nombre aléatoire
    item = my_list[0]               #Donne une quote de la liste
    return item                     #Retour valeur


user_answer = "A"

while user_answer !="B":
    print(get_random_item_in(quotes))
    user_answer = "B"

for quote in quotes:
    quote.capitalize()
    