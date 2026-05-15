from scramble import generate_scramble

solved_cube = {
    "white": {1: "⬜", 2: "⬜", 3: "⬜", 4: "⬜", 5: "⬜", 6: "⬜", 7: "⬜", 8: "⬜", 9: "⬜"},
    "yellow": {1: "🟨", 2: "🟨", 3: "🟨", 4: "🟨", 5: "🟨", 6: "🟨", 7: "🟨", 8: "🟨", 9: "🟨"},
    "green": {1: "🟩", 2: "🟩", 3: "🟩", 4: "🟩", 5: "🟩", 6: "🟩", 7: "🟩", 8: "🟩", 9: "🟩"},
    "blue": {1: "🟦", 2: "🟦", 3: "🟦", 4: "🟦", 5: "🟦", 6: "🟦", 7: "🟦", 8: "🟦", 9: "🟦"},
    "red": {1: "🟥", 2: "🟥", 3: "🟥", 4: "🟥", 5: "🟥", 6: "🟥", 7: "🟥", 8: "🟥", 9: "🟥"},
    "orange": {1: "🟧", 2: "🟧", 3: "🟧", 4: "🟧", 5: "🟧", 6: "🟧", 7: "🟧", 8: "🟧", 9: "🟧"},
}

default_orientaion = {
    "top": "white",
    "left": "orange",
    "front": "green",
    "right": "red",
    "back": "blue",
    "bottom": "yellow"
}

def print_cube(cube, orientation=default_orientaion):
    for stkr in range(1, 8, 3):
        print(f"      {cube[orientation["top"]][stkr+0]}{cube[orientation["top"]][stkr+1]}{cube[orientation["top"]][stkr+2]}")
    for stkr in range(1, 8, 3):
        print(f"{cube[orientation["left"]][stkr+0]}{cube[orientation["left"]][stkr+1]}{cube[orientation["left"]][stkr+2]}{cube[orientation["front"]][stkr+0]}{cube[orientation["front"]][stkr+1]}{cube[orientation["front"]][stkr+2]}{cube[orientation["right"]][stkr+0]}{cube[orientation["right"]][stkr+1]}{cube[orientation["right"]][stkr+2]}{cube[orientation["back"]][stkr+0]}{cube[orientation["back"]][stkr+1]}{cube[orientation["back"]][stkr+2]}")
    for stkr in range(1, 8, 3):
        print(f"      {cube[orientation["bottom"]][stkr+0]}{cube[orientation["bottom"]][stkr+1]}{cube[orientation["bottom"]][stkr+2]}")


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

    

def move_white(cube):
    side_stickers = [("orange", 1), ("orange", 2), ("orange", 3), ("green", 1), ("green", 2), ("green", 3), ("red", 1), ("red", 2), ("red", 3), ("blue", 1), ("blue", 2), ("blue", 3)]
    cube = cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("white", 4), ("white", 7), ("white", 8), ("white", 9), ("white", 6), ("white", 3), ("white", 2), ("white", 1)]
    cube = cycle_stickers(cube, top_stickers)
    return cube

def move_red(cube):
    side_stickers = [("white", 3), ("white", 6), ("white", 9), ("green", 3), ("green", 6), ("green", 9), ("yellow", 3), ("yellow", 6), ("yellow", 9), ("blue", 7), ("blue", 4), ("blue", 1)]
    cube = cycle_stickers(cube, side_stickers, side=True)
    top_stickers = [("red", 4), ("red", 7), ("red", 8), ("red", 9), ("red", 6), ("red", 3), ("red", 2), ("red", 1)]
    cube = cycle_stickers(cube, top_stickers)
    return cube

def test():
    cube = solved_cube
    for i in range(3):
        move_red(cube)
        move_white(cube)
    print_cube(cube)

test()