# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def longestPath(node):
            '''
            Recursive DFS calculate max height for node + update current max diameter
            '''
            if not node: 
                return 0

            height_left = longestPath(node.left)
            height_right = longestPath(node.right)
            
            # additional subrutine - check if diametr through node is maximum or not
            # Diameter = Height to the left from node + Height to the right from node
            nonlocal max_diam
            max_diam = max(max_diam, height_left + height_right) 

            # calculate node depth like in task 104
            return max(height_left, height_right) + 1

        longestPath(root)
        return max_diam