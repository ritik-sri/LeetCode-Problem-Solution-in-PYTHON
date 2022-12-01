class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if(len(nums)==0):
            return nums
        i=0
        while(i<len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]=nums[i]*2
                nums[i+1]=0
            i+=1
        #print(nums)
        left,right=0,0
        while(right<len(nums)):
            if(nums[right]==0):
                right+=1
            else:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                right+=1
                left+=1
        return nums
            
            