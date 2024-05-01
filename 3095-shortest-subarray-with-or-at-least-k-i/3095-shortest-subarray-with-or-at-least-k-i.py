class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        mi = float("inf")
        
        for i in range(len(nums)):
            bit = 0

            for j in range(i,len(nums)):
                bit |= nums[j]
                if bit >=k:
                    mi = min(mi,j-i+1)
                else:
                    continue

        return mi if mi != float("inf") else -1
