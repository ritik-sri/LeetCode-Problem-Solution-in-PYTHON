class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sumi=0
        dummy = curr = head
        curr = curr.next
        while curr:
            if curr.val!=0:
                sumi+=curr.val
            else:
                dummy=dummy.next
                dummy.val=sumi
                sumi=0
            curr=curr.next
        dummy.next=None
        return head.next  
                
