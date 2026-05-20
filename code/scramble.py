import random
import copy

scr_notation = [
    ["R","R'","R2","R2","L","L'","L2","L2"],
    ["U","U'","U2","U2","D","D'","D2","D2"],
    ["F","F'","F2","F2","B","B'","B2","B2"]
]

notation = [
    ["R","R'","R2","L","L'","L2"],
    ["U","U'","U2","D","D'","D2"],
    ["F","F'","F2","B","B'","B2"]
]


def generate_scramble(move_count): #producing ABA patterns
    available_moves = copy.copy(scr_notation)
    scramble = []
    last_move = "nothin"
    last_move_axis = "nothin"
    for i in range(move_count):
        axis = random.choice(available_moves)
        move = random.choice(axis)
        while move[0] == last_move[0]:
            move = random.choice(axis)
        scramble.append(move)
        if len(available_moves) < 3:
            available_moves = copy.copy(scr_notation)
        elif axis == last_move_axis:
            available_moves.remove(axis)
        last_move = move
        last_move_axis = axis
    return scramble

def generate_bf_moves(move_depth, movesets=None):
    if move_depth == 0:
        return movesets
    
    if not movesets:
        initial_movesets = []
        for axis in notation:
            for move in axis:
                initial_movesets.append([move])
        return generate_bf_moves(move_depth - 1, initial_movesets)
    
    else:
        new_movesets = []
        for moveset in movesets:
            for axis in notation:
                if len(moveset) > 1 and (moveset[-1] in axis and moveset[-2] in axis):
                    continue
                elif moveset[-1] in axis:
                    for move in axis:
                        if move[0] != moveset[-1][0]:
                            new_movesets.append(moveset + [move])
                else:
                    for move in axis:
                        new_movesets.append(moveset + [move])
        return generate_bf_moves(move_depth - 1, new_movesets)