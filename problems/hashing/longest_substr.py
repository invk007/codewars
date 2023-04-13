"""Given a string s, find the length of the longest substring without repeating
characters."""

from collections import Counter


def len_of_longest_substr(s: str) -> int:
    ans = j = 0
    seen = Counter()

    for i in range(len(s)):
        curr = s[i]
        seen[curr] += 1

        while seen[curr] > 1:
            seen[s[j]] -= 1
            j += 1

        ans = max(ans, i - j + 1)

    return ans
