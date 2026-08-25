class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        
        for (int num : nums) {
            int count = map.getOrDefault(num, 0) + 1;
            if (count > n / 2) {
                return num;
            }
            map.put(num, count);
        }
        
        return -1;
    }
}
