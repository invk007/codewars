import pytest

from problems.hashing.max_num_of_ballons import max_num_of_balloons


@pytest.mark.parametrize("string, expected", [
    ('nlaebolko', 1),
    ('loonbalxballpoon', 2),
    ('leetcode', 0),
])
def test_max_num_of_balloons(string: str, expected: int):
    assert max_num_of_balloons(string) == expected
