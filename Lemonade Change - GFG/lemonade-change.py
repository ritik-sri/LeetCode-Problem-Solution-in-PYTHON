#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def lemonadeChange(self, N, bills):
        count_5 = 0
        count_10 = 0
        count_20 = 0
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 >= 1:
                    count_5 -= 1
                    count_10 += 1
                else:
                    return False
            elif bill == 20:
                if count_10 >= 1 and count_5 >= 1:
                    count_10 -= 1
                    count_5 -= 1
                    count_20 += 1
                elif count_5 >= 3:
                    count_5 -= 3
                    count_20 += 1
                else:
                    return False
        return True

        
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends