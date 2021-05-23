import argparse
import game


def clean_state(state_str):
    """Clean string representing state.
    """
    state_list = state_str.split()
    for item in state_list:
        if not item.isdigit():
            return None
    state_list = [int(x) for x in state_list]

    return tuple(state_list)
    
def play_computer(state):
    """Play game with computer.
    """
    while True:
        print(state)
        if state.player_turn == 1:
            print("Your turn")
            row = int(input("Choose row to pop: "))
            pop = int(input("Choose pop to pop: "))
        else:
            val, row, pop = game.minimum(state)
        print("Play:", row, pop)
        state = game.play(state, row, pop)
        if game.is_end(state) != 0:
            print("Congrats to player", state.player_turn)
            break

def main():
    parser = argparse.ArgumentParser("Play the dot game.")
    parser.add_argument('--initial_state', type=int, nargs='+',
                        default=[2, 4, 5, 5, 5, 5, 5, 1],
                        help='Initial state of the game.')
    args = parser.parse_args()

    initial_state = game.State(tuple(args.initial_state), 1)

    print("Starting state...")
    print(initial_state)

    # Play multiple games with computer.
    # All results are cached.
    while True:
        answer = input("Do you want to play a game [Y/N, Default: Y]? ")
        if answer != "Y" and answer != "":
            break
        play_computer(initial_state)
    print("It was fun playing!")

    # Interactively get hints.
    while True:
        answer = input("Do you want a hint [Y/N, Default: Y]? ")
        if answer != "Y" and answer != "":
            break
        player = input("Are you player 1 or 2 [Default: 1? ")
        if player == "":
            player = 1
        else:
            player = int(player)

        while True:
            state = input("What is the current state of the game (insert space delimited sequence e.g. '2 2 1')? ")
            state = clean_state(state) 
            if state is not None:
                break
            else:
                print("Invalid state, try again")
        state = game.State(state, player)
        if player == 1:
            print(game.maximum(state))
        else:
            print(game.minimum(state))

if __name__ == "__main__":
    main()