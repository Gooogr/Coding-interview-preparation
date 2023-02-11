# https://leetcode.com/problems/palindrome-number/

# Naive solution with str converting
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        str_x = str(x)
        l, r = 0, len(str_x) - 1
        while l < r:
            if str_x[l] != str_x[r]:
                return False
            l += 1
            r -= 1
        return True

# More fancy approach without string convertion (bonus task)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        # Find 1e? size of x
        # For example div for 1221 is 1000
        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            left = x % 10    # 1221 -> 122 1
            right = x // div # 1221 // 1000-> 1 221

            if left != right: return False

            x = (x % div) // 10 # (1221 %1000) -> 221 // 10 -> 22 
            div = div / 100     # 1000 -> 10, because we truncated 1221 to 22  
        return True