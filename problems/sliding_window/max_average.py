def max_average(nums: list[int], k: int) -> float:
    current = sum(nums[:k])
    ans = current / k

    for i in range(k, len(nums)):
        current = current - nums[i - k] + nums[i]
        ans = max(ans, current / k)

    return ans


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    assert max_average(nums, k) == 12.75
