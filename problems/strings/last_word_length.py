"""Given a string s consisting of words and spaces, return the length of the
last word in the string."""


def last_word_length(word: str) -> int:
    if not word:
        return 0

    p = -1
    length = 0

    while -1 * p <= len(word) and word[p] == " ":
        p -= 1

    while -1 * p <= len(word) and word[p] != " ":
        length += 1
        p -= 1

    return length
