# https://leetcode.com/problems/kth-smallest-element-in-a-bst

from typing import Optional
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Naive approach with heap - iterate over all tree (don't use it search features),
# add values to min heap and pop k-th element
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(root):
            if not root:
                return None
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        heapq.heapify(arr)
        while k > 0:
             result = heapq.heappop(arr)
             k -= 1
        return result

# InOrder DFS - traverse to target node until k=0   
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None

        def dfs(root):
            nonlocal k, result
            if not root:
                return None
            dfs(root.left)
            k-= 1
            if k == 0:
                result = root.val
                return None
            dfs(root.right)
        dfs(root)
        return result