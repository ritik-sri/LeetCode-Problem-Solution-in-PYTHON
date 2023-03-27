class Solution:
    def dfs(self, graph, node, visit):
        visit.add(node)
        for nei in graph[node]:
            if nei not in visit:
                visit.add(nei)
                self.dfs(graph, nei, visit)
            elif nei in self.ans:
                self.ans.remove(nei)
    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
        print(graph)
        self.ans = set()
        visit = set()
        for i in range(n):
            if i not in visit:
                self.ans.add(i)
                self.dfs(graph, i, visit)
        
        return list(self.ans)