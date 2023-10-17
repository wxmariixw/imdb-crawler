import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.imdb.com/search/title/?groups=top_1000"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = []
release_year = []
rating = []
parental_rating = []
genre = []
votes_count = []
description = []

movie_data = soup.findAll("div", attrs={"class": "lister-item mode-advanced"})

for movie in movie_data:
    movie_title = movie.h3.a.text
    title.append(movie_title)

    movie_release_year = (
        movie.h3.find("span", class_="lister-item-year text-muted unbold")
        .text.replace("(", "")
        .replace(")", "")
        .replace("I", "")
    )
    release_year.append(movie_release_year)

    movie_rating = movie.find(
        "div", class_="inline-block ratings-imdb-rating"
    ).text.replace("\n", "")
    rating.append(movie_rating)

    text_muted = movie.findAll("p", class_="text-muted")
    movie_parental_rating = text_muted[0].find("span", class_="certificate").text
    parental_rating.append(movie_parental_rating)

    movie_genre = (
        text_muted[0]
        .find("span", class_="genre")
        .text.replace("\n", "")
        .replace(" ", "")
        .split(",")
    )
    genre.append(movie_genre)

    nv = movie.findAll("span", {"name": "nv"})
    votes = nv[0].text
    votes_count.append(votes)

    movie_description = text_muted[1].text
    description.append(movie_description)

    movie_DF = pd.DataFrame(
        {
            "Movie title": title,
            "Release year": release_year,
            "Movie rating": rating,
            "Parental rating": parental_rating,
            "Genre": genre,
            "Votes": votes_count,
            "Description": description,
        }
    )

    movie_DF.to_excel("Most_popular_IMDB_movies.xlsx")
