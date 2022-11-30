class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        a=len(dic.values())
        b=len(set(dic.values()))
        return a==b