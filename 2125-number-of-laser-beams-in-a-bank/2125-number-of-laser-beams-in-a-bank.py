class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        multi = 0
        total = 0
        count = 0
        last = -1

        rows, cols = len(bank), len(bank[0])

        for row in range(rows):
            for col in range(cols):
                if bank[row][col] == '1':
                    count +=1
                if last >= 0 and col == cols-1 and count > 0:
                    total+=(count*multi)

            if count > 0:
                last = row
                multi = count
            count = 0
        
        return total