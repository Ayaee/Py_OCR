import imp
import requests
from bs4 import BeautifulSoup
#from requests import get

# Page a Scrapper
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
#print(page)                                                # Test print page
soup = BeautifulSoup(page.content, "html.parser")           # Transformer le html en objet BS (parse)


# Récupérations des informations
titres_bs = soup.find_all("a", class_="gem-c-document-list__item-title")
titres = []
for titre in titres_bs:
    titres.append(titre.string)
#print(titres)                                                                      # Test print titres
descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []
for description in descriptions_bs:
    descriptions.append(description.string)
#print(descriptions)                                                                # Test print descriptions