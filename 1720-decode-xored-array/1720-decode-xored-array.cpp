class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        int n = encoded.size();
        vector<int> ans(n+1 , first);

        int x = ans[0];
        for(int i=0 ; i<n; i++){
            ans[i+1] = x ^ encoded[i];
            x = ans[i+1];
        }
        return ans;
    }
};