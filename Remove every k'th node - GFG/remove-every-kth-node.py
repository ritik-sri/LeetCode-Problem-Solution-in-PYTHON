def deleteK(head, k):
    # Edge cases
    if k == 1:
        return None

    # Traverse the linked list
    t = head
    cnt = 1
    while t is not None and t.next is not None:
        cnt += 1
        if cnt == k:
            cnt = 1
            t.next = t.next.next
        t = t.next

    # Return the updated head of the linked list
    return head


#{ 
 # Driver Code Starts
class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(ptr):
    while ptr!=None:
        print(ptr.data, end=" ")
        ptr= ptr.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        llist = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = int(input())
        for i in values:
            llist.insert(i)
        head = deleteK(llist.get_head(), k)
        printlist(head)
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends