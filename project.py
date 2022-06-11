from rich.console import Console
from tabulate import tabulate

import scraper
import os
import random
import re
import csv
import sys
import time

console = Console()



# A str that acts as a divider
DIV = "~" * 20

# Game's difficulty levels
DIF = f"""
[1] I'm sure you know at least 80{chr(37)} of the movies here. Kinda basic.
[2] Hmm, so you like movies a lot, huh? Interesting.
[3] You know these movies?!
"""

# Initial number of lives per start of a round
MAX_LIFE = 7

# Name of the csv file that will store players' usernames and scores
SCOREBOARD = "scoreboard.csv"


def main():
    while True:
        # Clear the terminal window and greet the player
        clear()
        print("🎥 Welcome to [IMDb]Man!~~ 🎥", DIV, sep="\n")

        # Ask the player's name
        while True:
            name = input("Tell me your name: ").strip()
            if validate_name(name):
                clear()
                print(f"Hello, {name}! Choose the game's difficulty.")
                break
            else:
                print(
                    DIV,
                    "Your name should be 4 to 10 characters long and only consist of alphanumeric characters. I'll ask you again.",
                    DIV,
                    sep="\n",
                )

        # Show the difficulty levels
        print(DIV + DIF + DIV)

        # Ask the player to pick a difficulty level
        while True:
            try:
                get_diff = input("Now pick: ")
                if validate_diff(get_diff):
                    diff = int(get_diff)
                    break
                else:
                    print(
                        DIV,
                        "See the numbers inside the square brackets? Let's try again.",
                        DIV,
                        sep="\n",
                    )
            except:
                print(
                    DIV,
                    "See the numbers inside the square brackets? Let's try again.",
                    DIV,
                    sep="\n",
                )

        # Gather movie data
        clear()
        with console.status("Gathering movies for you. Stay still...", spinner="arrow3"):
            movies_raw = scraper.get_movies(diff)
        movies = random.sample(movies_raw, 200)


        total_score = 0
        round = 1
        while len(movies) != 0:
            round_stats = game_area(movies, round)
            if round_stats['life'] == 0:
                print(DIV, f"Correct Answer: {round_stats['answer']}", sep="\n")
                print("~~~~~Game Over!~~~~~")
                print(f"Final Score: {total_score}", DIV, sep="\n")
                sorted_scoreboard = update_scoreboard(name, total_score, SCOREBOARD)
                header = ['Ranking', 'Username', 'Total Score']
                score_table = []
                for tr in sorted_scoreboard:
                    td = [tr['rank'], tr['name'], tr['score']]
                    score_table.append(td)
                print(tabulate(score_table, headers=header, tablefmt="grid"))
                print(DIV)
                while True:
                    prompt_new_game = input("New Game? [Y/N]:").upper()
                    if prompt_new_game in ["Y", "YES"]:
                        break
                    elif prompt_new_game in ["N", "NO"]:
                        print(DIV, "Understandable. Have a great day!", DIV, sep="\n")
                        sys.exit()
                    else:
                        print(DIV, "Invalid Input. Try again.", DIV, sep="\n")
                break
            else:
                total_score += round_stats['score'] * diff
                round += 1
                movies.remove(movies[round_stats['index']])
                print(DIV, "~~Congratulations!~~", sep="\n")
                print(f"Total Score: {total_score}", DIV, sep="\n")
                with console.status("Proceeding to the next round. Please wait...", spinner="dots2"):
                    time.sleep(5)
        if len(movies) == 0:
            clear()
            print("You have guessed all the movies in this session. Congratulations!", DIV, sep="\n")
            sorted_scoreboard = update_scoreboard(name, total_score, SCOREBOARD)
            header = ['Ranking', 'Username', 'Total Score']
            score_table = []
            for tr in sorted_scoreboard:
                td = [tr['rank'], tr['name'], tr['score']]
                score_table.append(td)
            print(tabulate(score_table, headers=header, tablefmt="grid"))
            print(DIV)
            while True:
                prompt_new_game = input("New Game? [Y/N]:").upper()
                if prompt_new_game in ["Y", "YES"]:
                    break
                elif prompt_new_game in ["N", "NO"]:
                    print(DIV, "Understandable. Have a great day!", DIV, sep="\n")
                    sys.exit()
                else:
                    print(DIV, "Invalid Input. Try again.", DIV, sep="\n")

