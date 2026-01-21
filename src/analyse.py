import sqlite3
from datetime import datetime
import pandas as pd
import numpy as np 



table = sqlite3.connect("database.db")
df = pd.read_sql_query("SELECT * FROM pokedex", table)

table.close()
#print(df.head())

print(df.columns)

pokemon_leger = df.loc[df["weight"].idxmin()]
print(pokemon_leger)


df1 = df[df["weight"] != "N/A"] #récupérer une colonne ou y'a pas les N/A 
pokemon_lourd = df1.loc[df1["weight"].idxmax()]
print(pokemon_lourd)