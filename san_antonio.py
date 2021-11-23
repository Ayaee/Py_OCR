import random
import  json


def read_value_from_json():                     # Lire les valeurs du fichier JSON
    values = []                                 # Crée une liste vide
    with open('characters.json', 'quotes.json') as f:          # Ouvre le fichier JSON avec mes objets
        data = json.load(f)                     # Charge toutes les données contenue dans le fichier. data = entrée
        for entry in data:                      # Ajoute chaque élément dans ma liste
            values.append(entry['character'])
            values.append(entry['quote'])
        return values                           # Retourn ma liste complete  

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1) # Donner un nombre aléatoire
    item = my_list[rand_numb]                       # Donne une quote de la liste
    return item                                     # Retour valeur

def random_character():
    all_values = read_value_from_json()
    return get_random_item_in(all_values)

def random_quote():
    all_values = read_value_from_json()
    return get_random_item_in(all_values)
    

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)


user_answer = input('Tapez entrée pour une autre citation ou B pour quitter le programme.')

while user_answer !="B":
    print(message(random_character(), message(random_quote())))
    user_answer = input('Tapez entrée pour une autre citation ou B pour quitter le programme.')