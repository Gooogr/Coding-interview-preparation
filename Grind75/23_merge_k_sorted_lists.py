# https://leetcode.com/problems/merge-k-sorted-lists/

from copy import copy
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Neetcode approach
# Apply merge sort
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Handle edgecases
        if not lists or len(lists) == 0:
            return None
        # Apply merge sort to our lists pairs
        while len(lists) > 1:
            subresult = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # if we have odd number of lists
                subresult.append(self.merge(l1, l2))
            lists = subresult
        return lists[0]

    def merge(self, l1, l2):
        """ 
        Merge two sorted lists. Leetcode 21 task
        """
        head = ListNode()
        tail = head
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return head.next


# My approach with copying new nodes. 
# Demands to re-create nodes, otherwise it will be deleted during lists traversing
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while lists:
            min_val = float("inf")
            min_idx = -1
            # select min element from current k-heads of sorted lists
            for idx, item in enumerate(lists):
                if item and item.val < min_val:
                    min_val = item.val
                    min_idx = idx
            # if all lists are None - exit loop
            if min_idx == -1:
                break

            # add current minimum to result linked list
            tail.next = ListNode(lists[min_idx].val)
            tail = tail.next

            # update previously selected list
            lists[min_idx] = lists[min_idx].next
            if lists[min_idx] is None:
                del lists[min_idx]
        
        return head.next
