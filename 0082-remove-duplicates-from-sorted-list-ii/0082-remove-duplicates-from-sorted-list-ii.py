# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict,Counter
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        l=[]
        dic=defaultdict(int)
        while a is not None:
            l.append(a.val)
            a=a.next
        dic=Counter(l)
        new=ListNode()
        dummy=new
        while head:
            if dic[head.val]==1:
                new.next=head
                new=new.next
                head=head.next
            else:
                head=head.next
            new.next=None
        return dummy.next