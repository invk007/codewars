from problems.trees.min_depth import min_depth
from tests.problems.trees.tree import tree


def test_min_depth(tree):
    assert min_depth(tree) == 3
