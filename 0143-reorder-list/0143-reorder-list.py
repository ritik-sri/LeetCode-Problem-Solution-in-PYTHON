# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1ststep:Find Middle
        
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        #2ndstep:Reverse
        
        curr,prev=slow.next,None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        slow.next=None
        
        #3rd step:merging
        merge=ListNode(-1)
        mergepoint=merge
        head1 ,head2 = head, prev
        while head1 and head2:
            merge.next=head1
            head1=head1.next
            merge=merge.next
            merge.next=head2
            head2=head2.next
            merge=merge.next
        while head1:
            merge.next=head1
            head1=head1.next
            merge=merge.next
        while head2:
            merge.next=head2
            head2=head2.next
            merge=merge.next
        return mergepoint
            