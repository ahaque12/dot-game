import game

def test_valid_pos():
    assert(game.valid_pos(game.State((1, 1), 1), 1, 1)), "This is a valid position!"
    assert(game.valid_pos(game.State((1, 1), 1), 1, 2)) is False, "This is not a valid position!"

def test_change_turn():
    assert(game.change_turn(1) == 2), "Player 1's changed turn should be player 2!"
    assert(game.change_turn(2) == 1), "Player 2's changed turn should be player 1!"

def test_is_end():
    assert(game.is_end(game.State((1, 1), 1)) == 0), "This game has not ended!"
    assert(game.is_end(game.State((0, 0), 1)) == 1), "Player 1 has won!"

def test_maximum():
    assert(game.maximum(game.State((2, 1), 1)) == (1, 0, 2)), "There is only one optimal play!"

    val, _, _ = game.maximum(game.State((2, 2), 1))
    assert(val == -1), "This scenario is impossible to win!"
