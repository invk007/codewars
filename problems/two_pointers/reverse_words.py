def reverse_words(s: str) -> str:
    """Non-pythonic solution to practice 2-pointers technic"""
    left = 0
    ans = list(s + ' ')

    for right in range(len(ans)):
        if ans[right] == ' ':
            temp_l = left
            temp_r = right - 1
            while temp_l < temp_r:
                ans[temp_l], ans[temp_r] = ans[temp_r], ans[temp_l]
                temp_l += 1
                temp_r -= 1
            left = right + 1

    return ''.join(ans[:-1])


def reverse_words_py(s: str) -> str:
    """Pythonic solution for the task"""
    return ' '.join([word[::-1] for word in s.split()])


if __name__ == '__main__':
    assert reverse_words('Hello World') == 'olleH dlroW'
    assert reverse_words_py('Hello World') == 'olleH dlroW'
