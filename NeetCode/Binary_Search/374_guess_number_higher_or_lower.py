# https://leetcode.com/problems/guess-number-higher-or-lower/

def guess(n: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            middle = (l + r) // 2
            tmp_guess = guess(middle)
            if tmp_guess == 0:
                return middle
            elif tmp_guess == 1: # my guess < target
                l = middle + 1
            else:
                r = middle -1
