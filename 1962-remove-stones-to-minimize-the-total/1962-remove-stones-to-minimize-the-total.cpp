class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        int s=0;
       /* sort(piles.begin(),piles.end());
        
        for(int i=piles.size()-1;  i>=0; i--){
            if(k>0 && piles[i]>0){
                piles[i]=piles[i]-(piles[i]/2);
                k--;
            }
            cout<<piles[i]<<endl;
            s=s+piles[i];
            if(i<0 && k>0){
                i=piles.size()-1;
            }
        }*/
       
       priority_queue<int>pq;
       for(int i=0;i<piles.size();i++){
           pq.push(piles[i]);
       }
       while(k--){
           int t=pq.top();
           //cout<<pq.top()<<endl;
           t=t-t/2;
          // cout<<t<<endl;
           pq.pop();
           pq.push(t);
       }
       


       while(!pq.empty()){
           s=s+pq.top();
           pq.pop();
       }


        return s;
        
    }
};