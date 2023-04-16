"""Find a sum of unique elements of an array"""

from collections import Counter


def sum_unique_elements(nums: list[int]) -> int:
    nums_counter = Counter(nums)
    return sum(val for val, qty in nums_counter.items() if qty == 1)
