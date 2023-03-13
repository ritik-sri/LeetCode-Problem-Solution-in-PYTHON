from typing import List
class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = [0] * V

        def DFS(node, parent):
            visited[node] = 1
            
            for neighbour in adj[node]:

                if not visited[neighbour]:
                    if DFS(neighbour, node)==True:
                        return True
                
                elif neighbour != parent: return True
            
            return False
            
        return any(DFS(i, -1) for i in range(V) if not visited[i])



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends