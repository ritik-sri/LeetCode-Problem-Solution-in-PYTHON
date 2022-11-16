class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        l=[]
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        a=len(nums)//3
        print(dic)
        for i,j in dic.items():
            if j > a:
                l.append(i)
        return l 
            