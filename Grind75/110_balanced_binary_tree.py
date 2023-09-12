# https://leetcode.com/problems/balanced-binary-tree

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
        
        def dfs(root):
            nonlocal is_balanced
            if not root: return 0
        
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            if abs(left_depth - right_depth) > 1:
                is_balanced = False

            return 1 + max(left_depth, right_depth)
    
        dfs(root)
        return is_balanced