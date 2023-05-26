import pytest

from problems.hashing.group_anagrams import group_anagrams


@pytest.mark.parametrize(
    'strs, expected',
    [
        (
            ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
            [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']],
        ),
        ([''], [['']]),
        (['a'], [['a']]),
    ],
)
def test_group_anagrams(strs, expected):
    result = group_anagrams(strs)

    sorted_expected = [sorted(lst) for lst in sorted(expected, key=len)]
    sorted_result = [sorted(lst) for lst in sorted(result, key=len)]

    assert sorted_expected == sorted_result
