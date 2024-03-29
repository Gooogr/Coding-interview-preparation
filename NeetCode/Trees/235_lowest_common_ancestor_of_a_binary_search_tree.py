# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        # Set order for correct comparison
        if p.val > q.val:
            p, q = q, p

        # Base case
        if p.val <= root.val <= q.val:
            return root
        # p > root, q > root => go right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # p < root, q < root => go left
        else:
            return self.lowestCommonAncestor(root.left, p, q)