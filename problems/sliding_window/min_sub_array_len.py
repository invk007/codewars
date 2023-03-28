"""Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to
target. If there is no such subarray, return 0 instead."""


def min_subarray_len(nums: list[int], target: int) -> int:
    i = 0
    ans = None
    sum_ = 0

    for j in range(len(nums)):
        sum_ += nums[j]
        while sum_ >= target:
            length = j - i + 1
            if ans is None:
                ans = length
            else:
                ans = min(ans, length)
            sum_ -= nums[i]
            i += 1

    return 0 if ans is None else ans


print(min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2)
print(min_subarray_len([1, 1, 1, 1, 1], 11) == 0)
print(min_subarray_len([4, 4, 4, 4], 4) == 1)
