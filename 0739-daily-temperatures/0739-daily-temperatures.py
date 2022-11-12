class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[]
        stk=[]
        for i in range(len(temperatures)-1,-1,-1):
            if(len(stk)<=0):
                l.append(0)
                stk.append([i,temperatures[i]])
            elif(len(stk) and stk[-1][1]>temperatures[i]):
                l.append(1)
                stk.append([i,temperatures[i]])
            else:
                while(len(stk)>0 and stk[-1][1]<=temperatures[i]):
                    stk.pop()
                if(len(stk)<=0):
                    l.append(0)
                    stk.append([i,temperatures[i]])
                else:
                    l.append(abs(i-stk[-1][0]))
                    stk.append([i,temperatures[i]])
        return l[::-1]