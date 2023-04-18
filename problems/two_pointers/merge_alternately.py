"""You are given two strings word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is longer than
the other, append the additional letters onto the end of the merged string.

Return the merged string."""


def merge_alternately(word_1: str, word_2: str) -> str:
    len_word1 = len(word_1)
    len_word2 = len(word_2)
    min_len = min(len_word1, len_word2)

    i = 0
    result = []

    while i < min_len:
        result.append(word_1[i])
        result.append(word_2[i])
        i += 1

    result.append(
        word_1[i:len_word1] if len_word1 > len_word2 else word_2[i:len_word2]
    )

    return ''.join(result)
