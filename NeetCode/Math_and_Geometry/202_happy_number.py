# https://leetcode.com/problems/happy-number

# Main idea:
# Happy number loop - until we met 1
# 19 -> 82 -> 68 -> 100 -> 1
# Unhappy number loop - until we met already seen number
# 2 -> _4_ -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> _4_ -> ...

class Solution:
    def isHappy(self, n: int) -> bool:
        prev_numbers = set()
        while True:
            if n == 1:
                return True
            if n in prev_numbers:
                return False
            # memorize n
            prev_numbers.add(n)
            # update n 
            tmp_val = 0
            for char in str(n):
                tmp_val += int(char)**2
            n = tmp_val


