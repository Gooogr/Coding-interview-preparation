# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS iterative approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # empty tree
        if not root:
            return 0

        queue = [root]
        levels = 0
        while queue:
            # for loops help us to iterate over current level and prepare next level
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels += 1
        return levels

# DFS recursion approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # empty tree
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# DFS iterative approach
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack: 
            node, depth = stack.pop()

            if node: # if tree is empty -> return res=0
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

