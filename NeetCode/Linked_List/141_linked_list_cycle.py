# https://leetcode.com/problems/linked-list-cycle

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time complexity O(n)
# Space complexity O(n) 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited_nodes = set()
        while curr:
            if curr in visited_nodes:
                return True
            visited_nodes.add(curr)
            curr = curr.next
        return False

# Time complexity O(n)
# Space complexity O(1) 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next      # slow pointer - one step
            fast = fast.next.next # fast pointer - two steps
            if fast == slow:
                return True       # if the meet again - we have loop
        return False