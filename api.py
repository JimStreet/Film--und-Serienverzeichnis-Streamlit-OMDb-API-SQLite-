import requests


def get_info_filme(filmtitel, typ):
    
    yourkey = "197c5188"
    api_url = f"http://www.omdbapi.com/?apikey={yourkey}&s={filmtitel}&type={typ}&page=1"
    
    
    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"Irgentetwas ist schief gelaufen: {response.status_code}!")

    elif response.status_code == 200:
        try:  
            data = response.json()
            return data
        except ValueError:
            print("Die Antwort ist nicht im JSON-Format.")


# def get_info_filme2(filmtitel, typ):
    
#     yourkey = "197c5188"
#     api_url = f"http://www.omdbapi.com/?apikey={yourkey}&s={filmtitel}&type={typ}&page=2"
    
    
#     response = requests.get(api_url)

#     if response.status_code != 200:
#         print(f"Irgentetwas ist schief gelaufen: {response.status_code}!")

#     elif response.status_code == 200:
#         try:  
#             data = response.json()
#             return data
#         except ValueError:
#             print("Die Antwort ist nicht im JSON-Format.")



def get_film_details(imdbID):
    
    yourkey = "197c5188"
    api_url = f"http://www.omdbapi.com/?apikey={yourkey}&i={imdbID}"
    
    
    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"Irgentetwas ist schief gelaufen: {response.status_code}!")

    elif response.status_code == 200:
        try:  
            data = response.json()
            return data
        except ValueError:
            print("Die Antwort ist nicht im JSON-Format.")




def get_film_by_title(film_title, typ):
    
    yourkey = "197c5188"
    api_url = f"http://www.omdbapi.com/?apikey={yourkey}&t={film_title}&type={typ}"
    
    
    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"Irgentetwas ist schief gelaufen: {response.status_code}!")
        return None
    
    elif response.status_code == 200:
        try:  
            data = response.json()
            return data
        except ValueError:
            print("Die Antwort ist nicht im JSON-Format.")



