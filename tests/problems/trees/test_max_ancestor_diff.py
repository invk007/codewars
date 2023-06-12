from problems.trees.max_ancerstor_diff import max_ancestor_diff


def test_max_ancestor_diff(tree):
    assert max_ancestor_diff(tree) == 5
