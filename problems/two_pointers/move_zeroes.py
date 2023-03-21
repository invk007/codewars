def move_zeroes(nums: list[int]) -> list[int]:
    """Given an integer array nums, move all 0's to the end of it while
    maintaining the relative order of the non-zero elements."""
    i = 0
    j = 1
    while i < len(nums) and j < len(nums):
        if nums[i] != 0:
            i += 1
            if j < i + 1:
                j = i + 1
        elif nums[j] == 0:
            j += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
    return nums


def move_zeroes_alt(nums: list[int]) -> list[int]:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1
    return nums


if __name__ == '__main__':
    assert [1, 12, 3, 0, 0] == move_zeroes([0, 1, 0, 12, 3])
    assert [0] == move_zeroes([0])
    assert [4, 2, 4, 3, 5, 1, 0, 0, 0, 0] == move_zeroes(
        [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    )
