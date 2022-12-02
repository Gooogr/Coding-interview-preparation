# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
#### While loop approach ####
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:          # repeat until we get to the end of original linked list
            temp = curr.next # save old link
            curr.next = prev # create new reversed link
            # make step
            prev = curr
            curr = temp
        return prev          # return new head

#### Recursive approach ####
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)
        return reverse(head, None)