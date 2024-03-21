import streamlit as st

st.set_page_config(layout="wide")


st.title("Film- und Serienverzeichnis (Streamlit, OMDb API & SQLite)")




einleitung = st.sidebar.toggle("Einleitung")
hauptteil = st.sidebar.toggle("Hauptteil")
schluss = st.sidebar.toggle("Schluss")


if einleitung:
    st.header("Einleitung")
    st.markdown("- Motivation: Arbeiten mit API, mehrere gelernte Konzepte")
    st.markdown("- Ideenfindung: Suche von API durch YouTube und Google")
    st.markdown("- Entscheidung Idee: Letterboxd hat anscheinend keine Serien (ein Freund beschwerte sich darüber)")
    st.markdown("- Findung API: Suche von API durch YouTube und Google; api = https://www.omdbapi.com/")



if hauptteil:
    st.header("Hauptteil")
    st.markdown("- Vorstellung vom Code: API, Datenbank-Schnittstelle und dann Main")
    st.markdown("- Vorführung: Movie Tracker App")



if schluss:
    st.header("Schluss")
    st.markdown("- Was hätte ich besser machen können")

    st.text("""
                - von anfang an die datenbank in externe datei
                - mir einen genaueren plan machen, was will ich funktionalität und design
                - bessere variablen und funktionsnamen
                - von anfang an notizen machen bzw. screenshots
                - von anfang an eine Testdatein""")

    st.markdown("- Wie könnte ich die App weiterentwickeln")

    st.text("""
                - login, email bestätigung etc.
                - pagination
                - design verbessern
                - uhrzeit und datum mit angeben bei den filmen
                - weitere Tracker bauen und in einer App anbieten z.b. Finanz, Ernährung, Fitness, Verhalten, Progress-Tracker etc.
                - echte Webseite daraus machen """)

    st.markdown("- Persönliche entwicklung")

    st.text("""
                - api bei search
                - api und datenbank im echten einsatz
                - selbstvertrauen
                - erkennung meiner grenzen und die grenzen bzw. arbeitsweisen von technologien in diesem fall Streamlit und SQlite.""")

    st.text("Ende")


