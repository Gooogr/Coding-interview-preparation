# https://leetcode.com/problems/binary-tree-inorder-traversal/

# 1
#  \
#   2
#  /
# 3
# 
# Should be [1, 3, 2]   
 
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive approach
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node: Optional[TreeNode]):
            if not node:
                return 
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        traverse(root)
        return result

# iterative approach
