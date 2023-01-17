# https://leetcode.com/problems/balanced-binary-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(root: Optional[TreeNode]):
            if not root: 
                return 0
            # Get node's subtrees height
            height_left, height_right = dfs(root.left), dfs(root.right)

            # Validate node based on height condition
            nonlocal is_balanced
            if abs(height_left - height_right) > 1:
                is_balanced = False

            # pass height to the next node
            return 1 + max(height_left, height_right)
        dfs(root)
        return is_balanced