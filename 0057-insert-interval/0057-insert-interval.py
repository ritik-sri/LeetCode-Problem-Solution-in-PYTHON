class Solution:
    def insert(self, A: List[List[int]], n: List[int]) -> List[List[int]]:
        L = bisect_left(A, n[0], key=itemgetter(1))
        R = bisect_right(A, n[1], key=itemgetter(0))
        n = [min(n[0], A[L][0]), max(n[1], A[R-1][1])] if L < R else n
        A[L:R] = n,
        return A