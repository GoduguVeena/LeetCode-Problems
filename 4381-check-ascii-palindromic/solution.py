class Solution:
    def isPalindromic(self, s: str) -> bool:
        # Convert each character to its 8-bit binary representation with leading zeros
        binary_str = "".join(format(ord(c), '08b') for c in s)
        
        # Check if the resulting binary string is a palindrome
        return binary_str == binary_str[::-1]
