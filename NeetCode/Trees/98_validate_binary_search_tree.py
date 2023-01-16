# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS, no recursion solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         # DFS search
        stack = [root]
        # Track left and right borders for earch node
        llimit = [float('-inf')]
        rlimit = [float('inf')]
        while stack:
            node = stack.pop()
            left = llimit.pop()
            right = rlimit.pop()

            # print(f'Node value: {node.value}, limits: ({left, right})')
            if not left < node.val < right:
                return False

            if node.left is not None:
                stack.append(node.left)
                rlimit.append(node.val)
                llimit.append(left)

            if node.right is not None:
                stack.append(node.right)
                rlimit.append(right)
                llimit.append(node.val)
        return True

# DFS, recursion solution
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
