class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hash_map = {}

        for char in t:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        for char in s:
            hash_map[char] -= 1

        for char in hash_map:
            if hash_map[char] == 1:
                return char
