class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] tab = new int[n];
        int maxLen = 1; 
        
        for (int i = 0; i < n; i++) {
            tab[i] = 1;
        }
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    tab[i] = Math.max(tab[i], tab[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, tab[i]);
        }
        return maxLen;
    }
}

