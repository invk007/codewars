"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
"""
from typing import Optional

from problems.trees.tree_node import TreeNode


def diameter_of_bin_tree(root: Optional[TreeNode]) -> int:
    """
    Max path is always between 2 leafs.

    1. Find max path length for left tree
    2. Find max path length for right tree
    3. Return a sum of paths for left and right tree
    :param root:
    :return:
    """
    diameter = 0

    def helper(node: Optional[TreeNode]):

        if node is None:
            return 0

        nonlocal diameter

        left_path = helper(node.left)
        right_path = helper(node.right)

        diameter = max(diameter, left_path + right_path)

        return max(left_path, right_path) + 1

    helper(root)

    return diameter


