# https://leetcode.com/problems/linked-list-cycle

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# With O(n) additional memory
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev, curr = None, head
        visited_nodes = set()
        while curr:
            if curr in visited_nodes:
                return True
            visited_nodes.add(curr)
            curr = curr.next
        return False

# With O(1) additional memory
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False