"""Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'."""

VOWELS = set('aeiou')


def max_vowels_substr(s: str, k: int) -> int:
    ans = current = i = 0
    for j in range(len(s)):
        if ans == k:
            return ans

        if s[j] in VOWELS:
            current += 1

        while j - i + 1 > k:
            if s[i] in VOWELS:
                current -= 1
            i += 1

        if current > ans:
            ans = current
    return ans


print(max_vowels_substr('abciiidef', 3) == 3)
print(max_vowels_substr('leetcode', 3) == 2)
