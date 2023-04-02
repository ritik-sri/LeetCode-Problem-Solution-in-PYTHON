class Solution(object):
    def successfulPairs(self, spells, potions, success):
        l = []
        potions.sort()
        for s in spells:
            count = float('inf')
            start = 0
            end = len(potions) - 1
            while start <= end:
                mid = (start + end) // 2
                if potions[mid] * s >= success:
                    count=min(count,mid)
                    end = mid - 1
                else:
                    start = mid + 1
            if count==float('inf'):
                l.append(0)
            else:
                l.append(len(potions)-count)
        return l
