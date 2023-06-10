class Solution:
    def uniqueRow(self, row, col, M):
        unique_rows = []
        unique_set = set()
        for i in range(row):
            current_row = ""
            for j in range(col):
                current_row += str(M[i][j])
            if current_row not in unique_set:
                unique_set.add(current_row)
                unique_rows.append(current_row)
        return unique_rows



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    testcase = int(input())
    while(testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = [[None for _ in range(col)]for _ in range(row)]
        s = input().split()
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(s[i*col+j])
        
        ob = Solution()
        a = ob.uniqueRow(row, col, matrix)
        
        for row in a:
            for value in row:
                print(value,end = " ")
            print("$",end = "")
        print()
        testcase -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends