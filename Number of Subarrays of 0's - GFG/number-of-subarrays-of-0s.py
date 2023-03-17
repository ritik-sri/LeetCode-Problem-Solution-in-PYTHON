#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        def f(n):
            if n==1:
                return 1
            else:
                return n+f(n-1)
                
        i=0
        l=[]
        j=0
        count=0
        ans=0
        while(j<=len(arr)-1):
            if(arr[j]==0):
                count+=1
            else:
                if count!=0:
                    ans+=(count*(count+1)//2)
                    count=0
            j+=1
        ans+=(count*(count+1)//2)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends