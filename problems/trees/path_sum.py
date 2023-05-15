"""Given the root of a binary tree and an integer targetSum, return true if
there is a path from the root to a leaf such that the sum of the nodes on the
path is equal to targetSum, and return false otherwise."""

from typing import Optional
from problems.trees.tree_node import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if root is None:
        return False
