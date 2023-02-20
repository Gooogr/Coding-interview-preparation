# https://leetcode.com/problems/reorder-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution with O(n), O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        # find median
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reorder half of list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # re-connect nodes
        left, right = head, prev
        while right.next:  # check if the right half is finished
            # keep old connections
            next_left, next_right = left.next, right.next
            # left1 -> right1
            left.next = right
            # left1 -> right1 -> left2
            right.next = next_left
            # make step
            left, right = next_left, next_right