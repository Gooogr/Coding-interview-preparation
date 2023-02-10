# https://leetcode.com/problems/first-bad-version

def isBadVersion(n:int) -> bool:
    pass

# Optimal binary search soolution
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            middle = (l + r) // 2
            # Move right border, to the first True direction
            # But we can'r cross it, bevause we don't +1
            if isBadVersion(middle): 
                r = middle
            # Move left border until l == r
            # Thus, we jump to the first True value 
            else:
                l = middle + 1 
        return l

# My shitty binary search solution
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            middle = (l + r) // 2

            # find optimal pair (False, True) of l, r poniters 
            if  not isBadVersion(l) and isBadVersion(r) and r - l == 1:
                return r

            # Safe cases to move pointers
            if not isBadVersion(middle) and not isBadVersion(middle + 1) :
                l = middle + 1
            elif isBadVersion(middle) and isBadVersion(middle - 1):
                r = middle - 1
            
            # (False, True) cases  in a middle +1 or middle -1 positions
            elif isBadVersion(middle) == False and isBadVersion(middle + 1) != False:
                return middle + 1
            elif isBadVersion(middle) == True and isBadVersion(middle - 1) == False:
                return middle
