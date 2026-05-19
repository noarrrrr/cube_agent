import copy
from enum import Enum
import time
import cProfile
from scramble import generate_scramble, generate_bf_moves

solved_cube = [
    0,0,0,0,0,0,0,0,0,  #bottom/white
    1,1,1,1,1,1,1,1,1,  #top/yellow
    2,2,2,2,2,2,2,2,2,  #left/red
    3,3,3,3,3,3,3,3,3,  #right/orange
    4,4,4,4,4,4,4,4,4,  #front/green
    5,5,5,5,5,5,5,5,5,  #back/blue
]

stkrs = ["⬜", "🟨", "🟥", "🟧", "🟩", "🟦"]

def print_cube(cube):
    print(f"""      {stkrs[cube[9]]}{stkrs[cube[10]]}{stkrs[cube[11]]}
      {stkrs[cube[12]]}{stkrs[cube[13]]}{stkrs[cube[14]]}
      {stkrs[cube[15]]}{stkrs[cube[16]]}{stkrs[cube[17]]}
{stkrs[cube[18]]}{stkrs[cube[19]]}{stkrs[cube[20]]}{stkrs[cube[36]]}{stkrs[cube[37]]}{stkrs[cube[38]]}{stkrs[cube[27]]}{stkrs[cube[28]]}{stkrs[cube[29]]}{stkrs[cube[45]]}{stkrs[cube[46]]}{stkrs[cube[47]]}
{stkrs[cube[21]]}{stkrs[cube[22]]}{stkrs[cube[23]]}{stkrs[cube[39]]}{stkrs[cube[40]]}{stkrs[cube[41]]}{stkrs[cube[30]]}{stkrs[cube[31]]}{stkrs[cube[32]]}{stkrs[cube[48]]}{stkrs[cube[49]]}{stkrs[cube[50]]}
{stkrs[cube[24]]}{stkrs[cube[25]]}{stkrs[cube[26]]}{stkrs[cube[42]]}{stkrs[cube[43]]}{stkrs[cube[44]]}{stkrs[cube[33]]}{stkrs[cube[34]]}{stkrs[cube[35]]}{stkrs[cube[51]]}{stkrs[cube[52]]}{stkrs[cube[53]]}
      {stkrs[cube[0]]}{stkrs[cube[1]]}{stkrs[cube[2]]}
      {stkrs[cube[3]]}{stkrs[cube[4]]}{stkrs[cube[5]]}
      {stkrs[cube[6]]}{stkrs[cube[7]]}{stkrs[cube[8]]}""")
    


    
def move_top(cube):
    cube[9], cube[10], cube[11], cube[14], cube[17], cube[16], cube[15], cube[12] = cube[15], cube[12], cube[9], cube[10], cube[11], cube[14], cube[17], cube[16]
    cube[47], cube[46], cube[45], cube[29], cube[28], cube[27], cube[38], cube[37], cube[36], cube[20], cube[19], cube[18] = cube[20], cube[19], cube[18], cube[47], cube[46], cube[45], cube[29], cube[28], cube[27], cube[38], cube[37], cube[36]

def move_bottom(cube):
    cube[0], cube[1], cube[2], cube[5], cube[8], cube[7], cube[6], cube[3] = cube[6], cube[3], cube[0], cube[1], cube[2], cube[5], cube[8], cube[7]
    cube[42], cube[43], cube[44], cube[33], cube[34], cube[35], cube[51], cube[52], cube[53], cube[24], cube[25], cube[26] = cube[24], cube[25], cube[26], cube[42], cube[43], cube[44], cube[33], cube[34], cube[35], cube[51], cube[52], cube[53]

def move_right(cube):
    cube[27], cube[28], cube[29], cube[32], cube[35], cube[34], cube[33], cube[30] = cube[33], cube[30], cube[27], cube[28], cube[29], cube[32], cube[35], cube[34]
    cube[17], cube[14], cube[11], cube[45], cube[48], cube[51], cube[8], cube[5], cube[2], cube[44], cube[41], cube[38] = cube[44], cube[41], cube[38], cube[17], cube[14], cube[11], cube[45], cube[48], cube[51], cube[8], cube[5], cube[2]

def move_left(cube):
    cube[18], cube[19], cube[20], cube[23], cube[26], cube[25], cube[24], cube[21] = cube[24], cube[21], cube[18], cube[19], cube[20], cube[23], cube[26], cube[25]
    cube[9], cube[12], cube[15], cube[36], cube[39], cube[42], cube[0], cube[3], cube[6], cube[53], cube[50], cube[47] = cube[53], cube[50], cube[47], cube[9], cube[12], cube[15], cube[36], cube[39], cube[42], cube[0], cube[3], cube[6]

