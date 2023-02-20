# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# One-pass approach, two pointers approach
# General idea - set left and right pointers.
# Push them until left will be before target, and right - in None
# Thus we will initialize left in dummy node before head
# and right pointer - in head + n distance
# 1 -> 2 -> 3 -> 4 -> 5, n = 2 (4)
# Initializtion:
# dummy (L) ->  1 -> 2 -> 3(R) -> 4 -> 5 -> None
# Destination
# dummy  ->  1 -> 2 -> 3(L) -> 4 -> 5 -> None(R)
# And after that just jump over target node
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left = dummy_node
        right = head
        # find starting right position
        while n > 0:
            right = right.next
            n -= 1
        # move pointer until right gets the end
        while right:
            left = left.next
            right = right.next
        # delete node
        left.next = left.next.next
        return dummy_node.next



# Naive three-pass approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        # Helper function
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev


        # Reverse the list
        reversed_head = reverseList(head)
        
        # Traverse to the node just before the Nth node
        count = 1
        curr = reversed_head
        while count < n:
            prev = curr
            curr = curr.next
            count += 1
        
        # Delete the Nth node
        if curr == reversed_head:
            reversed_head = curr.next
        else:
            prev.next = curr.next
        
        # Reverse the list back
        head = reverseList(reversed_head)
        
        return head
    

