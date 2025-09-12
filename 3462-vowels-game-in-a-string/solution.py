class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Define a set of vowels for efficient lookup.
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Check if any character in the string is a vowel.
        for char in s:
            if char in vowels:
                # If a vowel is present, Alice can always make a move and will win.
                return True
        
        # If no vowels are found, Alice cannot make a valid move.
        return False
