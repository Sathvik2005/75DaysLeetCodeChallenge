class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int currentCount = 0;
        
        for (int n : nums) {
            if (n == 1) {
                // Increment current streak
                currentCount++;
            } else {
                // Streak broken, update global max and reset current
                maxCount = Math.max(maxCount, currentCount);
                currentCount = 0;
            }
        }
        
        // Final check for a streak that ends at the last element
        return Math.max(maxCount, currentCount);
    }
}