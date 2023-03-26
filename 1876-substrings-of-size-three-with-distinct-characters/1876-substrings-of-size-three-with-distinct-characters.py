from collections import defaultdict
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        hashmap = {}
        i = j = 0
        ans = 0
        while j < len(s):
            if s[j] in hashmap:
                hashmap[s[j]] += 1
            else:
                hashmap[s[j]] = 1
            if (j-i+1) < 3:
                j += 1
            elif (j-i+1) == 3:
                if len(hashmap) == 3:
                    ans += 1
                j += 1
                hashmap[s[i]] -= 1
                if hashmap[s[i]] == 0:
                    del hashmap[s[i]]
                i += 1
        return ans
                
                
