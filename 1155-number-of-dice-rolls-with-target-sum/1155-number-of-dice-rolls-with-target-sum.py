class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo={}
        MOD=10**9+7
        def back(n,target):
            if target==0 and n==0:return 1
            if target<0 or n<=0:return 0
            
            if (n,target) in memo:return memo[(n,target)]
            memo[(n,target)]=0
            for i in range(1,min(k,target)+1):
                memo[(n,target)]+=back(n-1,target-i)
            return memo[(n,target)] % MOD
        return back(n,target)