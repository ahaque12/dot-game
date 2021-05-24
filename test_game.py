import pytest
import game


def test_valid_pos():
    assert(game.valid_pos(game.State((1, 1), 1), 1, 1)), "This is a valid position!"
    assert(game.valid_pos(game.State((1, 1), 1), 1, 2)) is False, "This is not a valid position!"
    assert(game.valid_pos(game.State((1, 1), 1), 3, 2)) is False, "This is not a valid position!"


def test_change_turn():
    assert(game.change_turn(1) == 2), "Player 1's changed turn should be player 2!"
    assert(game.change_turn(2) == 1), "Player 2's changed turn should be player 1!"

    with pytest.raises(ValueError):
        game.change_turn(3)


def test_is_end():
    assert(game.is_end(game.State((1, 1), 1)) == 0), "This game has not ended!"
    assert(game.is_end(game.State((0, 0), 1)) == 1), "Player 1 has won!"


def test_maximum():
    assert(game.maximum(game.State((2, 1), 1)) == (1, 0, 2)), "There is only one optimal play!"
    assert(game.maximum(game.State((2, 1), 2)) == (1, 0, 2)), "There is only one optimal play!"

    assert(game.maximum(game.State((1, 0), 2)) == (-1, 0, 1)), "There is only one optimal play, the player loses!"
    val, _, _ = game.maximum(game.State((2, 2), 1))
    assert(val == -1), "This scenario is impossible to win!"


def test_optimal_play():
    assert(game.optimal_play(game.State((2, 3), 1)) == (1, 1, 1)), "There is only one optimal play!"


def test_play():
    assert(game.play(game.State((2, 3), 1), 1, 1) == game.State((2, 2), 2)), "Game state is not valid!"
    with pytest.raises(ValueError):
        game.play(game.State((2, 3), 1), 3, 1)
