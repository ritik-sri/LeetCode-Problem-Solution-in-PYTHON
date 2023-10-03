from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = {i: [] for i in range(n)}
        
        for i in range(n):
            if i != headID:
                adj[manager[i]].append(i)
        
        def dfs(node):
            if not adj[node]:
                return 0
            max_time = 0
            for emp in adj[node]:
                max_time = max(max_time, dfs(emp))
            return max_time + informTime[node]
        
        return dfs(headID)
