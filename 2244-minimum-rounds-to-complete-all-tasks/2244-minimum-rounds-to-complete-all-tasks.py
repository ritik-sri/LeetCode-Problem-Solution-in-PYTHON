from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hash=Counter(tasks)
        a=hash.values()
        count=0
        for i in a:
            if i<2:
                return -1
            if i>3:
                g=math.ceil(i/3)
                count+=g
            else:
                count+=1
        return count