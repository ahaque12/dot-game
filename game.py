import functools
from collections import namedtuple


State = namedtuple("State", "current_state player_turn")

def valid_pos(state, row : int, to_pop : int):
    if row < 0 or row >= len(state.current_state):
        return False

    if state.current_state[row] < to_pop or to_pop == 0:
        return False

    return True

def is_end(state):
    
    if sum(state.current_state) == 0:
        return state.player_turn

    return 0

def change_turn(turn: int):
    if turn == 1:
        return 2
    else:
        return 1

    return turn

@functools.lru_cache(maxsize=2**20)
def maximum(state):

    maxv = -2
    result = is_end(state)

    if result == 1:
        return (1, 0, 0)
    elif result == 2:
        return (-1, 0, 0)

    for i in range(len(state.current_state)):
        for j in range(1, state.current_state[i] + 1):            
            new_state = play(state, i, j)

            (m, min_row, min_pop) = minimum(new_state)

            if m > maxv:
                maxv = m
                prow = i
                ppop = j

    return (maxv, prow, ppop)

@functools.lru_cache(maxsize=2**20)
def minimum(state):
    minv = 2
    result = is_end(state)

    if result == 1:
        return (1, 0, 0)
    elif result == 2:
        return (-1, 0, 0)

    for i in range(len(state.current_state)):
        for j in range(1, state.current_state[i] + 1):

            new_state = play(state, i, j)
            (m, max_row, max_pop) = maximum(new_state)
            if m < minv:
                minv = m
                prow = i
                ppop = j


    return (minv, prow, ppop)

def play(state, row, pop):
    if not valid_pos(state, row, pop):
        raise ValueError("Invalid input!")

    current_state = list(state.current_state)
    current_state[row] -= pop
    state = State(tuple(current_state), change_turn(state.player_turn))
    return state