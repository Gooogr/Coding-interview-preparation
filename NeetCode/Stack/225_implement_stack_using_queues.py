# https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        
    # Pushes element x to the top of the stack.
    def push(self, x: int) -> None:
        self.q.append(x)
        
    #  Removes the element on the top of the stack and returns it.
    def pop(self) -> int:
        # iterate over the queue and re-add all elements except top
        for _ in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
    
    # Returns the element on the top of the stack.
    def top(self) -> int:
        return self.q[-1]
        
    # Returns true if the stack is empty, false otherwise.
    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()