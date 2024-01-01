import java.util.*;
class Solution
{
    public int findContentChildren(int[] g, int[] s)
    {
        var j=0;
        Arrays.sort(g);
        Arrays.sort(s);
        for(var i=0;i<s.length && j<g.length;i++ )
        {
            if(s[i]>=g[j])
            {
                j++;
            }
        }
        return j;
    }
}