class Solution {
    public int singleNumber(int[] nums) {
        int res1=0,res2=0;
        for(int i=0;i<nums.length;i++){
            res1=res1^nums[i] &~res2;
            res2=res2^nums[i] & ~res1;
        }
        return res1;
    }
}
