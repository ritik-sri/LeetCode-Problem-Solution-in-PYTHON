from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(nums, output, ind, ans):
            if ind >= len(nums):
                ans.append(output[:])
                return
            output.append(nums[ind])
            f(nums, output, ind + 1, ans)
            output.pop()
            f(nums, output, ind + 1, ans)
        out = []
        ans = []
        f(nums, out, 0, ans)
        return ans