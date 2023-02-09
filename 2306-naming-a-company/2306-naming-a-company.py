class Solution:
    def distinctNames(self, A: List[str]) -> int:
        m, A = defaultdict(Counter), set(A)
        for w in A:
            m[w[0]] += Counter(x for x in ascii_lowercase if x + w[1:] not in A)
        return sum(m[x][y] * m[y][x] for x in m for y in m)
        