class Solution {
    public boolean isSubsequence(String s, String t) {
        int sPointer = 0;
        if (sPointer == s.length()) return true;
        
        for (int tPointer = 0; tPointer < t.length(); tPointer++) {
            
            if (s.charAt(sPointer) == t.charAt(tPointer)) {
                sPointer++;
                
                if (sPointer == s.length()) {
                    break;
                }
            }
        }
        
        return sPointer == s.length();
    }
}
