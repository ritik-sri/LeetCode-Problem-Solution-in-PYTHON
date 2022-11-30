class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            s=nums[i]
            while(j<k):
                if(s+nums[j]+nums[k]==0):
                    l.append((s,nums[j],nums[k]))
                    j+=1
                    k-=1
                elif(s + nums[j] + nums[k])>0:
                    k-=1
                else:
                    j+=1
        return set(l)