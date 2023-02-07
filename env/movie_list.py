import requests
from bs4 import BeautifulSoup

def parse_movies_and_export():
    r = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    soup = BeautifulSoup(r.content, "html.parser")

    #we get all the 'tr' tags, globally all the movies
    movies = soup.findAll('tr')

    nom = "Empty"
    url = "Empty"
    numero = "Empty"

    #i loop on all the movies
    for movie in movies:

        #i get the 'img' tag of the film
        img = movie.find('img')
        if img:
            #i get the alt property = the name of the film and url property which returns the image
            nom = img.get('alt')
            url = img.get('src')

        #i get the span tag for this film
        span = movie.find('span')
        if span:
            #i then retrieve its ranking
            numero = span.get('data-value')

        #i configure the path where I want the export
        path = r"C:\Users\root\Documents\scrap_movie_learning\films.csv"

        #i write for each film, always in the loop
        with open(path, "a", encoding='utf-16-le') as f:
                f.write(f"{numero}")
                f.write(f";")
                f.write(f"{nom}")
                f.write(f";")
                f.write(f"{url}\n")

#i call my function
parse_movies_and_export()