class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        smallest = []
        for element in matrix:
            smallest.extend(element)
        heapq.heapify(smallest)
        while k > 0:
            final = heapq.heappop(smallest)
            k -= 1
        return final