class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times=[]
        for hour in range(12):
            for min in range(60):
                if (bin(hour)+bin(min)).count('1')==turnedOn:
                    times.append(f'{hour}:{min:02d}')
        return times