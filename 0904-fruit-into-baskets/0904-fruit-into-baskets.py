from collections import defaultdict
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i,j=0,0
        ans=[]
        if len(fruits)<=2:
            return len(fruits)
        if len(Counter(fruits))<2:
            return len(fruits)
        mp = defaultdict(int)
        while(j<len(fruits)):
            mp[fruits[j]]+=1
            if(len(mp)<2):
                j+=1
            elif len(mp)==2:
                ans.append(j-i+1)
                j+=1
            elif len(mp)>2:
                while len(mp)>2:
                    mp[fruits[i]]-=1
                    if mp[fruits[i]]==0:
                        del mp[fruits[i]]
                    i+=1
                j+=1
        if len(ans)==0:
            return 0
        else:
            return max(ans)