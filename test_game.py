from game import *

def test_valid_pos():
    assert(valid_pos(State((1, 1), 1), 1, 1)), "This is a valid position!"
    assert(valid_pos(State((1, 1), 1), 1, 2)) is False, "This is not a valid position!"