import pytest

from problems.stacks.good_string import make_good_string


@pytest.mark.parametrize(
    's, expected', [('leEeetcode', 'leetcode'), ('abBAcC', ''), ('s', 's')]
)
def test_make_good_string(s, expected):
    assert make_good_string(s) == expected
