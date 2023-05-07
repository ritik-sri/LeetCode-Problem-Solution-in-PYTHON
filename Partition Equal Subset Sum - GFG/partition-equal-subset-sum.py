# User function Template for Python3

class Solution:
    def equalPartition(self, N, nums):
        # code here
        if not nums:
            return True
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        memo = {}
        
        def helper(total, i):
            nonlocal nums, memo
            if (total, i) in memo:
                return memo[(total, i)]
            if i == len(nums):
                return False
            if total == 0:
                return True
            memo[(total, i)] = helper(total-nums[i], i+1) or helper(total, i+1)
            return memo[(total, i)]
        
        return helper(target, 0) 


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends