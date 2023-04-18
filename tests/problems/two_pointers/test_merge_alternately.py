import pytest

from problems.two_pointers.merge_alternately import merge_alternately


@pytest.mark.parametrize("word_1, word_2, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
])
def test_merge_alternately(word_1: str, word_2: str, expected: str):
    assert merge_alternately(word_1, word_2) == expected
