# https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge sort
# Time complexity - O(n*logn)
# Space complexity - O(logn)
class Solution:
    def sortList(self, head):
        if not head or not head.next: 
            return head
        mid = self.get_middle_node(head)
        left, right = self.sortList(head), self.sortList(mid)
        return self.merge_sorted_lists(left, right)
    
    def get_middle_node(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next  # set head of the second half of the list
        slow.next = None # delete the connection between the first and second halves of the list.
        return mid
    
    def merge_sorted_lists(self, head1, head2):
        dummy = tail = ListNode(None)
        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        tail.next = head1 or head2
        return dummy.next