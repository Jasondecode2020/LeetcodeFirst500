# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy for fixed pointer, p pointer will move forward
        p = dummy = ListNode()
        # carry is used as plus more than 10
        carry = 0
        # 2 pointers move from first place to last, p will pointer to next
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
            elif l1:
                val = l1.val + carry
            else:
                val = l2.val + carry
            p.next = ListNode(val % 10)
            p = p.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            carry = val // 10
        if carry:
            p.next = ListNode(1)
        return dummy.next