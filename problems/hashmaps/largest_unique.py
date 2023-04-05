from collections import Counter


def largest_unique_num(nums: list[int]) -> int:
    counter = Counter(nums)
    ans = -1

    for val, qty in counter.items():
        if val > ans and qty == 1:
            ans = val

    return ans


if __name__ == '__main__':
    assert 8 == largest_unique_num([5, 7, 3, 9, 4, 9, 8, 3, 1])
    assert -1 == largest_unique_num([9, 9, 8, 8])
