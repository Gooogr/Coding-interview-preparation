# https://leetcode.com/problems/unique-paths/
# https://youtu.be/oBt53YbR9Kk?t=3552 explanation from FreeCodeCamp

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