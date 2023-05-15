"""Given the root of a binary tree and an integer targetSum, return true if
there is a path from the root to a leaf such that the sum of the nodes on the
path is equal to targetSum, and return false otherwise."""

from typing import Optional
from problems.trees.tree_node import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    def dfs(node: TreeNode, curr: int) -> bool:
        if not node:
            return False

        if not node.left and not node.right:
            return (node.val + curr) == target_sum

        curr += node.val

        left = dfs(node.left, curr)
        right = dfs(node.right, curr)

        return left or right

    return dfs(root, 0)
