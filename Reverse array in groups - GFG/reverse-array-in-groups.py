#User function template for Python
class Solution:
    #Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        # code here
        i=0
        while(i<=N):
            lst = arr[i:i+K][::-1]
            arr[i:i+K] = lst
            lst=[]
            i+=K
        return arr
#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends