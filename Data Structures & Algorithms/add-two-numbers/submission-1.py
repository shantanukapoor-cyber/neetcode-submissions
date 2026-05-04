# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first - (l1.val + l2.val) = final.val, next node is None.
        # if final.val > 9, store final.val//10 as carry 
        # and final.val%10 as final.val
        # then second - carry.val + l1.val + l2.val, 
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = value // 10
            value = value % 10
            dummy.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        if l1:
            while l1:
                value = l1.val + carry
                carry = value // 10
                value = value % 10
                dummy.next = ListNode(value)
                l1 = l1.next
                dummy = dummy.next
        else:
            while l2:
                value = l2.val + carry
                carry = value // 10
                value = value % 10
                dummy.next = ListNode(value)
                l2 = l2.next
                dummy = dummy.next
        if carry != 0:
            dummy.next = ListNode(1)
        return cur.next
        

