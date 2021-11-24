# -*- coding: utf8 -*-
import random
import json


def read_values_from_json(file, key):   # Lire les valeurs du fichier JSON
    values = []                         # Crée une liste vide
    with open(file) as f:               # Ouvre le fichier JSON avec mes objets
        data = json.load(f)             # Charge toutes les données contenue dans le fichier. data = entrée
        for entry in data:              # Ajoute chaque élément dans ma liste
            values.append(entry[key])
    return values                       # Retourn ma liste complete  

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1) # Donner un nombre aléatoire
    item = my_list[rand_numb]                       # Donne une quote de la liste
    return item                                     # Retour valeur

def get_random_character():
    all_values = read_values_from_json('characters.json', 'character')
    return get_random_item_in(all_values)

def get_random_quote():
    all_values = read_values_from_json('quotes.json', 'quote')
    return get_random_item_in(all_values)
    

#Programme
user_answer = input('Tapez entrée pour une autre citation ou B pour quitter le programme.')

while user_answer !="B":
    print(message(get_random_character(), get_random_quote()))
    user_answer = input('Tapez entrée pour une autre citation ou B pour quitter le programme.')