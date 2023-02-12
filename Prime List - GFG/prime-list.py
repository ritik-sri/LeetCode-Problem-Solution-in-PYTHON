from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""
class Solution:
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        def isprime(n):
            if n <= 1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        def nearestprime(n):
            if(n==1):
                return 2
            elif n==2:
                return 3
            elif n>=3:
                i=1
                while(True):
                    if(isprime(n-i)):
                        break
                    i+=1
                j=1
                while(True):
                    if(isprime(n+j)):
                        break
                    j+=1
            if(i<j):
                return n-i
            elif i>j:
                return n+j
            else:
                return min(n-i,n+j)
        a=head
        new=Node(-1)
        p=new
        while a:
            if(isprime(a.data)):
                new.next=a
                new=new.next
            else:
                subs=nearestprime(a.data)
                new.next=Node(subs)
                new=new.next
            a=a.next
        return p.next

#{ 
 # Driver Code Starts
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()
def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        head = inputList()
        
        obj = Solution()
        res = obj.primeList(head)
        
        printList(res)
        

# } Driver Code Ends