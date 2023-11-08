import heapq

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l = [-a, -b, -c]
        heapq.heapify(l)
        count = 0
        
        while len(l) > 1:
            a = abs(heapq.heappop(l))
            b = abs(heapq.heappop(l))
            a -= 1
            b -= 1
            if a > 0:
                heapq.heappush(l, -a)  
            if b > 0:
                heapq.heappush(l, -b)
            count += 1
        
        return count
