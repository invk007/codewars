"""Given a string path, which is an absolute path (starting with a slash '/') to
a file or directory in a Unix-style file system, convert it to the simplified
canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a
double period '..' refers to the directory up a level, and any multiple
consecutive slashes (i.e. '//') are treated as a single slash '/'. For this
problem, any other format of periods such as '...' are treated as
file/directory names.

Return the simplified canonical path.
"""


def simplify_path(path: str) -> str:
    i = j = 0
    stack = []
    
    while j < len(path):

        while path[j] != "/":
            j += 1
            if j == len(path):
                break

        substr = path[i:j]

        if substr == "..":
            if stack:
                stack.pop()
        elif substr != "" and substr != ".":
            stack.append(substr)

        i = j + 1
        j += 1

    return "/" + "/".join(stack)

