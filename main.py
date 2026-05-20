import sys
import copy
from scramble import generate_scramble
from cube import solved_cube, print_cube, print_cube_transformation, apply_moves, find_cross
from splashes import welcome_splash, cross_splash


def main():
    home()

def home():
    print("\033[2J\033[H", end="")
    print(welcome_splash)
    selection("home")

def scramble_page():
    print("\033[2J\033[H", end="")
    scramble = generate_scramble(17)
    cube = copy.copy(solved_cube)
    print(f"\033[1m\nScramble applied with green in front and yellow on top.\n\n{" ".join(scramble)}\n\033[0m")
    apply_moves(cube, scramble)
    print_cube(cube)
    selection("scramble")

def cross_finder():
    print("\033[2J\033[H", end="")
    print(cross_splash)
    print(f"\033[1mFinding suitable scramble...\n\nThis could take a minute on slow PCs!\n\033[0m")
    print("""The white cross is the first and most intuitive step of solving the Rubik's Cube.
Cross Finder is a tool to help users find efficient ways to solve the cross.
This step can take up to 8 moves to solve, but due to the speed limitations of Python,
you will only be working with cross solutions of 5 or less moves.""")
    scramble, solution = find_cross()
    cube = copy.copy(solved_cube)
    input(f"\033[1m\nFound Scramble! Press Enter to Continue\n\033[0m")
    print("\033[2J\033[H", end="")
    print(f"\033[1m\nScramble applied with green in front and yellow on top.\n\n{" ".join(scramble)}\n\033[0m")
    apply_moves(cube, scramble)
    print_cube(cube)
    input(f"\nCross can be solved in {len(solution)} moves!\n\nPress Enter to See Solution\n")
    print("\033[2J\033[H", end="")
    print(f"\033[1m\nSolution:\n\n{" ".join(solution)}\n\033[0m")
    print_cube_transformation(cube, solution)
    selection("cross")

def selection(page):
    if page == "home":
        choice = input("1. Generate Scramble\n2. Cross Finder\n3. Exit\n")
        if choice == "1":
            scramble_page()
        elif choice == "2":
            cross_finder()
        elif choice == "3":
            print("\033[2J\033[H", end="")
            sys.exit(0)
    elif page == "scramble":
        choice = input("\n1. New Scramble\n2. Home Page\n3. Exit\n")
        if choice == "1":
            scramble_page()
        elif choice == "2":
            home()
        elif choice == "3":
            print("\033[2J\033[H", end="")
            sys.exit(0)
    elif page == "cross":
        choice = input("1. New Cross\n2. Home Page\n3. Exit\n")
        if choice == "1":
            cross_finder()
        elif choice == "2":
            home()
        elif choice == "3":
            print("\033[2J\033[H", end="")
            sys.exit(0)

main()