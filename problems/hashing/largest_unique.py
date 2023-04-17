from collections import Counter


def largest_unique_num(nums: list[int]) -> int:
    counter = Counter(nums)
    ans = -1

    for val, qty in counter.items():
        if val > ans and qty == 1:
            ans = val

    return ans
