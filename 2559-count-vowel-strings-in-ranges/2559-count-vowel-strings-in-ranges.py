class Solution1:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        a=[0]*len(words)
        s="aeiou"
        l=[]
        count=0
        for i,j in enumerate(words):
            if j[0] in s and j[-1] in s:
                a[i]=1
            else:
                a[i]=0
        for i in queries:
            f,g=i[0],i[1]
            for j in range(f,g+1):
                if a[j]==1:
                    count+=1
            l.append(count)
            count=0
        return l
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = 'aeiou'
        num = []
        l = 0 
        for w in words:
            if w[0] in v and w[-1] in v:
                l += 1
                num.append(l)
            else:
                num.append(l)
        res = []
        for a, b in queries:
            if a != 0:
                res.append(num[b] - num[a-1])
            else:
                res.append(num[b])
        
        return res
    