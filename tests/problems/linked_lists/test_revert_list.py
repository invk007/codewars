import pytest

from problems.linked_lists.revert_linked_list import revert_list
from problems.linked_lists.utils import (array_to_linked_list,
                                         linked_list_to_array)


@pytest.mark.parametrize('input_array', [[1, 2, 3, 4, 5], [5]])
def test_reverse_list(input_array):
    head = array_to_linked_list(input_array)
    result = revert_list(head)
    assert linked_list_to_array(result) == input_array[::-1]
