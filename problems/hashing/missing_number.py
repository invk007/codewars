"""Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array."""


def find_missing_num(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) / 2
    return int(expected_sum - sum(nums))


def find_missing_num_add_space(nums: list[int]) -> int:
    present_nums = set(nums)
    for i in range(len(nums) + 1):
        if i not in present_nums:
            return i
    return -1
