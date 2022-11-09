class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        dic={}
        l=[]
        for i in a:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in b:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic.keys():
            l.append(i)
        return sorted(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends