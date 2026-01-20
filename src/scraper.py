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


nom= soup.find_all('a',class_='ent-name')
for n in nom:
    type= n.find('td',class_='cell-icon')
    total=n.find('td',class_='cell-num cell-total')
    print(n,type,total)



