"""Given the root of a binary tree, find the length of the longest path from the
root to a leaf."""

from typing import Optional

from problems.trees.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1
