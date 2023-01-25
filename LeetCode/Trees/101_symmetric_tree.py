# https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_subtree_symmetric(root.left, root.right)
    
    def is_subtree_symmetric(self, left_node, right_node):
        '''
        Helper function to compare left and right subtrees.
        '''
        if left_node is None and right_node is None:
            return True
        if left_node is None or right_node is None:
            return False
        if left_node.val != right_node.val:
            return False
        # If somwhere we get False - it will sift up through stack call
        # In symmetric case we will pass True case from bottom to up
        return (
            self.is_subtree_symmetric(left_node.left, right_node.right) and
            self.is_subtree_symmetric(left_node.right, right_node.left)
        )