from collections import defaultdict
class Solution:
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, n, sum):
        mp=defaultdict(int)
        subs=0
        pref=0
        mp[0]=1
        for i in range(n):
            pref+=arr[i]
            subs+=mp[pref-sum]
            mp[pref]+=1
        return subs
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sum=int(input())
        
        print(Solution().subArraySum(arr, n, sum))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends