class Solution:
    
    def reverse(self,h):
        if not h or not h.next:
            return h
        ptr = None
        while h:
            temp = h.next
            h.next = ptr
            ptr = h
            h = temp
        return ptr
    
    def rex(self,head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            slow = slow.next
        ex = slow.next
        slow.next = None
        return ex
        
    def reorderList(self,head):
        h = self.rex(head)
        h = self.reverse(h)
        p = head
        while h:
            x = h.next
            h.next = p.next
            p.next = h
            p = p.next.next
            h = x
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self,head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob=Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends