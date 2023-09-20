class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int total_sum = 0;
        int n = nums.size();
        for(int i = 0; i < n; i++)
            total_sum += nums[i];
        total_sum -= x;

        int ans = INT_MAX;
        int sum = 0;
        int i = 0, j = 0;
        while(j < n){
            sum += nums[j];
            if(sum > total_sum)
                while(i <= j && sum > total_sum)
                    sum -= nums[i++];

            if(sum == total_sum)
                ans = min(ans, n - (j - i) - 1);
            j++;
        }

        return ans == INT_MAX ? -1 : ans;

    }
};
