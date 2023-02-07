from collections import defaultdict
class Solution:
    def totalFruit(self, f: List[int]) -> int:
        mp = defaultdict(int)
        n = len(f)
        i = 0
        j = 0
        maxi = 0
        while i < n:
            mp[f[i]] += 1
            while len(mp) > 2:
                mp[f[j]] -= 1
                if mp[f[j]] == 0:
                    del mp[f[j]]
                j += 1
            maxi = max(maxi, i - j + 1)
            i += 1
        return maxi
'''
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        i=0
        j=0
        maxi=0
        d=defaultdict(int)
        while(j<n):
            d[fruits[j]]+=1
            while len(d)>2:
                d[fruits[i]]-=1
                if(d[fruits[i]])==0:
                    del d[fruits[i]]
                i+=1
            j+=1
            maxi=max(j-i+1,maxi)
            j+=1
        return maxi
        '''