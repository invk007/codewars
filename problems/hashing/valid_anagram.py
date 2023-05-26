"""Given two strings s and t, return true if t is an anagram of s, and false
otherwise."""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    counter_s = Counter(s)
    counter_t = Counter(t)
    return counter_s == counter_t
