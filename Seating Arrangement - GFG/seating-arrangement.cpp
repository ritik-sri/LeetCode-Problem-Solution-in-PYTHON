//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
bool is_possible_to_get_seats(int n, int m, vector<int>&arr){
        // Write your code here.
        for(int i = 0 ; i  < m ; i++){
            if(n==0) break;
            if(i>0 && i < m-1 && arr[i-1]==0 && arr[i+1]==0 && !arr[i]){
                n--;
                arr[i] = 1;
            }
            else if(i==0 && arr[i+1]==0 && !arr[i]){
                n--;
                arr[i] = 1;
            }
            else if(i==m-1 && arr[i-1]==0 && !arr[i]){
                n--;
                arr[i] = 1;
            }
            
        }
        return n==0;
    }
    
};

//{ Driver Code Starts.

int main(){

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int m;
        cin >> m;
        vector<int> seats(m);
        for (int i = 0; i < m; i++) {
            cin >> seats[i];
        }
        Solution obj;
        if (obj.is_possible_to_get_seats(n, m, seats)) {
            cout << "Yes" << endl;
        }
        else {
            cout << "No" << endl;
        }
    }
}

// } Driver Code Ends