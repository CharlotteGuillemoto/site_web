import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM pokedex", conn)
conn.close()


df["weight_num"] = pd.to_numeric(df["weight"].str.extract(r"([\d\.]+)")[0], errors="coerce")
df["height_num"] = pd.to_numeric(df["height"].str.extract(r"([\d\.]+)")[0], errors="coerce")
df["total_num"] = pd.to_numeric(df["total"], errors="coerce")

#Histogramme du poids
plt.figure(figsize=(8,5))
plt.hist(df["weight_num"].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title("Distribution du poids des Pokémon")
plt.xlabel("Poids (kg)")
plt.ylabel("Nombre de Pokémon")
plt.grid(axis='y', alpha=0.7)
plt.show()

#Histogramme de la taille
plt.figure(figsize=(8,5))
plt.hist(df["height_num"].dropna(), bins=30, color='lightgreen', edgecolor='black')
plt.title("Distribution de la taille des Pokémon")
plt.xlabel("Taille (m)")
plt.ylabel("Nombre de Pokémon")
plt.grid(axis='y', alpha=0.7)
plt.show()

#Nombre de Pokémon par type
types = df["type"].str.split(", ").explode()
type_counts = types.value_counts()

plt.figure(figsize=(10,6))
type_counts.plot(kind='bar', color='salmon', edgecolor='black')
plt.title("Nombre de Pokémon par type")
plt.xlabel("Type")
plt.ylabel("Nombre de Pokémon")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.7)
plt.show()