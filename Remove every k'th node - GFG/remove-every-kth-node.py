#Your task is to complete this function
#Your function should return the new head pointer
def deleteK(head, k):
    #code here
    if head is None or k==1:
        return None
    if k==0:
        return head
    a=head
    count=1
    while a is not None and a.next is not None:
        count+=1
        if count==k:
            a.next=a.next.next
            count=1
        a=a.next
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