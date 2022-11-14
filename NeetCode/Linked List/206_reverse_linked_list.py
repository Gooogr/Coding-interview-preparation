# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # end point of reversed list
        curr = head # head of list that will connect to reversed list at first
        # Geneal idea:
        # None, 1->2
        # None<-1, 2
        # None<-1<-2 
        # Next element in original order for 2 is None - exit while loop
        while curr:
            next_original = curr.next # remember next step before broken link
            curr.next = prev          # change link from -> to <-       
            prev = curr               # step forward in original order   
            curr = next_original      # step forward in original order
        return prev

# Recursive approach
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