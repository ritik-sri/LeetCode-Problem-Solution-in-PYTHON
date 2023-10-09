from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstposition(nums, target):
            start = 0
            end = len(nums) - 1
            res = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] == target:
                    res = mid
                    end = mid - 1
                else:
                    end = mid - 1
            return res
        
        def lastposition(nums, target):
            start = 0
            end = len(nums) - 1
            res = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] == target:
                    res = mid
                    start = mid + 1
                else:
                    end = mid - 1
            return res
        
        a = firstposition(nums, target)
        b = lastposition(nums, target)
        return [a, b]
