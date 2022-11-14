# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1    # connect object to linked list
                list1 = list1.next   # make step
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # if one linked list is bigger than other - add final chunk
        tail.next = list1 or list2
        return dummy.next
        