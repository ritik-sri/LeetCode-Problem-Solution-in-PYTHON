class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = {0}
        while q:
            node = q.popleft()
            for k in rooms[node]:
                if k not in visited:
                    visited.add(k)
                    q.append(k)
        return len(visited) == len(rooms)