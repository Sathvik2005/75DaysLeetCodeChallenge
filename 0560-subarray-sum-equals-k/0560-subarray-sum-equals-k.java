class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int currentSum = 0;
        // Map to store (prefixSum, frequency)
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // Base case: a prefix sum of 0 has been seen once (empty subarray)
        map.put(0, 1);
        
        for (int num : nums) {
            currentSum += num;
            
            // If (currentSum - k) exists in the map, it means there are 
            // subarrays ending here that sum to k.
            if (map.containsKey(currentSum - k)) {
                count += map.get(currentSum - k);
            }
            
            // Update the frequency of the current prefix sum in the map
            map.put(currentSum, map.getOrDefault(currentSum, 0) + 1);
        }
        
        return count;
    }
}