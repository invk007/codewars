from problems.interview.find_max_sublist import find_max_sublist


def test_find_max_sublist():
    assert find_max_sublist([1, 5, 3, 2, 4], [3, 3, 2, 4, 1, 5, 6]) == [3, 2, 4]