from scraper import get_movies, get_params, get_total


def test_get_movies():
    assert len(get_movies(1)) == 250


def test_get_params():
    assert get_params(1) == {
                "min_rating": 5,
                "max_rating": 10,
                "min_votes": 100000,
                "max_votes": 10000000,
            }


def test_get_total():
    test_url = "https://www.imdb.com/search/title/?title_type=documentary&release_date=1894-01-01,1950-12-31"
    assert get_total(test_url) == 35035