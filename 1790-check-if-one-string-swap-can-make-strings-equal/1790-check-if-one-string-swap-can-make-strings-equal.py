class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if Counter(s1)!=Counter(s2):
            return False
        else:
            count=0
            for i,j in zip(s1,s2):
                if i!=j:
                    count+=1
            if(count==2):
                return True
            else:
                return False
         
            