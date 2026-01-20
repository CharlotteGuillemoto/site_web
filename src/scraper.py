import requests
import bs4
from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/all"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)


type(html)

soup = BeautifulSoup(html, "html.parser")
type(soup)

tableau = soup.find("table", id="pokedex") #on va chercher que le tableau, pour éviter d'avoir trop d'infos 
#print(tableau)

noms = soup.find_all("a", class_="ent-name") #ça va chercher que les cases avec le nom des pokémons

for e in noms : 
    print(e.prettify()) #prettify, ça réarrange pour faire plus beau, à ne pas utiliser sur noms directement parce que c'est une liste 

#print(html) (trop moche)