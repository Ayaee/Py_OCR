# -*- coding: utf8 -*-
import random
import json

# Donne le fichier Json et retourn la liste
def readValues_fromJson(path, key):   # Lire les valeurs du fichier JSON
    values = []                         # Crée une liste vide
    with open(path) as f:               # Ouvre le fichier JSON avec mes objets
        data = json.load(f)             # Charge toutes les données contenue dans le fichier. data = entrée
        for entry in data:              # Ajoute chaque élément dans ma liste
            values.append(entry[key])
    return values                       # Retourn ma liste complete  

# Donne json et retourne la liste
def cleanString(sentences):
    cleaned = []
    for sentence in sentences:              # Conserve les quotes dans une liste. Créer une liste vide et ajoute chaque phrase une par une
        cleanSentence = sentence.strip()    # Nettoie les quotes des espaces blanc et ainsi de suite
        cleaned.append(cleanSentence)       # Ne pas utiliser extend car il ajoute chaque lettre une par une !
    return cleaned
    
# Retourne un item random de la liste
def randomItem(objectList):
    randNumb = random.randint(0, len(objectList) - 1)   # Donner un nombre aléatoire
    #item = myList[randNumb]                            # Donne une quote de la liste
    return objectList[randNumb]                         # Retour valeur

# Retourne une valeur random du fichier json
def randomValue(sourcePath, key):
    allValues = readValues_fromJson(sourcePath, key)
    cleanValues = cleanString(allValues)
    return randomItem(cleanValues)
   
   
################
#### QUOTES ####
################

# Recueille des citations de San Antonio
def randomQuote():
    #all_values = readValues_fromJson('quotes.json', 'quote')
    return randomValue('quotes.json', 'quote')

####################
#### CHARACTERS ####
####################

def randomCharacter():
    #all_values = readValues_fromJson('characters.json', 'character')
    return randomValue('characters.json', 'character')


#####################
#### INTERACTION ####
#####################

def printRandom_sentence():
    randQuote = randomQuote()
    randCharacter = randomCharacter()
    print(">>>> {} a dit : {}".format(randCharacter, randQuote))
    
def mainLoop():
    while True:
        printRandom_sentence()
        message = ('Voulez-vous une autre citation ? Tapez sur [Entrer].'
                   'Pour quitter, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break
        
# Lancer la boucle!
mainLoop()