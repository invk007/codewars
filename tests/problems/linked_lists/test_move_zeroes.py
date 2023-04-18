import pytest

from problems.two_pointers.move_zeroes import move_zeroes


@pytest.mark.parametrize("input, expected", [
    ([0, 1, 0, 12, 3], [1, 12, 3, 0, 0]),
    ([0], [0]),
    ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
])
def test_move_zeroes(input: list[int], expected: list[int]):
    assert move_zeroes(input) == expected
