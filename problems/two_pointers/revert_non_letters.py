def reverse_only_letters(s: str) -> str:
    ans = list(s)
    left = 0
    right = len(ans) - 1

    while left < right:
        if not ans[left].isalpha():
            left += 1
        elif not ans[right].isalpha():
            right -= 1
        else:
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
    return ''.join(ans)


if __name__ == '__main__':
    assert 'dc-ba' == reverse_only_letters('ab-cd')
    assert '++--' == reverse_only_letters('++--')
