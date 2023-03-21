#User function Template for python3

class Solution:
    def solve(self, ans, nums, i):
        if i == len(nums):
            if "".join(nums[:]) not in ans:
                ans.append("".join(nums[:]))
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.solve(ans, nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]
    
    def find_permutation(self, S):
        ans = []
        nums=list(S)
        self.solve(ans, nums, 0)
        ans=sorted(ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends