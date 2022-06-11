from project import validate_name, validate_diff, game_area, get_alpha, update_scoreboard
from unittest import mock

import pytest
import builtins
import csv
import os


# Confirm that the function only accepts alphanumeric strings with 4 to 10 characters
def test_validate_name():
    assert validate_name('Vin.ce') == False
    assert validate_name('Vince uwu') == False
    assert validate_name('Vince023') == True
    assert validate_name('VinceEusebio') == False


# Confirm that the function only accepts 1, 2, and 3
def test_validate_diff():
    assert validate_diff('1') == True
    assert validate_diff('4') == False
    with pytest.raises(ValueError):
        assert validate_diff('uwu')


# Provide a mock input and ensure that the function returns a dict with the correct values
def test_game_area():
    test_unit = [{'title': 'Top Gun', 'year': '1986', 'genre': 'Action, Drama'}]
    with mock.patch.object(builtins, "input", side_effect=['q', 'z', 'x', 'k', 'w', 'v', 'm']):
        assert game_area(test_unit, 1) == {'answer': 'TOP GUN', 'life': 0, 'score': 0, 'index': 0}


# Confirm that the function removes non-alphabetic characters from a given string
def test_get_alpha():
    assert get_alpha('Top Gun') == ['T', 'O', 'P', 'G', 'U', 'N']


# Ensure that the function updates the scoreboard
def test_update_scoreboard():
    # Create a test csv file
    test_file = [
        {'name': 'foo', 'score': 100},
        {'name': 'bar', 'score': 200},
        {'name': 'baz', 'score': 150}
    ]
    with open('testcsv.csv', 'w') as tf:
        writer = csv.DictWriter(tf, fieldnames=['name', 'score'])
        writer.writeheader()
        for i in test_file:
            writer.writerow(i)
    # Ensure that the test unit will be added to the test csv file then sort by descending score and ranking
    assert update_scoreboard('boom', 175, 'testcsv.csv') == [
        {'name': 'bar', 'score': '200', 'rank': 1},
        {'name': 'boom', 'score': '175', 'rank': 2},
        {'name': 'baz', 'score': '150', 'rank': 3},
        {'name': 'foo', 'score': '100', 'rank': 4}
    ]
    os.remove('testcsv.csv')