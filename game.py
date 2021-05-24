import functools
from typing import NamedTuple, Tuple


class State(NamedTuple):
    current_state: Tuple[int, ...]
    player_turn: int

    def __str__(self):
        return "Player turn: {}\n".format(self.player_turn) + \
               "\n".join(["Row {}: ".format(i) +
                          'o'*x for (i, x) in enumerate(self.current_state)])


def valid_pos(state: State, row: int, to_pop: int) -> bool:
    """Determine if position is valid.
    """
    if row < 0 or row >= len(state.current_state):
        return False

    if state.current_state[row] < to_pop or to_pop == 0:
        return False

    return True


def is_end(state: State) -> int:
    """Determine if game has ended and who wins.
    """
    if sum(state.current_state) == 0:
        return state.player_turn

    return 0


def change_turn(turn: int) -> int:
    """Change a player's turn from 1 to 2 and vice versa.
    """
    if turn == 1:
        return 2
    else:
        return 1

    return turn


def optimal_play(state: State) -> Tuple[int, int, int]:
    """Determine optimal move for player.
    """
    val, row, pop = maximum(state, min=state.player_turn != 1)

    # Rows can be different after sorting in
    # descending order. Adjust row to find original row
    # with the same number of dots.
    adjusted_row = row
    sorted_state = sorted(state.current_state, reverse=True)
    for i, dots in enumerate(state.current_state):
        if state.current_state[i] == sorted_state[row]:
            adjusted_row = i
            break

    return (val, adjusted_row, pop)


def sort(func):
    """Sorting decorator to sort state prior to passing to downstream function.
    """
    def wrapper(state: State, **kwargs):
        return func(State(tuple(sorted(state.current_state, reverse=True)),
                          state.player_turn
                          ),
                          **kwargs 
                    )
    return wrapper


@sort
@functools.lru_cache(maxsize=2**20)
def maximum(state: State, min=False) -> Tuple[int, int, int]:
    """Find the move that minimizes player 1's likelihood of winning.

    If min is true then this will minimize player 1's likelihood of winning.
    """
    # "Worst" value to benchmark against.
    maxv = 2 if min else -2
    result = is_end(state)

    if result == 1:
        return (1, 0, 0)
    elif result == 2:
        return (-1, 0, 0)

    for i in range(len(state.current_state)):
        for j in range(1, state.current_state[i] + 1):
            new_state = play(state, i, j)

            (m, min_row, min_pop) = maximum(new_state, min=not min)

            if (not min) and (m > maxv):
                maxv = m
                prow = i
                ppop = j

            if min and (m < maxv):
                maxv = m
                prow = i
                ppop = j

    return (maxv, prow, ppop)


def play(state: State, row: int, pop: int) -> State:
    """Play a move in the given state.

    If a move is invalid an error is raised.
    """
    if not valid_pos(state, row, pop):
        raise ValueError("Invalid input!")

    current_state = list(state.current_state)
    current_state[row] -= pop
    state = State(tuple(current_state), change_turn(state.player_turn))
    return state
