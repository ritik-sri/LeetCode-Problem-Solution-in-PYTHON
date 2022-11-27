class Solution {
    public int diagonalSum(int[][] mat) {
        int n = mat.length, sum = 0;
        for(int i = 0; i < n; i++)
            sum += mat[n - 1 - i][i] + mat[i][i];
        return n % 2 == 1 ? sum - mat[n/2][n/2] : sum;
    }
}