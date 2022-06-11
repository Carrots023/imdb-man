from scraper import get_movies, get_params, get_total


# Check output by comparing the number of scraped movies
def test_get_movies():
    assert len(get_movies(1)) == 250


# Ensure the function is returning the correct query parameter based on player's chosen difficulty
def test_get_params():
    assert get_params(1) == {"min_rating": 5, "max_rating": 10, "min_votes": 100000, "max_votes": 10000000}


# Check if the correct data is scraped by test querying with a specific parameter
def test_get_total():
    test_url = "https://www.imdb.com/search/title/?title_type=documentary&release_date=1894-01-01,1950-12-31"
    assert get_total(test_url) == 35035