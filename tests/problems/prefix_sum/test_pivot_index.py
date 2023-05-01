import pytest
from problems.prefix_sum.pivot_index import pivot_index


@pytest.mark.parametrize("nums, expected", [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
    ([-1, -1, -1, 1, 1, -1], -1),
])
def test_pivot_index(nums: list[int], expected):
    assert pivot_index(nums) == expected
