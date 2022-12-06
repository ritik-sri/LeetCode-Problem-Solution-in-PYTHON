# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=odd=ListNode(-1)
        p2=even=ListNode(-1)
        count=1
        while head:
            count+=1
            if count%2==0:
                odd.next=head
                odd=odd.next
            else:
                even.next=head
                even=even.next
            head=head.next
        even.next=None
        odd.next=p2.next
        return p1.next
        
        
        
            