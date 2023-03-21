"""Given a 0-indexed string word and a character ch, reverse the segment of word
that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
If the character ch does not exist in word, do nothing."""


def revert_prefix_py(word: str, ch: str) -> str:
    """Pythonic solution"""
    try:
        j = word.index(ch)
        return word[: j + 1][::-1] + word[j + 1 :]
    except ValueError:
        return word


def revert_prefix(word: str, ch: str) -> str:
    """Two pointers practice"""
    i = j = 0

    try:
        while word[j] != ch:
            j += 1
    except IndexError:
        return word

    word_list = list(word[: j + 1])    # list objects are mutable
    suffix = word[j + 1 :]

    while i < j:
        word_list[i], word_list[j] = word_list[j], word_list[i]
        i += 1
        j -= 1

    return ''.join(word_list) + suffix


if __name__ == '__main__':
    assert 'zbade' == revert_prefix_py('abzde', 'z')
    assert 'zbade' == revert_prefix('abzde', 'z')
    assert 'abcd' == revert_prefix('abcd', 'z')
