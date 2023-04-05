def longest_ones(nums: list[int], k: int) -> int:
    ans = curr = i = 0

    for j in range(len(nums)):
        if nums[j] == 0:
            curr += 1

        while curr > k:
            if nums[i] == 0:
                curr -= 1
            i += 1

        ans = max(ans, len(nums[i : j + 1]))

    return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    assert longest_ones(nums, k) == 6
