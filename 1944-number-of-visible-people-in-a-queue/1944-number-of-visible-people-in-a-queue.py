class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        l=[]
        stk=[]
        n=len(heights)
        for i in range(n-1,-1,-1):
            if(len(stk)<=0):
                l.append(0)
                stk.append([i,heights[i]])
            elif(len(stk) and (stk[-1][1]>heights[i])):
                l.append(1)
                stk.append([i,heights[i]])
            else:
                cnt=0
                while(len(stk)>0 and stk[-1][1]<=heights[i]):
                    stk.pop()
                    cnt+=1
                if(len(stk)<=0):
                    l.append(cnt)
                    stk.append([i,heights[i]])
                else:
                    l.append(cnt+1)
                    stk.append([i,heights[i]])
        l=l[::-1]
        return l