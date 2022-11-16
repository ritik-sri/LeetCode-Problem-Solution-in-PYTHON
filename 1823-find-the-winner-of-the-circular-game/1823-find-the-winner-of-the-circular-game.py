class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends=[i for i in range(1,n+1)]
        p=0
        while(len(friends)>1):
            p=(p+k-1)%len(friends)
            friends.pop(p)
        return friends[0]
            