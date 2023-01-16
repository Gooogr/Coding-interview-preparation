# https://leetcode.com/problems/unique-binary-search-trees/

# With Catalan's numbers
class Solution:
    def numTrees(self, n: int) -> int:
        sol = 1
        for i in range (0, n):
            sol = sol * 2 * (2 * i + 1) / (i + 2)
        return int(sol)

# recirsive, non-dp approach
# https://leetcode.com/problems/unique-binary-search-trees/solutions/853183/python-recursion-memoization/

