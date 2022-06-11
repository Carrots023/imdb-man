import os

# A str that acts as a divider
DIV = "~" * 20

# Game's difficulty levels
DIF = f"""
[1] I'm sure you know at least 80{chr(37)} of the movies here. Kinda basic.
[2] Hmm, so you like movies a lot, huh? Interesting.
[3] You know these movies?!
"""


def main():
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
                break
            else:
                print(DIV, "See the numbers inside the square brackets? Let's try again.", DIV, sep="\n")
        except:
            print(DIV, "See the numbers inside the square brackets? Let's try again.", DIV, sep="\n")

    print("TODO")


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
        ValueError: Will occur if player entered a non-integer input

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


def clear():
    """Clears the terminal window
    """
    os.system("clear||cls")


if __name__ == "__main__":
    main()
