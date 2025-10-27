def solution(nums: list[int]) -> list[int]:
    i = 0

    if len(nums) == 1:
        return nums

    while i < len(nums):
        if nums[i] == 0:
            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j == len(nums):
                break
            nums[i] = nums[j]
            nums[j] = 0
        i += 1

    return nums


if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    solution(arr)
    print(f"{arr=}")
