# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            
            middle = (l + r) // 2
            square = middle * middle
            plus_square = (middle + 1)*(middle + 1)
            
            # exlude upper bound sqrt(8)~= 2.7 -> [2, 3)
            if square <= x < plus_square:
                return middle
            elif square > x:
                r = middle - 1
            else:
                l = middle + 1