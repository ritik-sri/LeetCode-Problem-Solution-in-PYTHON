class Solution {
    public int maxDepth(TreeNode root)
    {
        if(root==null)
        {
            return 0;
        }
        int left=maxDepth(root.left);
        int right=maxDepth(root.right);
        System.out.print(left);
        System.out.print(right);
        int maxi=Math.max(left,right);
        return maxi+1;
    }
}