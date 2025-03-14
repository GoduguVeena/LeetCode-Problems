class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Early check: if total candies is less than k, return 0
        total = sum(candies)
        if total < k:
            return 0
        
        # Binary search for the maximum possible allocation
        left, right = 1, total // k
        
        while left < right:
            mid = (left + right + 1) // 2  # Ceiling division to avoid infinite loop
            
            # Count how many children can get 'mid' candies
            count = sum(candy // mid for candy in candies)
            
            if count >= k:
                left = mid  # We can allocate at least 'mid' candies to each child
            else:
                right = mid - 1  # We need to allocate fewer candies
        
        return left
