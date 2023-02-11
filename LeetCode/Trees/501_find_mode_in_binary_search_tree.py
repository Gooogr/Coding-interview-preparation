# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Naive solution with O(n) space complexity for edge values stroring
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        # Collect all tree values
        values = []
        while queue:
            node = queue.pop(0)
            values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Count all values frequency
        freq_dict = {}
        for val in values:
            freq_dict[val] = freq_dict.get(val, 0) + 1
        result = sorted(freq_dict.items(), key = lambda x: x[1], reverse=True)

        # Get mode(s)
        max_freq = result[0][1]
        output = []
        for item in result:
            if item[1] == max_freq:
                output.append(item[0])
        return output

# Optimal solution with O(1) spacy complexity
