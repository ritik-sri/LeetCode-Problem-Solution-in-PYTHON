//{ Driver Code Starts
/* Driver program to test above function */

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
    int fun(vector<vector<int>>& A, int k){
        int i, j;
        int n = A.size();
        
        int cnt = 0;
        bool f = false;
        
        for(i=0; i < n; i++){
           int diff = (A[i][1] - A[i][0] + 1);
            if((cnt + diff) < k){
                cnt += diff;
            }
            else{
                int temp = cnt;
                cnt = (A[i][0]-1 + k - temp);
                f = true;
                break;
            }
        }
        
        if(f)
            return cnt;
        else return -1;
    }
    
    vector<int>kthSmallestNum(int n, vector<vector<int>>&range, int q, vector<int>queries){
        //Write your code here
        
        int i, j;
        sort(range.begin(), range.end());
        // merge the intervals;
        vector<vector<int>> v;
        
        vector<int> I = range[0];
        
        for(i=1; i < n; i++){
            if(range[i][0] > I[1]){
                v.push_back(I);
                I = range[i];
            }
            else{
                I[0] = min(I[0], range[i][0]);
                I[1] = max(I[1], range[i][1]);
            }
        }
        
        v.push_back(I);
        
        // solve for the queries: O(q*n)
        
        vector<int> ans;
        
        for(i=0; i < q; i++){
            int val = fun(v, queries[i]);
            
            ans.push_back(val);
        }
        
        return ans;
        
        
    } 
};


//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin >> n;
	    vector<vector<int>>range(n, vector<int>(2, 0));
	    for(int i = 0 ; i < n; i++){
	        cin >> range[i][0] >> range[i][1];
	    }
	    int q;
	    cin >> q;
	    vector<int>queries;
	    for(int i = 0 ; i < q; i++){
	        int x;
            cin >> x;
	        queries.push_back(x);
	    }
	    Solution ob;
	    vector<int>ans = ob.kthSmallestNum(n, range, q, queries);
	    for(auto it : ans){
	        cout << it << " ";
	    }
	    cout << endl;
	}
	return 0;
}

// } Driver Code Ends