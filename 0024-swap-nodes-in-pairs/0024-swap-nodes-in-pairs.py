# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p=head 
        c=1
        while p.next:
            if c:
                p.val,p.next.val=p.next.val,p.val
                p=p.next
                c=0
            else:
                p=p.next 
                c=1
        return head