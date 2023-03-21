def remove_val(nums: list[int], val: int) -> list[int]:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums[:slow]


if __name__ == '__main__':
    print(remove_val([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(remove_val([3], 2))
    print(remove_val([2, 2, 2], 2))
