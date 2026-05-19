import sys
#from scramble import generate_scramble
#from cube import solved_cube
from splashes import welcome_splash


def main():
    home()

def home():
    print("\033[2J\033[H", end="")
    print(welcome_splash)
    selection("home")

def scramble_page():
    pass

def cross_puzzle():
    pass

def selection(page):
    if page == "home":
        choice = input("1. Generate Scramble\n2. Cross Puzzle\n3. Exit\n")
        if choice == "1":
            scramble_page()
        elif choice == "2":
            cross_puzzle()
        elif choice == "3":
            print("\033[2J\033[H", end="")
            sys.exit(0)

main()