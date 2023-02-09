# https://leetcode.com/problems/remove-linked-list-elements/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy_head = ListNode(0)
        dummy_head.next = head

        curr = dummy_head # not head, dummy_head!
        while curr.next:
            if curr.next.val == val: #jump over target node
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy_head.next
