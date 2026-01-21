import sqlite3
from datetime import datetime
class DatabaseManager:

    def __init__(self,fichierdb):
        self.fichierdb = fichierdb
        self.conn = sqlite3.connect(self.fichierdb)
        self.cursor = self.conn.cursor()

    def insert_annonce(self, nom, type, total, weight, height, commit=True):
        self.cursor.execute("""
            INSERT INTO annonces (
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

        if commit:
            self.conn.commit()


    def close(self):
        self.conn.close()