def validate_name(name):
    """Validates the player's name

    Args:
        name (str): player's name

    Returns:
        bool: return True if conditions are met, else return False
    """
    if 10 >= len(name) >= 4 and name.isalnum():
        return True
    else:
        return False


def validate_diff(get_diff):
    """Validates the player's difficulty input

    Args:
        get_diff (str): player's difficulty input

    Raises:
        ValueError: will occur if player entered a non-integer input

    Returns:
        bool: returns True if player's input is either 1, 2, or 3, else return False
    """
    try:
        if int(get_diff) in [1, 2, 3]:
            return True
        else:
            return False
    except ValueError:
        raise ValueError


def game_area(movies, round):
    """Executes the game

    Args:
        movies (list): a list of dictionary with the following keys: 'title', 'year', and 'genre'
        round (int): current round of the game, starts at 1

    Returns:
        dict: returns a dict which consists of the round's title to be guessed, remaining lives, score, and index of the guessed movie
    """
    clear()
    round_movie = random.choice(movies)
    title, year, genre = round_movie['title'], round_movie['year'], round_movie['genre']
    life = MAX_LIFE
    alpha_text = set(get_alpha(title))
    entered_char = []
    goal = len(alpha_text)
    score = 0
    while True:
        clear()
        print(DIV, f"Round {round}", f"Year: {year}", f"Genre: {genre}", DIV, sep="\n")
        print("Title: ", end="")
        for char in title.upper():
            if char.isalpha() and char not in entered_char:
                print("_", end="")
            else:
                print(char, end="")
        print("\nEntered letters: ", end="")
        for char in entered_char:
            if char in alpha_text:
                console.print(char, style="bold green", end="")
            else:
                console.print(char, style="bold red", end="")
        print("\n" + DIV)
        print("Lives:", "❤️" * life, "❌" * (MAX_LIFE - life))
        if life == 0 or score == goal:
            break
        while True:
            print(DIV)
            letter = input("Enter a letter: ").upper()
            if letter.isalpha() and len(letter) == 1:
                if letter in entered_char:
                    print(DIV, "Letter already entered. Try again.", sep="\n")
                else:
                    break
            else:
                print(DIV, "Invalid input. Try again", sep="\n")
        entered_char.append(letter)
        if letter in alpha_text:
            score += 1
        else:
            life -= 1
    return {
        'answer': title.upper(),
        'life': life,
        'score': life * 10,
        'index': movies.index(round_movie)
    }


def get_alpha(title):
    """Removes non-alphabetic characters from a string"

    Args:
        title (string): the title of the movie to be guessed in the round

    Returns:
        list: returns a list of all letters in the title
    """
    regex = re.compile("[A-Z]")
    return regex.findall(title.upper())


def update_scoreboard(name, score, filename):
    new_row = {
        'name': name,
        'score': score
    }
    with open(filename, 'a') as a_file:
        writer = csv.DictWriter(a_file, fieldnames=['name', 'score'])
        writer.writerow(new_row)
    scores = []
    with open(filename, 'r') as r_file:
        reader = csv.DictReader(r_file)
        for row in reader:
            scores.append(row)
    sorted_scores = sorted(scores, key=lambda score: score['score'])
    for row in sorted_scores:
        i = sorted_scores.index(row)
        row['rank'] = i + 1
    return sorted_scores

def clear():
    """Clears the terminal window"""
    os.system("clear||cls")


if __name__ == "__main__":
    main()
