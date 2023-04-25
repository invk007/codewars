def strip_comments(string: str, markers: list[str]) -> str:
    i = 0
    stack = []

    while i < len(string):
        if string[i] in markers:
            j = i
            while j < len(string) and string[j] != "\n":
                j += 1
            i = j
            while stack and (stack[-1] == " " or stack[-1] == "\t"):
                stack.pop()
        else:
            stack.append(string[i])
            i += 1

    return "".join(stack)
