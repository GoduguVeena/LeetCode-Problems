class Solution {
    public boolean uniformArray(int[] nums1) {
        int minOdd = Integer.MAX_VALUE;
        int minEven = Integer.MAX_VALUE;
        
        // Find smallest odd and smallest even
        for (int num : nums1) {
            if (num % 2 == 0) {
                minEven = Math.min(minEven, num);
            } else {
                minOdd = Math.min(minOdd, num);
            }
        }
        
        // If all numbers are odd or all are even
        if (minOdd == Integer.MAX_VALUE || minEven == Integer.MAX_VALUE) {
            return true;
        }
        
        // If smallest even < smallest odd → cannot make uniform parity
        if (minEven < minOdd) {
            return false;
        }
        
        return true;
    }
}

