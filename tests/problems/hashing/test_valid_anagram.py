import pytest

from problems.hashing.valid_anagram import is_anagram


@pytest.mark.parametrize(
    's, t, expected', [('anagram', 'nagaram', True), ('car', 'rat', False)]
)
def test_is_anagram(s, t, expected):
    assert is_anagram(s, t) == expected
