class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        a=0
        b=1
        c=1
        sum=0
        for i in range(3,n+1):
            t=c+a+b
            a=b
            b=c
            c=t
        return t