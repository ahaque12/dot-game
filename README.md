# Dot Game
The dot game is a game where two players have a grid of dots that can be pressed in. Each
row in the grid can have an arbitrary number of dots. On each player's turn, they can 
press in as many dots as they'd like, as long as the dots are within the same row. Players must press in at least
one dot on their turn. Whichever player presses in the last dot loses.

## Playing a game
To play a game with the AI 

```bash
> python main.py --initial_state 2 3
Starting state...
State(current_state=(2, 3), player_turn=1)
Do you want to play a game [Y/N, Default: Y]?
State(current_state=(2, 3), player_turn=1)
Your turn
Choose row to pop: 1
Choose pop to pop: 1
Play: 1 1
State(current_state=(2, 2), player_turn=2)
Play: 0 1
State(current_state=(1, 2), player_turn=1)
Your turn
Choose row to pop: 1
Choose pop to pop: 2
Play: 1 2
State(current_state=(1, 0), player_turn=2)
Play: 0 1
Congrats to player 1
Do you want to play a game [Y/N, Default: Y]? N
It was fun playing!
```

After completing a game you are prompted with the option of playing a new game. If the answer is no, you can then request hints for different moves to play based on the state of the game. This can be used to assist you in gameplay against another human.

Responses for each hint is (Outcome assuming optimal play [1: Player 1 wins, 2: Player 1 loses], row, number of dots to push).

```bash
Do you want a hint [Y/N, Default: Y]?
Are you player 1 or 2 [Default: 1?
What is the current state of the game (insert space delimited sequence e.g. '2 2 1')? 2 3
(1, 1, 1)
Do you want a hint [Y/N, Default: Y]?
Are you player 1 or 2 [Default: 1? 2
What is the current state of the game (insert space delimited sequence e.g. '2 2 1')? 2 2
(1, 0, 1)
Do you want a hint [Y/N, Default: Y]? N
```