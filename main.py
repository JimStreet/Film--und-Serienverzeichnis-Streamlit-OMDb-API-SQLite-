import streamlit as st
from api import get_info_filme, get_film_details, get_film_by_title #, get_info_filme2
from datenbank_schnittstelle import get_all_data, add_to_database, remove_from_database, create_table



st.set_page_config(layout="wide")


create_table()

st.title("Filme und Serien")

filmname = st.text_input("Name des Films oder der Serie")

typ = st.selectbox("Filter nach Typ", ("movie", "series", "episode"))

min_rating, max_rating = st.slider("Filter nach IMDb Rating", value=(0.0, 10.0))


# st.sidebar.title("Serverantwort")
# st.sidebar.json(get_info_filme(filmname, typ))
# #st.sidebar.json(get_info_filme2(filmname, typ))
# st.sidebar.json(get_film_by_title(filmname, typ))


if filmname:
    film_list = get_info_filme(filmname, typ)

    st.header("Such Ergebnisse")


    if "Search" in film_list:
        for film in film_list["Search"]:
            film_imdbID = film.get("imdbID")

            film_details = get_film_details(film_imdbID)

            imdb_rating = film_details.get("imdbRating")

            if imdb_rating != "N/A":
               imdb_rating = float(imdb_rating)
            else:
                imdb_rating = 0.0

            if min_rating <= imdb_rating <= max_rating:

                st.markdown("""---""")

                bild, infos, hinzufügen, entfernen = st.columns([2,4,1,1])

                with bild:
                    if film_details["Poster"] != "N/A":
                        st.image(film_details["Poster"], caption= f"{film_details['Title']} ({film_details['Year']})", use_column_width  = True)
                    else:
                        st.image("kein_bild_vorhanden.jpg")

                with infos:
                    st.header(film_details["Title"])

                    imdb_rating, rated, runtime = st.columns(3)
                    with imdb_rating:
                        if film_details["imdbRating"] != "N/A":
                            st.text(f"IMDb Rating: {film_details['imdbRating']}")
                        else:
                            st.text("IMDb Rating: - ")
                    with rated:
                        if film_details["Rated"] != "N/A":
                            st.text(f"Rated: {film_details['Rated']}")
                        else:
                            st.text(f"Rated: - ")
                    with runtime:
                        if film_details["Runtime"] != "N/A":
                            st.text(f"Länge: {film_details['Runtime']}")
                        else:
                            st.text(f"Länge: - ")


                    if film_details["Type"] != "N/A":
                        st.text(f"Typ: {film_details['Type']}")
                    else:
                        st.text(f"Typ: - ")

                    if film_details["Year"] != "N/A":
                        st.text(f"Jahr: {film_details['Year']}")
                    else:
                        st.text(f"Jahr: - ")

                    if film_details["Released"] != "N/A":
                        st.text(f"Veröffentlicht: {film_details['Released']}")
                    else:
                        st.text(f"Veröffentlicht: - ")

                    if film_details["Genre"] != "N/A":
                        st.text(f"Genre: {film_details['Genre']}")
                    else:
                        st.text("Genre: - ")

                    if film_details["Director"] != "N/A":
                        st.text(f"Regisseur: {film_details['Director']}")
                    else:
                        st.text("Regisseur: - ")

                    if film_details["Actors"] != "N/A":
                        st.text(f"Schauspieler: {film_details['Actors']}")
                    else:
                        st.text("Schauspieler: - ")

                    with st.container():
                        if film_details['Plot'] != "N/A":
                            st.write(f"Handlung: {film_details['Plot']}")
                        else:
                            st.text("Handlung: - ")

                with hinzufügen:
                    if st.button("Hinzufügen :heavy_plus_sign:", key=f"hinzufügen_{film_details['imdbID']}"):
                        
                        add_to_database(film_details["imdbID"])
                        
                        st.text("wurde hinzugefügt")

                with entfernen:
                    if st.button("Entfernen :heavy_minus_sign:", key=f"entfernen_{film_details['imdbID']}"):

                        remove_from_database(film_details["imdbID"])
        
                        st.text("wurde entfernt")


#suche nach einem Film

    elif "Search" not in film_list:
        film_info = get_film_by_title(filmname, typ)

        if film_info.get("Response") == "True":

            film_imdbID = film_info.get("imdbID")
            film_details = get_film_details(film_imdbID)

            st.markdown("""---""")

            bild, infos, hinzufügen, entfernen = st.columns([2,4,1,1])
            with bild:
                if film_details["Poster"] != "N/A":
                    st.image(film_details["Poster"], caption= f"{film_details['Title']} ({film_details['Year']})")
                else:
                    st.image("kein_bild_vorhanden.jpg")


            with infos:
                st.header(film_details["Title"])

                imdb_rating, rated, runtime = st.columns(3)
                with imdb_rating:
                    if film_details["imdbRating"] != "N/A":
                        st.text(f"IMDb Rating: {film_details['imdbRating']}")
                    else:
                        st.text("IMDb Rating: - ")
                with rated:
                    if film_details["Rated"] != "N/A":
                        st.text(f"Rated: {film_details['Rated']}")
                    else:
                        st.text(f"Rated: - ")
                with runtime:
                    if film_details["Runtime"] != "N/A":
                        st.text(f"Länge: {film_details['Runtime']}")
                    else:
                        st.text(f"Länge: - ")


                if film_details["Type"] != "N/A":
                    st.text(f"Typ: {film_details['Type']}")
                else:
                    st.text(f"Typ: - ")

                if film_details["Year"] != "N/A":
                    st.text(f"Jahr: {film_details['Year']}")
                else:
                    st.text(f"Jahr: - ")

                if film_details["Released"] != "N/A":
                    st.text(f"Veröffentlicht: {film_details['Released']}")
                else:
                    st.text(f"Veröffentlicht: - ")

                if film_details["Genre"] != "N/A":
                    st.text(f"Genre: {film_details['Genre']}")
                else:
                    st.text("Genre: - ")

                if film_details["Director"] != "N/A":
                    st.text(f"Regisseur: {film_details['Director']}")
                else:
                    st.text("Regisseur: - ")

                if film_details["Actors"] != "N/A":
                    st.text(f"Schauspieler: {film_details['Actors']}")
                else:
                    st.text("Schauspieler: - ")

                with st.container():
                    if film_details['Plot'] != "N/A":
                        st.write(f"Handlung: {film_details['Plot']}")
                    else:
                        st.text("Handlung: - ")


            with hinzufügen:
                if st.button("Hinzufügen :heavy_plus_sign:", key=f"hinzufügen_{film_details['imdbID']}"):

                    add_to_database(film_details["imdbID"])
                    
                    st.text("wurde hinzugefügt")


            with entfernen:
                if st.button("Entfernen :heavy_minus_sign:", key=f"entfernen_{film_details['imdbID']}"):

                    remove_from_database(film_details["imdbID"])

                    st.text("wurde entfernt")

        else:
            st.error("Keine Ergebnisse")



st.sidebar.header("bereits gesehen:")

gesehene_filme, gesehene_typ, gesehene_imdbID = get_all_data()
for filmname_aus_datenbank, typ_aus_datenbank, gesehene_imdbID in zip(reversed(gesehene_filme), reversed(gesehene_typ), reversed(gesehene_imdbID)):

        st.sidebar.write(f"{filmname_aus_datenbank}, {typ_aus_datenbank}")

        if st.sidebar.button("Entfernen", key=f"entfernen_bereits_gesehen_{gesehene_imdbID}"):
            remove_from_database(gesehene_imdbID)

            st.sidebar.text("wurde entfernt")
            st.rerun()








