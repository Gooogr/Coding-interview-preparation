# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize list for stack constructure
        stack = []
        # Map parenthood between brackets
        map_symbols = {"]":"[", "}":"{", ")":"("}
        
        for item in s:
            # If we got opening bracket - add it to the stack
            if item in map_symbols.values():
                stack.append(item)
                
            # Else - we got closing bracket
            else:
                # Check if stack is already empty or previous bracket doesn't match with current one
                if stack == [] or stack[-1] != map_symbols[item]:
                    return False
                # If everything is OK - remove opening bracket from stack, because we have found a pair for it.
                stack.pop()
         
        # Return final stack state after all iterations 
        return stack == []
