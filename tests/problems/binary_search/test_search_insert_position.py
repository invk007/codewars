import pytest


from problems.binary_search.search_insert_position import search_insert


@pytest.mark.parametrize("nums, target, expected", [
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 2, 1),
    ([1, 3], 2, 1)
])
def test_search_insert(nums: list[int], target: int, expected: int):
    assert search_insert(nums, target) == expected