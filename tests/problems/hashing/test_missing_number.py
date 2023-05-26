from problems.hashing.missing_number import find_missing_num, find_missing_num_add_space


def test_find_missing_number():
    assert find_missing_num([6, 1, 2, 7, 9, 4, 0, 3, 5]) == 8


def test_find_missing_number_additional_space():
    assert find_missing_num_add_space([6, 1, 2, 7, 9, 4, 0, 3, 5]) == 8
