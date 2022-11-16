class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        l=[]
        ans=[]
        dic={}
        for i in nums:
            if i%2==0:
                l.append(i)
        for i in l:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        if len(dic)<=0:
            return -1
        a=max(dic.values())
        for i,j in dic.items():
            if j == a:
                ans.append(i)
        return min(ans) 
                