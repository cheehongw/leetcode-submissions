class Solution {
    public int[] countBits(int n) {
        int[] output = new int[n + 1];
        output[0] = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 2 != 0) { //i is odd
                output[i] = output[i - 1] + 1;
            } else {
                output[i] = output[i/2];
            }
        }
        
        return output;
        
    }
}
