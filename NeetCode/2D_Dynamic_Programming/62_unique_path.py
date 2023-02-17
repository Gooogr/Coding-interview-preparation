# https://leetcode.com/problems/unique-paths/

# Base cases
# F(i, 0) = 0, where i is any number
# F(0, i) = 0
# F(1, 1) = 1, do nothing case

# More complec example
# F(3, 3) = F(2, 3) + F(3, 2)
# F(2, 3) = F(1, 3) + F(2, 2)
# ...

# Time O(m*n) - keep only necessary combination
# Memory O(m + n) - from trimmed recursion tree
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def get_path(m, n, cache={}):
            if m == 1 and n == 1:
                return 1
            if m == 0 or n == 0:
                return 0
            key = str(f'{m} {n}') #possible optimization (m, n) and (n, m) is same values
           
            if key in cache:
                return cache[key]
            cache[key] = get_path(m - 1, n, cache) + get_path(m, n - 1, cache)
            return cache[key]
        result = get_path(m, n)
        return result


# Tabular approach
# Time O(m*n)  - two for loops
# Memory O(m*n) - we store full dp matrix
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We initialize our dp by 1 because 
        # F(i, 1) = 1, F(1, j) = 1
        # We can move only in one direction in this "corridors"
        dp = [[1] * m for _ in range(n)] # because 
        print(dp)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# Memory optimized tabular approach
# We need only two last lines
# Time O(m*n) 
# Memory O(n) 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            newRow = [1] * n                       # add new 1D "corridor"
            for j in range(1, n):
                newRow[j] = newRow[j - 1] + row[j] # expand all path with this 1D 
            row = newRow
        return row[-1]