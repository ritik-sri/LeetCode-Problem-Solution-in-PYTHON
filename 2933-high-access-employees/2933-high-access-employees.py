from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        mp = defaultdict(list)
        for it in access_times:
            time = int(it[1])
            mp[it[0]].append(time)

        for _, times in mp.items():
            times.sort()

        ans = []
        for _, times in mp.items():
            for i in range(2, len(times)):
                if times[i] - times[i - 2] < 100:
                    ans.append(_)
                    break

        return ans
