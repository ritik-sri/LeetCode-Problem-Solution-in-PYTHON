class Solution:

    def merge(self,head1,head2):

        hf=None

        ht=None

        while head1!=None and head2!=None:

            if ht==None and hf==None:

                if head1.data<head2.data:

                    hf=head1

                    ht=head1

                    head1=head1.next

                else:

                    ht=head2

                    hf=head2

                    head2=head2.next

            else:

                if head1.data<head2.data:

                    ht.next=head1

                    ht=ht.next

                    head1=head1.next

                else:

                    ht.next=head2

                    ht=ht.next

                    head2=head2.next

        if head1!=None:

            ht.next=head1

        if head2!=None:

            ht.next=head2

        return hf

    def mergeKLists(self,arr,K):
        last=K-1

        while last!=0:

            i=0

            j=last

            while i<j:

                arr[i]=self.merge(arr[i],arr[j])

                i+=1

                j-=1

                if i>=j:

                    last=j

        return arr[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends