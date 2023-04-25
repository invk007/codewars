import pytest

from problems.stacks.simplify_path import simplify_path


@pytest.mark.parametrize("path, expected", [
    ("/../", "/"),
    ("/a///b//c////../d", "/a/b/d"),
    ("/home//foo/", "/home/foo")
])
def test_simplify_path(path: str, expected: str):
    assert simplify_path(path) == expected
