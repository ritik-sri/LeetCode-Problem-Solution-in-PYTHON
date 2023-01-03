class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic={}
        l=[]
        bulls,cows=0,0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if guess[i] in dic:
                    dic[guess[i]]+=1
                else:
                    dic[guess[i]]=1
                l.append(secret[i])
        for i in l:
            if i in dic and dic[i]>0:
                dic[i]-=1
                cows+=1
        ans=""
        ans=str(bulls)+"A"+str(cows)+"B"
        return ans