class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=bin(x)
        y=bin(y)
        x=str(x)[2:]
        y=str(y)[2:]
        count=0
        if len(x)<len(y):
            a=len(y)-len(x)
            x="0"*a+x
        else:
            b=len(x)-len(y)
            y="0"*b+y
        print(x,y)
        for i,j in zip(x,y):
            if i!=j:
                count+=1
        return count