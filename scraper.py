from bs4 import BeautifulSoup

import requests
import random
import re


def get_movies(diff) -> list:
    """Scrapes movie data from IMDb.com

    Args:
        diff (int): the difficulty level that the player entered

    Returns:
        list: returns a list of dictionary with the following keys: 'title', 'year', and 'genre'
    """
    q = get_params(diff)
    url = f"https://www.imdb.com/search/title/?title_type=feature&user_rating={q['min_rating']},{q['max_rating']}&num_votes={q['min_votes']},{q['max_votes']}&count=250"
    total = get_total(url)
    start = random.randint(1, total - 249)
    movie_url = f"https://www.imdb.com/search/title/?title_type=feature&user_rating={q['min_rating']},{q['max_rating']}&num_votes={q['min_votes']},{q['max_votes']}&count=250&start={start}"
    movie_link = requests.get(movie_url)
    movie_soup = BeautifulSoup(movie_link.text, "lxml")
    movie_html = movie_soup.find_all("div", class_="lister-item mode-advanced")
    movies = []
    for movie_list in movie_html:
        title = movie_list.find("h3", class_="lister-item-header").find_next("a").text
        year = movie_list.find("span", class_="lister-item-year text-muted unbold").text
        genre = movie_list.find("span", class_="genre").text
        movies.append(
            {
                "title": title,
                "year": re.sub(r"[()]", "", year).split()[-1],
                "genre": genre.strip(),
            }
        )
    return movies


def get_params(d) -> dict:
    """Gets the query parameters for scraping movie data from IMDb.com

    Args:
        d (int): the difficulty level that the player entered

    Returns:
        dict: returns query parameters depending on the player's chosen difficulty level
    """
    if d == 1:
        return {
            "min_rating": 5,
            "max_rating": 10,
            "min_votes": 100000,
            "max_votes": 10000000,
        }
    elif d == 2:
        return {
            "min_rating": 2.5,
            "max_rating": 7.5,
            "min_votes": 50000,
            "max_votes": 100000,
        }
    else:
        return {
            "min_rating": 1,
            "max_rating": 5,
            "min_votes": 10000,
            "max_votes": 50000,
        }


def get_total(url) -> int:
    """Gets the total number of movies that fit the query parameters

    Args:
        url (str): 

    Returns:
        int: returns the total movies that can be scraped
    """
    link = requests.get(url)
    soup = BeautifulSoup(link.text, "lxml")
    total_text = soup.find("div", class_="desc").text
    total = total_text.split(" ")[2]
    if "," in total:
        total = int(total.replace(",", ""))
    else:
        total = int(total)
    return total
