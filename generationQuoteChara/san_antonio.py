# -*- coding: utf8 -*-
import json
import random


# Donne le fichier Json et retourne une liste
def readValues_fromJson(path, key):     # Lire les valeurs du fichier JSON
    values = []                         # Crée une liste vide
    with open(path) as f:               # Ouvre le fichier JSON avec mes objets
        data = json.load(f)             # Charge toutes les données contenue dans le fichier. data = entrée
        for entry in data:              # Ajoute chaque élément dans ma liste
            values.append(entry[key])
    return values                       # Retourn ma liste complete  


# Donne json et retourne la liste
def cleanString(sentences):
    cleaned = []
    for sentence in sentences:              # Stock les quotes dans une liste. Créer une liste vide et ajoute chaque phrase une par une
        cleanSentence = sentence.strip()    # Nettoie les quotes des espaces blanc
        cleaned.append(cleanSentence)       # Ne pas utiliser extend car il ajoute chaque lettre une par une
    return cleaned


# Retourne un item random dans la liste
def randomItem(objectList):
    randNumb = random.randint(0, len(objectList) - 1)   # Donner un nombre aléatoire
    #item = myList[randNumb]                            # Donne une quote de la liste
    return objectList[randNumb]                         # Retour valeur


# Retourne une valeur random à partir du fichier json
def randomValue(sourcePath, key):
    allValues = readValues_fromJson(sourcePath, key)
    cleanValues = cleanString(allValues)
    return randomItem(cleanValues)
   
   
################
#### QUOTES ####
################

# Recueille les quotes de San Antonio
def randomQuote():
    return randomValue('quotes.json', 'quote')

####################
#### CHARACTERS ####
####################


# Receuille les characters de Wikipédia
def randomCharacter():
    return randomValue('characters.json', 'character')


#####################
#### INTERACTION ####
#####################

# Print une phrase random
def printRandom_sentence():
    randQuote = randomQuote()
    randCharacter = randomCharacter()
    print(">>>> {} a dit : {}".format(randCharacter, randQuote))


def mainLoop():
    while True:
        printRandom_sentence()
        message = ('Voulez-vous voir une autre citation ? Tapez [Entrer].'
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break                                                           # Cela mettra fin à la boucle


if __name__ == '__main__':
    mainLoop()