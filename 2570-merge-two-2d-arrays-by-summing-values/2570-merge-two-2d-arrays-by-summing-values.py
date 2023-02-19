class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while i<len(nums1) and j<len(nums2):
            if(nums1[i][0]==nums2[j][0]):
                ans.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            else:
                if(nums1[i][0]<nums2[j][0]):
                    ans.append(nums1[i])
                    i+=1
                else:
                    ans.append(nums2[j])
                    j+=1
        while i<len(nums1):
            ans.append(nums1[i])
            i+=1
        while j<len(nums2):
            ans.append(nums2[j])
            j+=1
        return ans