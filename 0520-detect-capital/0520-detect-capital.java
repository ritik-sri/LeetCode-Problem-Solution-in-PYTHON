import java.util.*;
class Solution
{
    public boolean detectCapitalUse(String word) 
    {
        String h=word;
        if(h.toLowerCase().equals(word))
        {
            return true;
        }       
        if(h.toUpperCase().equals(word))
        {
            return true;
        }
        if (((int)h.charAt(0)>=65 && h.charAt(0)<=90)&&((h.substring(1).toLowerCase()).equals(word.substring(1))))
        {
            return true;
        }
    return false;
    }
} 