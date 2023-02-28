# https://leetcode.com/problems/koko-eating-bananas/

# Time complexity O(log(max_p) * p)
# where p is amount of piles, and max_p - max value in piles

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # max possible value
        while l <= r:
            k = (l + r) // 2
            hours = 0 
            # how many hours Koko need to eat all piles with current k
            for pile in piles:
                hours += math.ceil(pile / k)
            # if time is enough - update result and move right pointer
            if hours <= h:
                res = k #min(res, k)
                r = k - 1
            # else - increase left pointer
            else:
                l = k + 1
        return res