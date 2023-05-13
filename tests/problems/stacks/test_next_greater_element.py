import pytest

from problems.stacks.next_greater_element import next_greater_element


@pytest.mark.parametrize("nums1, nums2, expected", [
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
])
def test_next_greater_element(nums1, nums2, expected):
    assert next_greater_element(nums1, nums2) == expected