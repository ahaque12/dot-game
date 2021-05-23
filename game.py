import functools
from typing import NamedTuple, Tuple


class State(NamedTuple):
    current_state: Tuple[int, ...]
    player_turn: int


def valid_pos(state: State, row: int, to_pop: int) -> bool:
    if row < 0 or row >= len(state.current_state):
        return False

    if state.current_state[row] < to_pop or to_pop == 0:
        return False

    return True


def is_end(state: State):
    if sum(state.current_state) == 0:
        return state.player_turn

    return 0


def change_turn(turn: int):
    if turn == 1:
        return 2
    else:
        return 1

    return turn


def sort(func):
    def wrapper(state: State):
        return func(State(tuple(sorted(state.current_state, reverse=True)),
                          state.player_turn
                          )
                    )
    return wrapper


# @sort
@functools.lru_cache(maxsize=2**20)
def maximum(state: State):

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


# @sort
@functools.lru_cache(maxsize=2**20)
def minimum(state: State):
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


def play(state: State, row: int, pop: int) -> State:
    if not valid_pos(state, row, pop):
        raise ValueError("Invalid input!")

    current_state = list(state.current_state)
    current_state[row] -= pop
    current_state.sort(reverse=True)
    state = State(tuple(current_state), change_turn(state.player_turn))
    return state
