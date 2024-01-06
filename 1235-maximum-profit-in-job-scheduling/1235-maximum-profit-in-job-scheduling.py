class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #stores the array values as tuples in intervals
        intervals = sorted(zip(startTime,endTime,profit))

        #to prevent the sub problem re-executing
        cache = {}

        
        def recursive(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            #don't include
            res = recursive(i + 1)

            #include
            #bisect is binarysearch function
            j = bisect.bisect(intervals,(intervals[i][1],-1,-1))

            cache[i] = res = max(res , intervals[i][2] +  recursive(j))

            return res
        
        return recursive(0)
