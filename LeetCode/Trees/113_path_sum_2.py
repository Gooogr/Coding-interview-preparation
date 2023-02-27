# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        result = []
        def dfs(root, path, curr_sum):
            nonlocal result
            if not root:
                return None
            path.append(root.val)  
            curr_sum += root.val        
            if not root.left and not root.right:
                if curr_sum==targetSum:
                    result.append(path.copy()) # to break this path unmutable in result
            dfs(root.left, path, curr_sum)
            dfs(root.right, path, curr_sum)
            path.pop()
            return result  

        return dfs(root, [], 0)