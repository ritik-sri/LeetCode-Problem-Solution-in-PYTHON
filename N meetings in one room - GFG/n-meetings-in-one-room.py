#User function Template for python3
import heapq
class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        l=[]
        for i in range(n):
            l.append([start[i],end[i]])
        l.sort(key=lambda x:x[1])
        minheap=[]
        cnt=1
        for i,j in l:
            if(len(minheap)==0):
                heapq.heappush(minheap,j)
            else:
                c=heapq.heappop(minheap)
                if(c<i):
                    cnt+=1
                    heapq.heappush(minheap,j)
                else:
                    heapq.heappush(minheap,c)
        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends