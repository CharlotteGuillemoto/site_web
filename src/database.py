import sqlite3
from datetime import datetime
class DatabaseManager:

    def __init__(self,fichierdb):
        self.fichierdb = fichierdb
        self.conn = sqlite3.connect(self.fichierdb)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokedex (
                nom TEXT NOT NULL,
                type TEXT,
                total INTEGER,
                weight INTEGER,
                height INTEGER,
                date_scraping TEXT NOT NULL
            )
        """)
        self.conn.commit() #création de la table pokedex

    def insert_pokedex(self, nom, type, total, weight, height, commit=True):
        self.cursor.execute("""
            INSERT INTO pokedex (
                nom, type, total, weight, height, date_scraping
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            nom,
            type,
            total,
            weight,
            height,
            datetime.now().isoformat(timespec="seconds") #date_scraping= date ou le scraping a été fait
        ))

        
        self.conn.commit()


    def close(self):
        self.conn.close()
