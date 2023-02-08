# https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time complexity O(n)
# Space complexity O(n) - non-optimal solution
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hash_node = set()
        curr = head
        while curr:
            if curr in hash_node:
                return curr
            hash_node.add(curr)
            curr = curr.next

# Time complexity O(n)
# Space complexity O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
            slow, fast = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                 # first option - we confirmed the cycle
                if fast == slow:
                    break    
            # second option - the LL doesn't have cycle
            if not fast or not fast.next:
                return None

            # Track the cycle start node
            # Currently pointer somewhere in cycle
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast


# The logic behind cycle start traking (final while loop):
#  The distance between the head of the linked list and the start of the cycle 
# (L) is equal to the distance between the meeting point of the slow and 
# fast pointers and the start of the cycle (S).