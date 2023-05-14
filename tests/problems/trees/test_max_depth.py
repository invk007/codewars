from problems.trees.max_depth import max_depth
from tests.problems.trees.tree import tree


def test_max_depth(tree):
    assert max_depth(tree) == 4
