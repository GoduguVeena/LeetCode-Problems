class Solution {
    int[] memo; 

    public int rob(int[] nums) {
        int n = nums.length; 
        if (n == 0) return 0; 
if (n == 1) return nums[0]; 
if (n == 2) return Math.max(nums[0], nums[1]);
        
        // 3 houses and above 
        memo = new int[n]; 
        Arrays.fill(memo, -1); 
        int rob1 = recur(n - 2, 0, nums); 
        
        Arrays.fill(memo, -1); 
        int rob2 = recur(n - 1, 1, nums); 
        
        return Math.max(rob1, rob2); 
    } 

    private int recur(int n, int st, int[] nums) {
        if (n == st) return nums[st];
        if(n ==st+1) return Math.max(nums[st],nums[st+1]);

        if (memo[n] != -1) return memo[n];

        memo[n] = Math.max(nums[n] + recur(n - 2, st, nums), recur(n - 1, st, nums));
        
        return memo[n];
    } 

} 
