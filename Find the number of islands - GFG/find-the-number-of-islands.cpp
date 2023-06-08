//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    // Function to find the number of islands.
    void dfs(vector<vector<char>>& v,int i,int j)
    {
        if(i<0 || j<0 || i>=v.size() || j>=v[0].size() || v[i][j]=='0')
            return;
        
        v[i][j]='0';// reset to 0 as this is already included
        dfs(v,i-1,j);
        dfs(v,i+1,j);
        dfs(v,i,j-1);
        dfs(v,i,j+1);
        dfs(v,i-1,j+1);
        dfs(v,i+1,j-1);
        dfs(v,i-1,j-1);
        dfs(v,i+1,j+1);
    }
    int numIslands(vector<vector<char>>& grid) {
        // Code here
        int res=0;
        for(int i=0;i<grid.size();i++)
            for(int j=0;j<grid[i].size();j++)
                if(grid[i][j]=='1')// if 1, call the dfs and make res++ to add this island 
                {
                    dfs(grid,i,j);
                    res++;
                }
        return res;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
// } Driver Code Ends