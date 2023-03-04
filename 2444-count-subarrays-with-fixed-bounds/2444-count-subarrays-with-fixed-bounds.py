class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_out = last_k1 = last_k2 = -1
        ret = 0
        for idx, i in enumerate(nums):
            if i == minK: last_k1 = idx
            if i == maxK: last_k2 = idx
            if i < minK or i > maxK: last_out = idx
            else: ret += max(min(last_k1, last_k2) - last_out, 0)
        return ret