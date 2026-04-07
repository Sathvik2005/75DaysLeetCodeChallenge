class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        for (int num : nums) {
            // If count is 0, we pick the current number as the new candidate
            if (count == 0) {
                candidate = num;
            }
            
            // Increment count if num matches candidate, else decrement
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
}
