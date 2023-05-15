# Find max sublist
# For instance ofr [1, 5, 3, 2, 4] and [3, 3, 2, 4, 1, 5, 6] the answer is
# [3, 2, 4]

def find_max_sublist(nums1: list[int], nums2: list[int]) -> list[int]:
    if not nums1 or not nums2:
        return []

    ans = []

    for i, el1 in enumerate(nums1):
        for j, el2 in enumerate(nums2):
            if el1 == el2:
                m = i + 1
                n = j + 1

                while m < len(nums1) and n < len(nums2) and nums1[m] == nums2[n]:
                    m += 1
                    n += 1

                if len(nums1[i:m]) > len(ans):
                    ans = list(nums1[i:m])

    return ans
