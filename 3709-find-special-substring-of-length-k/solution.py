class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        
        for i in range(n - k + 1):
            # Check if substring s[i:i+k] consists of only one distinct character
            if len(set(s[i:i + k])) == 1:
                # Check boundary conditions
                if (i == 0 or s[i - 1] != s[i]) and (i + k == n or s[i + k] != s[i]):
                    return True
                    
        return False

# Example usage
sol = Solution()
print(sol.hasSpecialSubstring("aaabaaa", 3))  # Output: True
print(sol.hasSpecialSubstring("abc", 2))      # Output: False

