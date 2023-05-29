"""Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order."""


def find_top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq_map = {freq: [] for freq in range(len(nums) + 1)}

    counts = {num: 0 for num in nums}

    for num in nums:
        counts[num] += 1

    for val, freq in counts.items():
        freq_map[freq].append(val)

    result = []

    for freq in range(len(nums), 0, -1):
        if freq_map[freq]:
            for num in freq_map[freq]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result

    return result
