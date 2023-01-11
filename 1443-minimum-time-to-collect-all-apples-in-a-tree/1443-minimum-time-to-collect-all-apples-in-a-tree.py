from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(set)

        for (a,b) in edges:
            graph[a].add(b)
            graph[b].add(a)

        def pre(node, res, visited):
            visited.add(node)
            y = False
            for x in graph[node]:
                if(x not in visited):
                    y = pre(x, res, visited) or y
            res[node] = hasApple[node] or y
            return res[node]
        
        apples = [False for _ in range(n)]
        pre(0, apples, set())

        def process(node,res, visited):
            visited.add(node)
            temp = 0
            for x in graph[node]:
                if(x not in visited and apples[x]):
                    res[node] += 2 + process(x,res, visited)
            return res[node]
        
        result = defaultdict(int)
        process(0, result, set())

        return result[0]