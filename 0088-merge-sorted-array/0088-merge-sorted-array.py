class Solution(object):
    def merge(self, nums1, m, nums2, n):
        del nums1[m:len(nums1)]
        del nums2[n:len(nums2)]
        for i in nums2:
            nums1.append(i)
        nums1.sort()