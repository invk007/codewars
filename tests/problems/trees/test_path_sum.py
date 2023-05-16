import pytest

from problems.trees.path_sum import has_path_sum


@pytest.mark.parametrize("target_sum, expected", [
    (10, False),
    (5, True)
])
def test_has_path_sum(target_sum, expected, tree):
    assert has_path_sum(tree, target_sum) == expected
