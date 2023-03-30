"""Given an integer array arr, count how many elements x there are, such that
x + 1 is also in arr. If there are duplicates in arr, count them separately."""


def count_elements(nums: list[int]) -> int:
    cnt = 0
    hs = set(nums)

    for el in nums:
        if el + 1 in hs:
            cnt += 1

    return cnt


if __name__ == '__main__':
    assert 2 == count_elements([1, 2, 3])
    assert 2 == count_elements([1, 1, 2, 2])
    assert 0 == count_elements([1, 1, 3, 3, 5, 5, 7, 7])
