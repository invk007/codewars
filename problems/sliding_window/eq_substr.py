"""You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of
t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values
of the characters).

Return the maximum length of a substring of s that can be changed to be the same
as the corresponding substring of t with a cost less than or equal to maxCost.
If there is no substring from s that can be changed to its corresponding
substring from t, return 0."""


def equal_substring(s: str, t: str, max_cost: int) -> int:
    curr_cost = ans = i = 0
    for j in range(len(s)):
        curr_cost += abs(ord(s[j]) - ord(t[j]))

        while curr_cost > max_cost:
            curr_cost -= abs(ord(s[i]) - ord(t[i]))
            i += 1

        if (len_ := j - i + 1) > ans:
            ans = len_

    return ans


assert 3 == equal_substring('abcd', 'bcdf', 3)
assert 1 == equal_substring('abcd', 'acde', 0)
