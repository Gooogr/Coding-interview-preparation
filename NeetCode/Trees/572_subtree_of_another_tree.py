# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional

# Time complexity: O(n*m), 
# where n is nodes amount in tree, m - in subtree
# Memory complexity: O(n + m)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(
        self, 
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:
        # Empty subroot case
        if not subRoot:
            return True
        # Non-empty subroot and empty root case
        if subRoot and not root:
            return False
        # Check is current trees are same or not. 
        # Two same trees are substree for each other
        if self.is_same_tree(root, subRoot):
            return True
        # Run comparison on every subtree of bigger tree and same smaller tree
        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
               )

    def is_same_tree(
        self, 
        root1: Optional[TreeNode], 
        root2: Optional[TreeNode]
    ) -> bool:
        '''
        Helper function. Check is two trees are same or not
        '''
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        else:
            return (
                root1.val == root2.val and
                self.is_same_tree(root1.left, root2.left) and
                self.is_same_tree(root1.right, root2.right)
                )