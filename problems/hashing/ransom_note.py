"""Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""

from collections import Counter


def can_construct(note: str, magazine: str) -> bool:
    note_counter = Counter(note)
    magazine_counter = Counter(magazine)

    for k in note_counter.keys():
        if k not in magazine_counter:
            return False
        if note_counter[k] > magazine_counter[k]:
            return False

    return True
