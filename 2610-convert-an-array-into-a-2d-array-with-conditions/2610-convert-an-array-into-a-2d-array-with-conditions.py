class Solution(object):
    def findMatrix(self, nums):
        ans=[]
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        while dic:
            l=[]
            for i,j in dic.items():
                dic[i]-=1
                l.append(i)
                if dic[i]==0:
                    del dic[i]
            ans.append(l)
        return ans