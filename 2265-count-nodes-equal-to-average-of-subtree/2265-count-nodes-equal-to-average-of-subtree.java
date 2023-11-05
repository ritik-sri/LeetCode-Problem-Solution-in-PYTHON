/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans = 0;

    public TreeNode helper1(TreeNode root) {
        if (root == null) return null;
        if (root.left == null && root.right == null) return new TreeNode(1);

        TreeNode l = l = helper1(root.left);
        TreeNode r = r = helper1(root.right);
        
        if (root.left == null) return new TreeNode(1 + r.val, null, r);
        if (root.right == null) return new TreeNode(1 + l.val, l, null);

        return new TreeNode(1 + l.val + r.val, l, r);
    }

    public TreeNode helper2(TreeNode root, TreeNode count) {
        if (root == null) return new TreeNode(0);

        int l = helper2(root.left, count.left).val;
        int r = helper2(root.right, count.right).val;

        if (root.val == (root.val + l + r) / count.val) ans++;
        root.val += l + r;

        return root;
    }

    public int averageOfSubtree(TreeNode root) {
        helper2(root, helper1(root));
        return ans;
    }
}