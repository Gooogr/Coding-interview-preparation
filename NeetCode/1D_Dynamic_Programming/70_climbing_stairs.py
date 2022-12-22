# https://leetcode.com/problems/climbing-stairs/

# Bottom up dynamic approach
class Solution:
    def climbStairs(self, n: int) -> int:
        # edge cases
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2