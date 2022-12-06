#User function Template for python3
import heapq
def kthSmallest(mat, n, k): 
    # Your code goes here
    ans=0
    if k > n*n:
        return 2147483647
    minheap=[]
    for i in mat:
        s=i
        for j in s:
            heapq.heappush(minheap,j)
    if k>len(minheap):
        k=k%len(minheap)
    for i in range(k):
        ans=heapq.heappop(minheap)
    return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()




# } Driver Code Ends