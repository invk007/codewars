from problems.linked_lists.delete_duplicates import delete_duplicates
from problems.linked_lists.utils import (array_to_linked_list,
                                         linked_list_to_array)


def test_delete_duplicates():
    head = array_to_linked_list([1, 1, 2, 3, 3])
    actual = delete_duplicates(head)

    assert linked_list_to_array(actual) == [1, 2, 3]
