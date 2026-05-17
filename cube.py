from scramble import generate_scramble

solved_cube = {
    "top": {1: "⬜", 2: "⬜", 3: "⬜", 4: "⬜", 5: "⬜", 6: "⬜", 7: "⬜", 8: "⬜", 9: "⬜"},
    "bottom": {1: "🟨", 2: "🟨", 3: "🟨", 4: "🟨", 5: "🟨", 6: "🟨", 7: "🟨", 8: "🟨", 9: "🟨"},
    "front": {1: "🟩", 2: "🟩", 3: "🟩", 4: "🟩", 5: "🟩", 6: "🟩", 7: "🟩", 8: "🟩", 9: "🟩"},
    "back": {1: "🟦", 2: "🟦", 3: "🟦", 4: "🟦", 5: "🟦", 6: "🟦", 7: "🟦", 8: "🟦", 9: "🟦"},
    "right": {1: "🟥", 2: "🟥", 3: "🟥", 4: "🟥", 5: "🟥", 6: "🟥", 7: "🟥", 8: "🟥", 9: "🟥"},
    "left": {1: "🟧", 2: "🟧", 3: "🟧", 4: "🟧", 5: "🟧", 6: "🟧", 7: "🟧", 8: "🟧", 9: "🟧"},
}

def print_cube(cube):
    for stkr in range(1, 8, 3):
        print(f"      {cube["top"][stkr+0]}{cube["top"][stkr+1]}{cube["top"][stkr+2]}")
    for stkr in range(1, 8, 3):
        print(f"{cube["left"][stkr+0]}{cube["left"][stkr+1]}{cube["left"][stkr+2]}{cube["front"][stkr+0]}{cube["front"][stkr+1]}{cube["front"][stkr+2]}{cube["right"][stkr+0]}{cube["right"][stkr+1]}{cube["right"][stkr+2]}{cube["back"][stkr+0]}{cube["back"][stkr+1]}{cube["back"][stkr+2]}")
    for stkr in range(1, 8, 3):
        print(f"      {cube["bottom"][stkr+0]}{cube["bottom"][stkr+1]}{cube["bottom"][stkr+2]}")


def cycle_stickers(cube, stickers, side=False):
    if side == True:
        temp_stkrs = stickers[:3]
        new_placement = stickers[3:] + temp_stkrs
    else:
        temp_stkrs = stickers[:2]
        new_placement = stickers[2:] + temp_stkrs

    new_placement_raw_data = []
    for i in range(0, len(stickers)):
        new_placement_raw_data.append(cube[new_placement[i][0]][new_placement[i][1]])

    for i in range(0, len(stickers)):
        cube[stickers[i][0]][stickers[i][1]] = new_placement_raw_data[i]
    return cube

    
def move_top(cube):
    side_stickers = [("left", 1), ("left", 2), ("left", 3), ("front", 1), ("front", 2), ("front", 3), ("right", 1), ("right", 2), ("right", 3), ("back", 1), ("back", 2), ("back", 3)]
    cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("top", 4), ("top", 7), ("top", 8), ("top", 9), ("top", 6), ("top", 3), ("top", 2), ("top", 1)]
    cycle_stickers(cube, top_stickers)

def move_bottom(cube):
    side_stickers = [("back", 9), ("back", 8), ("back", 7), ("right", 9), ("right", 8), ("right", 7), ("front", 9), ("front", 8), ("front", 7), ("left", 9), ("left", 8), ("left", 7)]
    cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("bottom", 4), ("bottom", 7), ("bottom", 8), ("bottom", 9), ("bottom", 6), ("bottom", 3), ("bottom", 2), ("bottom", 1)]
    cycle_stickers(cube, top_stickers)

def move_right(cube):
    side_stickers = [("top", 3), ("top", 6), ("top", 9), ("front", 3), ("front", 6), ("front", 9), ("bottom", 3), ("bottom", 6), ("bottom", 9), ("back", 7), ("back", 4), ("back", 1)]
    cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("right", 4), ("right", 7), ("right", 8), ("right", 9), ("right", 6), ("right", 3), ("right", 2), ("right", 1)]
    cycle_stickers(cube, top_stickers)

def move_left(cube):
    side_stickers = [("bottom", 7), ("bottom", 4), ("bottom", 1), ("front", 7), ("front", 4), ("front", 1), ("top", 7), ("top", 4), ("top", 1), ("back", 3), ("back", 6), ("back", 9)]
    cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("left", 4), ("left", 7), ("left", 8), ("left", 9), ("left", 6), ("left", 3), ("left", 2), ("left", 1)]
    cycle_stickers(cube, top_stickers)

def move_front(cube):
    side_stickers = [("bottom", 1), ("bottom", 2), ("bottom", 3), ("right", 7), ("right", 4), ("right", 1), ("top", 9), ("top", 8), ("top", 7), ("left", 3), ("left", 6), ("left", 9)]
    cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("front", 4), ("front", 7), ("front", 8), ("front", 9), ("front", 6), ("front", 3), ("front", 2), ("front", 1)]
    cycle_stickers(cube, top_stickers)

def move_back(cube):
    side_stickers = [("left", 7), ("left", 4), ("left", 1), ("top", 1), ("top", 2), ("top", 3), ("right", 3), ("right", 6), ("right", 9), ("bottom", 9), ("bottom", 8), ("bottom", 7)]
    cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("back", 4), ("back", 7), ("back", 8), ("back", 9), ("back", 6), ("back", 3), ("back", 2), ("back", 1)]
    cycle_stickers(cube, top_stickers)


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


def test():
    cube = solved_cube
    scramble = generate_scramble(17)
    print_cube(cube)
    print(f"Applying scramble:\n{" ".join(scramble)}")
    apply_moves(cube, scramble)
    print_cube(cube)

test()