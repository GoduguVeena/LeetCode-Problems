class Solution {
    public int singleNumber(int[] nums) {
        int res1=0;
        for(int num:nums){
            res1=res1^num;
        }
        return res1;
}
}
