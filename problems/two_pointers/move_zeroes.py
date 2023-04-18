"""Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements."""


def move_zeroes(nums: list[int]) -> list[int]:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1
    return nums
