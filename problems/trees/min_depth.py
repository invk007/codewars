"""Given a binary tree, find its minimum depth."""
from typing import Optional

from problems.trees.tree_node import TreeNode


def min_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if root.right is None and root.left is None:
        return 1

    left_depth = min_depth(root.left)
    right_depth = min_depth(root.right)

    if root.left is None:
        return right_depth + 1

    if root.right is None:
        return left_depth + 1

    return min(left_depth, right_depth) + 1
