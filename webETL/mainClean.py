import csv
import requests
from bs4 import BeautifulSoup


# Récupérations des informations
def extraire(elements):
    resultat = []
    for element in elements :
        resultat.append(element.string)
    return resultat

# Chargement informations dans fichier "csv"
def charge(nom, entete, titres, descriptions):
    with open(nom, 'w') as fichier :
        writer = csv.writer(fichier, delimiter=',')
        writer.writerow(entete)
        for titre, description in zip(titres, descriptions) :
            writer.writerow([titre, description])
            
# Page a Scrapper
def etl():
    url = "https://www.gov.uk/search/news-and-communications"
    page = requests.get(url)
    #print(page)                                                # Test print page
    soup = BeautifulSoup(page.content, "html.parser")           # Transformer le html en objet BS (parse)

    # Récupération titres et descriptions
    titres = soup.find_all("a", class_="gem-c-document-list__item-title")
    #print(titres)                                                                      # Test print titres
    descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
    #print(descriptions)                                                                # Test print descriptions
    
    entete = ["titre", "description"]
    titres = extraire(titres)
    descriptions = extraire(descriptions)
    charge("data.cvs", entete, titres, descriptions)
    
etl()
        
    