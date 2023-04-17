import pytest

from problems.hashing.largest_unique import largest_unique_num


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([5, 7, 3, 9, 4, 9, 8, 3, 1], 8),
        ([9, 9, 8, 8], -1),
    ],
)
def test_larget_unique_num(nums: list[int], expected: int):
    assert largest_unique_num(nums) == expected
