"""Given the root of a binary tree, find the maximum value v for which there
exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of
b.

A node a is an ancestor of b if either: any child of a is equal to b or any
child of a is an ancestor of b."""

from typing import Optional

from problems.trees.tree_node import TreeNode


def max_ancestor_diff(root: Optional[TreeNode]) -> int:
    def dfs_helper(node: Optional[TreeNode], cur_min: int, cur_max: int) -> int:
        if not node:
            return abs(cur_min - cur_max)

        if node.val < cur_min:
            cur_min = node.val

        if node.val > cur_max:
            cur_max = node.val

        left_max = dfs_helper(node.left, cur_min, cur_max)
        right_max = dfs_helper(node.right, cur_min, cur_max)

        return max(left_max, right_max)

    return dfs_helper(root, root.val, root.val)
