class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=odd=ListNode(-1)
        p2=even=ListNode(-1)
        count=0
        while head:
            count+=1
            if count%2!=0:
                odd.next=head
                odd=odd.next
                head=head.next
            else:
                even.next=head
                even=even.next
                head=head.next
        even.next=None
        odd.next=p2.next
        return p1.next