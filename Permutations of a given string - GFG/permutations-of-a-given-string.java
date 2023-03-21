//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
	public static void main(String[] args) throws IOException
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0)
        {
            String S = br.readLine().trim();
            Solution obj = new Solution();
            List<String> ans = obj.find_permutation(S);
            for( int i = 0; i < ans.size(); i++)
            {
                System.out.print(ans.get(i)+" ");
            }
            System.out.println();
                        
        }
	}
}


// } Driver Code Ends

class Solution {

         public void find(int index,String s,List<String>ans)

         {

               if(index==s.length())

               {

                     if(!ans.contains(s))

                     ans.add(s);

                     return;

               }

               for(int i=index;i<s.length();i++){

                    s=swap(i,index,s);

                    find(index+1,s,ans);

                    s=swap(i,index,s);

               }

         }

        public String swap(int i,int j,String s)

        {

               char [] ch=s.toCharArray();

                char c=ch[i];

                ch[i]=ch[j];

                ch[j]=c;

                return String.valueOf(ch);

        }

    public List<String> find_permutation(String S) {

        // Code here

        List<String>ans=new ArrayList<>();

        find(0,S,ans);

        Collections.sort(ans);

        return ans;

    }

}


































    