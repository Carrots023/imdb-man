from project import validate_name, validate_diff, game_area, get_alpha, update_scoreboard
from unittest import mock

import pytest
import builtins
import csv
import os

def test_validate_name():
    assert validate_name('Vince') == True
    assert validate_name('Vince uwu') == False


def test_validate_diff():
    assert validate_diff('1') == True
    assert validate_diff('4') == False
    with pytest.raises(ValueError):
        assert validate_diff('uwu')


def test_game_area():
    test_unit = [{'title': 'Top Gun', 'year': '1986', 'genre': 'Action, Drama'}]
    with mock.patch.object(builtins, "input", side_effect=['q', 'z', 'x', 'k', 'w', 'v', 'm']):
        assert game_area(test_unit, 1) == {'answer': 'TOP GUN', 'life': 0, 'score': 0, 'index': 0}


def test_get_alpha():
    assert get_alpha('Top Gun') == ['T', 'O', 'P', 'G', 'U', 'N']


def test_update_scoreboard():
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
    assert update_scoreboard('boom', 175, 'testcsv.csv') == [
        {'name': 'bar', 'score': '200', 'rank': 1},
        {'name': 'boom', 'score': '175', 'rank': 2},
        {'name': 'baz', 'score': '150', 'rank': 3},
        {'name': 'foo', 'score': '100', 'rank': 4}
    ]
    os.remove('testcsv.csv')