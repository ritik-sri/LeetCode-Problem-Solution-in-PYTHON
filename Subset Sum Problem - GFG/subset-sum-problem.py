class Solution:
    def isSubsetSum(self, N, arr, target):
        memo = {}

        def find(ind, target):
            if (ind, target) in memo:
                return memo[(ind, target)]
            if target == 0:
                memo[(ind, target)] = True
                return True
            if ind == 0:
                memo[(ind, target)] = arr[0] == target
                return memo[(ind, target)]
            take = False
            if target >= arr[ind]:
                take = find(ind - 1, target - arr[ind])
                memo[(ind - 1, target - arr[ind])] = take
            not_take = find(ind - 1, target)
            memo[(ind - 1, target)] = not_take
            return take or not_take

        return find(N - 1, target)


        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends