# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        cr=0
        while l1 or l2 or cr:
            d1,d2=0,0
            if l1:
                d1=l1.val
            if l2:
                d2=l2.val
            sumi=d1+d2+cr
            cr=sumi//10
            curr.next=ListNode(sumi%10)
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next