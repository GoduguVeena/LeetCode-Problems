class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        
        for money in nums:
            # At each house, we decide:
            # 1. Skip it (keep prev1)
            # 2. Rob it (add its money to prev2)
            curr = max(prev1, money + prev2)
            
            # Move our pointers forward for the next iteration
            prev2 = prev1
            prev1 = curr
            
        return prev1
