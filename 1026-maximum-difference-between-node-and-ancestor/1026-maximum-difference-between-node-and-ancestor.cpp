/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res =0;

    int maxAncestorDiff(TreeNode* root) {
        int mx = INT_MIN;
        int mn = INT_MAX;
        pre(root , mx , mn);
        return res;
    }

    void pre(TreeNode* node , int mx , int mn){
        if(!node){
            return ;
        }
        if(mx!=INT_MIN) res = max(res , abs(mx - node->val));
        if(mn!=INT_MAX) res = max(res , abs(node->val - mn));

        mx = max(mx , node->val);
        mn = min(mn , node->val);
        pre(node->left , mx , mn);
        pre(node->right , mx , mn);
    }
};