def move_front(cube):
    cube[36], cube[37], cube[38], cube[41], cube[44], cube[43], cube[42], cube[39] = cube[42], cube[39], cube[36], cube[37], cube[38], cube[41], cube[44], cube[43]
    cube[15], cube[16], cube[17], cube[27], cube[30], cube[33], cube[2], cube[1], cube[0], cube[26], cube[23], cube[20] = cube[26], cube[23], cube[20], cube[15], cube[16], cube[17], cube[27], cube[30], cube[33], cube[2], cube[1], cube[0]

def move_back(cube):
    cube[45], cube[46], cube[47], cube[50], cube[53], cube[52], cube[51], cube[48] = cube[51], cube[48], cube[45], cube[46], cube[47], cube[50], cube[53], cube[52]
    cube[11], cube[10], cube[9], cube[18], cube[21], cube[24], cube[6], cube[7], cube[8], cube[35], cube[32], cube[29] = cube[35], cube[32], cube[29], cube[11], cube[10], cube[9], cube[18], cube[21], cube[24], cube[6], cube[7], cube[8]


def apply_moves(cube, moves):
    for move in moves:
        if move == "R":
            move_right(cube)
        elif move == "R'":
            for _ in range(3):
                move_right(cube)
        elif move == "R2":
            for _ in range(2):
                move_right(cube)
        
        elif move == "L":
            move_left(cube)
        elif move == "L'":
            for _ in range(3):
                move_left(cube)
        elif move == "L2":
            for _ in range(2):
                move_left(cube)

        elif move == "U":
            move_top(cube)
        elif move == "U'":
            for _ in range(3):
                move_top(cube)
        elif move == "U2":
            for _ in range(2):
                move_top(cube)

        elif move == "D":
            move_bottom(cube)
        elif move == "D'":
            for _ in range(3):
                move_bottom(cube)
        elif move == "D2":
            for _ in range(2):
                move_bottom(cube)
        
        elif move == "F":
            move_front(cube)
        elif move == "F'":
            for _ in range(3):
                move_front(cube)
        elif move == "F2":
            for _ in range(2):
                move_front(cube)

        elif move == "B":
            move_back(cube)
        elif move == "B'":
            for _ in range(3):
                move_back(cube)
        elif move == "B2":
            for _ in range(2):
                move_back(cube)

def reverse_moves(cube, moves):
    for move in reversed(moves):
        if move == "R'":
            move_right(cube)
        elif move == "R":
            for _ in range(3):
                move_right(cube)
        elif move == "R2":
            for _ in range(2):
                move_right(cube)
        
        elif move == "L'":
            move_left(cube)
        elif move == "L":
            for _ in range(3):
                move_left(cube)
        elif move == "L2":
            for _ in range(2):
                move_left(cube)

        elif move == "U'":
            move_top(cube)
        elif move == "U":
            for _ in range(3):
                move_top(cube)
        elif move == "U2":
            for _ in range(2):
                move_top(cube)

        elif move == "D'":
            move_bottom(cube)
        elif move == "D":
            for _ in range(3):
                move_bottom(cube)
        elif move == "D2":
            for _ in range(2):
                move_bottom(cube)
        
        elif move == "F'":
            move_front(cube)
        elif move == "F":
            for _ in range(3):
                move_front(cube)
        elif move == "F2":
            for _ in range(2):
                move_front(cube)

        elif move == "B'":
            move_back(cube)
        elif move == "B":
            for _ in range(3):
                move_back(cube)
        elif move == "B2":
            for _ in range(2):
                move_back(cube)


def find_cross(cube):
    solution_found = False
    solution_count = 0
    for depth in range(1, 6):
        print(f"Searching {depth} moves deep")
        possible_solutions = generate_bf_moves(depth)
        for moves in possible_solutions:
            if check_for_cross(cube, moves):
                if solution_count < 3:
                    print(f"Found Solution!\n{" ".join(moves)}")
                    apply_moves(cube, moves)
                    print_cube(cube)
                    reverse_moves(cube, moves)
                    solution_count += 1
                    solution_found = True
                else:
                    return
        if solution_found == True:
            return

        
    print("Something's amiss")

def check_for_cross(cube, moves):
    apply_moves(cube, moves)
    if (
        cube[1] == 0 and
        cube[5] == 0 and
        cube[7] == 0 and
        cube[3] == 0 and
        cube[43] == 4 and
        cube[34] == 3 and
        cube[52] == 5 and
        cube[25] == 2
    ):
        reverse_moves(cube, moves)
        return True
    reverse_moves(cube, moves)
    return False



def test():
    cube = solved_cube
    scramble = generate_scramble(17)
    #print_cube(cube)
    #print_cube(cube)
    print(f"Applying scramble:\n{" ".join(scramble)}")
    apply_moves(cube, scramble)
    print_cube(cube)
    print("Searching for White Cross...")
    cProfile.run(f"find_cross({cube})")

test()