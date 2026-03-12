class Solution {
    public int[] twoSum(int[] nums, int target) {
         HashMap<Integer,Integer> s=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int c=target-nums[i];
            if(s.containsKey(c)){
                return new int[]{s.get(c),i};
            }            
            s.put(nums[i],i);
        }
        return new int[]{};
    }
}