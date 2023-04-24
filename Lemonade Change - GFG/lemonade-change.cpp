//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
bool lemonadeChange(int N, vector<int> &bills) {
        int five=0;
        int ten=0;
        int twenty=0;
        for(int i=0;i<bills.size();i++){
            if(bills[i]==5){
                five++;
            }
            if(bills[i]==10){
                if(five==0) return false;
                ten++;
                five--;
            }
            if(bills[i]==20){
                if(ten==0){
                    if(five<3) return false;
                    else{
                        five=five-3;
                    }
                }
                if(ten>0){
                    if(five==0)return false;
                    if(five>0){
                        ten--;
                        five--;
                    }
                }
            }
        }
        return true;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;

        vector<int> bills(N);
        for (int i = 0; i < N; i++) cin >> bills[i];

        Solution obj;
        int ans = obj.lemonadeChange(N, bills);
        if (ans)
            cout << "True" << endl;
        else
            cout << "False" << endl;
    }
    return 0;
}
// } Driver Code Ends