def prefix_sum(nums: list[int]) -> list[int]:
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    return prefix


if __name__ == '__main__':
    nums = [5, 2, 1, 6, 3, 8]
    assert [5, 7, 8, 14, 17, 25] == prefix_sum(nums)
