from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        n = len(edges)
        for i in range(n):
            self.graph[edges[i][0]].append(edges[i][1])
            self.graph[edges[i][1]].append(edges[i][0])
        maxi=max(self.graph)
        for i,j in self.graph.items():
            if len(j)==maxi-1:
                return i