class Solution {
public:
    int totalFruit(vector<int>& f) {
        unordered_map<int,int>mp;
        
        int n=f.size();
        int i=0,j=0;
        int maxi=INT_MIN;
        
        while(i<n)
        {
            mp[f[i]]++;
            while(mp.size()>2)
            {
                mp[f[j]]--;
                if(mp[f[j]]==0)
                    mp.erase(f[j]);
                j++;
            }
            
            maxi=max(maxi,i-j+1);
            i++;
        }
        
        return maxi;
        
    }
};