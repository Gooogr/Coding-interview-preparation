# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traverse(root, nodes = []):
            if not root:
                return
            nodes.append(root.val)
            for child in root.children:
                traverse(child, nodes)
            return nodes
        return traverse(root)