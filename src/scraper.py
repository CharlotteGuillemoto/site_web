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




tableau = soup.find("table", id="pokedex") #on va chercher que le tableau, pour éviter d'avoir trop d'infos 
#print(tableau)



from database import DatabaseManager
db = DatabaseManager("database.db")

for l in tableau.find_all("tr")[1:]: #on enlève la première ligne (qui sert a rien)
    nom_s = l.find("a", class_="ent-name").text #plus propre
    type_s = l.find_all("a", class_="type-icon")
    typespokemon = [e.text for e in type_s]
    total_s = l.find("td", class_="cell-num cell-total").text
    url = f"https://pokemondb.net/pokedex/{nom_s}"
    response = requests.get(url)
    html = response.text
    soup_pokemon = BeautifulSoup(response.text, "html.parser")
    height_th = soup_pokemon.find("th", string=lambda x: x and "Height" in x)
    weight_th = soup_pokemon.find("th", string=lambda x: x and "Weight" in x) #méthode qui nous permet d'aller chercher des infos qui ne sont pas sur la page principale mais ou il faut creuser
    if height_th:
        height_s = height_th.find_next_sibling("td").text.strip()
    else:
        height_s = "N/A" #sinon il beugue quand y'a rien donc on est obligées de rajouter une étape
    if weight_th:
        weight_s = weight_th.find_next_sibling("td").text.strip()
    else:
        weight_s = "N/A"
    db.insert_pokedex( #la on commence à insérer les données dans notre table pokedex
        nom = nom_s,
        type = ', '.join(typespokemon), #il accepte pas les listes donc on les sépare comme on peut
        total=total_s,
        weight=weight_s,
        height=height_s
    )
    
    print(f"{nom_s}|Types: {', '.join(typespokemon)} | Total: {total_s}| Height: {height_s} | Weight: {weight_s}") #bon ça c'est pas hyper important au final mais 

db.close()
