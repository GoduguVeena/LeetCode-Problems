class Solution {
    public int pivotIndex(int[] nums) {
        int len = nums.length;
        int rightSum = 0;
        int leftSum = 0;

        for (int i = 0; i < len; i++) {
            rightSum += nums[i];
        }

        for (int i = 0; i < len; i++) {
            if (leftSum == rightSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}
