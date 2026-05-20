import sys
from scramble import generate_scramble
from cube import solved_cube, print_cube, apply_moves, find_cross
from splashes import welcome_splash, scramble_splash, cross_splash


def main():
    home()

def home():
    print("\033[2J\033[H", end="")
    print(welcome_splash)
    selection("home")

def scramble_page():
    print("\033[2J\033[H", end="")
    scramble = generate_scramble(17)
    cube = solved_cube
    print(f"\033[1m\nGenerating Scramble...\n\n{" ".join(scramble)}\n\033[0m")
    apply_moves(cube, scramble)
    print_cube(cube)
    selection("scramble")

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
    elif page == "scramble":
        choice = input("\n1. New Scramble\n2. Home Page\n3. Exit\n ")
        if choice == "1":
            scramble_page()
        elif choice == "2":
            home()
        elif choice == "3":
            print("\033[2J\033[H", end="")
            sys.exit(0)

main()