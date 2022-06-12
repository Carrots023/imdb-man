# IMDb-Man
#### Video Demo: [https://youtu.be/C_0hZQj-UH4](https://youtu.be/C_0hZQj-UH4)
## Description
IMDb-Man is my final project for CS50's Introduction to Programming with Python. This project is inspired by the popular kid's game, Hangman, but the words to be guessed are scraped from IMDb.com using BeautifulSoup.

## Folder Contents
- **project.py**: This is the file which contains my ```main``` function and the other functions necessary to implement the game.
- **scraper.py** : This file contains the functions that I used to scrape movie data from IMDb.com.
- **scoreboard.csv**: This file stores the players' names and their final scores after each game.
- **requirements.txt**: All ```pip```-installable libraries that I used for this project are listed here.
- **test_project.py**: This file contains my test functions for project.py.
- **test_scraper.py**: This file contains my test functions for scraper.py.

## Libraries Used
- ```rich``` : for spinners while a task is being executed as well as for differentiating correct letter inputs in the game (red font color for incorrect guesses, while green for the correct ones)
- ```tabulate``` : for printing a scoreboard with all the players' names and scores shown and ranked
- ```beautifulsoup4``` : for scraping movie data from IMDb.com
- ```pytest``` : for testing functions

## Game Mechanics
- Run the program via
    ```
    python project.py
    ```
- Enter your preferred username when prompted. A valid username consists of alphanumeric characters and is 4-10 characters long. You'll be reprompted continuously until a valid username is entered.
- Choose a game difficulty from ```1``` to ```3```, with ```1``` being the easy mode and ```3``` as the (somehow) hard mode. The easy mode has movie titles that have higher popularity, while the hard mode has ones with lower popularity.
- After a few seconds, the game area will be loaded and the movie title to be guessed will be shown as a series of underscores. The goal is to enter all the correct letters before your life runs out until the full title is uncovered.
- At the start of each round, you'll be given 7 hearts, which will decrease each time you enter an incorrect letter. A round will be finished when the movie title is fully uncovered.
- After each round, your score will be computed as follows: ```remaining hearts * 10 * difficulty (1, 2, or 3)```
- The game will end when your hearts fall down to zero. Your final score will be the sum of all the points you gained after each round.
- A scoreboard will be shown at the end of the game, wherein you can see your ranking among other players.
- You'll then be asked if you wish to start a new game or end the program.

## Documentation
### project.py Functions (excluding main)
```python
def validate_name(name):
```
**Description:**
- Validates the player's name.

**Args:**
- ```name``` (```str```): player's name

**Returns:**
- ```bool```: return ```True``` if conditions are met, else return ```False```
```python
def validate_diff(get_diff):
```
**Description:**
- Validates the player's difficulty input

**Args:**
- ```get_diff``` (```str```): player's difficulty input

**Raises:**
- ```ValueError```: will occur if player entered a non-integer input

**Returns:**
- ```bool```: returns ```True``` if player's input is either ```1```, ```2```, or ```3```, else return ```False```
```python
def game_area(movies, round):
```
**Description:**
- Executes the game

**Args:**
- ```movies``` (```list```): a list of dictionary with the following keys: ```'title'```, ```'year'```, and ```'genre'```
- ```round``` (```int```): current round of the game, starts at ```1```

**Returns:**
- ```dict```: returns a dictionary which consists of the round's title to be guessed, remaining lives, score, and index of the guessed movie
```python
def get_alpha(title):
```
**Description:**
- Removes non-alphabetic characters from a string"

**Args:**
- ```title``` (```str```): the title of the movie to be guessed in the round

**Returns:**
- ```list```: returns a list of all letters in the title
```python
def update_scoreboard(name, score, filename):
```
**Description:**
- Stores the player's name and score in the scoreboard

**Args:**
- ```name``` (```str```): player's name
- ```score``` (```int```): player's final score
- ```filename``` (```str```): filename of the scoreboard

**Returns:**
- ```list```: returns a list of dictionary, sorted by score, descending, with column for ranking

### scraper.py Functions
```python
def get_movies(diff) -> list:
```
**Description:**
- Scrapes movie data from IMDb.com

**Args:**
- ```diff``` (```int```): the difficulty level that the player entered

**Returns:**
- ```list```: returns a list of dictionary with the following keys: ```'title'```, ```'year'```, and ```'genre'```

```python
def get_params(d) -> dict:
```
**Description**
- Gets the query parameters for scraping movie data from IMDb.com

**Args:**
- ```d``` (```int```): the difficulty level that the player entered

**Returns:**
- ```dict```: returns query parameters depending on the player's chosen difficulty level

```python
def get_total(url) -> int:
```
**Description**
- Gets the total number of movies that fit the query parameters

**Args:**
- ```url``` (```str```): the url of IMDb.com with the query parameters

**Returns:**
- ```int```: returns the total movies that can be scraped