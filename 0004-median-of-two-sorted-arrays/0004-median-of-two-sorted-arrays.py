class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=[]
        i,j=0,0
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<=nums2[j]):
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        while i<len(nums1):
            l.append(nums1[i])
            i+=1
        print(j)
        while j<len(nums2):
            l.append(nums2[j])
            j+=1
        n=len(l)
        a=0
        if(len(l)%2==0):
            a=(l[n//2-1]+l[(n//2)])/2
        else:
            a=l[n//2]
        print(l)
        return a
            
                