import pytest

from problems.trees.tree_node import TreeNode


@pytest.fixture(scope='session')
def tree() -> TreeNode:
    root = TreeNode(val=1)
    node1 = TreeNode(val=1)
    node2 = TreeNode(val=2)
    node3 = TreeNode(val=3)
    node4 = TreeNode(val=4)
    node5 = TreeNode(val=5)
    node6 = TreeNode(val=6)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    node5.right = node6

    return root
