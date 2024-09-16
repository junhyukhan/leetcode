# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getVal(node):
            if not node:
                return 0
            return node.val
        ret = ListNode()

        head = ret
        carry = 0
        while l1 or l2:
            a = getVal(l1)
            b = getVal(l2)
            val = a + b + carry
            if val >= 10:
                carry = 1
                val %= 10
            else:
                carry = 0
            head.next = ListNode(val)
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            head.next = ListNode(carry)
        return ret.next