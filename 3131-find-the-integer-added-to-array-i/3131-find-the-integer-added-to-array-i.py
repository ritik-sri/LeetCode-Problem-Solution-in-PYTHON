from collections import Counter
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1==nums2:
            return 0
        if len(nums1)==1 and len(nums2)==1:
            return nums2[0]-nums1[0]
        dic=Counter(nums2)
        a=min(nums2)-min(nums1)
        for i in nums1:
            if i+a not in dic:
                return False
        return a
                