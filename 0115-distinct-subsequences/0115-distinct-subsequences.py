def f(i, j, s, t, memo):
    if j < 0:
        return 1
    if i < 0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if s[i] == t[j]:
        memo[(i, j)] = f(i-1, j-1, s, t, memo) + f(i-1, j, s, t, memo)
    else:
        memo[(i, j)] = f(i-1, j, s, t, memo)
    return memo[(i, j)]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s) 
        n = len(t)
        memo = {}
        return f(m-1, n-1, s, t, memo)
