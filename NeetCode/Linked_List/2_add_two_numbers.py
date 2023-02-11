# https://leetcode.com/problems/add-two-numbers/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Naive 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_str_val = ''
        second_str_val = ''

        # get the first number
        curr = l1
        while curr:
            first_str_val += str(curr.val)
            curr = curr.next

        # get the second number
        curr = l2
        while curr:
            second_str_val += str(curr.val)
            curr = curr.next

        # create final string
        result_value = int(first_str_val[::-1]) + int(second_str_val[::-1])
        result_str = str(result_value)[::-1]

        # create LL from string
        head = ListNode(int(result_str[0]))
        tail = head
        for letter in result_str[1:]:
            tail.next = ListNode(int(letter))
            tail = tail.next

        return head

# Effective. But complexity is the same
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next