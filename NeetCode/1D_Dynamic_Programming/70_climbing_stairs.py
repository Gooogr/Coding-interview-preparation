# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        def get_climbs(n: int, cache: dict={}):
            if n < 2:      # Base case
                return 1
            if n in cache: # Memorization 
                return cache[n]
            # ladder[i] = ladder[i - 1] + ladder[i - 2] # by final possible steps amount
            cache[n] = get_climbs(n - 1, cache) + get_climbs(n - 2, cache)
            return cache[n]
        result = get_climbs(n)
        return result