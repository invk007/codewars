import pytest

from problems.linked_lists.middle_node import middle_node
from problems.linked_lists.utils import array_to_linked_list


@pytest.mark.parametrize(
    'input_list, expected', [([1, 2, 3, 4, 5], 3), ([1, 2, 3, 4, 5, 6], 4)]
)
def test_middle_node(input_list: list[int], expected: int):
    head = array_to_linked_list(input_list)
    actual = middle_node(head)
    assert actual.val == expected
