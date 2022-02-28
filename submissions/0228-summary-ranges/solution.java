class Solution {
    public List<String> summaryRanges(int[] nums) {
        Integer rangeStart = null;
        Integer rangeEnd = null;
        ArrayList<String> outputArr = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            rangeStart = rangeStart == null ? i : rangeStart;
            rangeEnd = rangeEnd == null ? i : rangeEnd;
            
            if (nums[i] == nums[rangeEnd] + 1) {
                rangeEnd++;
            } else if (nums[i] > nums[rangeEnd] + 1) {
                outputArr.add(rangeString(rangeStart, rangeEnd, nums));
                rangeStart = i;
                rangeEnd = i;
            }
        }
        
        if (rangeStart != null) {
            outputArr.add(rangeString(rangeStart, rangeEnd, nums));   
        }
        
        return outputArr;
    }
    
    public String rangeString(int rangeStart, int rangeEnd, int[] nums) {
        if (rangeStart == rangeEnd) {
            return String.valueOf(nums[rangeStart]);
        } else {
            return String.valueOf(nums[rangeStart])
                + "->" 
                + String.valueOf(nums[rangeEnd]);
        }
        
    }
}
