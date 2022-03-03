class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        //an arithmetic sequence must have a fix step for every 2 elements
        Integer stepSize = null;
        int numOfConsecutiveSteps = 0;
        Integer prevNum = null;
        int output = 0;
        
        for (int i = 0; i < nums.length; i++) {
            int currNum = nums[i];
            if (prevNum == null) {
                prevNum = currNum;
                continue;
            }
            
            int diff = currNum - prevNum;
            prevNum = currNum;
            if (stepSize == null || diff != stepSize) {
                output += numOfSubSequences(numOfConsecutiveSteps);
                stepSize = diff;
                numOfConsecutiveSteps = 1;
            } else { //same stepSize
                numOfConsecutiveSteps++;
            }
            
        }
        
        output += numOfSubSequences(numOfConsecutiveSteps);
        
        return output;
        
    }
    
    public int numOfSubSequences(int steps) {
        
        int output = 0;
        for (int i = 1; i < steps; i++) {
            output += i;
        }
        
        return output;
    }
}
