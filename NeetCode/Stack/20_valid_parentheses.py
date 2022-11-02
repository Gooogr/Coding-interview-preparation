# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close2open = {")":"(", "]":"[", "}":"{"}
        for item in s:
            if item in close2open:
                # if we get closing braket for correct stack it should have opening pair
                # and stack should not be empty. Thus, we can drop this valid pair
                if stack and stack[-1] == close2open[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return stack == []
