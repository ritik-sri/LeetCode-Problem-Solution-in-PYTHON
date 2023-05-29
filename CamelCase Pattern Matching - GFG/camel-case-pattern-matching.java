//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N = Integer.parseInt(read.readLine());
            String[] Dictionary=read.readLine().split(" ");
            String Pattern=read.readLine();
            Solution ob = new Solution();
            ArrayList <String> ans=ob.CamelCase(N,Dictionary,Pattern);
            for(String u:ans)
             System.out.print(u+" ");
            System.out.println(); 
        }
    }
}
// } Driver Code Ends

class Solution {
    ArrayList<String> CamelCase(int N, String[] Dictionary, String Pattern) {
        ArrayList<String> ans = new ArrayList<>();
        int len = Pattern.length();

        for (int i = 0; i < Dictionary.length; i++) {
            int j = 0;
            int k = 0;

            while (j < Dictionary[i].length() && k < len) {
                if (Character.isUpperCase(Dictionary[i].charAt(j))) {
                    if (Dictionary[i].charAt(j) == Pattern.charAt(k)) {
                        k++;
                    } else {
                        break;
                    }
                }
                j++;
            }

            if (k == len) {
                ans.add(Dictionary[i]);
            }
        }

        if (ans.size() == 0) {
            ans.add("-1");
        }
        
        Collections.sort(ans);

        return ans;
    }
}



