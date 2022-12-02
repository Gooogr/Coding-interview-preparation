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
        
        # Find middle and end of LL
        while fast and fast.next: #make sure that we don't jump over LL
            fast = fast.next.next
            slow = slow.next
            
        # Reverse second half of LL
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # Now we can compare both parts
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            