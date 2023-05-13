from problems.stacks.next_greater_element import next_greater_element


def test_next_greater_element():
    assert next_greater_element([4, 1, 2],  [1, 3, 4, 2]) == [-1, 3, -1]