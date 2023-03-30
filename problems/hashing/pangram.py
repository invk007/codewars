from string import ascii_lowercase


def check_pangram(sentence: str) -> bool:
    len_ = len(ascii_lowercase)
    seen = set()
    for ch in sentence:
        seen.add(ch)
        if len(seen) == len_:
            return True
    return False


if __name__ == "__main__":
    assert check_pangram('thequickbrownfoxjumpsoverthelazydog')
    assert not check_pangram('leetcode')
