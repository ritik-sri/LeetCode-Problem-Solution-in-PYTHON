class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i=0
        total=0
        while tickets[k]>0:
            for i in range(len(tickets)):
                if tickets[i]!=0:
                    tickets[i]-=1
                    total+=1
                    if not tickets[k]:
                        break
        return total