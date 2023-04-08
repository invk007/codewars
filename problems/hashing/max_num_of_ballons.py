"""Given a string text, you want to use the characters of text to form as many
instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of
instances that can be formed."""
from itertools import zip_longest


def max_num_of_balloons(text: str) -> int:
    string = 'balloon'
    hashmap = dict(zip_longest(string, [0], fillvalue=0))

    for ch in text:
        if ch in string:
            hashmap[ch] += 1

    hashmap['l'] //= 2
    hashmap['o'] //= 2

    return min(hashmap.values())


if __name__ == '__main__':
    assert 1 == max_num_of_balloons('nlaebolko')
    assert 2 == max_num_of_balloons('loonbalxballpoon')
    assert 0 == max_num_of_balloons('leetcode')
