# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head       # 1
        even = head.next # 2
        even_head = even
        
        while even and even.next:
            # create connection over next even node
            odd.next = even.next
            # move pointer
            odd = odd.next
            # create connection over new odd node
            even.next = odd.next
            # move pointer
            even = even.next
        
        # connect head of evens to the tail of odds
        odd.next = even_head
        return head