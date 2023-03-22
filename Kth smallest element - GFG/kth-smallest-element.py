#User function Template for python3
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        l=[]
        for i in arr:
            heapq.heappush(l,1*i)
        i=0
        while i<k-1:
            heapq.heappop(l)
            i+=1
        return abs(heapq.heappop(l))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends