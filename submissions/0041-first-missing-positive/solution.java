class Solution {
    public int firstMissingPositive(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 1 || nums[i] > nums.length) {
                nums[i] = nums.length + 1;
            }
        }
        
        for (int i = 0; i < nums.length; i++) {
            
            int numberAtIndexI = Math.abs(nums[i]);
            
            if (numberAtIndexI != nums.length + 1) {
                nums[numberAtIndexI - 1] = -1 * Math.abs(nums[numberAtIndexI - 1]);
            }
        }
        
        System.out.println(Arrays.toString(nums));
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0 ) {
                return i + 1;
            }
        }
        
        return nums.length + 1;
        
        
        
    }
}
