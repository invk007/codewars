import pytest

from problems.hashing.sum_of_unique_elements import sum_unique_elements


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 2, 3, 2], 4),
        ([1, 1, 1, 1, 1], 0),
        ([1, 2, 3, 4, 5], 15),
    ],
)
def test_sum_unique_elements(nums: list[int], expected: int):
    assert sum_unique_elements(nums) == expected
