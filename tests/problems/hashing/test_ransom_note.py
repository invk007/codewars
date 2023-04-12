import pytest

from problems.hashing.ransom_note import can_construct


@pytest.mark.parametrize(
    'note, magazine, expected', [('aa', 'aab', True), ('aa', 'ab', False)]
)
def test_can_construct(note, magazine, expected):
    assert can_construct(note, magazine) == expected
