class Solution {
public int[][] imageSmoother(int[][] img) {

    int m = img.length;
    int n = img[0].length;
    int img1[][] = new int[m][n];
    
    int dirs[][]= {{0,1},{1,0},{0,-1},{-1,0},{1,-1},{-1,1},{1,1},{-1,-1}};
    
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            int ele = img[i][j];
            int sum = ele;
            int d = 1;
            for(int dir[]:dirs){
                int r = dir[0] + i;
                int c = dir[1] + j;
                
                if(r>=0 && c>=0 && r< m && c <n){ 
                    sum +=img[r][c];
                    d++;
                }
            }
            img1[i][j] = sum/d;
        }
    }
    
    return img1;
	
}
}