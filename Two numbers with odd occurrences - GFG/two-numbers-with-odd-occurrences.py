#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        dic={}
        l=[]
        for i in Arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i,j in dic.items():
            if j%2!=0:
                l.append(i)
        return sorted(l)[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends