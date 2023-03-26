from typing import List
from collections import deque
class Solution:
    def bfs(node: int, adj: List[List[int]], col: List[int]) -> bool:
        queue = deque()
        queue.append(node)
        col[node] = 1
        while queue:
            v = queue.popleft()
            for j in adj[v]:
                if col[j] == -1:
                    col[j] = 1 - col[v]
                    queue.append(j)
                else:
                    if col[j] == col[v]:
                        return False
        return True
    def isBipartite(self, V, adj):
        col = [-1] * V
        for i in range(V):
            if col[i] == -1:
                if not Solution.bfs(i, adj, col):
                    return False
        return True

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends