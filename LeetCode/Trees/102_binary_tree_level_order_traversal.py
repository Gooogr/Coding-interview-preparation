# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # Use queue for BFS
        queue = [root]
        traversal_result = []

        while queue:
            tmp_list = []
            # Collect DFS layer on nodes
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            traversal_result.append(tmp_list)
        return traversal_result