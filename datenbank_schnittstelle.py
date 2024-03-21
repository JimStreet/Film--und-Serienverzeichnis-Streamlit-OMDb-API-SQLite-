import sqlite3
from api import get_film_details

def create_table():
    connection = sqlite3.connect("gesehene_filme_datenbank.db")
    cur = connection.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS gesehene_filme (imdbID)")
    
    connection.commit()
    connection.close()


def get_all_data():
    connection = sqlite3.connect("gesehene_filme_datenbank.db")
    cur = connection.cursor()

    cur.execute('SELECT imdbID FROM gesehene_filme')


    imdb_ids = [row[0] for row in cur.fetchall()]

    film_titles = []
    film_typ = []
    film_imdbID = []

    for imdb_id in imdb_ids:
        film_details = get_film_details(imdb_id)
        title = film_details.get("Title")
        film_titles.append(title)

        typ = film_details.get("Type")
        film_typ.append(typ)

        imdbID = film_details.get("imdbID")
        film_imdbID.append(imdbID)

    connection.close()

    return film_titles, film_typ , film_imdbID


def add_to_database(imdbID):
    connection = sqlite3.connect("gesehene_filme_datenbank.db")
    cur = connection.cursor()

    ist_bereits_vorhanden = cur.execute(f"SELECT imdbID FROM gesehene_filme WHERE imdbID = '{imdbID}'").fetchone()
    if not ist_bereits_vorhanden:
        cur.execute(f"INSERT INTO gesehene_filme VALUES ('{imdbID}')")
        connection.commit()

    connection.close()

def remove_from_database(imdbID):
    connection = sqlite3.connect("gesehene_filme_datenbank.db")
    cur = connection.cursor()

    cur.execute(f"DELETE FROM gesehene_filme WHERE imdbID = '{imdbID}'")
    connection.commit()

    connection.close()







