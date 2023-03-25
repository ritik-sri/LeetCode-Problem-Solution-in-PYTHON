from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostk(nums,k):
            i=0
            j=0
            ans=0
            l=defaultdict(int)
            while(j<=len(nums)-1):
                l[nums[j]]+=1
                while(len(l)>k):
                    l[nums[i]]-=1
                    if(l[nums[i]]==0):
                        del l[nums[i]]
                    i+=1
                j+=1
                ans+=(j-i+1)
            return ans
        return atmostk(nums,k)-atmostk(nums,k-1)