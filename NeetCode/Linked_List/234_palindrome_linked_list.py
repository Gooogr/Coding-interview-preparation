# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#### Memory O(n) solution ####
# Convert linked list to array and use two pointers
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        # Collect all values of linked list
        while head:
            nums.append(head.val)
            head = head.next
        # Make two-pointers check
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l+=1
            r-=1
        return True

#### Memory O(1) solution ####
# Two pointers: fast and slow
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # Find middle (slow pointer end position)
        # iteate until fast in None or in last element
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the seconds half: from middle (slow pointer) to the end
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # Iterate again to the middle -> <-
        # 1 -> 2 -> 2 <- 1
        # 1 -> 2 -> 3 <- 2 <- 1
        left, right = head, prev
        while right: #until we get to the middle
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
            