import random

notation = [
    ["R","R'","R2","L","L'","L2"],
    ["U","U'","U2","D","D'","D2"],
    ["F","F'","F2","B","B'","B2"]
]

def generate_scramble():
    available_moves = notation
    scramble = []
    last_move = "nothin"
    last_move_axis = "nothin"
    axis_uses = 0
    for i in range(17):
        axis = random.choice(notation)
        move = random.choice(axis)
        while move[0] == last_move[0]:
            move = random.choice(axis)
        scramble.append(move)
        if len(available_moves) < 3:
            available_moves = notation
        elif axis == last_move_axis:
            axis_uses += 1
            if axis_uses == 2:
                available_moves.remove(axis)
        last_move = move
        last_move_axis = axis
    print(" ".join(scramble))

generate_scramble()