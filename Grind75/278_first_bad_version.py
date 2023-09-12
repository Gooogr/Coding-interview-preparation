# https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m # keep right border
            else:
                l = m + 1 # move left border towrads first bad version
        return l
