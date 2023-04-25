import pytest

from problems.prefix_sum.highest_altitude import highest_altitude


@pytest.mark.parametrize(
    "gain, expected",
    [
        ([-4, -3, -2, -1, 4, 3, 2], 0),
        ([-5, 1, 5, 0, -7], 1)
    ]
)
def test_highest_altitude(gain, expected):
    assert highest_altitude(gain) == expected
