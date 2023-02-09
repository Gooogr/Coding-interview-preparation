# https://leetcode.com/problems/remove-duplicates-from-sorted-list

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
               curr.next = curr.next.next # jump over repeated next node to the next-next node
            else:
                curr = curr.next
        return head