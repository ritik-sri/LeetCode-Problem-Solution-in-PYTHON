class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        while(i<j):
            if(nums[i]%2!=0 and nums[j]%2==0):
                nums[i],nums[j]=nums[j],nums[i]
            elif(nums[i]%2==0 and nums[j]%2==0):
                i+=1
            elif(nums[i]%2!=0 and nums[j]%2!=0):
                j-=1
            else:
                i+=1
                j-=1
        return nums