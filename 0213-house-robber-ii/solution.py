class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        def rob_range(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                curr = max(prev1, money + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1
            
        return max(rob_range(nums[:-1]), rob_range(nums[1:]))
