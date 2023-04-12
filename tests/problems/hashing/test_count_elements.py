import pytest

from problems.hashing.count_elements import count_elements


@pytest.mark.parametrize(
    'elements, expected',
    [([1, 2, 3], 2), ([1, 1, 2, 2], 2), ([1, 1, 3, 3, 5, 5, 7, 7], 0)],
)
def test_count_elements(elements, expected):
    assert expected == count_elements(elements)
