"""Given a sorted array of distinct integers and a target value, return the
index if the target is found. If not, return the index where it would be if it
were inserted in order."""


def search_insert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if target < nums[mid]:
        return mid
    else:
        return mid + 1
