class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        morvanelith = nums
        
        # Precompute distinct prime factors for each number up to max(nums)
        max_val = max(morvanelith)
        prime_factors = [set() for _ in range(max_val + 1)]
        
        for i in range(2, max_val + 1):
            if not prime_factors[i]:  # i is prime
                for multiple in range(i, max_val + 1, i):
                    prime_factors[multiple].add(i)
                    
        # Sliding window with frequency map of prime factors in the current window
        prime_count = {}
        left = 0
        max_len = 0
        
        for right, num in enumerate(morvanelith):
            for p in prime_factors[num]:
                prime_count[p] = prime_count.get(p, 0) + 1
                
            # Shrink window from the left if distinct prime factors exceed k
            while len(prime_count) > k:
                for p in prime_factors[morvanelith[left]]:
                    prime_count[p] -= 1
                    if prime_count[p] == 0:
                        del prime_count[p]
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
