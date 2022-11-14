class Solution:
    def isValid(self, s: str) -> bool:
        brack_map = { "}":"{", "]":"[", ")":"("}
        stack = []
        for item in s:
            if (item in brack_map): 
                if stack and (stack[-1] == brack_map[item]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return stack == []
                
