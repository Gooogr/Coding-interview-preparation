# https://leetcode.com/problems/middle-of-the-linked-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find list size
        curr = head
        counter = 0
        while curr:
            curr = curr.next
            counter += 1
        # iterate again to the target node
        middle_idx = counter // 2
        middle = head
        idx = 0
        while idx < middle_idx:
            middle = middle.next
            idx += 1

        return middle