class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i,j in dic.items():
            if(j>1):
                s=True
                break
            else:
                s=False
        return s
        