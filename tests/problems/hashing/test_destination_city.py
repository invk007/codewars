import pytest

from problems.hashing.destination_city import find_destination_city


@pytest.mark.parametrize(
    'paths, expected',
    [
        (
            [
                ['London', 'New York'],
                ['New York', 'Lima'],
                ['Lima', 'Sao Paulo'],
            ],
            'Sao Paulo',
        ),
        ([['B', 'C'], ['D', 'B'], ['C', 'A']], 'A'),
        ([['A', 'Z']], 'Z'),
    ],
)
def test_find_destination_city(paths, expected):
    assert find_destination_city(paths) == expected
