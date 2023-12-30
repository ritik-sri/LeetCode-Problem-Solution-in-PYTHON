class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        if len(jd)<d:
            return -1
        
        cache={}
        def dfs(i, d, cur_max):
            if i==len(jd):
                return 0 if d==0 else float("inf")
            if d==0:
                return float("inf")
            if (i, d, cur_max) in cache:
                return cache[(i,d, cur_max)]
            
            cur_max = max(cur_max, jd[i])
            ans = min(
                  dfs(i+1, d, cur_max), #continue day
                  cur_max + dfs(i+1, d-1, -1)     #end day
            )
            
            cache[(i,d, cur_max)] = ans
            return ans
        
        return dfs(0,d,-1)