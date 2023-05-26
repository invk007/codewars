"""Given an array of strings strs, group the anagrams together."""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(lambda: [])

    for s in strs:
        key = [0] * 26   # because there are 26 letters in english alphabet

        for c in s:
            key[ord(c) - ord('a')] += 1     # to map 'a' to 0, 'b' to 1 etc.

        groups[tuple(key)].append(s)

    return [val for val in groups.values()]
