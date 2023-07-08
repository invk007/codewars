import pytest

from problems.strings.last_word_length import last_word_length


@pytest.mark.parametrize("word, expected", [
    (" fly me to the moon  ", 4),
    ("", 0),
    ("   ", 0),
    ("a", 1),
    ("little brown fox", 3)
])
def test_last_word_length(word, expected):
    assert last_word_length(word) == expected