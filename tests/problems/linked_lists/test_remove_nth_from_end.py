import pytest

from problems.linked_lists.remove_nth import remove_nth_from_end
from problems.linked_lists.list import from_list_to_array, from_array_to_list


@pytest.mark.parametrize(
    "nums, n, expected",
    [
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([1,2], 1, [1]),
        ([1], 1, []),
        ([1, 2, 3], 3, [2, 3])
    ]
)
def test_remove_nth_from_end(nums, n, expected):
    l = from_array_to_list(nums)
    result = remove_nth_from_end(l, n)
    assert from_list_to_array(result) == expected
