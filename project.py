import os

DIV = "~" * 20


def main():
    clear()
    print("🎥 Welcome to [IMDb]Man!~~ 🎥", DIV, sep="\n")
    while True:
        name = input("Tell me your name: ")
        if validate_name(name):
            clear()
            print(f"Hello, {name}! Choose the game's difficulty.")
            break
        else:
            print(DIV, "Your name should be 4 to 10 characters long and only consist of alphanumeric characters. I'll ask you again.", DIV, sep="\n")


def validate_name(name):
    if 10 >= len(name) >= 4 and name.isalnum():
        return True
    else:
        return False


def clear():
    os.system("cls||clear")


if __name__ == "__main__":
    main()