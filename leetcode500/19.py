# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = q = dummy = ListNode(0)
        dummy.next = head
        counter = 0
        while p:
            counter += 1
            p = p.next
        k = counter - n
        i = 1
        while i < k:
            q = q.next
            i += 1
        q.next = q.next.next
        return dummy.next
            
        