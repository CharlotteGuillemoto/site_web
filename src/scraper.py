import requests

from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/all"
response = requests.get(url)
html = response.text

if response.status_code != 200:
    print("Erreur :", response.status_code)


type(html)

soup = BeautifulSoup(html, "html.parser")
type(soup)


'''nom= soup.find_all('a',class_='ent-name')
for n in nom:
    type= n.find('td',class_='cell-icon') #pour faire ressortir les type et le total de points pour chaque pokemon
    total=n.find('td',class_='cell-num cell-total')
    print(n,type,total)'''



tableau = soup.find("table", id="pokedex") #on va chercher que le tableau, pour éviter d'avoir trop d'infos 
#print(tableau)

'''noms = soup.find_all("a", class_="ent-name") #ça va chercher que les cases avec le nom des pokémons
type=soup.find_all('td',class_='cell-icon')
total=soup.find_all('td',class_='cell-num cell-total')

for e in noms : 
    print(e.prettify()) #prettify, ça réarrange pour faire plus beau, à ne pas utiliser sur noms directement parce que c'est une liste 
for e in type : 
    print(e.prettify())
for e in total : 
    print(e.prettify())
#print(html) (trop moche)'''

from database import DatabaseManager
db = DatabaseManager("database.db")

for l in tableau.find_all("tr")[1:]:
    nom_s = l.find("a", class_="ent-name").text
    type_s = l.find_all("a", class_="type-icon")
    typespokemon = [e.text for e in type_s]
    total_s = l.find("td", class_="cell-num cell-total").text
    url = f"https://pokemondb.net/pokedex/{nom_s}"
    response = requests.get(url)
    html = response.text
    soup_pokemon = BeautifulSoup(response.text, "html.parser")
    height_th = soup_pokemon.find("th", string=lambda x: x and "Height" in x)
    weight_th = soup_pokemon.find("th", string=lambda x: x and "Weight" in x)
    if height_th:
        height_s = height_th.find_next_sibling("td").text.strip()
    else:
        height_s = "N/A"
    if weight_th:
        weight_s = weight_th.find_next_sibling("td").text.strip()
    else:
        weight_s = "N/A"
    db.insert_annonce(
        nom = nom_s,
        type=typespokemon,
        total=total_s,
        weight=weight_s,
        height=height_s
    )
    
    print(f"{nom_s}|Types: {', '.join(typespokemon)} | Total: {total_s}| Height: {height_s} | Weight: {weight}")

db.close()
