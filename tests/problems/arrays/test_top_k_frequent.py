import pytest

from problems.arrays.top_k_frequent import find_top_k_frequent


@pytest.mark.parametrize(
    "nums, k, expected", [
        (
            [5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3],
            3,
            [3, 7, 10]
        ),
        ([1], 1, [1])
    ]
)
def test_find_top_k_frequest(nums, k, expected):
    assert sorted(find_top_k_frequent(nums, k)) == sorted(expected)