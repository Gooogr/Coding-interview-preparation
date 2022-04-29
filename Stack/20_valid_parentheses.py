# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map_symbols = {"]":"[", "}":"{", ")":"("}
        for item in s:
            if item in map_symbols.values():
                stack.append(item)
            else:
                if stack == [] or stack[-1] != map_symbols[item]:
                    return False
                stack.pop()
        return stack == []
