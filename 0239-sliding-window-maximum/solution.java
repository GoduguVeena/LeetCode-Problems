class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) { // Fixed condition: i < n
            // 1. Remove elements out of the current sliding window boundary
            if (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }
            
            // 2. Maintain monotonic decreasing order in the deque
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) {
                dq.pollLast();
            }
            
            // 3. Add current element index to the deque
            dq.addLast(i);
            
            // 4. Store the maximum element for the current window in the result array
            if (i >= k - 1) {
                res[i - (k - 1)] = nums[dq.peekFirst()];
            }
        }
        
        return res;
    }
}
