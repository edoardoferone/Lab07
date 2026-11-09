from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self) -> list[Biblioteca]:
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore nella connessione al database.")
            return []

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca ORDER BY nome"
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(
                Biblioteca(
                    id=row["id"],
                    nome=row["nome"],
                    indirizzo=row["indirizzo"]
                )
            )

        cursor.close()
        cnx.close()
        return result