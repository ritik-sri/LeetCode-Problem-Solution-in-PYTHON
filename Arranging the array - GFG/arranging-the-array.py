#User function Template for python3

def Rearrange( a, n):
    # Your code goes here
    pos=[]
    neg=[]
    for i in a:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)
    a[:]=neg+pos
    return a
        
    
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        Rearrange(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends