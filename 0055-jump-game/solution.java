class Solution {
    public boolean canJump(int[] nums) {

        int n = nums.length;
        int maxReach = 0;
        boolean ans = true;

        for (int i = 0; i < n; i++) {

            if (i > maxReach) {
                ans = false;
                break;
            }

            maxReach = Math.max(maxReach, i + nums[i]);

            if (maxReach >= n - 1) {
                ans = true;
                break;
            }
        }

        return ans;
    }
}
