import requests
from bs4 import BeautifulSoup

def parse_movies_and_export():
    r = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    soup = BeautifulSoup(r.content, "html.parser")
    movies = soup.findAll('tr')

    nom = "Vide"
    url = "Vide"
    numero = "Vide"

    for movie in movies:
        img = movie.find('img')
        if img:
            nom = img.get('alt')
            url = img.get('src')

        span = movie.find('span')
        if span:
            numero = span.get('data-value')

        chemin = r"C:\Users\root\Documents\scrap_movie_learning\films.csv"

        with open(chemin, "a", encoding='utf-16-le') as f:
                f.write(f"{numero}")
                f.write(f";")
                f.write(f"{nom}")
                f.write(f";")
                f.write(f"{url}\n")

#we start the treatment
parse_movies_and_export()