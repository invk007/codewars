import pytest

from problems.hashing.longest_substr import len_of_longest_substr


@pytest.mark.parametrize(
    's, expected', [('abcabcbb', 3), ('bbbbb', 1), ('pwwkew', 3)]
)
def test_len_of_longest_substr(s: str, expected: int):
    assert len_of_longest_substr(s) == expected
