class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ex_list = sorted(nums1+nums2)
        len_ex_list = len(ex_list)

        if len_ex_list % 2 == 0:
            return (ex_list[len_ex_list // 2] + ex_list[len_ex_list // 2 - 1])/2
        return ex_list[len_ex_list // 2]