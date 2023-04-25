"""Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and
s[i + 1] where:
    *   0 <= i <= s.length - 2
    *   s[i] is a lower-case letter and s[i + 1] is the same letter but in
        upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the
string bad and remove them. You can keep doing this until the string becomes
good.

Return the string after making it good. The answer is guaranteed to be unique
under the given constraints."""


def make_good_string(s: str) -> str:
    stack = []
    for ch in s:
        if stack:
            if (ch.isupper() and ch.lower() == stack[-1]) or (
                ch.islower() and ch.upper() == stack[-1]
            ):
                stack.pop()
                continue
        stack.append(ch)
    return ''.join(stack)
