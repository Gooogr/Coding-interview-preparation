# https://leetcode.com/problems/path-sum-iii/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Optimized approach where we store our rolling sum.
# Something like cache in 2sum task
# Time complexity: O(n)
# Memory complexity O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        freq_map = {0: 1} # zero sum - meets at last one, when don't take any nodes at all

        def dfs(root, prev_sum):
            nonlocal result
            if not root:
                return None
            # find cumulative sum  in branch up to current node
            curr_sum = prev_sum + root.val
            # diff between current cumsum and target
            delta = curr_sum - targetSum
            # if delta already exist - we can get valid path from the branch
            # like, remove it from our cumulative sum and get our target sum
            # from other nodes sum
            if delta in freq_map:
                result += freq_map[delta]
            # Update our hash
            freq_map[curr_sum] = freq_map.get(curr_sum, 0) + 1
            # dfs deeper until end of branch
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            # remove cumulative sum of the branch the we finished
            freq_map[curr_sum] -= 1

        dfs(root, 0)
        return result

# Naive approach where we visit every node and check all pathes from it
# Time complexity: O(n**2)
# Memory complexity O(n)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        result = 0
        
        def dfs(node, target):
            '''
            Traverse over all tree nodes
            '''
            if node is None: return
            find_path_from_node(node, target)
            dfs(node.left, target)
            dfs(node.right, target)
                
        def find_path_from_node(node, target):
            '''
            Find all valid pathes from current node
            '''
            nonlocal result
            if node is None: return
            if node.val == target: result += 1
            find_path_from_node(node.left, target-node.val)
            find_path_from_node(node.right, target-node.val)
            
        dfs(root, sum)
        
        return result