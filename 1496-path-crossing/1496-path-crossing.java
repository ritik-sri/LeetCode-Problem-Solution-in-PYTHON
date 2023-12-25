class Solution {
    public boolean isPathCrossing(String s) {
        int x=0,y=0;
		Set<String> map=new HashSet<>();
		map.add("0,0");
		
		
		for(int i=0;i<s.length();i++) {
			if(s.charAt(i)=='E') {
				x++;
			}
			if(s.charAt(i)=='W') {
				x--;
			}
			if(s.charAt(i)=='N') {
				y++;
			}
			if(s.charAt(i)=='S') {
				y--;
			}
			String curr=x+","+y;
			if(map.contains(curr)) {
				return true;
			}
			map.add(curr);
		}
		return false;
    }
}
