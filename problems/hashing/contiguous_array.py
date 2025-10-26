"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""

def find_the_max_length(nums: list[int]) -> int:
    ones = 0
    zeroes = 0
    ans = 0
    sums_map = {}

    for i in range(0, len(nums)):
        if nums[i] == 0:
            zeroes += 1
        if nums[i] == 1:
            ones += 1

        if zeroes == ones:
            ans = i + 1
        else:
            diff = ones - zeroes
            if diff in sums_map:
                ans = max(ans, i - sums_map[diff])
            else:
                sums_map[diff] = i
    return ans
