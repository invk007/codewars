from problems.trees.bin_tree_diameter import diameter_of_bin_tree


def test_diameter_of_bin_tree(tree):
    assert diameter_of_bin_tree(tree) == 5
    