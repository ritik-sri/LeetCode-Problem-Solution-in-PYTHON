class Solution {
    public int countBits(int n) {
        int c = 0;
        while(n != 0) {
            if(n % 2 == 1) { //for any odd number, we increase the count of 1's until its != 0
                c++;
            }
            n /= 2; //we keep decreasing the number 
        }
        return c;
    }
    public int[] sortByBits(int[] arr) {
        Arrays.sort(arr);
        for(int i = 0; i < arr.length; i++) { //we simply sort the elements
            for(int j = 0; j < arr.length - 1; j++) {
                if(countBits(arr[j]) > countBits(arr[j + 1])) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
                
            }
        }
        return arr;
    }
}