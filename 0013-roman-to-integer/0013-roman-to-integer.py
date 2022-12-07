class Solution:
    def romanToInt(self, s: str) -> int:
        count=0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        while(i<len(s)-1):
            if(s[i]=='I' and s[i+1]=='V'):
                count+=4
                i+=1
            elif(s[i]=='I' and s[i+1]=='X'):
                count+=9
                i+=1
            elif(s[i]=='X' and s[i+1]=='L'):
                count+=40
                i+=1
            elif(s[i]=='X' and s[i+1]=='C'):
                count+=90
                i+=1
            elif(s[i]=='C' and s[i+1]=='D'):
                count+=400
                i+=1
            elif(s[i]=='C' and s[i+1]=='M'):
                count+=900
                i+=1
            else:
                count+=dic[s[i]]
            i+=1
        if i!=len(s):
            count+=dic[s[len(s)-1]]
        return count
            