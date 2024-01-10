from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def adjacentList(root):
            graph = defaultdict(list)
            q = deque([root])
            while q:
                node = q.popleft()
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    q.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    q.append(node.right)
            return graph
        adj=adjacentList(root)
        
        q = deque([start])  
        count = -1
        visited ={start}
        while q:
            for _ in range(len(q)):
                a = q.popleft()
                for i in adj[a]:
                    if i not in visited:
                        q.append(i)
                        visited.add(i)
            count += 1
        return count