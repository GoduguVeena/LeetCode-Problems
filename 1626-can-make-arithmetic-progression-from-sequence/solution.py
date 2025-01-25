class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s = sorted(arr)
        diff = s[0] - s[1]
        for i in range(2, len(s)):
            if diff != s[i - 1] - s[i]:
                return False
        return True
