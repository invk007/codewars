"""Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the
left of the index is equal to the sum of all the numbers strictly to the
index's right.

If the index is on the left edge of the array, then the left sum is 0 because
there are no elements to the left. This also applies to the right edge of the
array.

Return the leftmost pivot index. If no such index exists, return -1."""


def pivot_index(nums: list[int]) -> int:
    left, right = 0, sum(nums)
    ans = -1
    i = 0

    for i in range(len(nums)):
        right -= nums[i]
        if left == right:
            ans = i
            break
        left += nums[i]

    return ans


print(3 == pivot_index([1, 7, 3, 6, 5, 6]))
print(-1 == pivot_index([1, 2, 3]))
print(0 == pivot_index([2, 1, -1]))
print(-1 == pivot_index([-1, -1, -1, 1, 1, -1]))
