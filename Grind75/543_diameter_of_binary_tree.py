# https://leetcode.com/problems/diameter-of-binary-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Very similar with 110 Balanced tree. Same subrutine approach
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def dfs(root):
            if not root:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            nonlocal max_diam
            max_diam = max(max_diam, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        dfs(root)
        return max_diam