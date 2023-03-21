class Solution:
    def solve(self, ans, nums, i):
        if i == len(nums):
            ans.append(nums[:])
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.solve(ans, nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve(ans, nums, 0)
        return ans
