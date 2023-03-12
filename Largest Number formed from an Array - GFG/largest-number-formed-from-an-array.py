#User function Template for python3
class Solution:

	def printLargest(self,arr):
	    arr = list(map(str, arr))

        # Define custom comparison function for sorting
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        # Sort the array using the custom comparison function
        arr = sorted(arr, key=functools.cmp_to_key(compare))

        # Concatenate the sorted strings
        result = ''.join(arr)

        # Handle leading zeros
        result = result.lstrip('0')

        # Return the result as a string
        if result == '':
            return '0'
        else:
            return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends