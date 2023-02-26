def f(i, j, s, t, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    if j < 0:
        memo[(i, j)] = i+1
    elif i < 0:
        memo[(i, j)] = j+1
    elif s[i] == t[j]:
        memo[(i, j)] = f(i-1, j-1, s, t, memo)
    else:
        memo[(i, j)] = 1 + min(f(i-1, j, s, t, memo), f(i, j-1, s, t, memo), f(i-1, j-1, s, t, memo))
    return memo[(i, j)]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        memo = {}
        return f(m-1, n-1, word1, word2, memo)
